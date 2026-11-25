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
row_count: 2
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
- `100-000227`: 1 rows
- `100-000234`: 1 rows

**LineNumber**
- `1`: 2 rows

**UseSalesTaxDirectionFromMainAccount**
- `No`: 2 rows

**MarkedInvoice**
- `100-000002`: 1 rows
- `100-000003`: 1 rows

**Voucher**
- `CPJ-000000001`: 1 rows
- `CPJ-000000002`: 1 rows

**DepositNumber**
- `None`: 2 rows

**ItemWithholdingTaxGroup**
- `None`: 2 rows

**OffsetAccountType**
- `Ledger`: 1 rows
- `Bank`: 1 rows

**PostdatedCheckCashierDisplayValue**
- `None`: 2 rows

**PostdatedCheckMaturityDate**
- `1900-01-01 12:00:00+00:00`: 2 rows

**SettleVoucher**
- `SelectedTransact`: 2 rows

**TransactionDate**
- `2026-10-26 12:00:00+00:00`: 1 rows
- `2026-10-23 12:00:00+00:00`: 1 rows

**NACHAIATOFACScreeningIndicator**
- `Zero`: 2 rows

**BankTransactionType**
- `None`: 2 rows

**PaymentReference**
- `None`: 2 rows

**CustomerName**
- `MICROSOFT CORPORATION`: 2 rows

**ChineseVoucherType**
- `None`: 2 rows

**NACHAIATForeignExchangeIndicator**
- `None`: 2 rows

**PostdatedCheckSalespersonDisplayValue**
- `None`: 2 rows

**NACHAIATForeignExchangeReferenceIndicator**
- `One`: 2 rows

**DebitAmount**
- `0`: 2 rows

**TaxItemGroup**
- `None`: 2 rows

**NACHAIATOFACSecondaryScreeningIndicator**
- `Zero`: 2 rows

**ThirdPartyBankAccountId**
- `None`: 2 rows

**TransactionText**
- `None`: 2 rows

**PostdatedCheckNumber**
- `None`: 2 rows

**AccountDisplayValue**
- `100\-000001`: 2 rows

**OffsetAccountDisplayValue**
- `None`: 1 rows
- `Central`: 1 rows

**DefaultDimensionsForAccountDisplayValue**
- `None`: 2 rows

**PostdatedCheckOriginalCheckNumber**
- `None`: 2 rows

**PaymentMethodName**
- `None`: 2 rows

**CentralBankImportDate**
- `1900-01-01 12:00:00+00:00`: 2 rows

**NACHAIATReceivingDFIQualifier**
- `One`: 2 rows

**OffsetTransactionText**
- `None`: 2 rows

**UseABankDepositSlip**
- `No`: 2 rows

**PaymentSpecification**
- `None`: 2 rows

**OffsetFinTagDisplayValue**
- `None`: 2 rows

**PostdatedCheckIsReplacementCheck**
- `No`: 2 rows

**NACHAIATOriginatingDFIQualifier**
- `One`: 2 rows

**AccountType**
- `Cust`: 2 rows

**TaxGroup**
- `None`: 2 rows

**ExchangeRate**
- `100`: 2 rows

**ReportingCurrencyExchRate**
- `100`: 2 rows

**FinTagDisplayValue**
- `None`: 2 rows

**PaymentId**
- `None`: 2 rows

**PostingProfile**
- `GEN`: 2 rows

**CalculateWithholdingTax**
- `No`: 2 rows

**PostdatedCheckReasonForStop**
- `None`: 2 rows

**CreditAmount**
- `1000`: 2 rows

**OverrideSalesTax**
- `No`: 2 rows

**IsPrepayment**
- `No`: 2 rows

**NACHAIATForeignExchangeReference**
- `None`: 2 rows

**DefaultDimensionsForOffsetAccountDisplayValue**
- `None`: 2 rows

**ReportingCurrencyExchRateSecondary**
- `0`: 2 rows

**CurrencyCode**
- `USD`: 2 rows

**SecondaryExchangeRate**
- `0`: 2 rows

**PostdatedCheckReceivedDate**
- `1900-01-01 12:00:00+00:00`: 2 rows

**PostdatedCheckBankBranch**
- `None`: 2 rows

**CentralBankPurposeCode**
- `None`: 2 rows

**PostdatedCheckReplacementComments**
- `None`: 2 rows

**PostdatedCheckStopPayment**
- `No`: 2 rows

**ChineseVoucher**
- `None`: 2 rows

**PostdatedCheckBankName**
- `None`: 2 rows

**CentralBankPurposeText**
- `None`: 2 rows

**PaymentNotes**
- `None`: 2 rows

## Profile

