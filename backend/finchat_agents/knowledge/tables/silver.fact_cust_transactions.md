---
name: fact_cust_transactions
schema: silver
layer: silver
domain: ar
type: table
status: broken
purpose: Customer transactions (invoices; payments) with amounts.
grain: one row per customer transaction (key unknown)
primary_key: []
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: table has no statistics (empty or not profiled)
proposed_fields: []
reviewed: false
broken_error: the profiling query failed in the catalog export (no row count); the error text is not in the workbook
---

# fact_cust_transactions

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `odata_etag` | string |  |  | `odata_etag` |
| `AccountNum` | string |  |  | `AccountNum` |
| `AmountCur` | decimal |  |  | `AmountCur` |
| `AmountMST` | decimal |  |  | `AmountMST` |
| `Approved` | string |  |  | `Approved` |
| `BankCentralBankPurposeCode` | string |  |  | `BankCentralBankPurposeCode` |
| `BankCentralBankPurposeText` | string |  |  | `BankCentralBankPurposeText` |
| `BankRemittanceFileId` | string |  |  | `BankRemittanceFileId` |
| `BillOfExchangeID` | string |  |  | `BillOfExchangeID` |
| `BillOfExchangeSeqNum` | long |  |  | `BillOfExchangeSeqNum` |
| `BillOfExchangeStatus` | string |  |  | `BillOfExchangeStatus` |
| `CancelledPayment` | string |  |  | `CancelledPayment` |
| `CashDiscBaseDate` | timestamp |  |  | `CashDiscBaseDate` |
| `CashDiscCode` | string |  |  | `CashDiscCode` |
| `CashPayment` | string |  |  | `CashPayment` |
| `Closed` | timestamp |  |  | `Closed` |
| `CollectionLetter` | string |  |  | `CollectionLetter` |
| `CollectionLetterCode` | string |  |  | `CollectionLetterCode` |
| `CompanyBankAccountId` | string |  |  | `CompanyBankAccountId` |
| `ControlNum` | string |  |  | `ControlNum` |
| `Correct` | string |  |  | `Correct` |
| `CurrencyCode` | string |  |  | `CurrencyCode` |
| `CustAutomationExclude` | string |  |  | `CustAutomationExclude` |
| `CustAutomationPredictionSent` | string |  |  | `CustAutomationPredictionSent` |
| `CustAutomationPredunningSent` | string |  |  | `CustAutomationPredunningSent` |
| `CustExchAdjustmentRealized` | decimal |  |  | `CustExchAdjustmentRealized` |
| `CustExchAdjustmentUnrealized` | decimal |  |  | `CustExchAdjustmentUnrealized` |
| `DeliveryMode` | string |  |  | `DeliveryMode` |
| `DocumentDate` | timestamp |  |  | `DocumentDate` |
| `DocumentNum` | string |  |  | `DocumentNum` |
| `DueDate` | timestamp |  |  | `DueDate` |
| `EUROTriangulation` | string |  |  | `EUROTriangulation` |
| `ExchAdjustment` | decimal |  |  | `ExchAdjustment` |
| `ExchAdjustmentReporting` | decimal |  |  | `ExchAdjustmentReporting` |
| `ExchRate` | decimal |  |  | `ExchRate` |
| `ExchRateSecond` | decimal |  |  | `ExchRateSecond` |
| `FixedExchRate` | string |  |  | `FixedExchRate` |
| `Interest` | string |  |  | `Interest` |
| `Invoice` | string |  |  | `Invoice` |
| `InvoiceProject` | string |  |  | `InvoiceProject` |
| `LastExchAdj` | timestamp |  |  | `LastExchAdj` |
| `LastExchAdjRate` | decimal |  |  | `LastExchAdjRate` |
| `LastExchAdjRateReporting` | decimal |  |  | `LastExchAdjRateReporting` |
| `LastExchAdjVoucher` | string |  |  | `LastExchAdjVoucher` |
| `LastSettleAccountNum` | string |  |  | `LastSettleAccountNum` |
| `LastSettleCompany` | string |  |  | `LastSettleCompany` |
| `LastSettleDate` | timestamp |  |  | `LastSettleDate` |
| `LastSettleVoucher` | string |  |  | `LastSettleVoucher` |
| `MCRPaymOrderID` | string |  |  | `MCRPaymOrderID` |
| `OrderAccount` | string |  |  | `OrderAccount` |
| `PackedExtensions` | string |  |  | `PackedExtensions` |
| `PaymId` | string |  |  | `PaymId` |
| `PaymMethod` | string |  |  | `PaymMethod` |
| `PaymMode` | string |  |  | `PaymMode` |
| `PaymReference` | string |  |  | `PaymReference` |
| `PaymSchedId` | string |  |  | `PaymSchedId` |
| `PaymSpec` | string |  |  | `PaymSpec` |
| `PaymTermId` | string |  |  | `PaymTermId` |
| `PostingProfile` | string |  |  | `PostingProfile` |
| `PostingProfileClose` | string |  |  | `PostingProfileClose` |
| `Prepayment` | string |  |  | `Prepayment` |
| `ReportingCurrencyAmount` | decimal |  |  | `ReportingCurrencyAmount` |
| `ReportingCurrencyCrossRate` | decimal |  |  | `ReportingCurrencyCrossRate` |
| `ReportingCurrencyExchRate` | decimal |  |  | `ReportingCurrencyExchRate` |
| `ReportingCurrencyExchRateSecondary` | decimal |  |  | `ReportingCurrencyExchRateSecondary` |
| `ReportingExchAdjustmentRealized` | decimal |  |  | `ReportingExchAdjustmentRealized` |
| `ReportingExchAdjustmentUnrealized` | decimal |  |  | `ReportingExchAdjustmentUnrealized` |
| `RetailCustTrans` | string |  |  | `RetailCustTrans` |
| `RetailStoreId` | string |  |  | `RetailStoreId` |
| `RetailTerminalId` | string |  |  | `RetailTerminalId` |
| `RetailTransactionId` | string |  |  | `RetailTransactionId` |
| `SettleAmountCur` | decimal |  |  | `SettleAmountCur` |
| `SettleAmountMST` | decimal |  |  | `SettleAmountMST` |
| `SettleAmountReporting` | decimal |  |  | `SettleAmountReporting` |
| `SettleAmount_MX` | decimal |  |  | `SettleAmount_MX` |
| `Settlement` | string |  |  | `Settlement` |
| `SysDataAreaId` | string |  |  | `SysDataAreaId` |
| `SysRecId` | long |  |  | `SysRecId` |
| `TaxInvoiceSalesId` | string |  |  | `TaxInvoiceSalesId` |
| `ThirdPartyBankAccountId` | string |  |  | `ThirdPartyBankAccountId` |
| `TransDate` | timestamp |  |  | `TransDate` |
| `TransType` | string |  |  | `TransType` |
| `Txt` | string |  |  | `Txt` |
| `Voucher` | string |  |  | `Voucher` |
| `dataAreaId` | string |  |  | `dataAreaId` |
