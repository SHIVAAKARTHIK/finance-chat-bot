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
- ContactPersonId
- CollectionsContactPersonId
- EmployeeResponsibleNumber
- PersonFirstName
- PersonLastNamePrefix
- PersonPhoneticMiddleName
- PersonLastName
- PersonPhoneticFirstName
- PersonMiddleName
- PersonPhoneticLastName
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: AddressBrazilianCNPJOrCPF, SalesTaxGroup all null
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
- `100-000001`
- `None`
- `TX 75207`

**AddressBrazilianCNPJOrCPF**
- `None`

**PartyType**
- `Organization`
- `No`
- `None`

**PrimaryContactFaxExtension**
- `None`
- `0`

**IsFuelSurchargeApplied**
- `None`
- `No`

**SalesTaxGroup**
- `None`

**AddressCountryRegionId**
- `None`
- `USA`

**CustomerPaymentFineCode**
- `None`

**BirthCountyCode**
- `None`
- `1447`

**InvoiceAddress**
- `None`
- `InvoiceAccount`

**PackingMaterialFeeLicenseNumber**
- `None`

**TransactionPresenceType**
- `None`
- `DoesNotApply`

**PrimaryContactTwitter**
- `None`

**InvoiceAddressCity**
- `None`
- `1309`

**IsFinalUser**
- `None`
- `No`

**DeliveryAddressCounty**
- `None`

**HasSuframaDiscountPISandCOFINS**
- `None`
- `No`

**InvoiceAddressStreet**
- `None`

**CURPNumber**
- `None`

**PrimaryContactLinkedInDescription**
- `None`

**DeliveryAddressCountryRegionId**
- `None`

**ItemCustomerGroupId**
- `None`

**PersonProfessionalTitle**
- `None`
- `No`

**SalesSegmentId**
- `None`

**IsServiceDeliveryAddressBased**
- `None`
- `No`

**PrimaryContactTelexDescription**
- `None`
- `No`

**InvoiceAddressDistrictName**
- `None`

**InvoiceAddressTimeZone**
- `None`
- `Always`

**SalesAccountNumber**
- `None`

**PrimaryContactFacebookDescription**
- `None`
- `No`

**PrimaryContactPhoneIsMobile**
- `No`
- `None`

**PrimaryContactFaxRecordId**
- `None`
- `0`

**TCSGroup**
- `None`

**DeliveryAddressLocationId**
- `None`

**AddressZipCode**
- `75207`
- `None`
- `11`

**GiroTypeProjInvoice**
- `0`
- `None`

**LineOfBusinessId**
- `None`

**OrganizationPhoneticName**
- `None`

**CreditCardCVC**
- `None`

**DeliveryAddressCountryRegionISOCode**
- `None`

**DeliveryAddressValidFrom**
- `0`
- `1900-01-01 00:00:00.0000000 +00:00`
- `None`

**GiroTypeAccountStatement**
- `None`

**CalculateWithholdingTax**
- `None`
- `No`

**ElectronicInvoiceEAN**
- `None`

**DeliveryFreightZone**
- `None`

**PrimaryContactFax**
- `None`
- `USD`

**TaxExemptNumber**
- `None`
- `AllocationPriority10`

**DeliveryAddressDescription**
- `None`
- `No`

**DeliveryAddressLongitude**
- `None`
- `0`

**BirthPlace**
- `None`

**AddressCity**
- `None`
- `DALLAS`

**PersonInitials**
- `None`

**DefaultECommerceOperator**
- `None`

**CentralBankPurposeCode**
- `None`

**GiroTypeCollectionletter**
- `None`

**FullPrimaryAddress**
- `None`
- `1950 N STEMMONS FWY SUITE 5010`

**OrderEntryDeadline**
- `None`

**ForeignerId**
- `None`
- `0`

**WarehouseIsASNGenerated**
- `None`

**AddressLongitude**
- `None`

**CustomerType**
- `None`
- `No`

**PrimaryContactLinkedIn**
- `None`

**PrimaryContactURL**
- `None`
- `5637146371`

**IsFreightAccrued**
- `None`

**PartyState**
- `None`

**PartyNumber**
- `None`

**InvoiceAccount**
- `None`

**CentralBankPurposeNotes**
- `None`
- `0`

**AddressBuildingComplement**
- `None`
- `No`

**PersonMaritalStatus**
- `None`

**AddressLocationId**
- `None`
- `TX`

**PaymentSchedule**
- `None`
- `No`

**PrimaryContactTwitterPurpose**
- `None`
- `No`

**GiroType**
- `None`

