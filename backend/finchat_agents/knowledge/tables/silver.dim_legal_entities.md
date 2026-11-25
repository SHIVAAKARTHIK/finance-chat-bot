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
row_count: 45
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
- `No`: 45 rows

**primary_contact_linkedin_description**
- `None`: 45 rows

**primary_contact_phone_purpose**
- `None`: 45 rows

**primary_contact_facebook**
- `None`: 45 rows

**address_time_zone**
- `None`: 45 rows

**curp_number**
- `None`: 45 rows

**national_registry_number**
- `None`: 45 rows

**cuc**
- `None`: 45 rows

**external_legal_representative_name**
- `None`: 45 rows

**address_description**
- `Royal Premium Budget`: 2 rows
- `CIBL`: 1 rows
- `INS26`: 1 rows
- `Burns & Wilcox, Ltd`: 1 rows
- `INS59`: 1 rows
- `HWKGL`: 1 rows
- `Canadian Reports`: 1 rows
- `AJK Enterprises`: 1 rows
- `INS28`: 1 rows
- `US Reports`: 1 rows
- `INS25`: 1 rows
- `INS63`: 1 rows
- `INS14`: 1 rows
- `INS24`: 1 rows
- `Global Excess Partners`: 1 rows
- `Lovable 5`: 1 rows
- `INS62`: 1 rows
- `INS27`: 1 rows
- `Node International`: 1 rows
- `RB Jones, Marine`: 1 rows
- `CAN`: 1 rows
- `Node`: 1 rows
- `HKEUR`: 1 rows
- `INS36`: 1 rows
- `None`: 1 rows
- `Burns & Wilcox Canada Claims`: 1 rows
- `A.J. Kaufman Institute, LLC`: 1 rows
- `Busines`: 1 rows
- `Lovable 3`: 1 rows
- `INS33`: 1 rows
- `Burns & Wilcox, LTD`: 1 rows
- `INSHOLDING`: 1 rows
- `Noremac Marketing`: 1 rows
- `AJK Enterprises, Inc.`: 1 rows
- `Burns & Wilcox, RE`: 1 rows
- `RBJ`: 1 rows
- `INS01`: 1 rows
- `INS08`: 1 rows
- `Lovable 4`: 1 rows
- `INS65`: 1 rows
- `INS38`: 1 rows
- `INS30`: 1 rows
- `Business`: 1 rows
- `AJK Canada Insurance Holdings`: 1 rows

**rfc**
- `None`: 45 rows

**address_location_roles**
- `Business`: 44 rows
- `None`: 1 rows

**primary_contact_fax_extension**
- `None`: 45 rows

**certified_tax_accountant_name**
- `None`: 45 rows

**primary_contact_phone_extension**
- `None`: 45 rows

**report_folder**
- `None`: 45 rows

**legal_form**
- `None`: 45 rows

**address_longitude**
- `0`: 45 rows

**person_in_charge**
- `None`: 45 rows

**primary_contact_phone_is_mobile**
- `No`: 45 rows

