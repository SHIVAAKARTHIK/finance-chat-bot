---
name: dim_customers_v3
schema: silver
layer: silver
domain: ar
type: table
status: active
purpose: D365 customer master (account; party type; address; tax settings).
grain: one row per HASH_KEY (one customer)
primary_key:
- HASH_KEY
entity_column: dataAreaId
period_columns: []
pii_columns:
- PrimaryContactEmailIsIM
- PrimaryContactEmail
- PrimaryContactEmailDescription
- ReceiptEmail
- PrimaryContactEmailPurpose
- PrimaryContactEmailRecordId
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: AddressBrazilianCNPJOrCPF, SalesTaxGroup all null
row_count: 3
proposed_fields:
- grain
- primary_key
reviewed: false
---

# dim_customers_v3

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `dataAreaId` | string |  |  | `dataAreaId` |
| `CustomerAccount` | string |  |  | `CustomerAccount` |
| `AddressBrazilianCNPJOrCPF` | string |  |  | `AddressBrazilianCNPJOrCPF` |
| `PartyType` | string |  |  | `PartyType` |
| `PrimaryContactFaxExtension` | string |  |  | `PrimaryContactFaxExtension` |
| `IsFuelSurchargeApplied` | string |  |  | `IsFuelSurchargeApplied` |
| `SalesTaxGroup` | string |  |  | `SalesTaxGroup` |
| `AddressCountryRegionId` | string |  |  | `AddressCountryRegionId` |
| `ContactPersonId` | string |  |  | `ContactPersonId` |
| `CustomerPaymentFineCode` | string |  |  | `CustomerPaymentFineCode` |
| `BirthCountyCode` | string |  |  | `BirthCountyCode` |
| `InvoiceAddress` | string |  |  | `InvoiceAddress` |
| `PackingMaterialFeeLicenseNumber` | string |  |  | `PackingMaterialFeeLicenseNumber` |
| `TransactionPresenceType` | string |  |  | `TransactionPresenceType` |
| `PrimaryContactTwitter` | string |  |  | `PrimaryContactTwitter` |
| `PrimaryContactEmailIsIM` | string |  |  | `PrimaryContactEmailIsIM` |
| `InvoiceAddressCity` | string |  |  | `InvoiceAddressCity` |
| `IsFinalUser` | string |  |  | `IsFinalUser` |
| `PrimaryContactEmail` | string |  |  | `PrimaryContactEmail` |
| `DeliveryAddressCounty` | string |  |  | `DeliveryAddressCounty` |
| `HasSuframaDiscountPISandCOFINS` | string |  |  | `HasSuframaDiscountPISandCOFINS` |
| `InvoiceAddressStreet` | string |  |  | `InvoiceAddressStreet` |
| `CURPNumber` | string |  |  | `CURPNumber` |
| `PrimaryContactLinkedInDescription` | string |  |  | `PrimaryContactLinkedInDescription` |
| `DeliveryAddressCountryRegionId` | string |  |  | `DeliveryAddressCountryRegionId` |
| `ItemCustomerGroupId` | string |  |  | `ItemCustomerGroupId` |
| `PersonProfessionalTitle` | string |  |  | `PersonProfessionalTitle` |
| `SalesSegmentId` | string |  |  | `SalesSegmentId` |
| `IsServiceDeliveryAddressBased` | string |  |  | `IsServiceDeliveryAddressBased` |
| `PrimaryContactTelexDescription` | string |  |  | `PrimaryContactTelexDescription` |
| `InvoiceAddressDistrictName` | string |  |  | `InvoiceAddressDistrictName` |
| `InvoiceAddressTimeZone` | string |  |  | `InvoiceAddressTimeZone` |
| `SalesAccountNumber` | string |  |  | `SalesAccountNumber` |
| `PrimaryContactFacebookDescription` | string |  |  | `PrimaryContactFacebookDescription` |
| `PrimaryContactPhoneIsMobile` | string |  |  | `PrimaryContactPhoneIsMobile` |
| `PrimaryContactFaxRecordId` | string |  |  | `PrimaryContactFaxRecordId` |
| `TCSGroup` | string |  |  | `TCSGroup` |
| `DeliveryAddressLocationId` | string |  |  | `DeliveryAddressLocationId` |
| `InterCompanyAutoCreateOrders` | string |  |  | `InterCompanyAutoCreateOrders` |
| `AddressZipCode` | string |  |  | `AddressZipCode` |
| `GiroTypeProjInvoice` | string |  |  | `GiroTypeProjInvoice` |
| `LineOfBusinessId` | string |  |  | `LineOfBusinessId` |
| `OrganizationPhoneticName` | string |  |  | `OrganizationPhoneticName` |
| `CreditCardCVC` | string |  |  | `CreditCardCVC` |
| `DeliveryAddressCountryRegionISOCode` | string |  |  | `DeliveryAddressCountryRegionISOCode` |
| `DeliveryAddressValidFrom` | string |  |  | `DeliveryAddressValidFrom` |
| `GiroTypeAccountStatement` | string |  |  | `GiroTypeAccountStatement` |
| `CalculateWithholdingTax` | string |  |  | `CalculateWithholdingTax` |
| `ElectronicInvoiceEAN` | string |  |  | `ElectronicInvoiceEAN` |
| `DeliveryFreightZone` | string |  |  | `DeliveryFreightZone` |
| `PrimaryContactFax` | string |  |  | `PrimaryContactFax` |
| `TaxExemptNumber` | string |  |  | `TaxExemptNumber` |
| `DeliveryAddressDescription` | string |  |  | `DeliveryAddressDescription` |
| `DeliveryAddressLongitude` | string |  |  | `DeliveryAddressLongitude` |
| `BirthPlace` | string |  |  | `BirthPlace` |
| `AddressCity` | string |  |  | `AddressCity` |
| `PersonInitials` | string |  |  | `PersonInitials` |
| `DefaultECommerceOperator` | string |  |  | `DefaultECommerceOperator` |
| `CentralBankPurposeCode` | string |  |  | `CentralBankPurposeCode` |
| `GiroTypeCollectionletter` | string |  |  | `GiroTypeCollectionletter` |
| `FullPrimaryAddress` | string |  |  | `FullPrimaryAddress` |
| `OrderEntryDeadline` | string |  |  | `OrderEntryDeadline` |
| `ForeignerId` | string |  |  | `ForeignerId` |
| `WarehouseIsASNGenerated` | string |  |  | `WarehouseIsASNGenerated` |
| `AddressLongitude` | string |  |  | `AddressLongitude` |
| `CustomerType` | string |  |  | `CustomerType` |
| `PrimaryContactLinkedIn` | string |  |  | `PrimaryContactLinkedIn` |
| `PrimaryContactURL` | string |  |  | `PrimaryContactURL` |
| `IsFreightAccrued` | string |  |  | `IsFreightAccrued` |
| `PartyState` | string |  |  | `PartyState` |
| `PartyNumber` | string |  |  | `PartyNumber` |
| `InvoiceAccount` | string |  |  | `InvoiceAccount` |
| `CentralBankPurposeNotes` | string |  |  | `CentralBankPurposeNotes` |
| `AddressBuildingComplement` | string |  |  | `AddressBuildingComplement` |
| `CollectionsContactPersonId` | string |  |  | `CollectionsContactPersonId` |
| `PersonMaritalStatus` | string |  |  | `PersonMaritalStatus` |
| `AddressLocationId` | string |  |  | `AddressLocationId` |
| `PaymentSchedule` | string |  |  | `PaymentSchedule` |
| `PrimaryContactTwitterPurpose` | string |  |  | `PrimaryContactTwitterPurpose` |
| `GiroType` | string |  |  | `GiroType` |
| `InvoiceAddressDescription` | string |  |  | `InvoiceAddressDescription` |
| `AddressDistrictName` | string |  |  | `AddressDistrictName` |
| `DeliveryTerms` | string |  |  | `DeliveryTerms` |
| `NumberSequenceGroup` | string |  |  | `NumberSequenceGroup` |
| `PersonChildrenNames` | string |  |  | `PersonChildrenNames` |
| `PaymentMethod` | string |  |  | `PaymentMethod` |
| `ForeignResident` | string |  |  | `ForeignResident` |
| `DeliveryMode` | string |  |  | `DeliveryMode` |
| `PersonProfessionalSuffix` | string |  |  | `PersonProfessionalSuffix` |
| `OnHoldStatus` | string |  |  | `OnHoldStatus` |
| `WarehouseId` | string |  |  | `WarehouseId` |
| `AccountStatement` | string |  |  | `AccountStatement` |
| `DestinationCode` | string |  |  | `DestinationCode` |
| `EInvoiceRegister` | string |  |  | `EInvoiceRegister` |
| `IRS1099CIndicator` | string |  |  | `IRS1099CIndicator` |
| `FrenchSiret` | string |  |  | `FrenchSiret` |
| `PaymentDay` | string |  |  | `PaymentDay` |
| `BrazilianNIT` | string |  |  | `BrazilianNIT` |
| `FederalIndicator` | string |  |  | `FederalIndicator` |
| `EmployeeResponsibleNumber` | string |  |  | `EmployeeResponsibleNumber` |
| `PersonAnniversaryYear` | string |  |  | `PersonAnniversaryYear` |
| `DefaultInventoryStatusId` | string |  |  | `DefaultInventoryStatusId` |
| `PrimaryContactEmailDescription` | string |  |  | `PrimaryContactEmailDescription` |
| `AddressTimeZone` | string |  |  | `AddressTimeZone` |
| `PrimaryContactPhone` | string |  |  | `PrimaryContactPhone` |
| `PrimaryContactPhoneRecordId` | string |  |  | `PrimaryContactPhoneRecordId` |
| `DeliveryAddressCity` | string |  |  | `DeliveryAddressCity` |
| `InvoiceAddressCounty` | string |  |  | `InvoiceAddressCounty` |
| `PANReferenceNumber` | string |  |  | `PANReferenceNumber` |
| `DeliveryAddressStreet` | string |  |  | `DeliveryAddressStreet` |
| `SalesCurrencyCode` | string |  |  | `SalesCurrencyCode` |
| `Priority` | string |  |  | `Priority` |
| `IsSalesTaxIncludedInPrices` | string |  |  | `IsSalesTaxIncludedInPrices` |
| `BrazilianCNPJOrCPF` | string |  |  | `BrazilianCNPJOrCPF` |
| `PaymentFactoringAccount` | string |  |  | `PaymentFactoringAccount` |
| `PANNumber` | string |  |  | `PANNumber` |
| `PrimaryContactTwitterDescription` | string |  |  | `PrimaryContactTwitterDescription` |
| `PersonFirstName` | string |  |  | `PersonFirstName` |
| `BrazilianCCM` | string |  |  | `BrazilianCCM` |
| `ReceiptEmail` | string |  |  | `ReceiptEmail` |
| `TDSGroup` | string |  |  | `TDSGroup` |
| `MultiLineDiscountCode` | string |  |  | `MultiLineDiscountCode` |
| `PersonAnniversaryDay` | string |  |  | `PersonAnniversaryDay` |
| `DefaultDimensionDisplayValue` | string |  |  | `DefaultDimensionDisplayValue` |
| `SupplementaryItemGroupId` | string |  |  | `SupplementaryItemGroupId` |
| `IsWithholdingTaxCalculated` | string |  |  | `IsWithholdingTaxCalculated` |
| `PaymentSpecification` | string |  |  | `PaymentSpecification` |
| `AddressRecordId` | string |  |  | `AddressRecordId` |
| `AddressBooks` | string |  |  | `AddressBooks` |
| `PrimaryContactEmailPurpose` | string |  |  | `PrimaryContactEmailPurpose` |
| `FulfillmentPolicyName` | string |  |  | `FulfillmentPolicyName` |
| `SalesDistrict` | string |  |  | `SalesDistrict` |
| `ConsolidationDay` | string |  |  | `ConsolidationDay` |
| `IsExpressBillOfLadingAccepted` | string |  |  | `IsExpressBillOfLadingAccepted` |
| `CreditCardAddressVerification` | string |  |  | `CreditCardAddressVerification` |
| `InvoiceAddressBuildingComplement` | string |  |  | `InvoiceAddressBuildingComplement` |
| `AddressState` | string |  |  | `AddressState` |
| `AllowOnAccount` | string |  |  | `AllowOnAccount` |
| `IsExcludedFromCollectionFeeCalculation` | string |  |  | `IsExcludedFromCollectionFeeCalculation` |
| `CustomerPaymentFinancialInterestCode` | string |  |  | `CustomerPaymentFinancialInterestCode` |
| `IsTransactionPostedAsShipment` | string |  |  | `IsTransactionPostedAsShipment` |
| `IsExternallyMaintained` | string |  |  | `IsExternallyMaintained` |
| `CreditLimitIsMandatory` | string |  |  | `CreditLimitIsMandatory` |
| `PaymentTermsBaseDays` | string |  |  | `PaymentTermsBaseDays` |
| `FiscalCode` | string |  |  | `FiscalCode` |
| `KnownAs` | string |  |  | `KnownAs` |
| `PrimaryContactTelex` | string |  |  | `PrimaryContactTelex` |
| `PaymentBankAccount` | string |  |  | `PaymentBankAccount` |
| `BrazilianIE` | string |  |  | `BrazilianIE` |
| `PrimaryContactEmailRecordId` | string |  |  | `PrimaryContactEmailRecordId` |
| `PreferentialCustomer` | string |  |  | `PreferentialCustomer` |
| `ReceiptOption` | string |  |  | `ReceiptOption` |
| `AddressBrazilianIE` | string |  |  | `AddressBrazilianIE` |
| `PersonAnniversaryMonth` | string |  |  | `PersonAnniversaryMonth` |
| `PrimaryContactPhoneExtension` | string |  |  | `PrimaryContactPhoneExtension` |
| `InvoiceAddressStreetNumber` | string |  |  | `InvoiceAddressStreetNumber` |
| `PrimaryContactPhonePurpose` | string |  |  | `PrimaryContactPhonePurpose` |
| `ExportSale` | string |  |  | `ExportSale` |
| `OrganizationNumber` | string |  |  | `OrganizationNumber` |
| `InvoicePostingType` | string |  |  | `InvoicePostingType` |
| `CreditCardAddressVerificationIsAuthorizationVoidedOnFailure` | string |  |  | `CreditCardAddressVerificationIsAuthorizationVoidedOnFailure` |
| `InvoiceAddressState` | string |  |  | `InvoiceAddressState` |
| `ReceiptCalendar` | string |  |  | `ReceiptCalendar` |
| `DeliveryAddressState` | string |  |  | `DeliveryAddressState` |
| `StateInscription` | string |  |  | `StateInscription` |
| `PersonLastNamePrefix` | string |  |  | `PersonLastNamePrefix` |
| `SalesReturnTaxGroup` | string |  |  | `SalesReturnTaxGroup` |
| `PrimaryContactURLDescription` | string |  |  | `PrimaryContactURLDescription` |
| `CustomerWithholdingContributionType` | string |  |  | `CustomerWithholdingContributionType` |
| `IsElectronicInvoice` | string |  |  | `IsElectronicInvoice` |
| `FederalAgencyLocationCode` | string |  |  | `FederalAgencyLocationCode` |
| `GiroTypeFreeTextInvoice` | string |  |  | `GiroTypeFreeTextInvoice` |
| `DeliveryAddressValidTo` | string |  |  | `DeliveryAddressValidTo` |
| `PersonPhoneticMiddleName` | string |  |  | `PersonPhoneticMiddleName` |
| `OrganizationABCCode` | string |  |  | `OrganizationABCCode` |
| `BrazilianCNAE` | string |  |  | `BrazilianCNAE` |
| `WithholdingTaxGroupCode` | string |  |  | `WithholdingTaxGroupCode` |
| `NAFCode` | string |  |  | `NAFCode` |
| `AddressLatitude` | string |  |  | `AddressLatitude` |
| `TotalDiscountCode` | string |  |  | `TotalDiscountCode` |
| `PaymentCashDiscount` | string |  |  | `PaymentCashDiscount` |
| `AddressLocationRoles` | string |  |  | `AddressLocationRoles` |
| `DeliveryAddressDistrictName` | string |  |  | `DeliveryAddressDistrictName` |
| `CollectionLetterCode` | string |  |  | `CollectionLetterCode` |
| `EInvoiceAttachment` | string |  |  | `EInvoiceAttachment` |
| `MerchantID` | string |  |  | `MerchantID` |
| `CreditRating` | string |  |  | `CreditRating` |
| `PrimaryContactFacebook` | string |  |  | `PrimaryContactFacebook` |
| `DeliveryAddressBuildingComplement` | string |  |  | `DeliveryAddressBuildingComplement` |
| `DeliveryAddressStreetNumber` | string |  |  | `DeliveryAddressStreetNumber` |
| `InvoiceAddressLongitude` | string |  |  | `InvoiceAddressLongitude` |
| `LineDiscountCode` | string |  |  | `LineDiscountCode` |
| `PartyCountry` | string |  |  | `PartyCountry` |
| `InvoiceAddressLatitude` | string |  |  | `InvoiceAddressLatitude` |
| `IsInSuframaRegion` | string |  |  | `IsInSuframaRegion` |
| `IsIncomingFiscalDocumentGenerated` | string |  |  | `IsIncomingFiscalDocumentGenerated` |
| `SalesMemo` | string |  |  | `SalesMemo` |
| `ReliefGroupId` | string |  |  | `ReliefGroupId` |
| `IsExcludedFromInterestChargeCalculation` | string |  |  | `IsExcludedFromInterestChargeCalculation` |
| `StatisticsGroupId` | string |  |  | `StatisticsGroupId` |
| `SalesOrderPoolId` | string |  |  | `SalesOrderPoolId` |
| `OrganizationName` | string |  |  | `OrganizationName` |
| `IsOrderNumberReferenceUsed` | string |  |  | `IsOrderNumberReferenceUsed` |
| `CustClassificationId` | string |  |  | `CustClassificationId` |
| `AddressValidTo` | string |  |  | `AddressValidTo` |
| `FederalComments` | string |  |  | `FederalComments` |
| `PersonGender` | string |  |  | `PersonGender` |
| `PaymentTerms` | string |  |  | `PaymentTerms` |
| `PrimaryContactPhoneDescription` | string |  |  | `PrimaryContactPhoneDescription` |
| `AddressPostbox` | string |  |  | `AddressPostbox` |
| `SalesSubsegmentId` | string |  |  | `SalesSubsegmentId` |
| `CustomerRebateGroupId` | string |  |  | `CustomerRebateGroupId` |
| `WarehouseOutboundShipmentProcessingPolicyName` | string |  |  | `WarehouseOutboundShipmentProcessingPolicyName` |
| `AddressCounty` | string |  |  | `AddressCounty` |
| `PrimaryContactURLRecordId` | string |  |  | `PrimaryContactURLRecordId` |
| `IsICMSContributor` | string |  |  | `IsICMSContributor` |
| `InvoiceAddressValidTo` | string |  |  | `InvoiceAddressValidTo` |
| `DeliveryAddressTimeZone` | string |  |  | `DeliveryAddressTimeZone` |
| `InvoiceAddressValidFrom` | string |  |  | `InvoiceAddressValidFrom` |
| `CreditLimit` | string |  |  | `CreditLimit` |
| `CreditCardAddressVerificationLevel` | string |  |  | `CreditCardAddressVerificationLevel` |
| `WarehouseIsEntireShipmentFilled` | string |  |  | `WarehouseIsEntireShipmentFilled` |
| `PackingDutyLicense` | string |  |  | `PackingDutyLicense` |
| `NationalRegistryNumber` | string |  |  | `NationalRegistryNumber` |
| `SiteId` | string |  |  | `SiteId` |
| `InvoiceAddressCountryRegionISOCode` | string |  |  | `InvoiceAddressCountryRegionISOCode` |
| `IsAllowCreateIndirectOrderLines` | string |  |  | `IsAllowCreateIndirectOrderLines` |
| `PrimaryContactURLPurpose` | string |  |  | `PrimaryContactURLPurpose` |
| `ChargesGroupId` | string |  |  | `ChargesGroupId` |
| `PanStatus` | string |  |  | `PanStatus` |
| `CommissionSalesGroupId` | string |  |  | `CommissionSalesGroupId` |
| `NameAlias` | string |  |  | `NameAlias` |
| `PrimaryContactFaxPurpose` | string |  |  | `PrimaryContactFaxPurpose` |
| `AddressStreetNumber` | string |  |  | `AddressStreetNumber` |
| `PersonLastName` | string |  |  | `PersonLastName` |
| `PaymentIdType` | string |  |  | `PaymentIdType` |
| `VendorAccount` | string |  |  | `VendorAccount` |
| `AddressCountryRegionISOCode` | string |  |  | `AddressCountryRegionISOCode` |
| `ResidenceForeignCountryRegionId` | string |  |  | `ResidenceForeignCountryRegionId` |
| `RFCNumber` | string |  |  | `RFCNumber` |
| `PersonHobbies` | string |  |  | `PersonHobbies` |
| `ElectronicLocationId` | string |  |  | `ElectronicLocationId` |
| `InvoiceAddressZipCode` | string |  |  | `InvoiceAddressZipCode` |
| `PrimaryContactLinkedInPurpose` | string |  |  | `PrimaryContactLinkedInPurpose` |
| `IsOneTimeCustomer` | string |  |  | `IsOneTimeCustomer` |
| `ForeignCustomer` | string |  |  | `ForeignCustomer` |
| `CustomerTMAGroupId` | string |  |  | `CustomerTMAGroupId` |
| `AddressValidFrom` | string |  |  | `AddressValidFrom` |
| `OrganizationNumberOfEmployees` | string |  |  | `OrganizationNumberOfEmployees` |
| `CompanyType` | string |  |  | `CompanyType` |
| `CustomerGroupId` | string |  |  | `CustomerGroupId` |
| `GiroTypeInterestNote` | string |  |  | `GiroTypeInterestNote` |
| `DeliveryAddressZipCode` | string |  |  | `DeliveryAddressZipCode` |
| `DeliveryReason` | string |  |  | `DeliveryReason` |
| `TaxRegistrationId` | string |  |  | `TaxRegistrationId` |
| `PaymentUseCashDiscount` | string |  |  | `PaymentUseCashDiscount` |
| `DiscountPriceGroupId` | string |  |  | `DiscountPriceGroupId` |
| `AddressDescription` | string |  |  | `AddressDescription` |
| `SuframaNumber` | string |  |  | `SuframaNumber` |
| `IdentificationNumber` | string |  |  | `IdentificationNumber` |
| `AuthorityOffice` | string |  |  | `AuthorityOffice` |
| `PersonPhoneticFirstName` | string |  |  | `PersonPhoneticFirstName` |
| `PrimaryContactTelexPurpose` | string |  |  | `PrimaryContactTelexPurpose` |
| `DeliveryAddressLatitude` | string |  |  | `DeliveryAddressLatitude` |
| `InvoiceAddressCountryRegionId` | string |  |  | `InvoiceAddressCountryRegionId` |
| `PrimaryContactFacebookPurpose` | string |  |  | `PrimaryContactFacebookPurpose` |
| `CompanyChain` | string |  |  | `CompanyChain` |
| `OverrideSalesTax` | string |  |  | `OverrideSalesTax` |
| `BrazilianINSSCEI` | string |  |  | `BrazilianINSSCEI` |
| `CommissionCustomerGroupId` | string |  |  | `CommissionCustomerGroupId` |
| `PrimaryContactFaxDescription` | string |  |  | `PrimaryContactFaxDescription` |
| `NatureOfAssessee` | string |  |  | `NatureOfAssessee` |
| `WriteoffReason` | string |  |  | `WriteoffReason` |
| `PersonMiddleName` | string |  |  | `PersonMiddleName` |
| `InvoiceAddressLocationId` | string |  |  | `InvoiceAddressLocationId` |
| `PersonPhoneticLastName` | string |  |  | `PersonPhoneticLastName` |
| `LanguageId` | string |  |  | `LanguageId` |
| `IsPurchRequestUsed` | string |  |  | `IsPurchRequestUsed` |
| `AddressStreet` | string |  |  | `AddressStreet` |
| `IsPublicSector_IT` | string |  |  | `IsPublicSector_IT` |
| `SATRegistrationName_MX` | string |  |  | `SATRegistrationName_MX` |
| `TaxRegimeCode_MX` | string |  |  | `TaxRegimeCode_MX` |
| `CFDITemporaryExport_MX` | string |  |  | `CFDITemporaryExport_MX` |
| `IsSimplifiedPrimaryAddress` | string |  |  | `IsSimplifiedPrimaryAddress` |
| `IsSimplifiedDeliveryAddress` | string |  |  | `IsSimplifiedDeliveryAddress` |
| `IsSimplifiedInvoiceAddress` | string |  |  | `IsSimplifiedInvoiceAddress` |
| `CredManEligibleCreditLimitCurrency` | string |  |  | `CredManEligibleCreditLimitCurrency` |
| `CredManCustCreditMaxAlt` | string |  |  | `CredManCustCreditMaxAlt` |
| `CredManStatusReasonId` | string |  |  | `CredManStatusReasonId` |
| `CredManEligibleCreditMax` | string |  |  | `CredManEligibleCreditMax` |
| `CredManCustUnlimitedCredit` | string |  |  | `CredManCustUnlimitedCredit` |
| `CredManEligibleCreditLimitDate` | string |  |  | `CredManEligibleCreditLimitDate` |
| `CredManWithAgency` | string |  |  | `CredManWithAgency` |
| `CredManCreditLimitDate` | string |  |  | `CredManCreditLimitDate` |
| `CredManNextSchedReviewDate` | string |  |  | `CredManNextSchedReviewDate` |
| `CredManLastReviewDate` | string |  |  | `CredManLastReviewDate` |
| `CredManCustomerSince` | string |  |  | `CredManCustomerSince` |
| `CredManTitleHeld` | string |  |  | `CredManTitleHeld` |
| `CredManExclude` | string |  |  | `CredManExclude` |
| `CredManBusinessStarted` | string |  |  | `CredManBusinessStarted` |
| `CredManNotes` | string |  |  | `CredManNotes` |
| `CredManCollectionGroupId` | string |  |  | `CredManCollectionGroupId` |
| `CredManGroupId` | string |  |  | `CredManGroupId` |
| `CredManAccountStatusId` | string |  |  | `CredManAccountStatusId` |
| `CredManCreditLimitExpiryDate` | string |  |  | `CredManCreditLimitExpiryDate` |
| `KPFNettingActive` | string |  |  | `KPFNettingActive` |
| `QMSApprovedCustomerGroupId` | string |  |  | `QMSApprovedCustomerGroupId` |
| `QMSWillPrintCustomerSpecificCertificateOfAnalysis` | string |  |  | `QMSWillPrintCustomerSpecificCertificateOfAnalysis` |
| `QMSCertificateOfAnalysisCustomerGroupId` | string |  |  | `QMSCertificateOfAnalysisCustomerGroupId` |
| `QMSApprovedCustomerListCheckMethod` | string |  |  | `QMSApprovedCustomerListCheckMethod` |
| `source_file_name` | string |  |  | `source_file_name` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**CustomerAccount**
- `100-000001`: 1 rows
- `None`: 1 rows
- `TX 75207`: 1 rows

