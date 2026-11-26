---
name: fact_customer_payment_journal_lines
schema: silver
layer: silver
domain: ar
type: table
status: active
purpose: Lines of customer payment journals (voucher; invoice being paid).
grain: one row per dataAreaId + JournalBatchNumber + LineNumber (one payment line)
primary_key: []
entity_column: dataAreaId
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
proposed_fields: []
reviewed: false
---

# fact_customer_payment_journal_lines

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `dataAreaId` | string |  |  | `dataAreaId` |
| `JournalBatchNumber` | string |  |  | `JournalBatchNumber` |
| `LineNumber` | int |  |  | `LineNumber` |
| `UseSalesTaxDirectionFromMainAccount` | string |  |  | `UseSalesTaxDirectionFromMainAccount` |
| `MarkedInvoice` | string |  |  | `MarkedInvoice` |
| `Voucher` | string |  |  | `Voucher` |
| `DepositNumber` | string |  |  | `DepositNumber` |
| `ItemWithholdingTaxGroup` | string |  |  | `ItemWithholdingTaxGroup` |
| `OffsetAccountType` | string |  |  | `OffsetAccountType` |
| `PostdatedCheckCashierDisplayValue` | string |  |  | `PostdatedCheckCashierDisplayValue` |
| `PostdatedCheckMaturityDate` | timestamp |  |  | `PostdatedCheckMaturityDate` |
| `SettleVoucher` | string |  |  | `SettleVoucher` |
| `TransactionDate` | timestamp |  |  | `TransactionDate` |
| `NACHAIATOFACScreeningIndicator` | string |  |  | `NACHAIATOFACScreeningIndicator` |
| `BankTransactionType` | string |  |  | `BankTransactionType` |
| `PaymentReference` | string |  |  | `PaymentReference` |
| `CustomerName` | string |  |  | `CustomerName` |
| `ChineseVoucherType` | string |  |  | `ChineseVoucherType` |
| `NACHAIATForeignExchangeIndicator` | string |  |  | `NACHAIATForeignExchangeIndicator` |
| `PostdatedCheckSalespersonDisplayValue` | string |  |  | `PostdatedCheckSalespersonDisplayValue` |
| `NACHAIATForeignExchangeReferenceIndicator` | string |  |  | `NACHAIATForeignExchangeReferenceIndicator` |
| `DebitAmount` | decimal |  |  | `DebitAmount` |
| `TaxItemGroup` | string |  |  | `TaxItemGroup` |
| `NACHAIATOFACSecondaryScreeningIndicator` | string |  |  | `NACHAIATOFACSecondaryScreeningIndicator` |
| `ThirdPartyBankAccountId` | string |  |  | `ThirdPartyBankAccountId` |
| `TransactionText` | string |  |  | `TransactionText` |
| `PostdatedCheckNumber` | string |  |  | `PostdatedCheckNumber` |
| `AccountDisplayValue` | string |  |  | `AccountDisplayValue` |
| `OffsetAccountDisplayValue` | string |  |  | `OffsetAccountDisplayValue` |
| `DefaultDimensionsForAccountDisplayValue` | string |  |  | `DefaultDimensionsForAccountDisplayValue` |
| `PostdatedCheckOriginalCheckNumber` | string |  |  | `PostdatedCheckOriginalCheckNumber` |
| `PaymentMethodName` | string |  |  | `PaymentMethodName` |
| `CentralBankImportDate` | timestamp |  |  | `CentralBankImportDate` |
| `NACHAIATReceivingDFIQualifier` | string |  |  | `NACHAIATReceivingDFIQualifier` |
| `OffsetTransactionText` | string |  |  | `OffsetTransactionText` |
| `MarkedInvoiceCompany` | string |  |  | `MarkedInvoiceCompany` |
| `UseABankDepositSlip` | string |  |  | `UseABankDepositSlip` |
| `PaymentSpecification` | string |  |  | `PaymentSpecification` |
| `OffsetFinTagDisplayValue` | string |  |  | `OffsetFinTagDisplayValue` |
| `PostdatedCheckIsReplacementCheck` | string |  |  | `PostdatedCheckIsReplacementCheck` |
| `NACHAIATOriginatingDFIQualifier` | string |  |  | `NACHAIATOriginatingDFIQualifier` |
| `AccountType` | string |  |  | `AccountType` |
| `TaxGroup` | string |  |  | `TaxGroup` |
| `ExchangeRate` | decimal |  |  | `ExchangeRate` |
| `ReportingCurrencyExchRate` | decimal |  |  | `ReportingCurrencyExchRate` |
| `FinTagDisplayValue` | string |  |  | `FinTagDisplayValue` |
| `PaymentId` | string |  |  | `PaymentId` |
| `PostingProfile` | string |  |  | `PostingProfile` |
| `CalculateWithholdingTax` | string |  |  | `CalculateWithholdingTax` |
| `PostdatedCheckReasonForStop` | string |  |  | `PostdatedCheckReasonForStop` |
| `CreditAmount` | decimal |  |  | `CreditAmount` |
| `OverrideSalesTax` | string |  |  | `OverrideSalesTax` |
| `OffsetCompany` | string |  |  | `OffsetCompany` |
| `IsPrepayment` | string |  |  | `IsPrepayment` |
| `NACHAIATForeignExchangeReference` | string |  |  | `NACHAIATForeignExchangeReference` |
| `DefaultDimensionsForOffsetAccountDisplayValue` | string |  |  | `DefaultDimensionsForOffsetAccountDisplayValue` |
| `ReportingCurrencyExchRateSecondary` | decimal |  |  | `ReportingCurrencyExchRateSecondary` |
| `CurrencyCode` | string |  |  | `CurrencyCode` |
| `SecondaryExchangeRate` | decimal |  |  | `SecondaryExchangeRate` |
| `PostdatedCheckReceivedDate` | timestamp |  |  | `PostdatedCheckReceivedDate` |
| `Company` | string |  |  | `Company` |
| `PostdatedCheckBankBranch` | string |  |  | `PostdatedCheckBankBranch` |
| `CentralBankPurposeCode` | string |  |  | `CentralBankPurposeCode` |
| `PostdatedCheckReplacementComments` | string |  |  | `PostdatedCheckReplacementComments` |
| `PostdatedCheckStopPayment` | string |  |  | `PostdatedCheckStopPayment` |
| `ChineseVoucher` | string |  |  | `ChineseVoucher` |
| `PostdatedCheckBankName` | string |  |  | `PostdatedCheckBankName` |
| `CentralBankPurposeText` | string |  |  | `CentralBankPurposeText` |
| `PaymentNotes` | string |  |  | `PaymentNotes` |