**address_valid_from**
- `2026-11-04 15:30:38.0000000 +00:00`: 1 rows
- `2026-11-04 10:28:46.0000000 +00:00`: 1 rows
- `2026-11-04 15:30:20.0000000 +00:00`: 1 rows
- `2026-11-04 10:32:30.0000000 +00:00`: 1 rows
- `2026-11-05 09:49:52.0000000 +00:00`: 1 rows
- `2026-11-04 10:27:12.0000000 +00:00`: 1 rows
- `2026-11-05 11:39:01.0000000 +00:00`: 1 rows
- `2026-11-04 15:30:56.0000000 +00:00`: 1 rows
- `2026-11-04 10:29:52.0000000 +00:00`: 1 rows
- `2026-11-04 10:29:13.0000000 +00:00`: 1 rows
- `2026-11-04 10:33:11.0000000 +00:00`: 1 rows
- `2026-11-05 11:40:20.0000000 +00:00`: 1 rows
- `2026-11-04 10:25:31.0000000 +00:00`: 1 rows
- `2026-11-04 10:32:14.0000000 +00:00`: 1 rows
- `2026-11-04 15:26:34.0000000 +00:00`: 1 rows
- `2026-11-05 11:40:07.0000000 +00:00`: 1 rows
- `2026-11-05 11:42:36.0000000 +00:00`: 1 rows
- `2026-11-04 15:31:14.0000000 +00:00`: 1 rows
- `2026-11-05 11:41:44.0000000 +00:00`: 1 rows
- `2026-11-04 10:30:10.0000000 +00:00`: 1 rows
- `2026-11-04 14:11:26.0000000 +00:00`: 1 rows
- `2026-11-04 10:33:36.0000000 +00:00`: 1 rows
- `2026-11-05 11:42:22.0000000 +00:00`: 1 rows
- `2026-11-04 10:32:53.0000000 +00:00`: 1 rows
- `2026-11-05 11:37:44.0000000 +00:00`: 1 rows
- `2026-11-04 10:29:33.0000000 +00:00`: 1 rows
- `2026-11-05 11:40:31.0000000 +00:00`: 1 rows
- `2026-11-05 11:41:09.0000000 +00:00`: 1 rows
- `2026-11-05 11:38:33.0000000 +00:00`: 1 rows
- `2026-10-15 12:25:55.0000000 +00:00`: 1 rows
- `2026-11-05 11:38:20.0000000 +00:00`: 1 rows
- `2026-10-15 12:26:13.0000000 +00:00`: 1 rows
- `2026-10-15 12:26:25.0000000 +00:00`: 1 rows
- `2026-11-04 10:30:26.0000000 +00:00`: 1 rows
- `2026-10-15 12:27:22.0000000 +00:00`: 1 rows
- `1900-01-01 00:00:00.0000000 +00:00`: 1 rows
- `2026-11-05 11:38:46.0000000 +00:00`: 1 rows
- `2026-11-13 17:53:24.0000000 +00:00`: 1 rows
- `2026-10-15 12:27:07.0000000 +00:00`: 1 rows
- `2026-11-05 11:40:56.0000000 +00:00`: 1 rows
- `2026-11-04 10:26:49.0000000 +00:00`: 1 rows
- `2026-11-05 09:51:02.0000000 +00:00`: 1 rows
- `2026-11-04 10:31:51.0000000 +00:00`: 1 rows
- `2026-11-04 10:31:26.0000000 +00:00`: 1 rows
- `2026-11-05 11:39:29.0000000 +00:00`: 1 rows

**primary_contact_fax_purpose**
- `None`: 45 rows

**primary_contact_telex_description**
- `None`: 45 rows

**print_corrective_invoice_starting_date**
- `1900-01-01 12:00:00.0000000 +00:00`: 45 rows

**primary_contact_phone_description**
- `None`: 45 rows

**legal_nature**
- `None`: 45 rows

**name_alias**
- `Royal Premium Budget`: 2 rows
- `Pinnacle Ventures`: 1 rows
- `RBJ`: 1 rows
- `Burns & Wilcox, Ltd`: 1 rows
- `AJK Enterprises, Inc`: 1 rows
- `Sterling Enterprises`: 1 rows
- `AJK Canada Insurance`: 1 rows
- `Evergreen Solutions`: 1 rows
- `Noremac Marketing`: 1 rows
- `Canadian Reports`: 1 rows
- `PrimeEdge Inc.`: 1 rows
- `INS63`: 1 rows
- `Node`: 1 rows
- `HWKGL`: 1 rows
- `INS36`: 1 rows
- `INS27`: 1 rows
- `Burns & Wilcox, LTD`: 1 rows
- `INS59`: 1 rows
- `Grandview Holdings`: 1 rows
- `INS33`: 1 rows
- `CAN`: 1 rows
- `Global Excess Partne`: 1 rows
- `INS25`: 1 rows
- `INS24`: 1 rows
- `CIBL`: 1 rows
- `Burns & Wilcox, RE`: 1 rows
- `A.J. Kaufman Institu`: 1 rows
- `INS14`: 1 rows
- `INS08`: 1 rows
- `INS62`: 1 rows
- `US Reports`: 1 rows
- `Burns & Wilcox Canad`: 1 rows
- `HKEUR`: 1 rows
- `INS28`: 1 rows
- `INSHOLDING`: 1 rows
- `Company accounts dat`: 1 rows
- `INS65`: 1 rows
- `Node International`: 1 rows
- `AJK Enterprises`: 1 rows
- `INS26`: 1 rows
- `INS38`: 1 rows
- `INS01`: 1 rows
- `INS30`: 1 rows
- `RB Jones, Marine`: 1 rows