**AddressBrazilianCNPJOrCPF**
- `None`: 3 rows

**PartyType**
- `Organization`: 1 rows
- `No`: 1 rows
- `None`: 1 rows

**PrimaryContactFaxExtension**
- `None`: 2 rows
- `0`: 1 rows

**IsFuelSurchargeApplied**
- `None`: 1 rows
- `No`: 1 rows

**SalesTaxGroup**
- `None`: 3 rows

**AddressCountryRegionId**
- `None`: 2 rows
- `USA`: 1 rows

**ContactPersonId**
- `None`: 2 rows
- `No`: 1 rows

**CustomerPaymentFineCode**
- `None`: 3 rows

**BirthCountyCode**
- `None`: 2 rows
- `1447`: 1 rows

**InvoiceAddress**
- `None`: 2 rows
- `InvoiceAccount`: 1 rows

**PackingMaterialFeeLicenseNumber**
- `None`: 3 rows

**TransactionPresenceType**
- `None`: 2 rows
- `DoesNotApply`: 1 rows

**PrimaryContactTwitter**
- `None`: 3 rows

**InvoiceAddressCity**
- `None`: 2 rows
- `1309`: 1 rows

**IsFinalUser**
- `None`: 2 rows
- `No`: 1 rows

**DeliveryAddressCounty**
- `None`: 2 rows