## Values

**JournalBatchNumber**
- `100-000227`
- `100-000234`

**LineNumber**
- `1`

**UseSalesTaxDirectionFromMainAccount**
- `No`

**MarkedInvoice**
- `100-000002`
- `100-000003`

**Voucher**
- `CPJ-000000001`
- `CPJ-000000002`

**DepositNumber**
- `None`

**ItemWithholdingTaxGroup**
- `None`

**OffsetAccountType**
- `Ledger`
- `Bank`

**PostdatedCheckCashierDisplayValue**
- `None`

**PostdatedCheckMaturityDate**
- `1900-01-01 12:00:00+00:00`

**SettleVoucher**
- `SelectedTransact`

**TransactionDate**
- `2026-10-26 12:00:00+00:00`
- `2026-10-23 12:00:00+00:00`

**NACHAIATOFACScreeningIndicator**
- `Zero`

**BankTransactionType**
- `None`

**PaymentReference**
- `None`

**CustomerName**
- `MICROSOFT CORPORATION`

**ChineseVoucherType**
- `None`

**NACHAIATForeignExchangeIndicator**
- `None`

**PostdatedCheckSalespersonDisplayValue**
- `None`

**NACHAIATForeignExchangeReferenceIndicator**
- `One`

**DebitAmount**
- `0`

**TaxItemGroup**
- `None`

**NACHAIATOFACSecondaryScreeningIndicator**
- `Zero`

**ThirdPartyBankAccountId**
- `None`

**TransactionText**
- `None`

**PostdatedCheckNumber**
- `None`

**AccountDisplayValue**
- `100\-000001`

**OffsetAccountDisplayValue**
- `None`
- `Central`

**DefaultDimensionsForAccountDisplayValue**
- `None`

**PostdatedCheckOriginalCheckNumber**
- `None`

**PaymentMethodName**
- `None`

**CentralBankImportDate**
- `1900-01-01 12:00:00+00:00`

**NACHAIATReceivingDFIQualifier**
- `One`

**OffsetTransactionText**
- `None`

**UseABankDepositSlip**
- `No`

**PaymentSpecification**
- `None`

**OffsetFinTagDisplayValue**
- `None`

**PostdatedCheckIsReplacementCheck**
- `No`

**NACHAIATOriginatingDFIQualifier**
- `One`

**AccountType**
- `Cust`

**TaxGroup**
- `None`

**ExchangeRate**
- `100`

**ReportingCurrencyExchRate**
- `100`

**FinTagDisplayValue**
- `None`

**PaymentId**
- `None`

**PostingProfile**
- `GEN`

**CalculateWithholdingTax**
- `No`

**PostdatedCheckReasonForStop**
- `None`

**CreditAmount**
- `1000`

**OverrideSalesTax**
- `No`

**IsPrepayment**
- `No`

**NACHAIATForeignExchangeReference**
- `None`

**DefaultDimensionsForOffsetAccountDisplayValue**
- `None`

**ReportingCurrencyExchRateSecondary**
- `0`

**CurrencyCode**
- `USD`

**SecondaryExchangeRate**
- `0`

**PostdatedCheckReceivedDate**
- `1900-01-01 12:00:00+00:00`

**PostdatedCheckBankBranch**
- `None`

**CentralBankPurposeCode**
- `None`

**PostdatedCheckReplacementComments**
- `None`

**PostdatedCheckStopPayment**
- `No`

**ChineseVoucher**
- `None`

**PostdatedCheckBankName**
- `None`

**CentralBankPurposeText**
- `None`

**PaymentNotes**
- `None`

## Empty columns

Empty in every row: `DepositNumber`, `ItemWithholdingTaxGroup`, `PostdatedCheckCashierDisplayValue`, `BankTransactionType`, `PaymentReference`, `ChineseVoucherType`, `PostdatedCheckSalespersonDisplayValue`, `TaxItemGroup`, `ThirdPartyBankAccountId`, `TransactionText`, `PostdatedCheckNumber`, `DefaultDimensionsForAccountDisplayValue`, `PostdatedCheckOriginalCheckNumber`, `PaymentMethodName`, `OffsetTransactionText`, `PaymentSpecification`, `OffsetFinTagDisplayValue`, `TaxGroup`, `FinTagDisplayValue`, `PaymentId`, `PostdatedCheckReasonForStop`, `NACHAIATForeignExchangeReference`, `DefaultDimensionsForOffsetAccountDisplayValue`, `PostdatedCheckBankBranch`, `CentralBankPurposeCode`, `PostdatedCheckReplacementComments`, `ChineseVoucher`, `PostdatedCheckBankName`, `CentralBankPurposeText`, `PaymentNotes`. Do not filter or group on them.
