---
name: portal_users_log
schema: gold
layer: gold
domain: null
type: table
status: active
purpose: Audits Digital Finance Portal sign-in events from Entra ID.
grain: one row per signin_id (one sign-in event)
primary_key:
- signin_id
entity_column: null
period_columns:
- signin_timestamp
pii_columns:
- user_principal_name
- user_display_name
synonyms: []
built_from: []
known_issues: []
row_count: 50
proposed_fields:
- grain
- primary_key
reviewed: false
---

# portal_users_log

Digital Finance Portal user sign-in audit log (sourced from Entra ID via Log Analytics). Currently populated with sample data.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `signin_id` | string | Unique Entra sign-in event ID |  | `signin_id` |
| `signin_timestamp` | timestamp | Sign-in event time (UTC) |  | `signin_timestamp` |
| `user_principal_name` | string | User UPN |  | `user_principal_name` |
| `user_display_name` | string | User display name |  | `user_display_name` |
| `user_type` | string | Member or Guest |  | `user_type` |
| `app_display_name` | string | Application signed into |  | `app_display_name` |
| `client_app_used` | string | Client app type (Browser, Mobile Apps and Desktop clients) |  | `client_app_used` |
| `ip_address` | string | Source IP address |  | `ip_address` |
| `country` | string | Country/region code (ISO 3166-1 alpha-2) |  | `country` |
| `state` | string | State / province |  | `state` |
| `city` | string | City |  | `city` |
| `operating_system` | string | Device operating system |  | `operating_system` |
| `browser` | string | Browser and version |  | `browser` |
| `device_id` | string | Entra device ID (null for unregistered devices) |  | `device_id` |
| `is_compliant` | boolean | Device compliant per Intune |  | `is_compliant` |
| `is_managed` | boolean | Device managed |  | `is_managed` |
| `authentication_requirement` | string | singleFactorAuthentication / multiFactorAuthentication |  | `authentication_requirement` |
| `authentication_methods` | string | Authentication methods used, comma separated |  | `authentication_methods` |
| `conditional_access_status` | string | success / failure / notApplied |  | `conditional_access_status` |
| `risk_level` | string | Aggregated risk level: none / low / medium / high |  | `risk_level` |
| `risk_state` | string | none / atRisk / remediated / dismissed |  | `risk_state` |
| `result_code` | int | Entra result code (0 = success) |  | `result_code` |
| `result_reason` | string | Result / failure reason |  | `result_reason` |
| `session_id` | string | Session correlation ID |  | `session_id` |
| `tenant_id` | string | Entra tenant ID |  | `tenant_id` |

## Values