**trader_number**
- `None`: 45 rows

**address_country_region_iso_code**
- `US`: 31 rows
- `CA`: 7 rows
- `GB`: 6 rows
- `None`: 1 rows

**print_inn_kpp_in_address**
- `No`: 45 rows

**primary_contact_twitter_purpose**
- `None`: 45 rows

**time_zone**
- `GMT_COORDINATEDUNIVERSALTIME`: 44 rows
- `GMTMINUS0800PACIFICTIME`: 1 rows

**business_item**
- `None`: 45 rows

**primary_address_location_id**
- `9103`: 1 rows
- `None`: 1 rows
- `9011`: 1 rows
- `7401`: 1 rows
- `9210`: 1 rows
- `9012`: 1 rows
- `9213`: 1 rows
- `9207`: 1 rows
- `9008`: 1 rows
- `7404`: 1 rows
- `9002`: 1 rows
- `9203`: 1 rows
- `9106`: 1 rows
- `9215`: 1 rows
- `9015`: 1 rows
- `9101`: 1 rows
- `9214`: 1 rows
- `9205`: 1 rows
- `9006`: 1 rows
- `7405`: 1 rows
- `9001`: 1 rows
- `9206`: 1 rows
- `9204`: 1 rows
- `9009`: 1 rows
- `9005`: 1 rows
- `9102`: 1 rows
- `9104`: 1 rows
- `9301`: 1 rows
- `9212`: 1 rows
- `9105`: 1 rows
- `9216`: 1 rows
- `9208`: 1 rows
- `9014`: 1 rows
- `9010`: 1 rows
- `9209`: 1 rows
- `7403`: 1 rows
- `9003`: 1 rows
- `9007`: 1 rows
- `9202`: 1 rows
- `7402`: 1 rows
- `9201`: 1 rows
- `9211`: 1 rows
- `9004`: 1 rows
- `9016`: 1 rows
- `9013`: 1 rows

**primary_contact_twitter**
- `None`: 45 rows

**primary_contact_telex**
- `None`: 45 rows

**initial_capital_investment**
- `0`: 45 rows

**primary_contact_facebook_description**
- `None`: 45 rows

**party_number**
- `7408`: 1 rows
- `5505`: 1 rows
- `7212`: 1 rows
- `8401`: 1 rows
- `7405`: 1 rows
- `7216`: 1 rows
- `7414`: 1 rows
- `7215`: 1 rows
- `7406`: 1 rows
- `7404`: 1 rows
- `7303`: 1 rows
- `5502`: 1 rows
- `{2CE71508-E13F-48A0-BB18-0B3518F330D3}`: 1 rows
- `7302`: 1 rows
- `7207`: 1 rows
- `5503`: 1 rows
- `7407`: 1 rows
- `7415`: 1 rows
- `7209`: 1 rows
- `7410`: 1 rows
- `7204`: 1 rows
- `7409`: 1 rows
- `7214`: 1 rows
- `7203`: 1 rows
- `7419`: 1 rows
- `7201`: 1 rows
- `7306`: 1 rows
- `7416`: 1 rows
- `7205`: 1 rows
- `5504`: 1 rows
- `7412`: 1 rows
- `7206`: 1 rows
- `7202`: 1 rows
- `7301`: 1 rows
- `7411`: 1 rows
- `7304`: 1 rows
- `7305`: 1 rows
- `7417`: 1 rows
- `7211`: 1 rows
- `7213`: 1 rows
- `5501`: 1 rows
- `7210`: 1 rows
- `7208`: 1 rows
- `7413`: 1 rows
- `7418`: 1 rows