**InvoiceAddressDescription**
- `None`
- `No`

**AddressDistrictName**
- `None`
- `No`

**DeliveryTerms**
- `None`
- `No`

**NumberSequenceGroup**
- `None`
- `0`

**PersonChildrenNames**
- `None`

**PaymentMethod**
- `None`
- `MICROSOFT CORPORATION`

**ForeignResident**
- `None`

**DeliveryMode**
- `None`

**PersonProfessionalSuffix**
- `None`

**OnHoldStatus**
- `None`
- `0`

**WarehouseId**
- `None`
- `No`

**AccountStatement**
- `None`
- `RetailEx3`

**DestinationCode**
- `None`

**EInvoiceRegister**
- `None`

**IRS1099CIndicator**
- `None`

**FrenchSiret**
- `None`

**PaymentDay**
- `None`

**BrazilianNIT**
- `None`
- `No`

**FederalIndicator**
- `None`

**PersonAnniversaryYear**
- `None`
- `No`

**DefaultInventoryStatusId**
- `None`

**AddressTimeZone**
- `None`

**PrimaryContactPhone**
- `None`

**PrimaryContactPhoneRecordId**
- `None`

**DeliveryAddressCity**
- `None`

**InvoiceAddressCounty**
- `None`

**PANReferenceNumber**
- `None`
- `Other`

**DeliveryAddressStreet**
- `None`
- `No`

**SalesCurrencyCode**
- `None`

**Priority**
- `None`

**IsSalesTaxIncludedInPrices**
- `None`
- `1900-01-01 00:00:00.0000000 +00:00`

**BrazilianCNPJOrCPF**
- `None`

**PaymentFactoringAccount**
- `None`

**PANNumber**
- `None`

**PrimaryContactTwitterDescription**
- `None`

**BrazilianCCM**
- `None`
- `0`

**TDSGroup**
- `None`

**MultiLineDiscountCode**
- `None`
- `Business`

**PersonAnniversaryDay**
- `None`

**DefaultDimensionDisplayValue**
- `None`

**SupplementaryItemGroupId**
- `None`
- `No`

**IsWithholdingTaxCalculated**
- `None`

**PaymentSpecification**
- `None`

**AddressRecordId**
- `None`

**AddressBooks**
- `None`

**FulfillmentPolicyName**
- `None`
- `0`

**SalesDistrict**
- `None`

**ConsolidationDay**
- `None`

**IsExpressBillOfLadingAccepted**
- `None`
- `0`

**CreditCardAddressVerification**
- `None`
- `No`

**InvoiceAddressBuildingComplement**
- `None`
- `No`

**AddressState**
- `None`

**AllowOnAccount**
- `None`

**IsExcludedFromCollectionFeeCalculation**
- `None`
- `No`

**CustomerPaymentFinancialInterestCode**
- `None`

**IsTransactionPostedAsShipment**
- `None`

**IsExternallyMaintained**
- `None`
- `MICROSOFT CORPORATION`

**CreditLimitIsMandatory**
- `None`
- `No`

**PaymentTermsBaseDays**
- `None`

**FiscalCode**
- `None`
- `2154-12-31 23:59:59.0000000 +00:00`

**KnownAs**
- `None`

**PrimaryContactTelex**
- `None`
- `Unknown`

**PaymentBankAccount**
- `None`

**BrazilianIE**
- `None`

**PreferentialCustomer**
- `None`

**ReceiptOption**
- `None`

**AddressBrazilianIE**
- `None`

**PersonAnniversaryMonth**
- `None`

**PrimaryContactPhoneExtension**
- `None`
- `0`

**InvoiceAddressStreetNumber**
- `None`
- `No`

**PrimaryContactPhonePurpose**
- `None`
- `1900-01-01 00:00:00.0000000 +00:00`

**ExportSale**
- `None`

**OrganizationNumber**
- `None`
- `1900-01-01 00:00:00.0000000 +00:00`

**InvoicePostingType**
- `None`
- `0`

**CreditCardAddressVerificationIsAuthorizationVoidedOnFailure**
- `None`
- `Accept`

**InvoiceAddressState**
- `None`
- `No`

**ReceiptCalendar**
- `None`

**DeliveryAddressState**
- `None`

**StateInscription**
- `None`

**SalesReturnTaxGroup**
- `None`
- `No`

**PrimaryContactURLDescription**
- `None`

**CustomerWithholdingContributionType**
- `None`

**IsElectronicInvoice**
- `None`
- `NotAvailable`

**FederalAgencyLocationCode**
- `None`