**HasSuframaDiscountPISandCOFINS**
- `None`: 2 rows
- `No`: 1 rows

**InvoiceAddressStreet**
- `None`: 3 rows

**CURPNumber**
- `None`: 3 rows

**PrimaryContactLinkedInDescription**
- `None`: 3 rows

**DeliveryAddressCountryRegionId**
- `None`: 3 rows

**ItemCustomerGroupId**
- `None`: 3 rows

**PersonProfessionalTitle**
- `None`: 2 rows
- `No`: 1 rows

**SalesSegmentId**
- `None`: 3 rows

**IsServiceDeliveryAddressBased**
- `None`: 2 rows
- `No`: 1 rows

**PrimaryContactTelexDescription**
- `None`: 2 rows
- `No`: 1 rows

**InvoiceAddressDistrictName**
- `None`: 3 rows

**InvoiceAddressTimeZone**
- `None`: 2 rows
- `Always`: 1 rows

**SalesAccountNumber**
- `None`: 3 rows

**PrimaryContactFacebookDescription**
- `None`: 2 rows
- `No`: 1 rows

**PrimaryContactPhoneIsMobile**
- `No`: 2 rows
- `None`: 1 rows

**PrimaryContactFaxRecordId**
- `None`: 2 rows
- `0`: 1 rows

**TCSGroup**
- `None`: 3 rows

**DeliveryAddressLocationId**
- `None`: 3 rows

**AddressZipCode**
- `75207`: 1 rows
- `None`: 1 rows
- `11`: 1 rows

**GiroTypeProjInvoice**
- `0`: 1 rows
- `None`: 1 rows

**LineOfBusinessId**
- `None`: 3 rows

**OrganizationPhoneticName**
- `None`: 3 rows

**CreditCardCVC**
- `None`: 2 rows

**DeliveryAddressCountryRegionISOCode**
- `None`: 3 rows

**DeliveryAddressValidFrom**
- `0`: 1 rows
- `1900-01-01 00:00:00.0000000 +00:00`: 1 rows
- `None`: 1 rows

**GiroTypeAccountStatement**
- `None`: 2 rows

**CalculateWithholdingTax**
- `None`: 2 rows
- `No`: 1 rows

**ElectronicInvoiceEAN**
- `None`: 3 rows

**DeliveryFreightZone**
- `None`: 3 rows

**PrimaryContactFax**
- `None`: 2 rows
- `USD`: 1 rows

**TaxExemptNumber**
- `None`: 2 rows
- `AllocationPriority10`: 1 rows

**DeliveryAddressDescription**
- `None`: 2 rows
- `No`: 1 rows

**DeliveryAddressLongitude**
- `None`: 2 rows
- `0`: 1 rows

**BirthPlace**
- `None`: 3 rows

**AddressCity**
- `None`: 2 rows
- `DALLAS`: 1 rows

**PersonInitials**
- `None`: 3 rows

**DefaultECommerceOperator**
- `None`: 3 rows

**CentralBankPurposeCode**
- `None`: 3 rows

**GiroTypeCollectionletter**
- `None`: 2 rows

**FullPrimaryAddress**
- `None`: 2 rows
- `1950 N STEMMONS FWY SUITE 5010`: 1 rows

**OrderEntryDeadline**
- `None`: 3 rows

**ForeignerId**
- `None`: 2 rows
- `0`: 1 rows

**WarehouseIsASNGenerated**
- `None`: 3 rows

**AddressLongitude**
- `None`: 3 rows

**CustomerType**
- `None`: 2 rows
- `No`: 1 rows

**PrimaryContactLinkedIn**
- `None`: 3 rows

**PrimaryContactURL**
- `None`: 2 rows
- `5637146371`: 1 rows

**IsFreightAccrued**
- `None`: 3 rows

**PartyState**
- `None`: 3 rows

**PartyNumber**
- `None`: 3 rows

