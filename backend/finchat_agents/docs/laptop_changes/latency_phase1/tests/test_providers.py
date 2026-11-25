"""Provider conversion and parsing, with fake SDK clients (no network)."""
from __future__ import annotations

import json
from types import SimpleNamespace as NS

import pytest
from botocore.exceptions import ClientError

from finchat_agents.llm.claude_bedrock import ClaudeBedrockProvider, messages_to_anthropic, tools_to_anthropic
from finchat_agents.llm.gpt_oss_bedrock import (
    GptOssBedrockProvider,
    map_boto_error,
    messages_to_converse,
    messages_to_openai,
    tools_to_converse,
    tools_to_openai,
)
from finchat_agents.llm.types import LLMError, Message, TextBlock, ToolResultBlock, ToolSpec, ToolUseBlock

ADD = ToolSpec(name="add", description="Add.", input_schema={"type": "object", "properties": {"a": {"type": "number"}}})

CONVO = [
    Message.user("2+2?"),
    Message(role="assistant", content=[TextBlock(text="let me add"), ToolUseBlock(id="t1", name="add", input={"a": 2})]),
    Message(role="user", content=[ToolResultBlock(tool_use_id="t1", content='{"sum": 4}'), TextBlock(text="go on")]),
]


def test_tools_defined_once_converted_per_provider():
    assert tools_to_anthropic([ADD])[0] == {
        "name": "add", "description": "Add.", "input_schema": ADD.input_schema, "cache_control": {"type": "ephemeral"},
    }
    assert tools_to_converse([ADD])[0] == {"toolSpec": {"name": "add", "description": "Add.", "inputSchema": {"json": ADD.input_schema}}}
    assert tools_to_openai([ADD])[0] == {"type": "function", "function": {"name": "add", "description": "Add.", "parameters": ADD.input_schema}}


def test_messages_to_anthropic():
    out = messages_to_anthropic(CONVO + [Message(role="assistant", content=[TextBlock(text="")])])
    assert len(out) == 3  # empty text message dropped
    assert out[1]["content"][1] == {"type": "tool_use", "id": "t1", "name": "add", "input": {"a": 2}}
    assert out[2]["content"][0] == {"type": "tool_result", "tool_use_id": "t1", "content": '{"sum": 4}', "is_error": False}


def test_messages_to_converse():
    out = messages_to_converse(CONVO)
    assert out[1]["content"][1] == {"toolUse": {"toolUseId": "t1", "name": "add", "input": {"a": 2}}}
    assert out[2]["content"][0]["toolResult"]["status"] == "success"


def test_messages_to_openai():
    out = messages_to_openai("sys", CONVO)
    assert [m["role"] for m in out] == ["system", "user", "assistant", "tool", "user"]
    assert out[2]["tool_calls"][0]["function"] == {"name": "add", "arguments": json.dumps({"a": 2})}
    assert out[3] == {"role": "tool", "tool_call_id": "t1", "content": '{"sum": 4}'}


class _FakeAnthropicMessages:
    def __init__(self):
        self.kwargs = None

    async def create(self, **kwargs):
        self.kwargs = kwargs
        return NS(
            content=[NS(type="text", text="adding"), NS(type="tool_use", id="tu1", name="add", input={"a": 1})],
            usage=NS(input_tokens=100, output_tokens=20, cache_read_input_tokens=80, cache_creation_input_tokens=0),
            stop_reason="tool_use",
        )


async def test_claude_provider_caches_system_and_tools():
    msgs = _FakeAnthropicMessages()
    p = ClaudeBedrockProvider("us-east-1", client=NS(messages=msgs))
    r = await p.complete("system prompt", [Message.user("hi")], [ADD], "claude-x", 512, 0.0)
    assert msgs.kwargs["system"] == [{"type": "text", "text": "system prompt", "cache_control": {"type": "ephemeral"}}]
    assert msgs.kwargs["tools"][-1]["cache_control"] == {"type": "ephemeral"}
    assert r.text == "adding" and r.tool_calls[0].name == "add" and r.stop_reason == "tool_use"
    assert r.usage.cache_read_tokens == 80


class _FakeBoto:
    def __init__(self, resp=None, exc=None):
        self.resp, self.exc, self.kwargs = resp, exc, None

    def converse(self, **kwargs):
        self.kwargs = kwargs
        if self.exc:
            raise self.exc
        return self.resp