**GiroTypeFreeTextInvoice**
- `None`
- `MICROSOFT CORPORATIO`

**DeliveryAddressValidTo**
- `None`

**OrganizationABCCode**
- `None`

**BrazilianCNAE**
- `None`

**WithholdingTaxGroupCode**
- `None`

**NAFCode**
- `None`
- `US`

**AddressLatitude**
- `None`

**TotalDiscountCode**
- `None`

**PaymentCashDiscount**
- `None`

**AddressLocationRoles**
- `None`

**DeliveryAddressDistrictName**
- `None`

**CollectionLetterCode**
- `None`

**EInvoiceAttachment**
- `None`
- `No`

**MerchantID**
- `None`
- `No`

**CreditRating**
- `None`

**PrimaryContactFacebook**
- `None`
- `2025-06-25 10:29:08.0000000 +00:00`

**DeliveryAddressBuildingComplement**
- `None`
- `0`

**DeliveryAddressStreetNumber**
- `None`
- `Blank`

**InvoiceAddressLongitude**
- `None`
- `Corporate`

**LineDiscountCode**
- `None`

**PartyCountry**
- `None`

**InvoiceAddressLatitude**
- `None`

**IsInSuframaRegion**
- `None`

**IsIncomingFiscalDocumentGenerated**
- `None`
- `Normal`

**SalesMemo**
- `None`

**ReliefGroupId**
- `None`
- `MICROSOFT CORPORATION`

**IsExcludedFromInterestChargeCalculation**
- `None`

**StatisticsGroupId**
- `None`

**SalesOrderPoolId**
- `None`

**OrganizationName**
- `None`

**IsOrderNumberReferenceUsed**
- `None`

**CustClassificationId**
- `None`
- `0`

**AddressValidTo**
- `None`

**FederalComments**
- `None`

**PersonGender**
- `None`

**PaymentTerms**
- `None`
- `No`

**PrimaryContactPhoneDescription**
- `None`

**AddressPostbox**
- `None`

**SalesSubsegmentId**
- `None`

**CustomerRebateGroupId**
- `None`
- `Company`

**WarehouseOutboundShipmentProcessingPolicyName**
- `None`

**AddressCounty**
- `None`

**PrimaryContactURLRecordId**
- `None`

**IsICMSContributor**
- `None`

**InvoiceAddressValidTo**
- `None`
- `en-US`

**DeliveryAddressTimeZone**
- `None`
- `No`

**InvoiceAddressValidFrom**
- `None`
- `1950 N STEMMONS FWY SUITE 5010`

**CreditLimit**
- `None`
- `No`

**CreditCardAddressVerificationLevel**
- `None`

**WarehouseIsEntireShipmentFilled**
- `None`

**PackingDutyLicense**
- `None`
- `No`

**NationalRegistryNumber**
- `None`
- `No`

**SiteId**
- `None`
- `No`

**InvoiceAddressCountryRegionISOCode**
- `None`
- `No`

**IsAllowCreateIndirectOrderLines**
- `None`

**PrimaryContactURLPurpose**
- `None`
- `0`

**ChargesGroupId**
- `None`

**PanStatus**
- `None`
- `0`

**CommissionSalesGroupId**
- `None`
- `No`

**NameAlias**
- `None`
- `1900-01-01 12:00:00.0000000 +00:00`

**PrimaryContactFaxPurpose**
- `None`
- `No`

**AddressStreetNumber**
- `None`
- `1900-01-01 12:00:00.0000000 +00:00`

**PaymentIdType**
- `None`
- `1900-01-01 12:00:00.0000000 +00:00`

**VendorAccount**
- `None`
- `1900-01-01 12:00:00.0000000 +00:00`

**AddressCountryRegionISOCode**
- `None`
- `No`

**ResidenceForeignCountryRegionId**
- `None`
- `No`

**RFCNumber**
- `None`
- `1900-01-01 12:00:00.0000000 +00:00`

**PersonHobbies**
- `None`

**ElectronicLocationId**
- `None`

**InvoiceAddressZipCode**
- `None`

**PrimaryContactLinkedInPurpose**
- `None`

**IsOneTimeCustomer**
- `None`
- `1900-01-01 12:00:00.0000000 +00:00`

**ForeignCustomer**
- `None`
- `No`

**CustomerTMAGroupId**
- `None`

**AddressValidFrom**
- `None`
- `No`

**OrganizationNumberOfEmployees**
- `None`

**CustomerGroupId**
- `None`

**GiroTypeInterestNote**
- `None`

**DeliveryAddressZipCode**
- `None`