Rows in the latest export: 2.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `dataAreaId` | STRING | 1 | 0 |  |  |
| `JournalBatchNumber` | STRING | 2 | 0 | 100-000227 | 100-000234 |
| `LineNumber` | INT | 1 | 0 | 1 | 1 |
| `UseSalesTaxDirectionFromMainAccount` | STRING | 1 | 0 | No | No |
| `MarkedInvoice` | STRING | 2 | 0 | 100-000002 | 100-000003 |
| `Voucher` | STRING | 2 | 0 | CPJ-000000001 | CPJ-000000002 |
| `DepositNumber` | STRING | 0 | 2 |  |  |
| `ItemWithholdingTaxGroup` | STRING | 0 | 2 |  |  |
| `OffsetAccountType` | STRING | 2 | 0 | Bank | Ledger |
| `PostdatedCheckCashierDisplayValue` | STRING | 0 | 2 |  |  |
| `PostdatedCheckMaturityDate` | TIMESTAMP | 1 | 0 | 1900-01-02 12:00:00 | 1900-01-02 12:00:00 |
| `SettleVoucher` | STRING | 1 | 0 | SelectedTransact | SelectedTransact |
| `TransactionDate` | TIMESTAMP | 2 | 0 | 2026-10-23 12:00:00 | 2026-10-26 12:00:00 |
| `NACHAIATOFACScreeningIndicator` | STRING | 1 | 0 | Zero | Zero |
| `BankTransactionType` | STRING | 0 | 2 |  |  |
| `PaymentReference` | STRING | 0 | 2 |  |  |
| `CustomerName` | STRING | 1 | 0 | MICROSOFT CORPORATION | MICROSOFT CORPORATION |
| `ChineseVoucherType` | STRING | 0 | 2 |  |  |
| `NACHAIATForeignExchangeIndicator` | STRING | 1 | 0 | None | None |
| `PostdatedCheckSalespersonDisplayValue` | STRING | 0 | 2 |  |  |
| `NACHAIATForeignExchangeReferenceIndicator` | STRING | 1 | 0 | One | One |
| `DebitAmount` | DECIMAL | 1 | 0 | 0 | 0 |
| `TaxItemGroup` | STRING | 0 | 2 |  |  |
| `NACHAIATOFACSecondaryScreeningIndicator` | STRING | 1 | 0 | Zero | Zero |
| `ThirdPartyBankAccountId` | STRING | 0 | 2 |  |  |
| `TransactionText` | STRING | 0 | 2 |  |  |
| `PostdatedCheckNumber` | STRING | 0 | 2 |  |  |
| `AccountDisplayValue` | STRING | 1 | 0 | 100\-000001 | 100\-000001 |
| `OffsetAccountDisplayValue` | STRING | 1 | 1 | Central | Central |
| `DefaultDimensionsForAccountDisplayValue` | STRING | 0 | 2 |  |  |
| `PostdatedCheckOriginalCheckNumber` | STRING | 0 | 2 |  |  |
| `PaymentMethodName` | STRING | 0 | 2 |  |  |
| `CentralBankImportDate` | TIMESTAMP | 1 | 0 | 1900-01-02 12:00:00 | 1900-01-02 12:00:00 |
| `NACHAIATReceivingDFIQualifier` | STRING | 1 | 0 | One | One |
| `OffsetTransactionText` | STRING | 0 | 2 |  |  |
| `MarkedInvoiceCompany` | STRING | 1 | 0 |  |  |
| `UseABankDepositSlip` | STRING | 1 | 0 | No | No |
| `PaymentSpecification` | STRING | 0 | 2 |  |  |
| `OffsetFinTagDisplayValue` | STRING | 0 | 2 |  |  |
| `PostdatedCheckIsReplacementCheck` | STRING | 1 | 0 | No | No |
| `NACHAIATOriginatingDFIQualifier` | STRING | 1 | 0 | One | One |
| `AccountType` | STRING | 1 | 0 | Cust | Cust |
| `TaxGroup` | STRING | 0 | 2 |  |  |
| `ExchangeRate` | DECIMAL | 1 | 0 | 100 | 100 |
| `ReportingCurrencyExchRate` | DECIMAL | 1 | 0 | 100 | 100 |
| `FinTagDisplayValue` | STRING | 0 | 2 |  |  |
| `PaymentId` | STRING | 0 | 2 |  |  |
| `PostingProfile` | STRING | 1 | 0 | GEN | GEN |
| `CalculateWithholdingTax` | STRING | 1 | 0 | No | No |
| `PostdatedCheckReasonForStop` | STRING | 0 | 2 |  |  |
| `CreditAmount` | DECIMAL | 1 | 0 | 1000 | 1000 |
| `OverrideSalesTax` | STRING | 1 | 0 | No | No |
| `OffsetCompany` | STRING | 1 | 0 |  |  |
| `IsPrepayment` | STRING | 1 | 0 | No | No |
| `NACHAIATForeignExchangeReference` | STRING | 0 | 2 |  |  |
| `DefaultDimensionsForOffsetAccountDisplayValue` | STRING | 0 | 2 |  |  |
| `ReportingCurrencyExchRateSecondary` | DECIMAL | 1 | 0 | 0 | 0 |
| `CurrencyCode` | STRING | 1 | 0 | USD | USD |
| `SecondaryExchangeRate` | DECIMAL | 1 | 0 | 0 | 0 |
| `PostdatedCheckReceivedDate` | TIMESTAMP | 1 | 0 | 1900-01-02 12:00:00 | 1900-01-02 12:00:00 |
| `Company` | STRING | 1 | 0 |  |  |
| `PostdatedCheckBankBranch` | STRING | 0 | 2 |  |  |
| `CentralBankPurposeCode` | STRING | 0 | 2 |  |  |
| `PostdatedCheckReplacementComments` | STRING | 0 | 2 |  |  |
| `PostdatedCheckStopPayment` | STRING | 1 | 0 | No | No |
| `ChineseVoucher` | STRING | 0 | 2 |  |  |
| `PostdatedCheckBankName` | STRING | 0 | 2 |  |  |
| `CentralBankPurposeText` | STRING | 0 | 2 |  |  |
| `PaymentNotes` | STRING | 0 | 2 |  |  |