**primary_contact_phone**
- `None`: 45 rows

**address_state**
- `None`: 45 rows

**use_for_financial_elimination_process**
- `No`: 43 rows
- `Yes`: 2 rows

**curp_legal_representative**
- `None`: 45 rows

**legal_representative_name**
- `None`: 45 rows

**fi_creditor_id**
- `None`: 45 rows

**address_city**
- `None`: 45 rows

**address_books**
- `None`: 45 rows

**address_zip_code**
- `None`: 45 rows

**state_inscription**
- `None`: 45 rows

**name**
- `Royal Premium Budget`: 2 rows
- `A.J. Kaufman Institute, LLC`: 1 rows
- `RBJ`: 1 rows
- `Burns & Wilcox, Ltd`: 1 rows
- `INS62`: 1 rows
- `HWKGL`: 1 rows
- `INS63`: 1 rows
- `Global Excess Partners`: 1 rows
- `Noremac Marketing`: 1 rows
- `Canadian Reports`: 1 rows
- `DAT`: 1 rows
- `Sterling Enterprises`: 1 rows
- `Node`: 1 rows
- `INS24`: 1 rows
- `Evergreen Solutions`: 1 rows
- `RB Jones, Marine`: 1 rows
- `Burns & Wilcox, LTD`: 1 rows
- `INS33`: 1 rows
- `Grandview Holdings`: 1 rows
- `Burns & Wilcox Canada Claims`: 1 rows
- `CAN`: 1 rows
- `AJK Enterprises, Inc.`: 1 rows
- `CIBL`: 1 rows
- `INS36`: 1 rows
- `PrimeEdge Inc.`: 1 rows
- `INS27`: 1 rows
- `INS14`: 1 rows
- `Pinnacle Ventures`: 1 rows
- `INS08`: 1 rows
- `INS59`: 1 rows
- `US Reports`: 1 rows
- `INSHOLDING`: 1 rows
- `HKEUR`: 1 rows
- `INS28`: 1 rows
- `Burns & Wilcox, RE`: 1 rows
- `INS25`: 1 rows
- `INS65`: 1 rows
- `Node International`: 1 rows
- `AJK Enterprises`: 1 rows
- `INS26`: 1 rows
- `INS38`: 1 rows
- `INS01`: 1 rows
- `INS30`: 1 rows
- `AJK Canada Insurance Holdings`: 1 rows

**primary_contact_linkedin**
- `None`: 45 rows

**primary_contact_facebook_purpose**
- `None`: 45 rows

**primary_contact_url**
- `None`: 45 rows

**primary_contact_url_description**
- `None`: 45 rows

**address_latitude**
- `0`: 45 rows

**registration_number**
- `None`: 45 rows

**primary_contact_telex_purpose**
- `None`: 45 rows

**rfc_legal_representative**
- `None`: 45 rows

**print_enterprise_register**
- `No`: 45 rows

**address_street**
- `None`: 45 rows

**accounting_personnel**
- `None`: 45 rows

**phonetic_name**
- `None`: 45 rows

**commerce_registration**
- `None`: 45 rows

**full_primary_address**
- `USA`: 31 rows
- `CAN`: 7 rows
- `GBR`: 6 rows
- `None`: 1 rows

**primary_contact_linkedin_is_private**
- `No`: 45 rows

**primary_contact_twitter_is_private**
- `No`: 45 rows

**naics**
- `None`: 45 rows

**primary_contact_url_purpose**
- `None`: 45 rows

**software_identification_code**
- `None`: 38 rows
- `AX030003`: 7 rows

**address_country_region_id**
- `USA`: 31 rows
- `CAN`: 7 rows
- `GBR`: 6 rows
- `None`: 1 rows

**address_district_name**
- `None`: 45 rows

**start_date_of_business**
- `1900-01-01 12:00:00.0000000 +00:00`: 45 rows

**language_id**
- `None`: 45 rows