**DeliveryReason**
- `None`

**TaxRegistrationId**
- `None`

**PaymentUseCashDiscount**
- `None`

**DiscountPriceGroupId**
- `None`

**AddressDescription**
- `None`

**SuframaNumber**
- `None`

**IdentificationNumber**
- `None`

**AuthorityOffice**
- `None`

**PrimaryContactTelexPurpose**
- `None`

**DeliveryAddressLatitude**
- `None`

**InvoiceAddressCountryRegionId**
- `None`

**PrimaryContactFacebookPurpose**
- `None`

**OverrideSalesTax**
- `None`

**BrazilianINSSCEI**
- `None`

**CommissionCustomerGroupId**
- `None`

**PrimaryContactFaxDescription**
- `None`

**NatureOfAssessee**
- `None`

**WriteoffReason**
- `None`

**InvoiceAddressLocationId**
- `None`

**LanguageId**
- `None`

**IsPurchRequestUsed**
- `None`

**AddressStreet**
- `None`

**IsPublicSector_IT**
- `None`

**SATRegistrationName_MX**
- `None`

**TaxRegimeCode_MX**
- `None`

**CFDITemporaryExport_MX**
- `None`

**IsSimplifiedPrimaryAddress**
- `None`

**IsSimplifiedDeliveryAddress**
- `None`

**IsSimplifiedInvoiceAddress**
- `None`

**CredManEligibleCreditLimitCurrency**
- `None`

**CredManCustCreditMaxAlt**
- `None`

**CredManStatusReasonId**
- `None`

**CredManEligibleCreditMax**
- `None`

**CredManCustUnlimitedCredit**
- `None`

**CredManEligibleCreditLimitDate**
- `None`

**CredManWithAgency**
- `None`

**CredManCreditLimitDate**
- `None`

**CredManNextSchedReviewDate**
- `None`

**CredManLastReviewDate**
- `None`

**CredManCustomerSince**
- `None`

**CredManTitleHeld**
- `None`

**CredManExclude**
- `None`

**CredManBusinessStarted**
- `None`

**CredManNotes**
- `None`

**CredManCollectionGroupId**
- `None`

**CredManGroupId**
- `None`

**CredManAccountStatusId**
- `None`

**CredManCreditLimitExpiryDate**
- `None`

**KPFNettingActive**
- `None`

**QMSApprovedCustomerGroupId**
- `None`

**QMSWillPrintCustomerSpecificCertificateOfAnalysis**
- `None`

**QMSCertificateOfAnalysisCustomerGroupId**
- `None`

**QMSApprovedCustomerListCheckMethod**
- `None`

**source_file_name**
- `customersv3__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:43:19.958440+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:19.958440+00:00`

## Empty columns