**signin_id**
- `cbfcf7d6-f7ba-41e1-819e-6cac3287cd39`: 1 rows
- `998bf133-c09a-4189-b4c7-d70c72f46f62`: 1 rows
- `c9a30488-b9e7-4886-8e86-f3c5b578860d`: 1 rows
- `49cebf16-f089-4530-8f93-ef6546ce1590`: 1 rows
- `1a118058-ed45-420f-ae15-3daf276fb7ab`: 1 rows
- `4e5d4de8-fc3d-4d73-b317-dd35599635c2`: 1 rows
- `5a733d51-69a7-4c07-8de1-a34b67b98f84`: 1 rows
- `7f7eb2c3-9b6f-48ff-9479-84abaf2d579a`: 1 rows
- `22101afb-53fb-49e5-997c-1a2791c0d0c2`: 1 rows
- `44f58dde-02ab-49c5-bbe3-b7ab9200edb9`: 1 rows
- `161ca506-c78c-405e-b02e-84b402e1f93f`: 1 rows
- `0afa51d4-fc67-44b1-b4b7-8b904741099c`: 1 rows
- `70d779bd-1f9c-4635-9ebf-cbe738675d72`: 1 rows
- `c91de7d9-d730-483e-b82c-8c78691b31c3`: 1 rows
- `6d8a3da8-d911-44c6-845d-c760c29ba3c1`: 1 rows
- `1db02415-64ee-4917-bb7d-d99ccb40e8c1`: 1 rows
- `34ce9467-2c20-4bc4-aefa-bf67114ccc63`: 1 rows
- `09df2f26-6931-4fa7-ace0-65f5af1c2a56`: 1 rows
- `bb3f354f-9b6b-4be2-b13f-44e073061dc3`: 1 rows
- `e6c1bf85-f9dd-4138-9257-d696912f03e9`: 1 rows
- `a8125b68-e36f-4fc5-8d74-7069680e2a75`: 1 rows
- `59bf5db0-ecc4-49e7-99f4-e586f035fc75`: 1 rows
- `d22ce6f2-00fe-4f36-a7d3-22ace2521b6a`: 1 rows
- `32e9c4ed-75f7-4440-bb0e-61ca6cd5d7f3`: 1 rows
- `43d84346-ac3f-4c89-85b7-a74f26e06a5c`: 1 rows
- `39ec5f4a-ac9e-48a3-ae5b-552127add68d`: 1 rows
- `39a52b7e-154a-4e40-8e04-3f99cd31eaa2`: 1 rows
- `b55b3785-090d-475b-a87f-a08e842fbdf0`: 1 rows
- `9e4d05f5-92f5-4d42-97ce-d66a89cb3700`: 1 rows
- `e03efc61-8095-4e23-a329-33e9290c6c66`: 1 rows
- `2edc820e-7dec-43de-8a75-1ac179eaf5a0`: 1 rows
- `2fdf3b47-b95a-4780-a197-61b762e2e36c`: 1 rows
- `5959c0df-7682-44b9-a61a-c089d0ac2ff8`: 1 rows
- `7a467c02-8880-4a9d-85c8-1eefc76fea87`: 1 rows
- `6b518200-3dc9-48df-884b-66df55db69a2`: 1 rows
- `fdffcd6a-9e9c-40f6-84aa-bd0ee2b16a04`: 1 rows
- `d80432a4-e771-4885-ac0f-7b7efb5f35d8`: 1 rows
- `5d265ec7-c044-4dcd-9874-5025e69151aa`: 1 rows
- `d1af2e61-c2f4-48e3-9995-efec338cf8a9`: 1 rows
- `69a891cf-c79f-42f6-874e-40957a9544fd`: 1 rows
- `90df0476-811d-4a3f-85cc-6904c5aaa640`: 1 rows
- `a93d0486-3d5c-4376-907b-9077fed31a80`: 1 rows
- `4597675f-5524-4d47-a108-1bc945018487`: 1 rows
- `08b9646e-bd5d-46f5-b080-7a17dbd6674b`: 1 rows
- `0170d296-7bb7-4d7e-9312-a09f71aef38c`: 1 rows
- `b995311a-006f-40cf-8f3f-1fac44be4935`: 1 rows
- `8adca196-08a9-43d2-b842-f2ade88beec0`: 1 rows
- `9a44779e-a030-4dfd-a2b7-68fe3b0304f8`: 1 rows
- `5ff0c794-fbeb-4a6a-a2dd-f44169cd0735`: 1 rows
- `bcf5e40a-7b9b-441a-941b-daae3b3c6bd1`: 1 rows