async def test_gpt_oss_converse_parses_tool_use_and_drops_reasoning():
    boto = _FakeBoto({
        "output": {"message": {"content": [
            {"reasoningContent": {"reasoningText": {"text": "thinking"}}},
            {"text": "<reasoning>hidden</reasoning>Sure."},
            {"toolUse": {"toolUseId": "x1", "name": "add", "input": {"a": 3}}},
        ]}},
        "stopReason": "tool_use",
        "usage": {"inputTokens": 50, "outputTokens": 9},
    })
    p = GptOssBedrockProvider("us-west-2", transport="converse", boto_client=boto)
    r = await p.complete("sys", [Message.user("hi")], [ADD], "openai.gpt-oss-120b-1:0", 256, 0.2)
    assert r.text == "Sure." and r.tool_calls[0].input == {"a": 3} and r.usage.input_tokens == 50
    assert boto.kwargs["toolConfig"]["tools"][0]["toolSpec"]["name"] == "add"
    assert boto.kwargs["system"] == [{"text": "sys"}]


async def test_gpt_oss_converse_without_tools_omits_tool_config():
    boto = _FakeBoto({"output": {"message": {"content": [{"text": "4"}]}}, "stopReason": "end_turn", "usage": {}})
    r = await GptOssBedrockProvider("us-west-2", boto_client=boto).complete("", [Message.user("2+2")], [], "m", 64, 0)
    assert r.text == "4" and "toolConfig" not in boto.kwargs and "system" not in boto.kwargs


def _client_error(code: str, status: int) -> ClientError:
    return ClientError({"Error": {"Code": code, "Message": "m"}, "ResponseMetadata": {"HTTPStatusCode": status}}, "Converse")


@pytest.mark.parametrize("code,status,retryable", [
    ("ThrottlingException", 429, True),
    ("ServiceUnavailableException", 503, True),
    ("ValidationException", 400, False),
    ("AccessDeniedException", 403, False),
])
def test_boto_error_mapping(code, status, retryable):
    err = map_boto_error(_client_error(code, status))
    assert err.retryable is retryable and err.status == status


async def test_gpt_oss_converse_raises_llm_error():
    p = GptOssBedrockProvider("us-west-2", boto_client=_FakeBoto(exc=_client_error("ThrottlingException", 429)))
    with pytest.raises(LLMError) as ei:
        await p.complete("", [Message.user("x")], [], "m", 10, 0)
    assert ei.value.retryable


class _FakeOpenAICompletions:
    def __init__(self):
        self.kwargs = None

    async def create(self, **kwargs):
        self.kwargs = kwargs
        call = NS(id="oc1", function=NS(name="add", arguments='{"a": 5}'))
        return NS(
            choices=[NS(message=NS(content=None, tool_calls=[call]), finish_reason="tool_calls")],
            usage=NS(prompt_tokens=30, completion_tokens=4),
        )


async def test_gpt_oss_openai_transport():
    comp = _FakeOpenAICompletions()
    client = NS(chat=NS(completions=comp))
    p = GptOssBedrockProvider("us-west-2", transport="openai", openai_client=client)
    r = await p.complete("sys", [Message.user("hi")], [ADD], "openai.gpt-oss-120b-1:0", 128, 0)
    assert r.tool_calls[0].input == {"a": 5} and r.stop_reason == "tool_use" and r.usage.output_tokens == 4
    assert comp.kwargs["tools"][0]["function"]["name"] == "add"
    assert comp.kwargs["messages"][0] == {"role": "system", "content": "sys"}


def test_unknown_transport_rejected():
    with pytest.raises(ValueError):
        GptOssBedrockProvider("us-west-2", transport="grpc")  # type: ignore[arg-type]


# ---------------------------------------------------------------- explicit AWS keys (from backend/.env), fake values only

def test_settings_builds_credentials_only_when_both_keys_are_set_and_never_prints_them():
    from finchat_agents.config import Settings

    assert Settings(_env_file=None).aws_credentials() is None
    assert Settings(_env_file=None, aws_access_key_id="AKIAFAKE").aws_credentials() is None  # one key is not enough
    s = Settings(_env_file=None, aws_access_key_id="AKIAFAKE", aws_secret_access_key="fake-secret", aws_session_token="fake-token")
    c = s.aws_credentials()
    assert (c.access_key_id, c.secret_access_key, c.session_token) == ("AKIAFAKE", "fake-secret", "fake-token")
    assert "fake-secret" not in repr(c) and "AKIAFAKE" not in repr(c)
    assert "fake-secret" not in repr(s) and "fake-secret" not in str(s.model_dump())