**InvoiceAccount**
- `None`: 3 rows

**CentralBankPurposeNotes**
- `None`: 2 rows
- `0`: 1 rows

**AddressBuildingComplement**
- `None`: 2 rows
- `No`: 1 rows

**CollectionsContactPersonId**
- `None`: 2 rows

**PersonMaritalStatus**
- `None`: 3 rows

**AddressLocationId**
- `None`: 2 rows
- `TX`: 1 rows

**PaymentSchedule**
- `None`: 2 rows
- `No`: 1 rows

**PrimaryContactTwitterPurpose**
- `None`: 2 rows
- `No`: 1 rows

**GiroType**
- `None`: 3 rows

**InvoiceAddressDescription**
- `None`: 2 rows
- `No`: 1 rows

**AddressDistrictName**
- `None`: 2 rows
- `No`: 1 rows

**DeliveryTerms**
- `None`: 2 rows
- `No`: 1 rows

**NumberSequenceGroup**
- `None`: 2 rows
- `0`: 1 rows

**PersonChildrenNames**
- `None`: 3 rows

**PaymentMethod**
- `None`: 2 rows
- `MICROSOFT CORPORATION`: 1 rows

**ForeignResident**
- `None`: 3 rows

**DeliveryMode**
- `None`: 3 rows

**PersonProfessionalSuffix**
- `None`: 3 rows

**OnHoldStatus**
- `None`: 2 rows
- `0`: 1 rows

**WarehouseId**
- `None`: 2 rows
- `No`: 1 rows

**AccountStatement**
- `None`: 2 rows
- `RetailEx3`: 1 rows

**DestinationCode**
- `None`: 3 rows

**EInvoiceRegister**
- `None`: 2 rows

**IRS1099CIndicator**
- `None`: 3 rows

**FrenchSiret**
- `None`: 3 rows

**PaymentDay**
- `None`: 3 rows

**BrazilianNIT**
- `None`: 2 rows
- `No`: 1 rows

**FederalIndicator**
- `None`: 3 rows

**EmployeeResponsibleNumber**
- `None`: 2 rows
- `Standard`: 1 rows

**PersonAnniversaryYear**
- `None`: 2 rows
- `No`: 1 rows

**DefaultInventoryStatusId**
- `None`: 3 rows

**AddressTimeZone**
- `None`: 3 rows

**PrimaryContactPhone**
- `None`: 3 rows

**PrimaryContactPhoneRecordId**
- `None`: 3 rows

**DeliveryAddressCity**
- `None`: 3 rows

**InvoiceAddressCounty**
- `None`: 3 rows

**PANReferenceNumber**
- `None`: 2 rows
- `Other`: 1 rows

**DeliveryAddressStreet**
- `None`: 2 rows
- `No`: 1 rows

**SalesCurrencyCode**
- `None`: 3 rows

**Priority**
- `None`: 2 rows

**IsSalesTaxIncludedInPrices**
- `None`: 2 rows
- `1900-01-01 00:00:00.0000000 +00:00`: 1 rows

**BrazilianCNPJOrCPF**
- `None`: 3 rows

**PaymentFactoringAccount**
- `None`: 2 rows

**PANNumber**
- `None`: 3 rows

**PrimaryContactTwitterDescription**
- `None`: 3 rows

**PersonFirstName**
- `None`: 3 rows

**BrazilianCCM**
- `None`: 2 rows
- `0`: 1 rows

**TDSGroup**
- `None`: 3 rows

**MultiLineDiscountCode**
- `None`: 2 rows
- `Business`: 1 rows

**PersonAnniversaryDay**
- `None`: 3 rows

**DefaultDimensionDisplayValue**
- `None`: 2 rows

**SupplementaryItemGroupId**
- `None`: 2 rows
- `No`: 1 rows

**IsWithholdingTaxCalculated**
- `None`: 3 rows

**PaymentSpecification**
- `None`: 3 rows

**AddressRecordId**
- `None`: 3 rows

**AddressBooks**
- `None`: 3 rows

**FulfillmentPolicyName**
- `None`: 2 rows
- `0`: 1 rows

**SalesDistrict**
- `None`: 3 rows

**ConsolidationDay**
- `None`: 3 rows

**IsExpressBillOfLadingAccepted**
- `None`: 2 rows
- `0`: 1 rows

**CreditCardAddressVerification**
- `None`: 2 rows
- `No`: 1 rows

**InvoiceAddressBuildingComplement**
- `None`: 2 rows
- `No`: 1 rows

**AddressState**
- `None`: 3 rows

**AllowOnAccount**
- `None`: 3 rows

**IsExcludedFromCollectionFeeCalculation**
- `None`: 2 rows
- `No`: 1 rows

**CustomerPaymentFinancialInterestCode**
- `None`: 3 rows

**IsTransactionPostedAsShipment**
- `None`: 3 rows

**IsExternallyMaintained**
- `None`: 2 rows
- `MICROSOFT CORPORATION`: 1 rows

**CreditLimitIsMandatory**
- `None`: 2 rows
- `No`: 1 rows

**PaymentTermsBaseDays**
- `None`: 3 rows

**FiscalCode**
- `None`: 2 rows
- `2154-12-31 23:59:59.0000000 +00:00`: 1 rows

**KnownAs**
- `None`: 3 rows

**PrimaryContactTelex**
- `None`: 2 rows
- `Unknown`: 1 rows

**PaymentBankAccount**
- `None`: 3 rows

**BrazilianIE**
- `None`: 3 rows

**PreferentialCustomer**
- `None`: 3 rows

**ReceiptOption**
- `None`: 3 rows

**AddressBrazilianIE**
- `None`: 3 rows

**PersonAnniversaryMonth**
- `None`: 3 rows

**PrimaryContactPhoneExtension**
- `None`: 2 rows
- `0`: 1 rows

**InvoiceAddressStreetNumber**
- `None`: 2 rows
- `No`: 1 rows

**PrimaryContactPhonePurpose**
- `None`: 2 rows
- `1900-01-01 00:00:00.0000000 +00:00`: 1 rows

**ExportSale**
- `None`: 3 rows

**OrganizationNumber**
- `None`: 2 rows
- `1900-01-01 00:00:00.0000000 +00:00`: 1 rows

**InvoicePostingType**
- `None`: 2 rows
- `0`: 1 rows

**CreditCardAddressVerificationIsAuthorizationVoidedOnFailure**
- `None`: 2 rows
- `Accept`: 1 rows

**InvoiceAddressState**
- `None`: 2 rows
- `No`: 1 rows

**ReceiptCalendar**
- `None`: 3 rows

**DeliveryAddressState**
- `None`: 3 rows

**StateInscription**
- `None`: 3 rows

**PersonLastNamePrefix**
- `None`: 3 rows

**SalesReturnTaxGroup**
- `None`: 2 rows
- `No`: 1 rows

**PrimaryContactURLDescription**
- `None`: 3 rows

**CustomerWithholdingContributionType**
- `None`: 3 rows

**IsElectronicInvoice**
- `None`: 2 rows
- `NotAvailable`: 1 rows

**FederalAgencyLocationCode**
- `None`: 3 rows

**GiroTypeFreeTextInvoice**
- `None`: 2 rows
- `MICROSOFT CORPORATIO`: 1 rows

**DeliveryAddressValidTo**
- `None`: 3 rows

**PersonPhoneticMiddleName**
- `None`: 2 rows
- `LB #842467`: 1 rows

**OrganizationABCCode**
- `None`: 3 rows

**BrazilianCNAE**
- `None`: 3 rows

**WithholdingTaxGroupCode**
- `None`: 3 rows

**NAFCode**
- `None`: 2 rows
- `US`: 1 rows

**AddressLatitude**
- `None`: 3 rows

**TotalDiscountCode**
- `None`: 3 rows

**PaymentCashDiscount**
- `None`: 3 rows

**AddressLocationRoles**
- `None`: 3 rows

**DeliveryAddressDistrictName**
- `None`: 3 rows

**CollectionLetterCode**
- `None`: 3 rows

**EInvoiceAttachment**
- `None`: 2 rows
- `No`: 1 rows

**MerchantID**
- `None`: 2 rows
- `No`: 1 rows

**CreditRating**
- `None`: 3 rows

**PrimaryContactFacebook**
- `None`: 2 rows
- `2025-06-25 10:29:08.0000000 +00:00`: 1 rows

**DeliveryAddressBuildingComplement**
- `None`: 2 rows
- `0`: 1 rows

**DeliveryAddressStreetNumber**
- `None`: 2 rows
- `Blank`: 1 rows

**InvoiceAddressLongitude**
- `None`: 2 rows
- `Corporate`: 1 rows

**LineDiscountCode**
- `None`: 2 rows

**PartyCountry**
- `None`: 3 rows

**InvoiceAddressLatitude**
- `None`: 3 rows

**IsInSuframaRegion**
- `None`: 3 rows

**IsIncomingFiscalDocumentGenerated**
- `None`: 2 rows
- `Normal`: 1 rows

**SalesMemo**
- `None`: 3 rows

**ReliefGroupId**
- `None`: 2 rows
- `MICROSOFT CORPORATION`: 1 rows

**IsExcludedFromInterestChargeCalculation**
- `None`: 3 rows

**StatisticsGroupId**
- `None`: 3 rows

**SalesOrderPoolId**
- `None`: 3 rows

**OrganizationName**
- `None`: 3 rows

**IsOrderNumberReferenceUsed**
- `None`: 3 rows

**CustClassificationId**
- `None`: 2 rows
- `0`: 1 rows

**AddressValidTo**
- `None`: 3 rows

**FederalComments**
- `None`: 3 rows

**PersonGender**
- `None`: 3 rows

**PaymentTerms**
- `None`: 2 rows
- `No`: 1 rows

**PrimaryContactPhoneDescription**
- `None`: 3 rows

**AddressPostbox**
- `None`: 3 rows

**SalesSubsegmentId**
- `None`: 3 rows

**CustomerRebateGroupId**
- `None`: 2 rows
- `Company`: 1 rows

**WarehouseOutboundShipmentProcessingPolicyName**
- `None`: 3 rows

**AddressCounty**
- `None`: 3 rows

**PrimaryContactURLRecordId**
- `None`: 3 rows

**IsICMSContributor**
- `None`: 3 rows

**InvoiceAddressValidTo**
- `None`: 2 rows
- `en-US`: 1 rows

**DeliveryAddressTimeZone**
- `None`: 2 rows
- `No`: 1 rows

**InvoiceAddressValidFrom**
- `None`: 2 rows
- `1950 N STEMMONS FWY SUITE 5010`: 1 rows

**CreditLimit**
- `None`: 2 rows
- `No`: 1 rows

**CreditCardAddressVerificationLevel**
- `None`: 3 rows

**WarehouseIsEntireShipmentFilled**
- `None`: 3 rows

**PackingDutyLicense**
- `None`: 2 rows
- `No`: 1 rows