**signin_timestamp**
- `2026-10-01 03:03:59+00:00`: 1 rows
- `2026-10-17 22:22:03+00:00`: 1 rows
- `2026-10-01 17:28:12+00:00`: 1 rows
- `2026-09-23 22:13:23+00:00`: 1 rows
- `2026-10-10 17:31:27+00:00`: 1 rows
- `2026-10-16 03:09:24+00:00`: 1 rows
- `2026-09-24 12:37:36+00:00`: 1 rows
- `2026-09-28 17:27:07+00:00`: 1 rows
- `2026-10-04 03:05:04+00:00`: 1 rows
- `2026-10-16 17:33:37+00:00`: 1 rows
- `2026-10-19 17:34:42+00:00`: 1 rows
- `2026-09-29 07:51:20+00:00`: 1 rows
- `2026-10-22 17:35:47+00:00`: 1 rows
- `2026-10-11 22:19:53+00:00`: 1 rows
- `2026-09-25 17:26:02+00:00`: 1 rows
- `2026-10-22 03:11:34+00:00`: 1 rows
- `2026-10-07 17:30:22+00:00`: 1 rows
- `2026-10-17 07:57:50+00:00`: 1 rows
- `2026-10-04 17:29:17+00:00`: 1 rows
- `2026-10-19 03:10:29+00:00`: 1 rows
- `2026-09-26 07:50:15+00:00`: 1 rows
- `2026-10-14 22:20:58+00:00`: 1 rows
- `2026-10-06 12:41:56+00:00`: 1 rows
- `2026-10-20 07:58:55+00:00`: 1 rows
- `2026-10-02 22:16:38+00:00`: 1 rows
- `2026-10-07 03:06:09+00:00`: 1 rows
- `2026-10-12 12:44:06+00:00`: 1 rows
- `2026-10-20 22:23:08+00:00`: 1 rows
- `2026-10-18 12:46:16+00:00`: 1 rows
- `2026-10-11 07:55:40+00:00`: 1 rows
- `2026-10-14 07:56:45+00:00`: 1 rows
- `2026-10-21 12:47:21+00:00`: 1 rows
- `2026-09-28 03:02:54+00:00`: 1 rows
- `2026-09-29 22:15:33+00:00`: 1 rows
- `2026-10-15 12:45:11+00:00`: 1 rows
- `2026-10-23 07:49:10+00:00`: 1 rows
- `2026-10-10 03:07:14+00:00`: 1 rows
- `2026-10-02 07:52:25+00:00`: 1 rows
- `2026-10-03 12:40:51+00:00`: 1 rows
- `2026-10-08 07:54:35+00:00`: 1 rows
- `2026-10-05 07:53:30+00:00`: 1 rows
- `2026-10-09 12:43:01+00:00`: 1 rows
- `2026-09-25 03:01:49+00:00`: 1 rows
- `2026-10-13 03:08:19+00:00`: 1 rows
- `2026-10-08 22:18:48+00:00`: 1 rows
- `2026-09-26 22:14:28+00:00`: 1 rows
- `2026-09-30 12:39:46+00:00`: 1 rows
- `2026-10-13 17:32:32+00:00`: 1 rows
- `2026-10-05 22:17:43+00:00`: 1 rows
- `2026-09-27 12:38:41+00:00`: 1 rows

**user_type**
- `Member`: 40 rows
- `Guest`: 10 rows

**app_display_name**
- `Digital Finance Portal`: 50 rows

**client_app_used**
- `Browser`: 42 rows
- `Mobile Apps and Desktop clients`: 8 rows

**country**
- `GB`: 19 rows
- `IN`: 13 rows
- `US`: 6 rows
- `AE`: 6 rows
- `IE`: 6 rows

**state**
- `England`: 12 rows
- `Maharashtra`: 7 rows
- `Scotland`: 7 rows
- `Dubai`: 6 rows
- `Leinster`: 6 rows
- `New York`: 6 rows
- `Karnataka`: 6 rows

**city**
- `Edinburgh`: 7 rows
- `Mumbai`: 7 rows
- `Dubai`: 6 rows
- `Dublin`: 6 rows
- `London`: 6 rows
- `Manchester`: 6 rows
- `New York`: 6 rows
- `Bengaluru`: 6 rows

**operating_system**
- `Windows 11`: 17 rows
- `Android 14`: 9 rows
- `Windows 10`: 8 rows
- `MacOs`: 8 rows
- `Ios 17.6`: 8 rows

**browser**
- `Chrome 130.0.6723`: 9 rows
- `Chrome Mobile 129.0`: 9 rows
- `Edge 130.0.2849`: 8 rows
- `Chrome 129.0.6668`: 8 rows
- `Safari 17.6`: 8 rows
- `Mobile Safari 17.6`: 8 rows

**device_id**
- `None`: 17 rows
- `d1e4f5a6-8c7b-40a1-9d3e-4f5a6b7c8d94`: 9 rows
- `c9d3e4f5-7b6a-49f0-8c2d-3e4f5a6b7c83`: 8 rows
- `b7e2d3c4-6a5f-48e9-8b1c-2d3e4f5a6b72`: 8 rows
- `a3f1c2d4-5b6e-47f8-9a0b-1c2d3e4f5a61`: 8 rows