def test_keys_in_a_dotenv_file_are_read_without_being_exported(tmp_path, monkeypatch):
    from finchat_agents.config import Settings

    for name in ("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "AWS_PROFILE"):
        monkeypatch.delenv(name, raising=False)
    env = tmp_path / ".env"
    env.write_text("AWS_ACCESS_KEY_ID=AKIAFAKE\nAWS_SECRET_ACCESS_KEY=fake-secret\nAWS_SESSION_TOKEN=\nAWS_PROFILE=\n", encoding="utf-8")
    s = Settings(_env_file=env)
    assert s.aws_profile is None and s.aws_credentials() == ("AKIAFAKE", "fake-secret", None)


def test_claude_provider_passes_explicit_keys_to_the_sdk(monkeypatch):
    import anthropic

    seen = {}

    class FakeClient:
        def __init__(self, **kw):
            seen.update(kw)

    monkeypatch.setattr(anthropic, "AsyncAnthropicBedrock", FakeClient)
    from finchat_agents.config import AwsCredentials
    from finchat_agents.llm.claude_bedrock import ClaudeBedrockProvider

    ClaudeBedrockProvider("us-east-1", profile="ignored", credentials=AwsCredentials("AKIAFAKE", "fake-secret", "tok"))._get_client()
    assert seen["aws_access_key"] == "AKIAFAKE" and seen["aws_secret_key"] == "fake-secret" and seen["aws_session_token"] == "tok"
    assert "aws_profile" not in seen  # explicit keys win over a profile
    seen.clear()
    ClaudeBedrockProvider("us-east-1", profile="myprofile")._get_client()
    assert seen["aws_profile"] == "myprofile" and "aws_access_key" not in seen  # no keys: the normal AWS chain


def test_gpt_oss_provider_passes_explicit_keys_to_boto3(monkeypatch):
    import boto3

    sessions = []

    class FakeSession:
        def __init__(self, **kw):
            sessions.append(kw)

        def client(self, name, **kw):
            return ("client", name, kw["region_name"])

    monkeypatch.setattr(boto3, "Session", FakeSession)
    from finchat_agents.config import AwsCredentials
    from finchat_agents.llm.gpt_oss_bedrock import GptOssBedrockProvider

    p = GptOssBedrockProvider("us-east-1", profile="ignored", credentials=AwsCredentials("AKIAFAKE", "fake-secret"))
    assert p._boto_client() == ("client", "bedrock-runtime", "us-east-1")
    assert sessions == [{"aws_access_key_id": "AKIAFAKE", "aws_secret_access_key": "fake-secret", "aws_session_token": None}]
    sessions.clear()
    GptOssBedrockProvider("us-east-1", profile="myprofile")._boto_client()
    assert sessions == [{"profile_name": "myprofile"}]


def test_gpt_oss_openai_transport_passes_explicit_keys(monkeypatch):
    import openai.providers as providers

    seen = {}
    monkeypatch.setattr(providers, "bedrock", lambda **kw: seen.update(kw) or "provider")
    import openai

    monkeypatch.setattr(openai, "AsyncOpenAI", lambda **kw: ("openai", kw["provider"]))
    from finchat_agents.config import AwsCredentials
    from finchat_agents.llm.gpt_oss_bedrock import GptOssBedrockProvider

    p = GptOssBedrockProvider("us-east-1", credentials=AwsCredentials("AKIAFAKE", "fake-secret", "tok"), transport="openai")
    assert p._openai_client() == ("openai", "provider")
    assert seen == {"endpoint": "runtime", "region": "us-east-1", "access_key_id": "AKIAFAKE",
                    "secret_access_key": "fake-secret", "session_token": "tok"}


def test_factory_hands_the_keys_to_both_models():
    from finchat_agents.config import Settings
    from finchat_agents.llm.factory import response_model, sql_model

    s = Settings(_env_file=None, aws_region="us-east-1", aws_access_key_id="AKIAFAKE", aws_secret_access_key="fake-secret")
    assert sql_model(s).provider._credentials == ("AKIAFAKE", "fake-secret", None)
    assert response_model(s).provider._credentials == ("AKIAFAKE", "fake-secret", None)


# ---------------------------------------------------------------- real SDK method, mock network (no AWS calls)

async def test_claude_call_goes_through_the_real_sdk_create_with_a_mock_network():
    """Fake clients cannot catch a keyword the real `messages.create` rejects (temperature once did). This uses the real
    AsyncAnthropicBedrock with fake keys and an in-process HTTP transport."""
    try:  # the anthropic SDK 2.x uses the httpx2 package; older ones use httpx
        import httpx2 as httpx
    except ImportError:
        import httpx
    from anthropic import AsyncAnthropicBedrock

    from finchat_agents.config import AwsCredentials
    from finchat_agents.llm.claude_bedrock import ClaudeBedrockProvider

    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        import json as _json

        seen["body"] = _json.loads(request.content)
        seen["auth"] = request.headers.get("authorization", "")
        return httpx.Response(200, json={
            "id": "msg_1", "type": "message", "role": "assistant", "model": "m",
            "content": [{"type": "text", "text": "OK"}], "stop_reason": "end_turn", "stop_sequence": None,
            "usage": {"input_tokens": 3, "output_tokens": 1}})

    creds = AwsCredentials("AKIAFAKE", "fake-secret")
    real = AsyncAnthropicBedrock(aws_region="us-east-1", aws_access_key=creds.access_key_id, aws_secret_key=creds.secret_access_key,
                                 http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)), max_retries=0)
    provider = ClaudeBedrockProvider("us-east-1", credentials=creds, client=real)
    r = await provider.complete("sys", [Message.user("hi")], [ADD], "us.anthropic.claude-sonnet-4-5-20250929-v1:0", 256, 0.2)
    assert r.text == "OK" and r.usage.input_tokens == 3
    assert "temperature" not in seen["body"] and seen["body"]["max_tokens"] == 256
    assert seen["body"]["tools"][-1]["cache_control"] == {"type": "ephemeral"}
    assert seen["auth"].startswith("AWS4-HMAC-SHA256")  # signed with the explicit keys


