---
name: dim_legal_entities
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: D365 legal entity master (address and contact details).
grain: one row per legal_entity_id (one legal entity)
primary_key:
- legal_entity_id
entity_column: legal_entity_id
period_columns: []
pii_columns:
- primary_contact_email_description
- primary_contact_email_purpose
- primary_contact_email
- primary_contact_email_is_im
- mdp_created_by
- mdp_modified_by
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: primary_contact_linkedin_description, primary_contact_phone_purpose, primary_contact_facebook, address_time_zone,
    curp_number all null
proposed_fields:
- grain
- primary_key
reviewed: false
---

# dim_legal_entities

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `legal_entity_id` | string |  |  | `legal_entity_id` |
| `primary_contact_facebook_is_private` | string |  |  | `primary_contact_facebook_is_private` |
| `primary_contact_linkedin_description` | string |  |  | `primary_contact_linkedin_description` |
| `primary_contact_phone_purpose` | string |  |  | `primary_contact_phone_purpose` |
| `primary_contact_facebook` | string |  |  | `primary_contact_facebook` |
| `address_time_zone` | string |  |  | `address_time_zone` |
| `curp_number` | string |  |  | `curp_number` |
| `national_registry_number` | string |  |  | `national_registry_number` |
| `cuc` | string |  |  | `cuc` |
| `external_legal_representative_name` | string |  |  | `external_legal_representative_name` |
| `address_description` | string |  |  | `address_description` |
| `rfc` | string |  |  | `rfc` |
| `address_location_roles` | string |  |  | `address_location_roles` |
| `primary_contact_fax_extension` | string |  |  | `primary_contact_fax_extension` |
| `certified_tax_accountant_name` | string |  |  | `certified_tax_accountant_name` |
| `primary_contact_phone_extension` | string |  |  | `primary_contact_phone_extension` |
| `report_folder` | string |  |  | `report_folder` |
| `legal_form` | string |  |  | `legal_form` |
| `address_longitude` | string |  |  | `address_longitude` |
| `company_name` | string |  |  | `company_name` |
| `person_in_charge` | string |  |  | `person_in_charge` |
| `national_classification_of_company_economic_activity` | string |  |  | `national_classification_of_company_economic_activity` |
| `primary_contact_phone_is_mobile` | string |  |  | `primary_contact_phone_is_mobile` |
| `address_valid_from` | string |  |  | `address_valid_from` |
| `primary_contact_fax_purpose` | string |  |  | `primary_contact_fax_purpose` |
| `primary_contact_telex_description` | string |  |  | `primary_contact_telex_description` |
| `print_corrective_invoice_starting_date` | string |  |  | `print_corrective_invoice_starting_date` |
| `primary_contact_phone_description` | string |  |  | `primary_contact_phone_description` |
| `legal_nature` | string |  |  | `legal_nature` |
| `name_alias` | string |  |  | `name_alias` |
| `trader_number` | string |  |  | `trader_number` |
| `address_country_region_iso_code` | string |  |  | `address_country_region_iso_code` |
| `print_inn_kpp_in_address` | string |  |  | `print_inn_kpp_in_address` |
| `primary_contact_twitter_purpose` | string |  |  | `primary_contact_twitter_purpose` |
| `primary_contact_email_description` | string |  |  | `primary_contact_email_description` |
| `time_zone` | string |  |  | `time_zone` |
| `business_item` | string |  |  | `business_item` |
| `primary_address_location_id` | string |  |  | `primary_address_location_id` |
| `primary_contact_email_purpose` | string |  |  | `primary_contact_email_purpose` |
| `primary_contact_twitter` | string |  |  | `primary_contact_twitter` |
| `primary_contact_telex` | string |  |  | `primary_contact_telex` |
| `initial_capital_investment` | string |  |  | `initial_capital_investment` |
| `primary_contact_facebook_description` | string |  |  | `primary_contact_facebook_description` |
| `party_number` | string |  |  | `party_number` |
| `primary_contact_phone` | string |  |  | `primary_contact_phone` |
| `address_state` | string |  |  | `address_state` |
| `use_for_financial_elimination_process` | string |  |  | `use_for_financial_elimination_process` |
| `curp_legal_representative` | string |  |  | `curp_legal_representative` |
| `legal_representative_name` | string |  |  | `legal_representative_name` |
| `fi_creditor_id` | string |  |  | `fi_creditor_id` |
| `address_city` | string |  |  | `address_city` |
| `address_books` | string |  |  | `address_books` |
| `address_zip_code` | string |  |  | `address_zip_code` |
| `state_inscription` | string |  |  | `state_inscription` |
| `primary_contact_email` | string |  |  | `primary_contact_email` |
| `name` | string |  |  | `name` |
| `primary_contact_linkedin` | string |  |  | `primary_contact_linkedin` |
| `primary_contact_facebook_purpose` | string |  |  | `primary_contact_facebook_purpose` |
| `company_country` | string |  |  | `company_country` |
| `primary_contact_url` | string |  |  | `primary_contact_url` |
| `primary_contact_url_description` | string |  |  | `primary_contact_url_description` |
| `address_latitude` | string |  |  | `address_latitude` |
| `registration_number` | string |  |  | `registration_number` |
| `primary_contact_telex_purpose` | string |  |  | `primary_contact_telex_purpose` |
| `rfc_legal_representative` | string |  |  | `rfc_legal_representative` |
| `primary_contact_email_is_im` | string |  |  | `primary_contact_email_is_im` |
| `print_enterprise_register` | string |  |  | `print_enterprise_register` |
| `company_type` | string |  |  | `company_type` |
| `address_street` | string |  |  | `address_street` |
| `accounting_personnel` | string |  |  | `accounting_personnel` |
| `phonetic_name` | string |  |  | `phonetic_name` |
| `commerce_registration` | string |  |  | `commerce_registration` |
| `full_primary_address` | string |  |  | `full_primary_address` |
| `primary_contact_linkedin_is_private` | string |  |  | `primary_contact_linkedin_is_private` |
| `primary_contact_twitter_is_private` | string |  |  | `primary_contact_twitter_is_private` |
| `company_representative` | string |  |  | `company_representative` |
| `naics` | string |  |  | `naics` |
| `primary_contact_url_purpose` | string |  |  | `primary_contact_url_purpose` |
| `software_identification_code` | string |  |  | `software_identification_code` |
| `address_country_region_id` | string |  |  | `address_country_region_id` |
| `address_district_name` | string |  |  | `address_district_name` |
| `start_date_of_business` | string |  |  | `start_date_of_business` |
| `language_id` | string |  |  | `language_id` |
| `use_for_financial_consolidation_process` | string |  |  | `use_for_financial_consolidation_process` |
| `primary_contact_fax` | string |  |  | `primary_contact_fax` |
| `print_corrective_invoice` | string |  |  | `print_corrective_invoice` |
| `dnb_routing_number` | string |  |  | `dnb_routing_number` |
| `primary_contact_fax_description` | string |  |  | `primary_contact_fax_description` |
| `primary_contact_twitter_description` | string |  |  | `primary_contact_twitter_description` |
| `fiscal_code` | string |  |  | `fiscal_code` |
| `address_county` | string |  |  | `address_county` |
| `accounts_office_reference_number` | string |  |  | `accounts_office_reference_number` |
| `primary_contact_linkedin_purpose` | string |  |  | `primary_contact_linkedin_purpose` |
| `address_valid_to` | string |  |  | `address_valid_to` |
| `localization_country_region_code` | string |  |  | `localization_country_region_code` |
| `vat_on_customer_behalf` | string |  |  | `vat_on_customer_behalf` |
| `vat_num` | string |  |  | `vat_num` |
| `profit_margin_scheme` | string |  |  | `profit_margin_scheme` |
| `vat_refund` | string |  |  | `vat_refund` |
| `import_vat_num` | string |  |  | `import_vat_num` |
| `source_file_name` | string |  |  | `source_file_name` |
| `hash_key` | string |  |  | `hash_key` |
| `mdp_created_by` | string |  |  | `mdp_created_by` |
| `mdp_created_date` | timestamp |  |  | `mdp_created_date` |
| `mdp_modified_by` | string |  |  | `mdp_modified_by` |
| `mdp_modified_date` | timestamp |  |  | `mdp_modified_date` |