**use_for_financial_consolidation_process**
- `No`: 43 rows
- `Yes`: 2 rows

**primary_contact_fax**
- `None`: 45 rows

**print_corrective_invoice**
- `No`: 45 rows

**dnb_routing_number**
- `None`: 45 rows

**primary_contact_fax_description**
- `None`: 45 rows

**primary_contact_twitter_description**
- `None`: 45 rows

**fiscal_code**
- `None`: 45 rows

**address_county**
- `None`: 45 rows

**accounts_office_reference_number**
- `None`: 45 rows

**primary_contact_linkedin_purpose**
- `None`: 45 rows

**address_valid_to**
- `2154-12-31 23:59:59.0000000 +00:00`: 44 rows
- `1900-01-01 00:00:00.0000000 +00:00`: 1 rows

**localization_country_region_code**
- `Default`: 45 rows

**vat_on_customer_behalf**
- `No`: 45 rows

**vat_num**
- `None`: 45 rows

**profit_margin_scheme**
- `No`: 45 rows

**vat_refund**
- `No`: 45 rows

**import_vat_num**
- `None`: 45 rows

**source_file_name**
- `legalentities__20261116_105417.csv`: 45 rows

**mdp_created_date**
- `2026-11-16 11:43:00.551016+00:00`: 45 rows

**mdp_modified_date**
- `2026-11-16 11:43:00.551016+00:00`: 45 rows

## Profile