## Sample rows

| JournalBatchNumber | LineNumber | UseSalesTaxDirectionFromMainAccount | MarkedInvoice | Voucher | DepositNumber | ItemWithholdingTaxGroup | OffsetAccountType | PostdatedCheckCashierDisplayValue | PostdatedCheckMaturityDate | SettleVoucher | TransactionDate | NACHAIATOFACScreeningIndicator | BankTransactionType | PaymentReference | CustomerName | ChineseVoucherType | NACHAIATForeignExchangeIndicator | PostdatedCheckSalespersonDisplayValue | NACHAIATForeignExchangeReferenceIndicator | DebitAmount | TaxItemGroup | NACHAIATOFACSecondaryScreeningIndicator | ThirdPartyBankAccountId | TransactionText | PostdatedCheckNumber | AccountDisplayValue | OffsetAccountDisplayValue | DefaultDimensionsForAccountDisplayValue | PostdatedCheckOriginalCheckNumber | PaymentMethodName | CentralBankImportDate | NACHAIATReceivingDFIQualifier | OffsetTransactionText | UseABankDepositSlip | PaymentSpecification | OffsetFinTagDisplayValue | PostdatedCheckIsReplacementCheck | NACHAIATOriginatingDFIQualifier | AccountType | TaxGroup | ExchangeRate | ReportingCurrencyExchRate | FinTagDisplayValue | PaymentId | PostingProfile | CalculateWithholdingTax | PostdatedCheckReasonForStop | CreditAmount | OverrideSalesTax | IsPrepayment | NACHAIATForeignExchangeReference | DefaultDimensionsForOffsetAccountDisplayValue | ReportingCurrencyExchRateSecondary | CurrencyCode | SecondaryExchangeRate | PostdatedCheckReceivedDate | PostdatedCheckBankBranch | CentralBankPurposeCode | PostdatedCheckReplacementComments | PostdatedCheckStopPayment | ChineseVoucher | PostdatedCheckBankName | CentralBankPurposeText | PaymentNotes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100-000227 | 1 | No | 100-000002 | CPJ-000000001 | NULL | NULL | Bank | NULL | 1900-01-02 12:00:00 | SelectedTransact | 2026-10-23 12:00:00 | Zero | NULL | NULL | MICROSOFT CORPORATION | NULL | None | NULL | One | 0 | NULL | Zero | NULL | NULL | NULL | 100\-000001 | Central | NULL | NULL | NULL | 1900-01-02 12:00:00 | One | NULL | No | NULL | NULL | No | One | Cust | NULL | 100 | 100 | NULL | NULL | GEN | No | NULL | 1000 | No | No | NULL | NULL | 0 | USD | 0 | 1900-01-02 12:00:00 | NULL | NULL | NULL | No | NULL | NULL | NULL | NULL |
| 100-000234 | 1 | No | 100-000003 | CPJ-000000002 | NULL | NULL | Ledger | NULL | 1900-01-02 12:00:00 | SelectedTransact | 2026-10-26 12:00:00 | Zero | NULL | NULL | MICROSOFT CORPORATION | NULL | None | NULL | One | 0 | NULL | Zero | NULL | NULL | NULL | 100\-000001 | NULL | NULL | NULL | NULL | 1900-01-02 12:00:00 | One | NULL | No | NULL | NULL | No | One | Cust | NULL | 100 | 100 | NULL | NULL | GEN | No | NULL | 1000 | No | No | NULL | NULL | 0 | USD | 0 | 1900-01-02 12:00:00 | NULL | NULL | NULL | No | NULL | NULL | NULL | NULL |