## Values

**primary_contact_facebook_is_private**
- `No`

**primary_contact_linkedin_description**
- `None`

**primary_contact_phone_purpose**
- `None`

**primary_contact_facebook**
- `None`

**address_time_zone**
- `None`

**curp_number**
- `None`

**national_registry_number**
- `None`

**cuc**
- `None`

**external_legal_representative_name**
- `None`

**address_description**
- `Royal Premium Budget`
- `CIBL`
- `INS26`
- `Burns & Wilcox, Ltd`
- `INS59`
- `HWKGL`
- `Canadian Reports`
- `AJK Enterprises`
- `INS28`
- `US Reports`
- `INS25`
- `INS63`
- `INS14`
- `INS24`
- `Global Excess Partners`
- `Lovable 5`
- `INS62`
- `INS27`
- `Node International`
- `RB Jones, Marine`
- `CAN`
- `Node`
- `HKEUR`
- `INS36`
- `None`
- `Burns & Wilcox Canada Claims`
- `A.J. Kaufman Institute, LLC`
- `Busines`
- `Lovable 3`
- `INS33`
- `Burns & Wilcox, LTD`
- `INSHOLDING`
- `Noremac Marketing`
- `AJK Enterprises, Inc.`
- `Burns & Wilcox, RE`
- `RBJ`
- `INS01`
- `INS08`
- `Lovable 4`
- `INS65`
- `INS38`
- `INS30`
- `Business`
- `AJK Canada Insurance Holdings`