**NationalRegistryNumber**
- `None`: 2 rows
- `No`: 1 rows

**SiteId**
- `None`: 2 rows
- `No`: 1 rows

**InvoiceAddressCountryRegionISOCode**
- `None`: 2 rows
- `No`: 1 rows

**IsAllowCreateIndirectOrderLines**
- `None`: 3 rows

**PrimaryContactURLPurpose**
- `None`: 2 rows
- `0`: 1 rows

**ChargesGroupId**
- `None`: 3 rows

**PanStatus**
- `None`: 2 rows
- `0`: 1 rows

**CommissionSalesGroupId**
- `None`: 2 rows
- `No`: 1 rows

**NameAlias**
- `None`: 2 rows
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**PrimaryContactFaxPurpose**
- `None`: 2 rows
- `No`: 1 rows

**AddressStreetNumber**
- `None`: 2 rows
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**PersonLastName**
- `None`: 2 rows
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**PaymentIdType**
- `None`: 2 rows
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**VendorAccount**
- `None`: 2 rows
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**AddressCountryRegionISOCode**
- `None`: 2 rows
- `No`: 1 rows

**ResidenceForeignCountryRegionId**
- `None`: 2 rows
- `No`: 1 rows

**RFCNumber**
- `None`: 2 rows
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**PersonHobbies**
- `None`: 3 rows

**ElectronicLocationId**
- `None`: 3 rows

**InvoiceAddressZipCode**
- `None`: 3 rows

**PrimaryContactLinkedInPurpose**
- `None`: 3 rows

**IsOneTimeCustomer**
- `None`: 2 rows
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**ForeignCustomer**
- `None`: 2 rows
- `No`: 1 rows

**CustomerTMAGroupId**
- `None`: 3 rows

**AddressValidFrom**
- `None`: 2 rows
- `No`: 1 rows

**OrganizationNumberOfEmployees**
- `None`: 3 rows

**CustomerGroupId**
- `None`: 3 rows

**GiroTypeInterestNote**
- `None`: 3 rows

**DeliveryAddressZipCode**
- `None`: 3 rows

**DeliveryReason**
- `None`: 3 rows

**TaxRegistrationId**
- `None`: 3 rows

**PaymentUseCashDiscount**
- `None`: 3 rows

**DiscountPriceGroupId**
- `None`: 3 rows

**AddressDescription**
- `None`: 3 rows

**SuframaNumber**
- `None`: 3 rows

**IdentificationNumber**
- `None`: 3 rows

**AuthorityOffice**
- `None`: 3 rows

**PersonPhoneticFirstName**
- `None`: 3 rows

**PrimaryContactTelexPurpose**
- `None`: 3 rows

**DeliveryAddressLatitude**
- `None`: 3 rows

**InvoiceAddressCountryRegionId**
- `None`: 3 rows

**PrimaryContactFacebookPurpose**
- `None`: 3 rows

**OverrideSalesTax**
- `None`: 3 rows

**BrazilianINSSCEI**
- `None`: 3 rows

**CommissionCustomerGroupId**
- `None`: 3 rows

**PrimaryContactFaxDescription**
- `None`: 3 rows

**NatureOfAssessee**
- `None`: 3 rows

**WriteoffReason**
- `None`: 3 rows

**PersonMiddleName**
- `None`: 3 rows

**InvoiceAddressLocationId**
- `None`: 3 rows

**PersonPhoneticLastName**
- `None`: 3 rows

**LanguageId**
- `None`: 3 rows

**IsPurchRequestUsed**
- `None`: 3 rows

**AddressStreet**
- `None`: 3 rows

**IsPublicSector_IT**
- `None`: 3 rows

**SATRegistrationName_MX**
- `None`: 3 rows

**TaxRegimeCode_MX**
- `None`: 3 rows

**CFDITemporaryExport_MX**
- `None`: 3 rows

**IsSimplifiedPrimaryAddress**
- `None`: 3 rows

**IsSimplifiedDeliveryAddress**
- `None`: 3 rows

**IsSimplifiedInvoiceAddress**
- `None`: 3 rows

**CredManEligibleCreditLimitCurrency**
- `None`: 3 rows

**CredManCustCreditMaxAlt**
- `None`: 3 rows

**CredManStatusReasonId**
- `None`: 3 rows

**CredManEligibleCreditMax**
- `None`: 3 rows

**CredManCustUnlimitedCredit**
- `None`: 3 rows

**CredManEligibleCreditLimitDate**
- `None`: 3 rows

**CredManWithAgency**
- `None`: 3 rows

**CredManCreditLimitDate**
- `None`: 3 rows

**CredManNextSchedReviewDate**
- `None`: 3 rows

**CredManLastReviewDate**
- `None`: 3 rows

**CredManCustomerSince**
- `None`: 3 rows

**CredManTitleHeld**
- `None`: 3 rows

**CredManExclude**
- `None`: 3 rows

**CredManBusinessStarted**
- `None`: 3 rows

**CredManNotes**
- `None`: 3 rows

**CredManCollectionGroupId**
- `None`: 3 rows

**CredManGroupId**
- `None`: 3 rows

**CredManAccountStatusId**
- `None`: 3 rows

**CredManCreditLimitExpiryDate**
- `None`: 3 rows

**KPFNettingActive**
- `None`: 3 rows

**QMSApprovedCustomerGroupId**
- `None`: 3 rows

**QMSWillPrintCustomerSpecificCertificateOfAnalysis**
- `None`: 3 rows

**QMSCertificateOfAnalysisCustomerGroupId**
- `None`: 3 rows

**QMSApprovedCustomerListCheckMethod**
- `None`: 3 rows

**source_file_name**
- `customersv3__20261116_105417.csv`: 3 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:43:19.958440+00:00`: 3 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:19.958440+00:00`: 3 rows

## Profile