**is_compliant**
- `True`: 33 rows
- `False`: 17 rows

**is_managed**
- `False`: 26 rows
- `True`: 24 rows

**authentication_requirement**
- `multiFactorAuthentication`: 33 rows
- `singleFactorAuthentication`: 17 rows

**authentication_methods**
- `Password, Microsoft Authenticator (push notification)`: 25 rows
- `Password`: 14 rows
- `Previously satisfied`: 10 rows
- `Password, Text message`: 1 rows

**conditional_access_status**
- `success`: 35 rows
- `notApplied`: 13 rows
- `failure`: 2 rows

**risk_level**
- `none`: 40 rows
- `low`: 6 rows
- `high`: 2 rows
- `medium`: 2 rows

**risk_state**
- `none`: 40 rows
- `atRisk`: 9 rows
- `remediated`: 1 rows

**result_code**
- `0`: 35 rows
- `50074`: 5 rows
- `50126`: 5 rows
- `50053`: 2 rows
- `53003`: 2 rows
- `500121`: 1 rows

**result_reason**
- `Success`: 35 rows
- `Strong Authentication is required.`: 5 rows
- `Error validating credentials due to invalid username or password.`: 5 rows
- `Account is locked because user tried to sign in too many times with an incorrect user ID or password.`: 2 rows
- `Access has been blocked by Conditional Access policies.`: 2 rows
- `Authentication failed during strong authentication request.`: 1 rows

**session_id**
- `e23d595b-0e3f-4a2d-a927-6db6d8e3a5da`: 1 rows
- `039fda2b-10c4-444c-8132-48bf15e04a10`: 1 rows
- `dcd0f098-449d-4221-aff9-d58bfeb3e383`: 1 rows
- `6c998646-f993-4650-9bd3-9304f76e7e3f`: 1 rows
- `fb11cd3b-6e09-42ee-adac-f4dd93973f9c`: 1 rows
- `bd3bf2af-6e7d-4243-8d8d-32df20f68095`: 1 rows
- `2f699b90-0a7e-416b-b4f5-6532ad227679`: 1 rows
- `84cec94f-906c-4b2d-a064-3d0d8c634e5c`: 1 rows
- `ddbd63d5-df70-473f-9b8c-f5ff4554362f`: 1 rows
- `5ffde729-ed72-4c58-af38-e4ec5f13e994`: 1 rows
- `a17fc570-906f-4b02-9b51-6aad340bbf37`: 1 rows
- `62453075-24f5-418b-8fb7-4c82c40e9f30`: 1 rows
- `83dda9f6-cda6-4f72-a49a-27876f3c5226`: 1 rows
- `8299586d-7f60-4884-a3ed-b218544e927f`: 1 rows
- `b1bf6dd5-5a37-4800-b2ae-a32390a0663e`: 1 rows
- `7a3a45e0-7ff7-4d4c-a533-a73d7df37740`: 1 rows
- `2f3c97b7-e2ef-4a96-a914-ed3de11eb518`: 1 rows
- `51bd3a23-c85b-4bc1-be52-570e3530886c`: 1 rows
- `d0958e0b-d9b1-4d57-bb91-970796c3b7d3`: 1 rows
- `07836a66-7351-433b-adc1-6ae52840d791`: 1 rows
- `fc9cb717-9e36-4490-9327-ec16ed3ebb29`: 1 rows
- `645463b5-cff1-48fa-8535-bae967af5ac6`: 1 rows
- `3b11dca1-bccb-4d23-88d9-50467074ca84`: 1 rows
- `454b9686-8b09-4a9e-90de-418b2c2bbe2b`: 1 rows
- `5abf2406-fbd8-49d3-92e5-d2c164571b0d`: 1 rows
- `fc8c1bcd-024a-4e16-9f69-22d83d6f7e46`: 1 rows
- `cf09bed4-5383-4ef0-8798-8545d521fc8d`: 1 rows
- `20b1f986-9d80-4856-9faa-7fd593814e0c`: 1 rows
- `c387e95d-045c-46d4-a55b-86e11aea4bbb`: 1 rows
- `bac9da2b-577a-4645-9a2c-5a3400f73253`: 1 rows
- `8f7d73ed-1137-438f-acfb-68bc7b8f9ee1`: 1 rows
- `b36a71bc-6638-4c6c-935d-651f589b6a38`: 1 rows
- `15bbc4b8-b5d7-4dac-9b7f-884353d6386e`: 1 rows
- `0152b5ba-8cc3-48b8-bd6f-c2da4ad0c562`: 1 rows
- `c9921281-77fd-4608-b17b-18066616ecfa`: 1 rows
- `a63c0463-3892-421d-b7d3-bc7e6cb0493a`: 1 rows
- `2f593a95-7953-4f1c-a620-359cdd9a3f1c`: 1 rows
- `dfc46295-a650-4058-b68f-b7ad620e934f`: 1 rows
- `282f707f-5274-4db3-a461-2ff3ffea661c`: 1 rows
- `0d28b5db-b801-45ea-aef7-d18b5182bfa6`: 1 rows
- `9864aa2b-4fd4-4a58-8990-7d81945133a5`: 1 rows
- `da398d32-54d4-4ca7-bf0e-bb385637d2f3`: 1 rows
- `75204b7b-1e03-49ea-acee-a12449878209`: 1 rows
- `d66a4fd6-3d3c-4d24-8e8c-cb091ae69f9e`: 1 rows
- `ec0d3fb6-b11c-4f46-9155-17e292b169e4`: 1 rows
- `54f43b37-d87b-4b8f-988e-a3827e4a5c59`: 1 rows
- `3f04c156-4d64-4ee8-a998-ab2f510c67c8`: 1 rows
- `cc138031-3a02-4030-b6e8-fe3197ccd057`: 1 rows
- `f31a0d2e-ccbf-4733-8a24-1c128b085ac6`: 1 rows
- `c9d0be90-3502-41f0-b5f0-06d9bec670e8`: 1 rows

