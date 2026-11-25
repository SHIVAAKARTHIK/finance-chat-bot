"""Download files created by actions: GET /v3/files/{conversation}/{file_name}.

Only the user who created a file may download it (owner record next to the file); anyone else gets 404, so the
route never reveals whether a file exists. Names are validated and resolved strictly inside OUTPUT_DIR (no path
traversal); owner records themselves are never served.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from fastapi import HTTPException
from fastapi.responses import FileResponse

from ..tools.actions import META_SUFFIX

_FOLDER = re.compile(r"[A-Za-z0-9_-]{1,80}")
_NAME = re.compile(r"[A-Za-z0-9_-]{1,100}\.(xlsx|md)")
MEDIA_TYPES = {
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".md": "text/markdown; charset=utf-8",
}


def not_found() -> HTTPException:
    return HTTPException(status_code=404, detail="File not found")


def resolve_file(output_dir: Path, folder: str, name: str, user_id: str) -> Path:
    if not _FOLDER.fullmatch(folder) or not _NAME.fullmatch(name):
        raise not_found()
    root = output_dir.resolve()
    path = (root / folder / name).resolve()
    if path.parent != root / folder or not path.is_file():
        raise not_found()
    meta_path = path.with_name(path.name + META_SUFFIX)
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        raise not_found() from None
    if not user_id or meta.get("user_id") != user_id:
        raise not_found()
    return path


def file_response(path: Path) -> FileResponse:
    return FileResponse(path, media_type=MEDIA_TYPES[path.suffix], filename=path.name,
                        headers={"Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff"})