Rows in the latest export: 3.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `dataAreaId` | STRING | 3 | 0 |  |  |
| `CustomerAccount` | STRING | 2 | 1 | TX 75207 | 100-000001 |
| `AddressBrazilianCNPJOrCPF` | STRING | 0 | 3 |  |  |
| `PartyType` | STRING | 2 | 1 | No | Organization |
| `PrimaryContactFaxExtension` | STRING | 1 | 2 | 0 | 0 |
| `IsFuelSurchargeApplied` | STRING | 2 | 1 | No | None |
| `SalesTaxGroup` | STRING | 0 | 3 |  |  |
| `AddressCountryRegionId` | STRING | 1 | 2 | USA | USA |
| `ContactPersonId` | STRING | 1 | 2 | No | No |
| `CustomerPaymentFineCode` | STRING | 0 | 3 |  |  |
| `BirthCountyCode` | STRING | 1 | 2 | 1447 | 1447 |
| `InvoiceAddress` | STRING | 1 | 2 | InvoiceAccount | InvoiceAccount |
| `PackingMaterialFeeLicenseNumber` | STRING | 0 | 3 |  |  |
| `TransactionPresenceType` | STRING | 1 | 2 | DoesNotApply | DoesNotApply |
| `PrimaryContactTwitter` | STRING | 0 | 3 |  |  |
| `PrimaryContactEmailIsIM` | STRING | 2 | 1 |  |  |
| `InvoiceAddressCity` | STRING | 1 | 2 | 1309 | 1309 |
| `IsFinalUser` | STRING | 1 | 2 | No | No |
| `PrimaryContactEmail` | STRING | 0 | 3 |  |  |
| `DeliveryAddressCounty` | STRING | 1 | 2 | None | None |
| `HasSuframaDiscountPISandCOFINS` | STRING | 1 | 2 | No | No |
| `InvoiceAddressStreet` | STRING | 0 | 3 |  |  |
| `CURPNumber` | STRING | 0 | 3 |  |  |
| `PrimaryContactLinkedInDescription` | STRING | 0 | 3 |  |  |
| `DeliveryAddressCountryRegionId` | STRING | 0 | 3 |  |  |
| `ItemCustomerGroupId` | STRING | 0 | 3 |  |  |
| `PersonProfessionalTitle` | STRING | 1 | 2 | No | No |
| `SalesSegmentId` | STRING | 0 | 3 |  |  |
| `IsServiceDeliveryAddressBased` | STRING | 1 | 2 | No | No |
| `PrimaryContactTelexDescription` | STRING | 1 | 2 | No | No |
| `InvoiceAddressDistrictName` | STRING | 0 | 3 |  |  |
| `InvoiceAddressTimeZone` | STRING | 1 | 2 | Always | Always |
| `SalesAccountNumber` | STRING | 0 | 3 |  |  |
| `PrimaryContactFacebookDescription` | STRING | 1 | 2 | No | No |
| `PrimaryContactPhoneIsMobile` | STRING | 1 | 1 | No | No |
| `PrimaryContactFaxRecordId` | STRING | 1 | 2 | 0 | 0 |
| `TCSGroup` | STRING | 0 | 3 |  |  |
| `DeliveryAddressLocationId` | STRING | 0 | 3 |  |  |
| `InterCompanyAutoCreateOrders` | STRING | 2 | 1 |  |  |
| `AddressZipCode` | STRING | 2 | 1 | 11 | 75207 |
| `GiroTypeProjInvoice` | STRING | 2 | 1 | 0 | None |
| `LineOfBusinessId` | STRING | 0 | 3 |  |  |
| `OrganizationPhoneticName` | STRING | 0 | 3 |  |  |
| `CreditCardCVC` | STRING | 1 | 2 | None | None |
| `DeliveryAddressCountryRegionISOCode` | STRING | 0 | 3 |  |  |
| `DeliveryAddressValidFrom` | STRING | 2 | 1 | 0 | 1900-01-01 00:00:00.0000000 +00:00 |
| `GiroTypeAccountStatement` | STRING | 1 | 2 | None | None |
| `CalculateWithholdingTax` | STRING | 1 | 2 | No | No |
| `ElectronicInvoiceEAN` | STRING | 0 | 3 |  |  |
| `DeliveryFreightZone` | STRING | 0 | 3 |  |  |
| `PrimaryContactFax` | STRING | 1 | 2 | USD | USD |
| `TaxExemptNumber` | STRING | 1 | 2 | AllocationPriority10 | AllocationPriority10 |
| `DeliveryAddressDescription` | STRING | 1 | 2 | No | No |
| `DeliveryAddressLongitude` | STRING | 1 | 2 | 0 | 0 |
| `BirthPlace` | STRING | 0 | 3 |  |  |
| `AddressCity` | STRING | 1 | 2 | DALLAS | DALLAS |
| `PersonInitials` | STRING | 0 | 3 |  |  |
| `DefaultECommerceOperator` | STRING | 0 | 3 |  |  |
| `CentralBankPurposeCode` | STRING | 0 | 3 |  |  |
| `GiroTypeCollectionletter` | STRING | 1 | 2 | None | None |
| `FullPrimaryAddress` | STRING | 1 | 2 | 1950 N STEMMONS FWY SUITE 5010 | 1950 N STEMMONS FWY SUITE 5010 |
| `OrderEntryDeadline` | STRING | 0 | 3 |  |  |
| `ForeignerId` | STRING | 1 | 2 | 0 | 0 |
| `WarehouseIsASNGenerated` | STRING | 0 | 3 |  |  |
| `AddressLongitude` | STRING | 0 | 3 |  |  |
| `CustomerType` | STRING | 1 | 2 | No | No |
| `PrimaryContactLinkedIn` | STRING | 0 | 3 |  |  |
| `PrimaryContactURL` | STRING | 1 | 2 | 5637146371 | 5637146371 |
| `IsFreightAccrued` | STRING | 0 | 3 |  |  |
| `PartyState` | STRING | 0 | 3 |  |  |
| `PartyNumber` | STRING | 0 | 3 |  |  |
| `InvoiceAccount` | STRING | 0 | 3 |  |  |
| `CentralBankPurposeNotes` | STRING | 1 | 2 | 0 | 0 |
| `AddressBuildingComplement` | STRING | 1 | 2 | No | No |
| `CollectionsContactPersonId` | STRING | 1 | 2 | None | None |
| `PersonMaritalStatus` | STRING | 0 | 3 |  |  |
| `AddressLocationId` | STRING | 1 | 2 | TX | TX |
| `PaymentSchedule` | STRING | 1 | 2 | No | No |
| `PrimaryContactTwitterPurpose` | STRING | 1 | 2 | No | No |
| `GiroType` | STRING | 0 | 3 |  |  |
| `InvoiceAddressDescription` | STRING | 1 | 2 | No | No |
| `AddressDistrictName` | STRING | 1 | 2 | No | No |
| `DeliveryTerms` | STRING | 1 | 2 | No | No |
| `NumberSequenceGroup` | STRING | 1 | 2 | 0 | 0 |
| `PersonChildrenNames` | STRING | 0 | 3 |  |  |
| `PaymentMethod` | STRING | 1 | 2 | MICROSOFT CORPORATION | MICROSOFT CORPORATION |
| `ForeignResident` | STRING | 0 | 3 |  |  |
| `DeliveryMode` | STRING | 0 | 3 |  |  |
| `PersonProfessionalSuffix` | STRING | 0 | 3 |  |  |
| `OnHoldStatus` | STRING | 1 | 2 | 0 | 0 |
| `WarehouseId` | STRING | 1 | 2 | No | No |
| `AccountStatement` | STRING | 1 | 2 | RetailEx3 | RetailEx3 |
| `DestinationCode` | STRING | 0 | 3 |  |  |
| `EInvoiceRegister` | STRING | 1 | 2 | None | None |
| `IRS1099CIndicator` | STRING | 0 | 3 |  |  |
| `FrenchSiret` | STRING | 0 | 3 |  |  |
| `PaymentDay` | STRING | 0 | 3 |  |  |
| `BrazilianNIT` | STRING | 1 | 2 | No | No |
| `FederalIndicator` | STRING | 0 | 3 |  |  |
| `EmployeeResponsibleNumber` | STRING | 1 | 2 | Standard | Standard |
| `PersonAnniversaryYear` | STRING | 1 | 2 | No | No |
| `DefaultInventoryStatusId` | STRING | 0 | 3 |  |  |
| `PrimaryContactEmailDescription` | STRING | 0 | 3 |  |  |
| `AddressTimeZone` | STRING | 0 | 3 |  |  |
| `PrimaryContactPhone` | STRING | 0 | 3 |  |  |
| `PrimaryContactPhoneRecordId` | STRING | 0 | 3 |  |  |
| `DeliveryAddressCity` | STRING | 0 | 3 |  |  |
| `InvoiceAddressCounty` | STRING | 0 | 3 |  |  |
| `PANReferenceNumber` | STRING | 1 | 2 | Other | Other |
| `DeliveryAddressStreet` | STRING | 1 | 2 | No | No |
| `SalesCurrencyCode` | STRING | 0 | 3 |  |  |
| `Priority` | STRING | 1 | 2 | None | None |
| `IsSalesTaxIncludedInPrices` | STRING | 1 | 2 | 1900-01-01 00:00:00.0000000 +00:00 | 1900-01-01 00:00:00.0000000 +00:00 |
| `BrazilianCNPJOrCPF` | STRING | 0 | 3 |  |  |
| `PaymentFactoringAccount` | STRING | 1 | 2 | None | None |
| `PANNumber` | STRING | 0 | 3 |  |  |
| `PrimaryContactTwitterDescription` | STRING | 0 | 3 |  |  |
| `PersonFirstName` | STRING | 0 | 3 |  |  |
| `BrazilianCCM` | STRING | 1 | 2 | 0 | 0 |
| `ReceiptEmail` | STRING | 0 | 3 |  |  |
| `TDSGroup` | STRING | 0 | 3 |  |  |
| `MultiLineDiscountCode` | STRING | 1 | 2 | Business | Business |
| `PersonAnniversaryDay` | STRING | 0 | 3 |  |  |
| `DefaultDimensionDisplayValue` | STRING | 1 | 2 | None | None |
| `SupplementaryItemGroupId` | STRING | 1 | 2 | No | No |
| `IsWithholdingTaxCalculated` | STRING | 0 | 3 |  |  |
| `PaymentSpecification` | STRING | 0 | 3 |  |  |
| `AddressRecordId` | STRING | 0 | 3 |  |  |
| `AddressBooks` | STRING | 0 | 3 |  |  |
| `PrimaryContactEmailPurpose` | STRING | 0 | 3 |  |  |
| `FulfillmentPolicyName` | STRING | 1 | 2 | 0 | 0 |
| `SalesDistrict` | STRING | 0 | 3 |  |  |
| `ConsolidationDay` | STRING | 0 | 3 |  |  |
| `IsExpressBillOfLadingAccepted` | STRING | 1 | 2 | 0 | 0 |
| `CreditCardAddressVerification` | STRING | 1 | 2 | No | No |
| `InvoiceAddressBuildingComplement` | STRING | 1 | 2 | No | No |
| `AddressState` | STRING | 0 | 3 |  |  |
| `AllowOnAccount` | STRING | 0 | 3 |  |  |
| `IsExcludedFromCollectionFeeCalculation` | STRING | 1 | 2 | No | No |
| `CustomerPaymentFinancialInterestCode` | STRING | 0 | 3 |  |  |
| `IsTransactionPostedAsShipment` | STRING | 0 | 3 |  |  |
| `IsExternallyMaintained` | STRING | 1 | 2 | MICROSOFT CORPORATION | MICROSOFT CORPORATION |
| `CreditLimitIsMandatory` | STRING | 1 | 2 | No | No |
| `PaymentTermsBaseDays` | STRING | 0 | 3 |  |  |
| `FiscalCode` | STRING | 1 | 2 | 2154-12-31 23:59:59.0000000 +00:00 | 2154-12-31 23:59:59.0000000 +00:00 |
| `KnownAs` | STRING | 0 | 3 |  |  |
| `PrimaryContactTelex` | STRING | 1 | 2 | Unknown | Unknown |
| `PaymentBankAccount` | STRING | 0 | 3 |  |  |
| `BrazilianIE` | STRING | 0 | 3 |  |  |
| `PrimaryContactEmailRecordId` | STRING | 0 | 3 |  |  |
| `PreferentialCustomer` | STRING | 0 | 3 |  |  |
| `ReceiptOption` | STRING | 0 | 3 |  |  |
| `AddressBrazilianIE` | STRING | 0 | 3 |  |  |
| `PersonAnniversaryMonth` | STRING | 0 | 3 |  |  |
| `PrimaryContactPhoneExtension` | STRING | 1 | 2 | 0 | 0 |
| `InvoiceAddressStreetNumber` | STRING | 1 | 2 | No | No |
| `PrimaryContactPhonePurpose` | STRING | 1 | 2 | 1900-01-01 00:00:00.0000000 +00:00 | 1900-01-01 00:00:00.0000000 +00:00 |
| `ExportSale` | STRING | 0 | 3 |  |  |
| `OrganizationNumber` | STRING | 1 | 2 | 1900-01-01 00:00:00.0000000 +00:00 | 1900-01-01 00:00:00.0000000 +00:00 |
| `InvoicePostingType` | STRING | 1 | 2 | 0 | 0 |
| `CreditCardAddressVerificationIsAuthorizationVoidedOnFailure` | STRING | 1 | 2 | Accept | Accept |
| `InvoiceAddressState` | STRING | 1 | 2 | No | No |
| `ReceiptCalendar` | STRING | 0 | 3 |  |  |
| `DeliveryAddressState` | STRING | 0 | 3 |  |  |
| `StateInscription` | STRING | 0 | 3 |  |  |
| `PersonLastNamePrefix` | STRING | 0 | 3 |  |  |
| `SalesReturnTaxGroup` | STRING | 1 | 2 | No | No |
| `PrimaryContactURLDescription` | STRING | 0 | 3 |  |  |
| `CustomerWithholdingContributionType` | STRING | 0 | 3 |  |  |
| `IsElectronicInvoice` | STRING | 1 | 2 | NotAvailable | NotAvailable |
| `FederalAgencyLocationCode` | STRING | 0 | 3 |  |  |
| `GiroTypeFreeTextInvoice` | STRING | 1 | 2 | MICROSOFT CORPORATIO | MICROSOFT CORPORATIO |
| `DeliveryAddressValidTo` | STRING | 0 | 3 |  |  |
| `PersonPhoneticMiddleName` | STRING | 1 | 2 | LB #842467 | LB #842467 |
| `OrganizationABCCode` | STRING | 0 | 3 |  |  |
| `BrazilianCNAE` | STRING | 0 | 3 |  |  |
| `WithholdingTaxGroupCode` | STRING | 0 | 3 |  |  |
| `NAFCode` | STRING | 1 | 2 | US | US |
| `AddressLatitude` | STRING | 0 | 3 |  |  |
| `TotalDiscountCode` | STRING | 0 | 3 |  |  |
| `PaymentCashDiscount` | STRING | 0 | 3 |  |  |
| `AddressLocationRoles` | STRING | 0 | 3 |  |  |
| `DeliveryAddressDistrictName` | STRING | 0 | 3 |  |  |
| `CollectionLetterCode` | STRING | 0 | 3 |  |  |
| `EInvoiceAttachment` | STRING | 1 | 2 | No | No |
| `MerchantID` | STRING | 1 | 2 | No | No |
| `CreditRating` | STRING | 0 | 3 |  |  |
| `PrimaryContactFacebook` | STRING | 1 | 2 | 2025-06-25 10:29:08.0000000 +00:00 | 2025-06-25 10:29:08.0000000 +00:00 |
| `DeliveryAddressBuildingComplement` | STRING | 1 | 2 | 0 | 0 |
| `DeliveryAddressStreetNumber` | STRING | 1 | 2 | Blank | Blank |
| `InvoiceAddressLongitude` | STRING | 1 | 2 | Corporate | Corporate |
| `LineDiscountCode` | STRING | 1 | 2 | None | None |
| `PartyCountry` | STRING | 0 | 3 |  |  |
| `InvoiceAddressLatitude` | STRING | 0 | 3 |  |  |
| `IsInSuframaRegion` | STRING | 0 | 3 |  |  |
| `IsIncomingFiscalDocumentGenerated` | STRING | 1 | 2 | Normal | Normal |
| `SalesMemo` | STRING | 0 | 3 |  |  |
| `ReliefGroupId` | STRING | 1 | 2 | MICROSOFT CORPORATION | MICROSOFT CORPORATION |
| `IsExcludedFromInterestChargeCalculation` | STRING | 0 | 3 |  |  |
| `StatisticsGroupId` | STRING | 0 | 3 |  |  |
| `SalesOrderPoolId` | STRING | 0 | 3 |  |  |
| `OrganizationName` | STRING | 0 | 3 |  |  |
| `IsOrderNumberReferenceUsed` | STRING | 0 | 3 |  |  |
| `CustClassificationId` | STRING | 1 | 2 | 0 | 0 |
| `AddressValidTo` | STRING | 0 | 3 |  |  |
| `FederalComments` | STRING | 0 | 3 |  |  |
| `PersonGender` | STRING | 0 | 3 |  |  |
| `PaymentTerms` | STRING | 1 | 2 | No | No |
| `PrimaryContactPhoneDescription` | STRING | 0 | 3 |  |  |
| `AddressPostbox` | STRING | 0 | 3 |  |  |
| `SalesSubsegmentId` | STRING | 0 | 3 |  |  |
| `CustomerRebateGroupId` | STRING | 1 | 2 | Company | Company |
| `WarehouseOutboundShipmentProcessingPolicyName` | STRING | 0 | 3 |  |  |
| `AddressCounty` | STRING | 0 | 3 |  |  |
| `PrimaryContactURLRecordId` | STRING | 0 | 3 |  |  |
| `IsICMSContributor` | STRING | 0 | 3 |  |  |
| `InvoiceAddressValidTo` | STRING | 1 | 2 | en-US | en-US |
| `DeliveryAddressTimeZone` | STRING | 1 | 2 | No | No |
| `InvoiceAddressValidFrom` | STRING | 1 | 2 | 1950 N STEMMONS FWY SUITE 5010 | 1950 N STEMMONS FWY SUITE 5010 |
| `CreditLimit` | STRING | 1 | 2 | No | No |
| `CreditCardAddressVerificationLevel` | STRING | 0 | 3 |  |  |
| `WarehouseIsEntireShipmentFilled` | STRING | 0 | 3 |  |  |
| `PackingDutyLicense` | STRING | 1 | 2 | No | No |
| `NationalRegistryNumber` | STRING | 1 | 2 | No | No |
| `SiteId` | STRING | 1 | 2 | No | No |
| `InvoiceAddressCountryRegionISOCode` | STRING | 1 | 2 | No | No |
| `IsAllowCreateIndirectOrderLines` | STRING | 0 | 3 |  |  |
| `PrimaryContactURLPurpose` | STRING | 1 | 2 | 0 | 0 |
| `ChargesGroupId` | STRING | 0 | 3 |  |  |
| `PanStatus` | STRING | 1 | 2 | 0 | 0 |
| `CommissionSalesGroupId` | STRING | 1 | 2 | No | No |
| `NameAlias` | STRING | 1 | 2 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `PrimaryContactFaxPurpose` | STRING | 1 | 2 | No | No |
| `AddressStreetNumber` | STRING | 1 | 2 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `PersonLastName` | STRING | 1 | 2 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `PaymentIdType` | STRING | 1 | 2 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `VendorAccount` | STRING | 1 | 2 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `AddressCountryRegionISOCode` | STRING | 1 | 2 | No | No |
| `ResidenceForeignCountryRegionId` | STRING | 1 | 2 | No | No |
| `RFCNumber` | STRING | 1 | 2 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `PersonHobbies` | STRING | 0 | 3 |  |  |
| `ElectronicLocationId` | STRING | 0 | 3 |  |  |
| `InvoiceAddressZipCode` | STRING | 0 | 3 |  |  |
| `PrimaryContactLinkedInPurpose` | STRING | 0 | 3 |  |  |
| `IsOneTimeCustomer` | STRING | 1 | 2 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `ForeignCustomer` | STRING | 1 | 2 | No | No |
| `CustomerTMAGroupId` | STRING | 0 | 3 |  |  |
| `AddressValidFrom` | STRING | 1 | 2 | No | No |
| `OrganizationNumberOfEmployees` | STRING | 0 | 3 |  |  |
| `CompanyType` | STRING | 1 | 2 |  |  |
| `CustomerGroupId` | STRING | 0 | 3 |  |  |
| `GiroTypeInterestNote` | STRING | 0 | 3 |  |  |
| `DeliveryAddressZipCode` | STRING | 0 | 3 |  |  |
| `DeliveryReason` | STRING | 0 | 3 |  |  |
| `TaxRegistrationId` | STRING | 0 | 3 |  |  |
| `PaymentUseCashDiscount` | STRING | 0 | 3 |  |  |
| `DiscountPriceGroupId` | STRING | 0 | 3 |  |  |
| `AddressDescription` | STRING | 0 | 3 |  |  |
| `SuframaNumber` | STRING | 0 | 3 |  |  |
| `IdentificationNumber` | STRING | 0 | 3 |  |  |
| `AuthorityOffice` | STRING | 0 | 3 |  |  |
| `PersonPhoneticFirstName` | STRING | 0 | 3 |  |  |
| `PrimaryContactTelexPurpose` | STRING | 0 | 3 |  |  |
| `DeliveryAddressLatitude` | STRING | 0 | 3 |  |  |
| `InvoiceAddressCountryRegionId` | STRING | 0 | 3 |  |  |
| `PrimaryContactFacebookPurpose` | STRING | 0 | 3 |  |  |
| `CompanyChain` | STRING | 0 | 3 |  |  |
| `OverrideSalesTax` | STRING | 0 | 3 |  |  |
| `BrazilianINSSCEI` | STRING | 0 | 3 |  |  |
| `CommissionCustomerGroupId` | STRING | 0 | 3 |  |  |
| `PrimaryContactFaxDescription` | STRING | 0 | 3 |  |  |
| `NatureOfAssessee` | STRING | 0 | 3 |  |  |
| `WriteoffReason` | STRING | 0 | 3 |  |  |
| `PersonMiddleName` | STRING | 0 | 3 |  |  |
| `InvoiceAddressLocationId` | STRING | 0 | 3 |  |  |
| `PersonPhoneticLastName` | STRING | 0 | 3 |  |  |
| `LanguageId` | STRING | 0 | 3 |  |  |
| `IsPurchRequestUsed` | STRING | 0 | 3 |  |  |
| `AddressStreet` | STRING | 0 | 3 |  |  |
| `IsPublicSector_IT` | STRING | 0 | 3 |  |  |
| `SATRegistrationName_MX` | STRING | 0 | 3 |  |  |
| `TaxRegimeCode_MX` | STRING | 0 | 3 |  |  |
| `CFDITemporaryExport_MX` | STRING | 0 | 3 |  |  |
| `IsSimplifiedPrimaryAddress` | STRING | 0 | 3 |  |  |
| `IsSimplifiedDeliveryAddress` | STRING | 0 | 3 |  |  |
| `IsSimplifiedInvoiceAddress` | STRING | 0 | 3 |  |  |
| `CredManEligibleCreditLimitCurrency` | STRING | 0 | 3 |  |  |
| `CredManCustCreditMaxAlt` | STRING | 0 | 3 |  |  |
| `CredManStatusReasonId` | STRING | 0 | 3 |  |  |
| `CredManEligibleCreditMax` | STRING | 0 | 3 |  |  |
| `CredManCustUnlimitedCredit` | STRING | 0 | 3 |  |  |
| `CredManEligibleCreditLimitDate` | STRING | 0 | 3 |  |  |
| `CredManWithAgency` | STRING | 0 | 3 |  |  |
| `CredManCreditLimitDate` | STRING | 0 | 3 |  |  |
| `CredManNextSchedReviewDate` | STRING | 0 | 3 |  |  |
| `CredManLastReviewDate` | STRING | 0 | 3 |  |  |
| `CredManCustomerSince` | STRING | 0 | 3 |  |  |
| `CredManTitleHeld` | STRING | 0 | 3 |  |  |
| `CredManExclude` | STRING | 0 | 3 |  |  |
| `CredManBusinessStarted` | STRING | 0 | 3 |  |  |
| `CredManNotes` | STRING | 0 | 3 |  |  |
| `CredManCollectionGroupId` | STRING | 0 | 3 |  |  |
| `CredManGroupId` | STRING | 0 | 3 |  |  |
| `CredManAccountStatusId` | STRING | 0 | 3 |  |  |
| `CredManCreditLimitExpiryDate` | STRING | 0 | 3 |  |  |
| `KPFNettingActive` | STRING | 0 | 3 |  |  |
| `QMSApprovedCustomerGroupId` | STRING | 0 | 3 |  |  |
| `QMSWillPrintCustomerSpecificCertificateOfAnalysis` | STRING | 0 | 3 |  |  |
| `QMSCertificateOfAnalysisCustomerGroupId` | STRING | 0 | 3 |  |  |
| `QMSApprovedCustomerListCheckMethod` | STRING | 0 | 3 |  |  |
| `source_file_name` | STRING | 1 | 0 | customersv3__20261116_105417.csv | customersv3__20261116_105417.csv |
| `HASH_KEY` | STRING | 3 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:19.958000 | 2026-11-16 11:43:19.958000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:19.958000 | 2026-11-16 11:43:19.958000 |