Rows in the latest export: 45.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `legal_entity_id` | STRING | 44 | 0 |  |  |
| `primary_contact_facebook_is_private` | STRING | 1 | 0 | No | No |
| `primary_contact_linkedin_description` | STRING | 0 | 45 |  |  |
| `primary_contact_phone_purpose` | STRING | 0 | 45 |  |  |
| `primary_contact_facebook` | STRING | 0 | 45 |  |  |
| `address_time_zone` | STRING | 0 | 45 |  |  |
| `curp_number` | STRING | 0 | 45 |  |  |
| `national_registry_number` | STRING | 0 | 45 |  |  |
| `cuc` | STRING | 0 | 45 |  |  |
| `external_legal_representative_name` | STRING | 0 | 45 |  |  |
| `address_description` | STRING | 42 | 1 | A.J. Kaufman Institute, LLC | US Reports |
| `rfc` | STRING | 0 | 45 |  |  |
| `address_location_roles` | STRING | 1 | 1 | Business | Business |
| `primary_contact_fax_extension` | STRING | 0 | 45 |  |  |
| `certified_tax_accountant_name` | STRING | 0 | 45 |  |  |
| `primary_contact_phone_extension` | STRING | 0 | 45 |  |  |
| `report_folder` | STRING | 0 | 45 |  |  |
| `legal_form` | STRING | 0 | 45 |  |  |
| `address_longitude` | STRING | 1 | 0 | 0 | 0 |
| `company_name` | STRING | 0 | 45 |  |  |
| `person_in_charge` | STRING | 0 | 45 |  |  |
| `national_classification_of_company_economic_activity` | STRING | 0 | 45 |  |  |
| `primary_contact_phone_is_mobile` | STRING | 1 | 0 | No | No |
| `address_valid_from` | STRING | 45 | 0 | 1900-01-01 00:00:00.0000000 +00:00 | 2026-11-13 17:53:24.0000000 +00:00 |
| `primary_contact_fax_purpose` | STRING | 0 | 45 |  |  |
| `primary_contact_telex_description` | STRING | 0 | 45 |  |  |
| `print_corrective_invoice_starting_date` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `primary_contact_phone_description` | STRING | 0 | 45 |  |  |
| `legal_nature` | STRING | 0 | 45 |  |  |
| `name_alias` | STRING | 44 | 0 | A.J. Kaufman Institu | US Reports |
| `trader_number` | STRING | 0 | 45 |  |  |
| `address_country_region_iso_code` | STRING | 3 | 1 | CA | US |
| `print_inn_kpp_in_address` | STRING | 1 | 0 | No | No |
| `primary_contact_twitter_purpose` | STRING | 0 | 45 |  |  |
| `primary_contact_email_description` | STRING | 0 | 45 |  |  |
| `time_zone` | STRING | 2 | 0 | GMTMINUS0800PACIFICTIME | GMT_COORDINATEDUNIVERSALTIME |
| `business_item` | STRING | 0 | 45 |  |  |
| `primary_address_location_id` | STRING | 44 | 1 | 7401 | 9301 |
| `primary_contact_email_purpose` | STRING | 0 | 45 |  |  |
| `primary_contact_twitter` | STRING | 0 | 45 |  |  |
| `primary_contact_telex` | STRING | 0 | 45 |  |  |
| `initial_capital_investment` | STRING | 1 | 0 | 0 | 0 |
| `primary_contact_facebook_description` | STRING | 0 | 45 |  |  |
| `party_number` | STRING | 45 | 0 | 5501 | {2CE71508-E13F-48A0-BB18-0B3518F330D3} |
| `primary_contact_phone` | STRING | 0 | 45 |  |  |
| `address_state` | STRING | 0 | 45 |  |  |
| `use_for_financial_elimination_process` | STRING | 2 | 0 | No | Yes |
| `curp_legal_representative` | STRING | 0 | 45 |  |  |
| `legal_representative_name` | STRING | 0 | 45 |  |  |
| `fi_creditor_id` | STRING | 0 | 45 |  |  |
| `address_city` | STRING | 0 | 45 |  |  |
| `address_books` | STRING | 0 | 45 |  |  |
| `address_zip_code` | STRING | 0 | 45 |  |  |
| `state_inscription` | STRING | 0 | 45 |  |  |
| `primary_contact_email` | STRING | 0 | 45 |  |  |
| `name` | STRING | 43 | 0 | A.J. Kaufman Institute, LLC | US Reports |
| `primary_contact_linkedin` | STRING | 0 | 45 |  |  |
| `primary_contact_facebook_purpose` | STRING | 0 | 45 |  |  |
| `company_country` | STRING | 0 | 45 |  |  |
| `primary_contact_url` | STRING | 0 | 45 |  |  |
| `primary_contact_url_description` | STRING | 0 | 45 |  |  |
| `address_latitude` | STRING | 1 | 0 | 0 | 0 |
| `registration_number` | STRING | 0 | 45 |  |  |
| `primary_contact_telex_purpose` | STRING | 0 | 45 |  |  |
| `rfc_legal_representative` | STRING | 0 | 45 |  |  |
| `primary_contact_email_is_im` | STRING | 1 | 0 |  |  |
| `print_enterprise_register` | STRING | 1 | 0 | No | No |
| `company_type` | STRING | 1 | 0 |  |  |
| `address_street` | STRING | 0 | 45 |  |  |
| `accounting_personnel` | STRING | 0 | 45 |  |  |
| `phonetic_name` | STRING | 0 | 45 |  |  |
| `commerce_registration` | STRING | 0 | 45 |  |  |
| `full_primary_address` | STRING | 3 | 1 | CAN | USA |
| `primary_contact_linkedin_is_private` | STRING | 1 | 0 | No | No |
| `primary_contact_twitter_is_private` | STRING | 1 | 0 | No | No |
| `company_representative` | STRING | 0 | 45 |  |  |
| `naics` | STRING | 0 | 45 |  |  |
| `primary_contact_url_purpose` | STRING | 0 | 45 |  |  |
| `software_identification_code` | STRING | 1 | 38 | AX030003 | AX030003 |
| `address_country_region_id` | STRING | 3 | 1 | CAN | USA |
| `address_district_name` | STRING | 0 | 45 |  |  |
| `start_date_of_business` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `language_id` | STRING | 0 | 45 |  |  |
| `use_for_financial_consolidation_process` | STRING | 2 | 0 | No | Yes |
| `primary_contact_fax` | STRING | 0 | 45 |  |  |
| `print_corrective_invoice` | STRING | 1 | 0 | No | No |
| `dnb_routing_number` | STRING | 0 | 45 |  |  |
| `primary_contact_fax_description` | STRING | 0 | 45 |  |  |
| `primary_contact_twitter_description` | STRING | 0 | 45 |  |  |
| `fiscal_code` | STRING | 0 | 45 |  |  |
| `address_county` | STRING | 0 | 45 |  |  |
| `accounts_office_reference_number` | STRING | 0 | 45 |  |  |
| `primary_contact_linkedin_purpose` | STRING | 0 | 45 |  |  |
| `address_valid_to` | STRING | 2 | 0 | 1900-01-01 00:00:00.0000000 +00:00 | 2154-12-31 23:59:59.0000000 +00:00 |
| `localization_country_region_code` | STRING | 1 | 0 | Default | Default |
| `vat_on_customer_behalf` | STRING | 1 | 0 | No | No |
| `vat_num` | STRING | 0 | 45 |  |  |
| `profit_margin_scheme` | STRING | 1 | 0 | No | No |
| `vat_refund` | STRING | 1 | 0 | No | No |
| `import_vat_num` | STRING | 0 | 45 |  |  |
| `source_file_name` | STRING | 1 | 0 | legalentities__20261116_105417.csv | legalentities__20261116_105417.csv |
| `hash_key` | STRING | 44 | 0 |  |  |
| `mdp_created_by` | STRING | 1 | 0 |  |  |
| `mdp_created_date` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:00.551000 | 2026-11-16 11:43:00.551000 |
| `mdp_modified_by` | STRING | 1 | 0 |  |  |
| `mdp_modified_date` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:00.551000 | 2026-11-16 11:43:00.551000 |