Empty in every row: `AddressBrazilianCNPJOrCPF`, `SalesTaxGroup`, `CustomerPaymentFineCode`, `PackingMaterialFeeLicenseNumber`, `PrimaryContactTwitter`, `PrimaryContactEmail`, `InvoiceAddressStreet`, `CURPNumber`, `PrimaryContactLinkedInDescription`, `DeliveryAddressCountryRegionId`, `ItemCustomerGroupId`, `SalesSegmentId`, `InvoiceAddressDistrictName`, `SalesAccountNumber`, `TCSGroup`, `DeliveryAddressLocationId`, `LineOfBusinessId`, `OrganizationPhoneticName`, `DeliveryAddressCountryRegionISOCode`, `ElectronicInvoiceEAN`, `DeliveryFreightZone`, `BirthPlace`, `PersonInitials`, `DefaultECommerceOperator`, `CentralBankPurposeCode`, `OrderEntryDeadline`, `WarehouseIsASNGenerated`, `AddressLongitude`, `PrimaryContactLinkedIn`, `IsFreightAccrued`, `PartyState`, `PartyNumber`, `InvoiceAccount`, `PersonMaritalStatus`, `GiroType`, `PersonChildrenNames`, `ForeignResident`, `DeliveryMode`, `PersonProfessionalSuffix`, `DestinationCode`, `IRS1099CIndicator`, `FrenchSiret`, `PaymentDay`, `FederalIndicator`, `DefaultInventoryStatusId`, `PrimaryContactEmailDescription`, `AddressTimeZone`, `PrimaryContactPhone`, `PrimaryContactPhoneRecordId`, `DeliveryAddressCity`, `InvoiceAddressCounty`, `SalesCurrencyCode`, `BrazilianCNPJOrCPF`, `PANNumber`, `PrimaryContactTwitterDescription`, `PersonFirstName`, `ReceiptEmail`, `TDSGroup`, `PersonAnniversaryDay`, `IsWithholdingTaxCalculated`, `PaymentSpecification`, `AddressRecordId`, `AddressBooks`, `PrimaryContactEmailPurpose`, `SalesDistrict`, `ConsolidationDay`, `AddressState`, `AllowOnAccount`, `CustomerPaymentFinancialInterestCode`, `IsTransactionPostedAsShipment`, `PaymentTermsBaseDays`, `KnownAs`, `PaymentBankAccount`, `BrazilianIE`, `PrimaryContactEmailRecordId`, `PreferentialCustomer`, `ReceiptOption`, `AddressBrazilianIE`, `PersonAnniversaryMonth`, `ExportSale`, `ReceiptCalendar`, `DeliveryAddressState`, `StateInscription`, `PersonLastNamePrefix`, `PrimaryContactURLDescription`, `CustomerWithholdingContributionType`, `FederalAgencyLocationCode`, `DeliveryAddressValidTo`, `OrganizationABCCode`, `BrazilianCNAE`, `WithholdingTaxGroupCode`, `AddressLatitude`, `TotalDiscountCode`, `PaymentCashDiscount`, `AddressLocationRoles`, `DeliveryAddressDistrictName`, `CollectionLetterCode`, `CreditRating`, `PartyCountry`, `InvoiceAddressLatitude`, `IsInSuframaRegion`, `SalesMemo`, `IsExcludedFromInterestChargeCalculation`, `StatisticsGroupId`, `SalesOrderPoolId`, `OrganizationName`, `IsOrderNumberReferenceUsed`, `AddressValidTo`, `FederalComments`, `PersonGender`, `PrimaryContactPhoneDescription`, `AddressPostbox`, `SalesSubsegmentId`, `WarehouseOutboundShipmentProcessingPolicyName`, `AddressCounty`, `PrimaryContactURLRecordId`, `IsICMSContributor`, `CreditCardAddressVerificationLevel`, `WarehouseIsEntireShipmentFilled`, `IsAllowCreateIndirectOrderLines`, `ChargesGroupId`, `PersonHobbies`, `ElectronicLocationId`, `InvoiceAddressZipCode`, `PrimaryContactLinkedInPurpose`, `CustomerTMAGroupId`, `OrganizationNumberOfEmployees`, `CustomerGroupId`, `GiroTypeInterestNote`, `DeliveryAddressZipCode`, `DeliveryReason`, `TaxRegistrationId`, `PaymentUseCashDiscount`, `DiscountPriceGroupId`, `AddressDescription`, `SuframaNumber`, `IdentificationNumber`, `AuthorityOffice`, `PersonPhoneticFirstName`, `PrimaryContactTelexPurpose`, `DeliveryAddressLatitude`, `InvoiceAddressCountryRegionId`, `PrimaryContactFacebookPurpose`, `CompanyChain`, `OverrideSalesTax`, `BrazilianINSSCEI`, `CommissionCustomerGroupId`, `PrimaryContactFaxDescription`, `NatureOfAssessee`, `WriteoffReason`, `PersonMiddleName`, `InvoiceAddressLocationId`, `PersonPhoneticLastName`, `LanguageId`, `IsPurchRequestUsed`, `AddressStreet`, `IsPublicSector_IT`, `SATRegistrationName_MX`, `TaxRegimeCode_MX`, `CFDITemporaryExport_MX`, `IsSimplifiedPrimaryAddress`, `IsSimplifiedDeliveryAddress`, `IsSimplifiedInvoiceAddress`, `CredManEligibleCreditLimitCurrency`, `CredManCustCreditMaxAlt`, `CredManStatusReasonId`, `CredManEligibleCreditMax`, `CredManCustUnlimitedCredit`, `CredManEligibleCreditLimitDate`, `CredManWithAgency`, `CredManCreditLimitDate`, `CredManNextSchedReviewDate`, `CredManLastReviewDate`, `CredManCustomerSince`, `CredManTitleHeld`, `CredManExclude`, `CredManBusinessStarted`, `CredManNotes`, `CredManCollectionGroupId`, `CredManGroupId`, `CredManAccountStatusId`, `CredManCreditLimitExpiryDate`, `KPFNettingActive`, `QMSApprovedCustomerGroupId`, `QMSWillPrintCustomerSpecificCertificateOfAnalysis`, `QMSCertificateOfAnalysisCustomerGroupId`, `QMSApprovedCustomerListCheckMethod`. Do not filter or group on them.