**rfc**
- `None`

**address_location_roles**
- `Business`
- `None`

**primary_contact_fax_extension**
- `None`

**certified_tax_accountant_name**
- `None`

**primary_contact_phone_extension**
- `None`

**report_folder**
- `None`

**legal_form**
- `None`

**address_longitude**
- `0`

**person_in_charge**
- `None`

**primary_contact_phone_is_mobile**
- `No`

**address_valid_from**
- `2026-11-04 15:30:38.0000000 +00:00`
- `2026-11-04 10:28:46.0000000 +00:00`
- `2026-11-04 15:30:20.0000000 +00:00`
- `2026-11-04 10:32:30.0000000 +00:00`
- `2026-11-05 09:49:52.0000000 +00:00`
- `2026-11-04 10:27:12.0000000 +00:00`
- `2026-11-05 11:39:01.0000000 +00:00`
- `2026-11-04 15:30:56.0000000 +00:00`
- `2026-11-04 10:29:52.0000000 +00:00`
- `2026-11-04 10:29:13.0000000 +00:00`
- `2026-11-04 10:33:11.0000000 +00:00`
- `2026-11-05 11:40:20.0000000 +00:00`
- `2026-11-04 10:25:31.0000000 +00:00`
- `2026-11-04 10:32:14.0000000 +00:00`
- `2026-11-04 15:26:34.0000000 +00:00`
- `2026-11-05 11:40:07.0000000 +00:00`
- `2026-11-05 11:42:36.0000000 +00:00`
- `2026-11-04 15:31:14.0000000 +00:00`
- `2026-11-05 11:41:44.0000000 +00:00`
- `2026-11-04 10:30:10.0000000 +00:00`
- `2026-11-04 14:11:26.0000000 +00:00`
- `2026-11-04 10:33:36.0000000 +00:00`
- `2026-11-05 11:42:22.0000000 +00:00`
- `2026-11-04 10:32:53.0000000 +00:00`
- `2026-11-05 11:37:44.0000000 +00:00`
- `2026-11-04 10:29:33.0000000 +00:00`
- `2026-11-05 11:40:31.0000000 +00:00`
- `2026-11-05 11:41:09.0000000 +00:00`
- `2026-11-05 11:38:33.0000000 +00:00`
- `2026-10-15 12:25:55.0000000 +00:00`
- `2026-11-05 11:38:20.0000000 +00:00`
- `2026-10-15 12:26:13.0000000 +00:00`
- `2026-10-15 12:26:25.0000000 +00:00`
- `2026-11-04 10:30:26.0000000 +00:00`
- `2026-10-15 12:27:22.0000000 +00:00`
- `1900-01-01 00:00:00.0000000 +00:00`
- `2026-11-05 11:38:46.0000000 +00:00`
- `2026-11-13 17:53:24.0000000 +00:00`
- `2026-10-15 12:27:07.0000000 +00:00`
- `2026-11-05 11:40:56.0000000 +00:00`
- `2026-11-04 10:26:49.0000000 +00:00`
- `2026-11-05 09:51:02.0000000 +00:00`
- `2026-11-04 10:31:51.0000000 +00:00`
- `2026-11-04 10:31:26.0000000 +00:00`
- `2026-11-05 11:39:29.0000000 +00:00`

**primary_contact_fax_purpose**
- `None`

**primary_contact_telex_description**
- `None`