**tenant_id**
- `7c1d9e2a-4b3f-4e8a-9d61-2f5a8b0c3e14`: 50 rows

## Profile

Rows in the latest export: 50.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `signin_id` | STRING | 46 | 0 | 0170d296-7bb7-4d7e-9312-a09f71aef38c | fdffcd6a-9e9c-40f6-84aa-bd0ee2b16a04 |
| `signin_timestamp` | TIMESTAMP | 49 | 0 | 2026-09-23 22:13:23 | 2026-10-23 07:49:10 |
| `user_principal_name` | STRING | 10 | 0 |  |  |
| `user_display_name` | STRING | 10 | 0 |  |  |
| `user_type` | STRING | 2 | 0 | Guest | Member |
| `app_display_name` | STRING | 1 | 0 | Digital Finance Portal | Digital Finance Portal |
| `client_app_used` | STRING | 2 | 0 | Browser | Mobile Apps and Desktop clients |
| `ip_address` | STRING | 52 | 0 | 192.0.2.101 | 203.0.113.89 |
| `country` | STRING | 5 | 0 | AE | US |
| `state` | STRING | 7 | 0 | Dubai | Scotland |
| `city` | STRING | 8 | 0 | Bengaluru | New York |
| `operating_system` | STRING | 5 | 0 | Android 14 | Windows 11 |
| `browser` | STRING | 6 | 0 | Chrome 129.0.6668 | Safari 17.6 |
| `device_id` | STRING | 4 | 17 | a3f1c2d4-5b6e-47f8-9a0b-1c2d3e4f5a61 | d1e4f5a6-8c7b-40a1-9d3e-4f5a6b7c8d94 |
| `is_compliant` | BOOLEAN | 2 | 0 | False | True |
| `is_managed` | BOOLEAN | 2 | 0 | False | True |
| `authentication_requirement` | STRING | 2 | 0 | multiFactorAuthentication | singleFactorAuthentication |
| `authentication_methods` | STRING | 4 | 0 | Password | Previously satisfied |
| `conditional_access_status` | STRING | 3 | 0 | failure | success |
| `risk_level` | STRING | 4 | 0 | high | none |
| `risk_state` | STRING | 3 | 0 | atRisk | remediated |
| `result_code` | INT | 6 | 0 | 0 | 500121 |
| `result_reason` | STRING | 6 | 0 | Access has been blocked by Conditiona... | Success |
| `session_id` | STRING | 48 | 0 | 0152b5ba-8cc3-48b8-bd6f-c2da4ad0c562 | fc9cb717-9e36-4490-9327-ec16ed3ebb29 |
| `tenant_id` | STRING | 1 | 0 | 7c1d9e2a-4b3f-4e8a-9d61-2f5a8b0c3e14 | 7c1d9e2a-4b3f-4e8a-9d61-2f5a8b0c3e14 |