def test_gpt_oss_boto_session_is_built_with_and_without_keys():
    """Real boto3 Session objects (no network): every branch must leave a session to build the client from."""
    from finchat_agents.config import AwsCredentials
    from finchat_agents.llm.gpt_oss_bedrock import GptOssBedrockProvider

    with_keys = GptOssBedrockProvider("us-east-1", credentials=AwsCredentials("AKIAFAKE", "fake-secret"))._boto_client()
    assert with_keys.meta.service_model.service_name == "bedrock-runtime" and with_keys.meta.region_name == "us-east-1"
    without = GptOssBedrockProvider("us-east-1")._boto_client()
    assert without.meta.region_name == "us-east-1"



def test_history_cache_marks_only_the_last_block_and_does_not_change_the_input():
    from finchat_agents.llm.claude_bedrock import with_history_cache

    msgs = [{"role": "user", "content": [{"type": "text", "text": "q"}]},
            {"role": "assistant", "content": [{"type": "tool_use", "id": "t1", "name": "run_sql", "input": {}}]},
            {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "t1", "content": "r1"},
                                         {"type": "text", "text": "more"}]}]
    out = with_history_cache(msgs)
    assert out[-1]["content"][-1]["cache_control"] == {"type": "ephemeral"}
    marked = [b for m in out for b in m["content"] if "cache_control" in b]
    assert len(marked) == 1  # with the tools and the system prompt: 3 of the 4 allowed breakpoints
    assert "cache_control" not in msgs[-1]["content"][-1]  # the caller's list is not modified
    assert with_history_cache([]) == []


async def test_claude_request_carries_the_history_cache_point(monkeypatch):
    import anthropic

    seen = {}

    class FakeMessages:
        async def create(self, **kw):
            seen.update(kw)
            from types import SimpleNamespace
            return SimpleNamespace(content=[SimpleNamespace(type="text", text="ok")], stop_reason="end_turn",
                                   usage=SimpleNamespace(input_tokens=1, output_tokens=1, cache_read_input_tokens=0,
                                                         cache_creation_input_tokens=0))

    class FakeClient:
        def __init__(self, **kw):
            self.messages = FakeMessages()

    monkeypatch.setattr(anthropic, "AsyncAnthropicBedrock", FakeClient)
    from finchat_agents.llm.claude_bedrock import ClaudeBedrockProvider

    await ClaudeBedrockProvider("us-east-1").complete("sys", [Message.user("hi")], [ADD], "m", 100, 0.0)
    assert seen["messages"][-1]["content"][-1]["cache_control"] == {"type": "ephemeral"}
    assert seen["system"][0]["cache_control"] == {"type": "ephemeral"} and seen["tools"][-1]["cache_control"] == {"type": "ephemeral"}