**print_corrective_invoice_starting_date**
- `1900-01-01 12:00:00.0000000 +00:00`

**primary_contact_phone_description**
- `None`

**legal_nature**
- `None`

**name_alias**
- `Royal Premium Budget`
- `Pinnacle Ventures`
- `RBJ`
- `Burns & Wilcox, Ltd`
- `AJK Enterprises, Inc`
- `Sterling Enterprises`
- `AJK Canada Insurance`
- `Evergreen Solutions`
- `Noremac Marketing`
- `Canadian Reports`
- `PrimeEdge Inc.`
- `INS63`
- `Node`
- `HWKGL`
- `INS36`
- `INS27`
- `Burns & Wilcox, LTD`
- `INS59`
- `Grandview Holdings`
- `INS33`
- `CAN`
- `Global Excess Partne`
- `INS25`
- `INS24`
- `CIBL`
- `Burns & Wilcox, RE`
- `A.J. Kaufman Institu`
- `INS14`
- `INS08`
- `INS62`
- `US Reports`
- `Burns & Wilcox Canad`
- `HKEUR`
- `INS28`
- `INSHOLDING`
- `Company accounts dat`
- `INS65`
- `Node International`
- `AJK Enterprises`
- `INS26`
- `INS38`
- `INS01`
- `INS30`
- `RB Jones, Marine`

**trader_number**
- `None`

**address_country_region_iso_code**
- `US`
- `CA`
- `GB`
- `None`

**print_inn_kpp_in_address**
- `No`

**primary_contact_twitter_purpose**
- `None`

**time_zone**
- `GMT_COORDINATEDUNIVERSALTIME`
- `GMTMINUS0800PACIFICTIME`

**business_item**
- `None`

**primary_address_location_id**
- `9103`
- `None`
- `9011`
- `7401`
- `9210`
- `9012`
- `9213`
- `9207`
- `9008`
- `7404`
- `9002`
- `9203`
- `9106`
- `9215`
- `9015`
- `9101`
- `9214`
- `9205`
- `9006`
- `7405`
- `9001`
- `9206`
- `9204`
- `9009`
- `9005`
- `9102`
- `9104`
- `9301`
- `9212`
- `9105`
- `9216`
- `9208`
- `9014`
- `9010`
- `9209`
- `7403`
- `9003`
- `9007`
- `9202`
- `7402`
- `9201`
- `9211`
- `9004`
- `9016`
- `9013`

**primary_contact_twitter**
- `None`

**primary_contact_telex**
- `None`

**initial_capital_investment**
- `0`

**primary_contact_facebook_description**
- `None`

**party_number**
- `7408`
- `5505`
- `7212`
- `8401`
- `7405`
- `7216`
- `7414`
- `7215`
- `7406`
- `7404`
- `7303`
- `5502`
- `{2CE71508-E13F-48A0-BB18-0B3518F330D3}`
- `7302`
- `7207`
- `5503`
- `7407`
- `7415`
- `7209`
- `7410`
- `7204`
- `7409`
- `7214`
- `7203`
- `7419`
- `7201`
- `7306`
- `7416`
- `7205`
- `5504`
- `7412`
- `7206`
- `7202`
- `7301`
- `7411`
- `7304`
- `7305`
- `7417`
- `7211`
- `7213`
- `5501`
- `7210`
- `7208`
- `7413`
- `7418`

**primary_contact_phone**
- `None`

**address_state**
- `None`

**use_for_financial_elimination_process**
- `No`
- `Yes`

**curp_legal_representative**
- `None`

**legal_representative_name**
- `None`

**fi_creditor_id**
- `None`

**address_city**
- `None`

**address_books**
- `None`

**address_zip_code**
- `None`

**state_inscription**
- `None`

**name**
- `Royal Premium Budget`
- `A.J. Kaufman Institute, LLC`
- `RBJ`
- `Burns & Wilcox, Ltd`
- `INS62`
- `HWKGL`
- `INS63`
- `Global Excess Partners`
- `Noremac Marketing`
- `Canadian Reports`
- `DAT`
- `Sterling Enterprises`
- `Node`
- `INS24`
- `Evergreen Solutions`
- `RB Jones, Marine`
- `Burns & Wilcox, LTD`
- `INS33`
- `Grandview Holdings`
- `Burns & Wilcox Canada Claims`
- `CAN`
- `AJK Enterprises, Inc.`
- `CIBL`
- `INS36`
- `PrimeEdge Inc.`
- `INS27`
- `INS14`
- `Pinnacle Ventures`
- `INS08`
- `INS59`
- `US Reports`
- `INSHOLDING`
- `HKEUR`
- `INS28`
- `Burns & Wilcox, RE`
- `INS25`
- `INS65`
- `Node International`
- `AJK Enterprises`
- `INS26`
- `INS38`
- `INS01`
- `INS30`
- `AJK Canada Insurance Holdings`