## Sample rows

| signin_id | signin_timestamp | user_principal_name | user_display_name | user_type | app_display_name | client_app_used | ip_address | country | state | city | operating_system | browser | device_id | is_compliant | is_managed | authentication_requirement | authentication_methods | conditional_access_status | risk_level | risk_state | result_code | result_reason | session_id | tenant_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5ff0c794-fbeb-4a6a-a2dd-f44169cd0735 | 2026-10-22 17:35:47 | <masked> | <masked> | Member | Digital Finance Portal | Browser | 198.51.100.23 | IN | Maharashtra | Mumbai | Windows 11 | Chrome 130.0.6723 | d1e4f5a6-8c7b-40a1-9d3e-4f5a6b7c8d94 | True | False | multiFactorAuthentication | Password, Microsoft Authenticator (pu... | success | none | none | 0 | Success | dcd0f098-449d-4221-aff9-d58bfeb3e383 | 7c1d9e2a-4b3f-4e8a-9d61-2f5a8b0c3e14 |
| 90df0476-811d-4a3f-85cc-6904c5aaa640 | 2026-10-22 03:11:34 | <masked> | <masked> | Member | Digital Finance Portal | Browser | 203.0.113.36 | GB | Scotland | Edinburgh | Android 14 | Chrome Mobile 129.0 | NULL | False | False | multiFactorAuthentication | Password, Microsoft Authenticator (pu... | success | none | none | 0 | Success | a63c0463-3892-421d-b7d3-bc7e6cb0493a | 7c1d9e2a-4b3f-4e8a-9d61-2f5a8b0c3e14 |
| 49cebf16-f089-4530-8f93-ef6546ce1590 | 2026-10-21 12:47:21 | <masked> | <masked> | Member | Digital Finance Portal | Mobile Apps and Desktop clients | 203.0.113.49 | GB | England | Manchester | Ios 17.6 | Mobile Safari 17.6 | c9d3e4f5-7b6a-49f0-8c2d-3e4f5a6b7c83 | True | True | multiFactorAuthentication | Password, Microsoft Authenticator (pu... | success | none | none | 0 | Success | 7a3a45e0-7ff7-4d4c-a533-a73d7df37740 | 7c1d9e2a-4b3f-4e8a-9d61-2f5a8b0c3e14 |
| 39a52b7e-154a-4e40-8e04-3f99cd31eaa2 | 2026-10-20 22:23:08 | <masked> | <masked> | Guest | Digital Finance Portal | Browser | 192.0.2.62 | US | New York | New York | MacOs | Safari 17.6 | NULL | False | False | multiFactorAuthentication | Password, Microsoft Authenticator (pu... | success | none | none | 0 | Success | 20b1f986-9d80-4856-9faa-7fd593814e0c | 7c1d9e2a-4b3f-4e8a-9d61-2f5a8b0c3e14 |
| 09df2f26-6931-4fa7-ace0-65f5af1c2a56 | 2026-10-20 07:58:55 | <masked> | <masked> | Member | Digital Finance Portal | Browser | 198.51.100.75 | AE | Dubai | Dubai | Windows 10 | Chrome 129.0.6668 | b7e2d3c4-6a5f-48e9-8b1c-2d3e4f5a6b72 | True | True | singleFactorAuthentication | Previously satisfied | success | none | none | 0 | Success | 75204b7b-1e03-49ea-acee-a12449878209 | 7c1d9e2a-4b3f-4e8a-9d61-2f5a8b0c3e14 |