## Sample rows

| primary_contact_facebook_is_private | primary_contact_linkedin_description | primary_contact_phone_purpose | primary_contact_facebook | address_time_zone | curp_number | national_registry_number | cuc | external_legal_representative_name | address_description | rfc | address_location_roles | primary_contact_fax_extension | certified_tax_accountant_name | primary_contact_phone_extension | report_folder | legal_form | address_longitude | person_in_charge | primary_contact_phone_is_mobile | address_valid_from | primary_contact_fax_purpose | primary_contact_telex_description | print_corrective_invoice_starting_date | primary_contact_phone_description | legal_nature | name_alias | trader_number | address_country_region_iso_code | print_inn_kpp_in_address | primary_contact_twitter_purpose | primary_contact_email_description | time_zone | business_item | primary_address_location_id | primary_contact_email_purpose | primary_contact_twitter | primary_contact_telex | initial_capital_investment | primary_contact_facebook_description | party_number | primary_contact_phone | address_state | use_for_financial_elimination_process | curp_legal_representative | legal_representative_name | fi_creditor_id | address_city | address_books | address_zip_code | state_inscription | primary_contact_email | name | primary_contact_linkedin | primary_contact_facebook_purpose | primary_contact_url | primary_contact_url_description | address_latitude | registration_number | primary_contact_telex_purpose | rfc_legal_representative | primary_contact_email_is_im | print_enterprise_register | address_street | accounting_personnel | phonetic_name | commerce_registration | full_primary_address | primary_contact_linkedin_is_private | primary_contact_twitter_is_private | naics | primary_contact_url_purpose | software_identification_code | address_country_region_id | address_district_name | start_date_of_business | language_id | use_for_financial_consolidation_process | primary_contact_fax | print_corrective_invoice | dnb_routing_number | primary_contact_fax_description | primary_contact_twitter_description | fiscal_code | address_county | accounts_office_reference_number | primary_contact_linkedin_purpose | address_valid_to | localization_country_region_code | vat_on_customer_behalf | vat_num | profit_margin_scheme | vat_refund | import_vat_num | source_file_name | mdp_created_by | mdp_created_date | mdp_modified_by | mdp_modified_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | No | 1900-01-01 00:00:00.0000000 +00:00 | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | Company accounts dat | NULL | NULL | No | NULL | <masked> | GMTMINUS0800PACIFICTIME | NULL | NULL | <masked> | NULL | NULL | 0 | NULL | {2CE71508-E13F-48A0-BB18-0B3518F330D3} | NULL | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | DAT | NULL | NULL | NULL | NULL | 0 | NULL | NULL | NULL | <masked> | No | NULL | NULL | NULL | NULL | NULL | No | No | NULL | NULL | NULL | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 1900-01-01 00:00:00.0000000 +00:00 | Default | No | NULL | No | No | NULL | legalentities__20261116_105417.csv | <masked> | 2026-11-16 11:43:00.551000 | <masked> | 2026-11-16 11:43:00.551000 |
| No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Busines | NULL | Business | NULL | NULL | NULL | NULL | NULL | 0 | NULL | No | 2026-10-15 12:25:55.0000000 +00:00 | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | Evergreen Solutions | NULL | US | No | NULL | <masked> | GMT_COORDINATEDUNIVERSALTIME | NULL | 7401 | <masked> | NULL | NULL | 0 | NULL | 5501 | NULL | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | Evergreen Solutions | NULL | NULL | NULL | NULL | 0 | NULL | NULL | NULL | <masked> | No | NULL | NULL | NULL | NULL | USA | No | No | NULL | NULL | NULL | USA | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2154-12-31 23:59:59.0000000 +00:00 | Default | No | NULL | No | No | NULL | legalentities__20261116_105417.csv | <masked> | 2026-11-16 11:43:00.551000 | <masked> | 2026-11-16 11:43:00.551000 |
| No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Business | NULL | Business | NULL | NULL | NULL | NULL | NULL | 0 | NULL | No | 2026-10-15 12:26:13.0000000 +00:00 | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | PrimeEdge Inc. | NULL | US | No | NULL | <masked> | GMT_COORDINATEDUNIVERSALTIME | NULL | 7402 | <masked> | NULL | NULL | 0 | NULL | 5502 | NULL | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | PrimeEdge Inc. | NULL | NULL | NULL | NULL | 0 | NULL | NULL | NULL | <masked> | No | NULL | NULL | NULL | NULL | USA | No | No | NULL | NULL | NULL | USA | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2154-12-31 23:59:59.0000000 +00:00 | Default | No | NULL | No | No | NULL | legalentities__20261116_105417.csv | <masked> | 2026-11-16 11:43:00.551000 | <masked> | 2026-11-16 11:43:00.551000 |
| No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Lovable 3 | NULL | Business | NULL | NULL | NULL | NULL | NULL | 0 | NULL | No | 2026-10-15 12:26:25.0000000 +00:00 | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | Sterling Enterprises | NULL | US | No | NULL | <masked> | GMT_COORDINATEDUNIVERSALTIME | NULL | 7403 | <masked> | NULL | NULL | 0 | NULL | 5503 | NULL | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | Sterling Enterprises | NULL | NULL | NULL | NULL | 0 | NULL | NULL | NULL | <masked> | No | NULL | NULL | NULL | NULL | USA | No | No | NULL | NULL | NULL | USA | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2154-12-31 23:59:59.0000000 +00:00 | Default | No | NULL | No | No | NULL | legalentities__20261116_105417.csv | <masked> | 2026-11-16 11:43:00.551000 | <masked> | 2026-11-16 11:43:00.551000 |
| No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Lovable 4 | NULL | Business | NULL | NULL | NULL | NULL | NULL | 0 | NULL | No | 2026-10-15 12:27:07.0000000 +00:00 | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | Grandview Holdings | NULL | US | No | NULL | <masked> | GMT_COORDINATEDUNIVERSALTIME | NULL | 7404 | <masked> | NULL | NULL | 0 | NULL | 5504 | NULL | NULL | Yes | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | Grandview Holdings | NULL | NULL | NULL | NULL | 0 | NULL | NULL | NULL | <masked> | No | NULL | NULL | NULL | NULL | USA | No | No | NULL | NULL | NULL | USA | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | Yes | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2154-12-31 23:59:59.0000000 +00:00 | Default | No | NULL | No | No | NULL | legalentities__20261116_105417.csv | <masked> | 2026-11-16 11:43:00.551000 | <masked> | 2026-11-16 11:43:00.551000 |