**primary_contact_linkedin**
- `None`

**primary_contact_facebook_purpose**
- `None`

**primary_contact_url**
- `None`

**primary_contact_url_description**
- `None`

**address_latitude**
- `0`

**registration_number**
- `None`

**primary_contact_telex_purpose**
- `None`

**rfc_legal_representative**
- `None`

**print_enterprise_register**
- `No`

**address_street**
- `None`

**accounting_personnel**
- `None`

**phonetic_name**
- `None`

**commerce_registration**
- `None`

**full_primary_address**
- `USA`
- `CAN`
- `GBR`
- `None`

**primary_contact_linkedin_is_private**
- `No`

**primary_contact_twitter_is_private**
- `No`

**naics**
- `None`

**primary_contact_url_purpose**
- `None`

**software_identification_code**
- `None`
- `AX030003`

**address_country_region_id**
- `USA`
- `CAN`
- `GBR`
- `None`

**address_district_name**
- `None`

**start_date_of_business**
- `1900-01-01 12:00:00.0000000 +00:00`

**language_id**
- `None`

**use_for_financial_consolidation_process**
- `No`
- `Yes`

**primary_contact_fax**
- `None`

**print_corrective_invoice**
- `No`

**dnb_routing_number**
- `None`

**primary_contact_fax_description**
- `None`

**primary_contact_twitter_description**
- `None`

**fiscal_code**
- `None`

**address_county**
- `None`

**accounts_office_reference_number**
- `None`

**primary_contact_linkedin_purpose**
- `None`

**address_valid_to**
- `2154-12-31 23:59:59.0000000 +00:00`
- `1900-01-01 00:00:00.0000000 +00:00`

**localization_country_region_code**
- `Default`

**vat_on_customer_behalf**
- `No`

**vat_num**
- `None`

**profit_margin_scheme**
- `No`

**vat_refund**
- `No`

**import_vat_num**
- `None`

**source_file_name**
- `legalentities__20261116_105417.csv`

**mdp_created_date**
- `2026-11-16 11:43:00.551016+00:00`

**mdp_modified_date**
- `2026-11-16 11:43:00.551016+00:00`

## Empty columns

Empty in every row: `primary_contact_linkedin_description`, `primary_contact_phone_purpose`, `primary_contact_facebook`, `address_time_zone`, `curp_number`, `national_registry_number`, `cuc`, `external_legal_representative_name`, `rfc`, `primary_contact_fax_extension`, `certified_tax_accountant_name`, `primary_contact_phone_extension`, `report_folder`, `legal_form`, `company_name`, `person_in_charge`, `national_classification_of_company_economic_activity`, `primary_contact_fax_purpose`, `primary_contact_telex_description`, `primary_contact_phone_description`, `legal_nature`, `trader_number`, `primary_contact_twitter_purpose`, `primary_contact_email_description`, `business_item`, `primary_contact_email_purpose`, `primary_contact_twitter`, `primary_contact_telex`, `primary_contact_facebook_description`, `primary_contact_phone`, `address_state`, `curp_legal_representative`, `legal_representative_name`, `fi_creditor_id`, `address_city`, `address_books`, `address_zip_code`, `state_inscription`, `primary_contact_email`, `primary_contact_linkedin`, `primary_contact_facebook_purpose`, `company_country`, `primary_contact_url`, `primary_contact_url_description`, `registration_number`, `primary_contact_telex_purpose`, `rfc_legal_representative`, `address_street`, `accounting_personnel`, `phonetic_name`, `commerce_registration`, `company_representative`, `naics`, `primary_contact_url_purpose`, `address_district_name`, `language_id`, `primary_contact_fax`, `dnb_routing_number`, `primary_contact_fax_description`, `primary_contact_twitter_description`, `fiscal_code`, `address_county`, `accounts_office_reference_number`, `primary_contact_linkedin_purpose`, `vat_num`, `import_vat_num`. Do not filter or group on them.