## Sample rows

| CustomerAccount | AddressBrazilianCNPJOrCPF | PartyType | PrimaryContactFaxExtension | IsFuelSurchargeApplied | SalesTaxGroup | AddressCountryRegionId | ContactPersonId | CustomerPaymentFineCode | BirthCountyCode | InvoiceAddress | PackingMaterialFeeLicenseNumber | TransactionPresenceType | PrimaryContactTwitter | PrimaryContactEmailIsIM | InvoiceAddressCity | IsFinalUser | PrimaryContactEmail | DeliveryAddressCounty | HasSuframaDiscountPISandCOFINS | InvoiceAddressStreet | CURPNumber | PrimaryContactLinkedInDescription | DeliveryAddressCountryRegionId | ItemCustomerGroupId | PersonProfessionalTitle | SalesSegmentId | IsServiceDeliveryAddressBased | PrimaryContactTelexDescription | InvoiceAddressDistrictName | InvoiceAddressTimeZone | SalesAccountNumber | PrimaryContactFacebookDescription | PrimaryContactPhoneIsMobile | PrimaryContactFaxRecordId | TCSGroup | DeliveryAddressLocationId | AddressZipCode | GiroTypeProjInvoice | LineOfBusinessId | OrganizationPhoneticName | CreditCardCVC | DeliveryAddressCountryRegionISOCode | DeliveryAddressValidFrom | GiroTypeAccountStatement | CalculateWithholdingTax | ElectronicInvoiceEAN | DeliveryFreightZone | PrimaryContactFax | TaxExemptNumber | DeliveryAddressDescription | DeliveryAddressLongitude | BirthPlace | AddressCity | PersonInitials | DefaultECommerceOperator | CentralBankPurposeCode | GiroTypeCollectionletter | FullPrimaryAddress | OrderEntryDeadline | ForeignerId | WarehouseIsASNGenerated | AddressLongitude | CustomerType | PrimaryContactLinkedIn | PrimaryContactURL | IsFreightAccrued | PartyState | PartyNumber | InvoiceAccount | CentralBankPurposeNotes | AddressBuildingComplement | CollectionsContactPersonId | PersonMaritalStatus | AddressLocationId | PaymentSchedule | PrimaryContactTwitterPurpose | GiroType | InvoiceAddressDescription | AddressDistrictName | DeliveryTerms | NumberSequenceGroup | PersonChildrenNames | PaymentMethod | ForeignResident | DeliveryMode | PersonProfessionalSuffix | OnHoldStatus | WarehouseId | AccountStatement | DestinationCode | EInvoiceRegister | IRS1099CIndicator | FrenchSiret | PaymentDay | BrazilianNIT | FederalIndicator | EmployeeResponsibleNumber | PersonAnniversaryYear | DefaultInventoryStatusId | PrimaryContactEmailDescription | AddressTimeZone | PrimaryContactPhone | PrimaryContactPhoneRecordId | DeliveryAddressCity | InvoiceAddressCounty | PANReferenceNumber | DeliveryAddressStreet | SalesCurrencyCode | Priority | IsSalesTaxIncludedInPrices | BrazilianCNPJOrCPF | PaymentFactoringAccount | PANNumber | PrimaryContactTwitterDescription | PersonFirstName | BrazilianCCM | ReceiptEmail | TDSGroup | MultiLineDiscountCode | PersonAnniversaryDay | DefaultDimensionDisplayValue | SupplementaryItemGroupId | IsWithholdingTaxCalculated | PaymentSpecification | AddressRecordId | AddressBooks | PrimaryContactEmailPurpose | FulfillmentPolicyName | SalesDistrict | ConsolidationDay | IsExpressBillOfLadingAccepted | CreditCardAddressVerification | InvoiceAddressBuildingComplement | AddressState | AllowOnAccount | IsExcludedFromCollectionFeeCalculation | CustomerPaymentFinancialInterestCode | IsTransactionPostedAsShipment | IsExternallyMaintained | CreditLimitIsMandatory | PaymentTermsBaseDays | FiscalCode | KnownAs | PrimaryContactTelex | PaymentBankAccount | BrazilianIE | PrimaryContactEmailRecordId | PreferentialCustomer | ReceiptOption | AddressBrazilianIE | PersonAnniversaryMonth | PrimaryContactPhoneExtension | InvoiceAddressStreetNumber | PrimaryContactPhonePurpose | ExportSale | OrganizationNumber | InvoicePostingType | CreditCardAddressVerificationIsAuthorizationVoidedOnFailure | InvoiceAddressState | ReceiptCalendar | DeliveryAddressState | StateInscription | PersonLastNamePrefix | SalesReturnTaxGroup | PrimaryContactURLDescription | CustomerWithholdingContributionType | IsElectronicInvoice | FederalAgencyLocationCode | GiroTypeFreeTextInvoice | DeliveryAddressValidTo | PersonPhoneticMiddleName | OrganizationABCCode | BrazilianCNAE | WithholdingTaxGroupCode | NAFCode | AddressLatitude | TotalDiscountCode | PaymentCashDiscount | AddressLocationRoles | DeliveryAddressDistrictName | CollectionLetterCode | EInvoiceAttachment | MerchantID | CreditRating | PrimaryContactFacebook | DeliveryAddressBuildingComplement | DeliveryAddressStreetNumber | InvoiceAddressLongitude | LineDiscountCode | PartyCountry | InvoiceAddressLatitude | IsInSuframaRegion | IsIncomingFiscalDocumentGenerated | SalesMemo | ReliefGroupId | IsExcludedFromInterestChargeCalculation | StatisticsGroupId | SalesOrderPoolId | OrganizationName | IsOrderNumberReferenceUsed | CustClassificationId | AddressValidTo | FederalComments | PersonGender | PaymentTerms | PrimaryContactPhoneDescription | AddressPostbox | SalesSubsegmentId | CustomerRebateGroupId | WarehouseOutboundShipmentProcessingPolicyName | AddressCounty | PrimaryContactURLRecordId | IsICMSContributor | InvoiceAddressValidTo | DeliveryAddressTimeZone | InvoiceAddressValidFrom | CreditLimit | CreditCardAddressVerificationLevel | WarehouseIsEntireShipmentFilled | PackingDutyLicense | NationalRegistryNumber | SiteId | InvoiceAddressCountryRegionISOCode | IsAllowCreateIndirectOrderLines | PrimaryContactURLPurpose | ChargesGroupId | PanStatus | CommissionSalesGroupId | NameAlias | PrimaryContactFaxPurpose | AddressStreetNumber | PersonLastName | PaymentIdType | VendorAccount | AddressCountryRegionISOCode | ResidenceForeignCountryRegionId | RFCNumber | PersonHobbies | ElectronicLocationId | InvoiceAddressZipCode | PrimaryContactLinkedInPurpose | IsOneTimeCustomer | ForeignCustomer | CustomerTMAGroupId | AddressValidFrom | OrganizationNumberOfEmployees | CustomerGroupId | GiroTypeInterestNote | DeliveryAddressZipCode | DeliveryReason | TaxRegistrationId | PaymentUseCashDiscount | DiscountPriceGroupId | AddressDescription | SuframaNumber | IdentificationNumber | AuthorityOffice | PersonPhoneticFirstName | PrimaryContactTelexPurpose | DeliveryAddressLatitude | InvoiceAddressCountryRegionId | PrimaryContactFacebookPurpose | OverrideSalesTax | BrazilianINSSCEI | CommissionCustomerGroupId | PrimaryContactFaxDescription | NatureOfAssessee | WriteoffReason | PersonMiddleName | InvoiceAddressLocationId | PersonPhoneticLastName | LanguageId | IsPurchRequestUsed | AddressStreet | IsPublicSector_IT | SATRegistrationName_MX | TaxRegimeCode_MX | CFDITemporaryExport_MX | IsSimplifiedPrimaryAddress | IsSimplifiedDeliveryAddress | IsSimplifiedInvoiceAddress | CredManEligibleCreditLimitCurrency | CredManCustCreditMaxAlt | CredManStatusReasonId | CredManEligibleCreditMax | CredManCustUnlimitedCredit | CredManEligibleCreditLimitDate | CredManWithAgency | CredManCreditLimitDate | CredManNextSchedReviewDate | CredManLastReviewDate | CredManCustomerSince | CredManTitleHeld | CredManExclude | CredManBusinessStarted | CredManNotes | CredManCollectionGroupId | CredManGroupId | CredManAccountStatusId | CredManCreditLimitExpiryDate | KPFNettingActive | QMSApprovedCustomerGroupId | QMSWillPrintCustomerSpecificCertificateOfAnalysis | QMSCertificateOfAnalysisCustomerGroupId | QMSApprovedCustomerListCheckMethod | source_file_name | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100-000001 | NULL | Organization | NULL | No | NULL | USA | NULL | NULL | NULL | InvoiceAccount | NULL | DoesNotApply | NULL | <masked> | NULL | No | <masked> | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | No | NULL | NULL | NULL | NULL | NULL | No | 0 | NULL | NULL | 75207 | None | NULL | NULL | None | NULL | 1900-01-01 00:00:00.0000000 +00:00 | None | No | NULL | NULL | NULL | NULL | NULL | 0 | NULL | DALLAS | NULL | NULL | NULL | None | 1950 N STEMMONS FWY SUITE 5010 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | customersv3__20261116_105417.csv | <masked> | 2026-11-16 11:43:19.958000 | <masked> | 2026-11-16 11:43:19.958000 |
| TX 75207 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | customersv3__20261116_105417.csv | <masked> | 2026-11-16 11:43:19.958000 | <masked> | 2026-11-16 11:43:19.958000 |
| NULL | NULL | No | 0 | None | NULL | NULL | No | NULL | 1447 | NULL | NULL | NULL | NULL | <masked> | 1309 | NULL | <masked> | None | NULL | NULL | NULL | NULL | NULL | NULL | No | NULL | NULL | No | NULL | Always | NULL | No | No | NULL | NULL | NULL | 11 | 0 | NULL | NULL | NULL | NULL | 0 | NULL | NULL | NULL | NULL | USD | AllocationPriority10 | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | No | NULL | 5637146371 | NULL | NULL | NULL | NULL | 0 | No | None | NULL | TX | No | No | NULL | No | No | No | 0 | NULL | MICROSOFT CORPORATION | NULL | NULL | NULL | 0 | No | RetailEx3 | NULL | None | NULL | NULL | NULL | No | NULL | Standard | No | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | Other | No | NULL | None | 1900-01-01 00:00:00.0000000 +00:00 | NULL | None | NULL | NULL | NULL | 0 | <masked> | NULL | Business | NULL | None | No | NULL | NULL | NULL | NULL | <masked> | 0 | NULL | NULL | 0 | No | No | NULL | NULL | No | NULL | NULL | MICROSOFT CORPORATION | No | NULL | 2154-12-31 23:59:59.0000000 +00:00 | NULL | Unknown | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | 0 | No | 1900-01-01 00:00:00.0000000 +00:00 | NULL | 1900-01-01 00:00:00.0000000 +00:00 | 0 | Accept | No | NULL | NULL | NULL | NULL | No | NULL | NULL | NotAvailable | NULL | MICROSOFT CORPORATIO | NULL | LB #842467 | NULL | NULL | NULL | US | NULL | NULL | NULL | NULL | NULL | NULL | No | No | NULL | 2025-06-25 10:29:08.0000000 +00:00 | 0 | Blank | Corporate | None | NULL | NULL | NULL | Normal | NULL | MICROSOFT CORPORATION | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | NULL | No | NULL | NULL | NULL | Company | NULL | NULL | NULL | NULL | en-US | No | 1950 N STEMMONS FWY SUITE 5010 | No | NULL | NULL | No | No | No | No | NULL | 0 | NULL | 0 | No | 1900-01-01 12:00:00.0000000 +00:00 | No | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | No | No | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | No | NULL | No | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | customersv3__20261116_105417.csv | <masked> | 2026-11-16 11:43:19.958000 | <masked> | 2026-11-16 11:43:19.958000 |
