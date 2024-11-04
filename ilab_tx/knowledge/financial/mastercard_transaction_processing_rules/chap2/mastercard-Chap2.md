# Authorization and Clearing Requirements

# 2.1 Acquirer Authorization Requirements

An Acquirer and each of its Merchants must support POS Transactions (authorized online by the Issuer or offline by the chip), and a full reversal when performed to cancel a POS Transaction that the Acquirer cannot complete due to a technical problem.

The Acquirer of a Merchant that accepts Maestro® Cards must support Maestro POS Transactions that either automatically access the primary account or allow the Cardholder to choose to access the checking account or savings account ("account selection").

Effective 12 April 2024, an Acquirer must support the online authorization of Mastercard®, Debit Mastercard®, and Maestro refund Transactions acquired on the Dual Message System and enable refund Transaction authorization service for a Merchant upon request. The Acquirer must pass the Issuer's refund Transaction authorization response to the Merchant.

An Acquirer may also support, and its Merchants may optionally offer, the following Transaction/Payment Transaction and message types. An Acquirer that supports and any of its Merchants that offer an optional Transaction and/or Payment Transaction or message type must comply with the Rules applicable to the optional Transaction and/or Payment Transaction or message type that is supported or offered.

- Purchase with cash back Transactions (Debit Mastercard and Maestro only, unless otherwise specified for a country or Region)
- Merchant-approved Maestro POS Transactions
- Payment Transactions
- Maestro POS Transaction preauthorization and completion (single message processing)
- Account Status Inquiry (ASI) requests
- Partial approval
- Balance response (prepaid only)
- Full reversal, including cancellation, and partial reversal (Merchant-initiated at the POS Terminal)
- POS balance inquiry (Debit Mastercard and Maestro only)
- Maestro refund Transactions and/or corrections acquired on the Single Message System
- Offline chip processing of refund Transactions

# Government Controlled Merchants

Each Authorization Request/0100 and Authorization Advice/0120 message for a Transaction conducted by a Government Controlled Merchant must include the Merchant Country of Origin for that Government Controlled Merchant as defined in Appendix C, whether such country is the same as or different from the country in which the Merchant is located or the Transaction occurs.

# Offline Chip Processing

If a Transaction that may be processed offline in accordance with the Terminal offline chip authorization limit cannot be processed offline for any reason, the Transaction must be


# Authorization and Clearing Requirements

# 2.1.1 Acquirer Host System Requirements

processed online; if the Transaction cannot be processed online, then the Transaction must be declined. A Mastercard Single Message System Acquirer may clear offline Chip Transaction by transmitting the required Transaction data in an online Financial Advice/0220 message or as part of a batch notification.

# Account Status Inquiry (ASI) Requests

An ASI request is an Authorization Request/0100 or Financial Transaction Request/0200 message initiated by an Acquirer or Merchant to obtain the Issuer's validation that a Cardholder's Account is open and active.

An ASI request is identified with a value of 8 (Account Status Inquiry Service [ASI]) in DE 61 (Point-of-Service [POS] Data), subfield 7 (POS Transaction Status), and when submitted in connection with a purchase, contains a value of 00 (Purchase) in DE 3 (Processing Code), subfield 1 (Cardholder Transaction Type Code). A Purchase ASI request must have a Transaction amount of zero.

Unless specifically permitted in the Standards, a purchase Transaction authorization request must not contain a Transaction amount value of one major unit of currency or any other nominal test amount that does not represent an actual purchase.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," "Europe Region," "Middle East/Africa Region," and "United States Region" sections at the end of this chapter.

# Echoing of Transaction Link ID

Effective 17 October 2025, an Acquirer must populate DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID]) of each incremental Authorization/0100, Authorization Advice/0120, Financial Transaction Request/0200, Financial Transaction Advice/0220, Reversal Request/0400, and Acquirer Reversal Advice/0420 message with the value in the TLID field received in the corresponding Authorization Request Response/0110, Financial Transaction Request Response/0210, or other original message response for the same Transaction.

# 2.2 Issuer Authorization Requirements

The Issuer of a debit Card Program or of a credit Card Program that provides cash access at ATM Terminals and Bank Branch Terminals:

1. Must support POS Transaction authorizations and preauthorizations from a debit Cardholder’s primary account, checking account, and savings account.


# Authorization and Clearing Requirements

# 2.2 Issuer Authorization Requirements

1. Must offer cash withdrawal and Merchandise Transactions from no account specified to debit Cardholders and cash advances to credit Cardholders.
2. May offer, at its option, balance inquiry to checking, savings, and credit card accounts; and transfers to and from checking and savings accounts.

# Offline Chip Processing

A Chip Card Issuer that elects to process offline Chip Transactions must support offline purchase and refund Transactions. If an offline Transaction type is not offered to a Cardholder, the chip must send the Transaction online for authorization or decline the Transaction offline. An Issuer must accept a Chip Transaction cleared online by an Acquirer following an offline authorization.

# Online Authorization of Refund Transactions

An Issuer must support the online authorization of refund Transactions for all Mastercard and Debit Mastercard Account ranges, with the exception of non-reloadable prepaid Account ranges. If not supported, the Issuer must provide a value of 57 indicating “transaction not permitted to issuer/cardholder” in DE 39 (Response Code) of the online authorization message.

# Chip Technical Fallback

An Issuer must decline authorization of a Transaction conducted in the Canada, Europe, Latin America and the Caribbean, or Middle East/Africa Region when technical fallback from chip to magnetic stripe occurred.

# Account Status Inquiry (ASI) Requests

An ASI request is an Authorization Request/0100 or Financial Transaction Request/0200 message initiated by an Acquirer or Merchant to obtain the Issuer's validation that a Cardholder's Account is open and active. An ASI request is identified with the values of 8 (Account Status Inquiry Service [ASI]) in DE 61 (Point-of-Service [POS] Data), subfield 7 (POS Transaction Status and 00 (Purchase) in DE 3 (Processing Code), subfield 1 (Cardholder Transaction Type Code) and has a Transaction amount of zero.

An Issuer that receives an ASI request must provide a valid and accurate value in DE 39 (Response Code) of the Authorization Request Response/0110 or Financial Transaction Request Response/0210 message. If a Mastercard or Debit Mastercard Account is open and active, the Issuer must provide a value of 00 (Approved) or 85 (Not Declined) in DE 39.

Mastercard will deem an Issuer to be noncompliant with this requirement if the Issuer declines an ASI request involving a Mastercard or Debit Mastercard Account and within 24 hours of such decline, approves a Transaction authorization request for a non-zero Transaction amount involving the same Merchant or Sponsored Merchant and the same Account. A noncompliant Issuer may be subject to fees under the global ASI Transaction Processing Excellence program.

NOTE: Modifications to this Rule appear in the “Asia/Pacific Region,” “Canada Region,” “Europe Region,” and “United States Region” sections at the end of this chapter.



42
# Authorization and Clearing Requirements

# 2.2.1 Issuer Host System Requirements

An Issuer's host system interfaces must support the online processing of:

- POS Transactions
- Purchase with cash back Transactions for Debit Mastercard (including prepaid) and Maestro (including prepaid) Account ranges, effective 1 July 2022
- Refund Transactions (for both Mastercard Dual Message System and Single Message System processing)
- Partial approval requests
- Balance response
- Reversal and correction requests
- POS balance inquiries (if required in a country or Region)
- Cash withdrawals and the purchase of Merchandise with no account specified at ATM Terminals and Bank Branch Terminals; and
- Payment Transactions

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," "Latin America and the Caribbean Region," and "United States Region" sections at the end of this chapter.

# 2.2.2 Stand-In Processing Service

An Issuer is liable for all Transactions authorized (with or without PIN validation) using the Stand-In Processing Service. The Issuer may establish Stand-In Processing Service PIN validation at its option.

For all of its Mastercard Card Programs, an Issuer must use the Stand-In Processing Service. Stand-In Parameters for Mastercard (including Debit Mastercard) Card Programs must be set at or above the Corporation’s default limits.

For all of its Maestro and Cirrus Card Programs, an Issuer must use the Stand-In Processing Service. This requirement does not apply if the Issuer commenced its use of an alternative on-behalf authorization service before 1 December 2003 and such service meets the Corporation’s performance standards as set forth in Rule 2.4.2. Stand-In Parameters for Maestro and Cirrus Card Programs must be set at or above the Corporation’s default limits.

In the event that fraudulent activity is detected with respect to a Mastercard BIN or BIN range, the Corporation, in its sole discretion and judgment, may take such action as the Corporation deems necessary or appropriate to safeguard the goodwill and reputation of the Corporation’s Marks. Such action may include, by way of example and not limitation, declining some or all Transaction authorization requests received by the Stand-in Processing Service relating to the use of Cards issued under such Mastercard BIN or BIN range.

An Issuer may employ a blocking service which declines all Transaction authorization requests during Stand-In processing for inactive BINs or in situations where Stand-In processing does not apply for regulatory reasons.

An Issuer’s use of the Stand-In Processing Service must include the following services:
# Authorization and Clearing Requirements

# Accumulative Transaction Limits

• Card Validation Code 1 (CVC 1) Verification in Stand-In must be used for all Cards bearing a magnetic stripe;

• Dynamic CVC 3 Validation in Stand-In must be used for all contactless-enabled Cards and Access Devices that support Magnetic Stripe Mode Contactless Transactions; and

• Dynamic AAV Verification in Stand-In must be used for all Mastercard Accounts and all e-commerce-enabled Maestro Accounts that are enrolled in Mastercard Identity Check, unless the Mastercard Identity Check AAV Verification Service is used.

NOTE: Modifications to this Rule appear in the "Europe Region," "United States Region," and "Additional U.S. Region and U.S. Territory Rules" sections at the end of this chapter.

# Accumulative Transaction Limits

An Issuer at its option, may use daily Stand-In Processing Service Transaction limits (“accumulative limits”) for a Card Program that are higher than the applicable default limits set by the Corporation. Refer to the Stand-In Processing—Accumulative Global Parameters (Form 041f) for the minimum (default) daily accumulative Transaction processing limit applicable to a particular Card Program.

# Chip Cryptogram Validation in Stand-In

An Issuer must use Chip Cryptogram Validation in Stand-In Processing for all of its Chip Card Programs.

# ATM Transaction Requirements for Mastercard Credit Card Issuers

A Mastercard credit Card Issuer must maintain a 70 percent minimum ATM Transaction approval rate and manage individual denial category rates in compliance with the following Standards.

|Category|Maximum Denial Rate|Reason Codes|
|---|---|---|
|Invalid PIN|13%|55|
|Insufficient Funds|10%|51|
|Invalid Transactions|14%|57|
|Exceed Limit|9%|61|
|Restricted Card|4%|62|

The Issuer determines the maximum cash withdrawal limits applicable to its Cardholders; however, the Issuer must permit its Mastercard credit Cardholders to withdraw at least the equivalent of USD 200 daily if the available credit exists, and there is no other reason to deny the transactions.


# Authorization and Clearing Requirements

# 2.3 Authorization Responses

To accommodate ATM Access Fees and currency conversions, the Issuer must authorize Transactions up to the equivalent of USD 10 or 10 percent, whichever is greater, more than the daily Transaction amount limit communicated to the Cardholder.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# 2.3 Authorization Responses

An Acquirer must comply with the authorization response wait time requirements set forth in “Maximum Response Times” in Chapter 2 of the Single Message System Specifications and in “Minimum Authorization Response Wait Time” in Chapter 4 of the Authorization Manual, as applicable.

An Issuer must comply with the authorization response requirements set forth in “Maximum Response Times” in Chapter 2 of the Single Message System Specifications manual and in “Routing Timer Values” in Chapter 5 of the Authorization Manual, as applicable. If the Issuer’s response is not received within the required time frame, then the Transaction will time out and be forwarded via Stand-In Processing System or another alternate authorization provider as specified by the Issuer.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# 2.4 Performance Standards

An Issuer or Acquirer that fails to meet the Corporation's authorization performance standards may be subject to the following noncompliance assessments.

|Occurrence|Penalty|
|---|---|
|First occurrence|USD 15,000|
|Second occurrence within the 12-month period following the first occurrence|USD 15,000|
|Third and any subsequent occurrence within the 12-month period following the second occurrence|USD 20,000|

After completion of a full calendar year without any violations, a subsequent violation is counted as a first violation.

# 2.4.1 Performance Standards—Acquirer Requirements

For Maestro POS Transactions and ATM Transactions, an Acquirer authorization failure rate that exceeds two percent for two consecutive months is deemed to be substandard authorization performance. The Acquirer authorization failure rate is based on Transactions.


# Authorization and Clearing Requirements

# 2.4.2 Performance Standards—Issuer Requirements

Processed through each Acquirer connection to the Interchange System and is calculated by taking the total number of Transactions declined due to invalid amount or format error divided by the total number of Transactions. The Acquirer failure rate is not applied until after the fourth calendar month of operation or upon processing 5,000 Maestro POS Transactions and/or and ATM Transactions in a calendar month, whichever occurs first.

# Issuer Failure Rate (Substandard Level 1)

For Maestro POS Transactions and ATM Transactions, an Issuer authorization failure rate that exceeds two percent for two consecutive months is deemed to be substandard level 1 performance. The Issuer failure rate is not applied until after the fourth calendar month of operation or upon processing 5,000 Maestro POS Transactions and/or ATM Transactions in a calendar month, whichever occurs first.

# Issuer Failure Rate (Substandard Level 2)

For Maestro POS Transactions and ATM Transactions, an Issuer authorization failure rate that exceeds three percent for two consecutive months is deemed to be substandard level 2 performance. The Issuer failure rate is not applied until after the fourth calendar month of operation or upon processing 5,000 Maestro POS Transactions and/or ATM Transactions in a calendar month, whichever occurs first.

# Calculation of the Issuer Failure Rate

The Issuer authorization failure rate for Maestro POS Transactions and ATM Transactions is calculated by taking the total number of Transactions declined due to Issuer unavailability, malfunction, or timeout divided by the total number of Transactions.

NOTE: Modifications to this Rule appear in the “Europe Region” and "United States Region" sections at the end of this chapter.

# 2.5 Preauthorizations

A Processed Transaction authorization request is properly identified as a preauthorization when DE 61 (Point-of-Service [POS] Data), subfield 7 (POS Transaction Status) contains a value of 4.

NOTE: Additions to this Rule appear in the "Asia/Pacific Region" and “Europe Region” sections at the end of this chapter.

# 2.5.1 Preauthorizations - Mastercard POS Transactions

An Acquirer is advised to identify a Mastercard POS Transaction authorization request as a preauthorization if:

1. Authorization is requested for an estimated amount that is greater than zero; or


# Authorization and Clearing Requirements

# 2.5.2 Preauthorizations - Maestro POS Transactions

2. The Transaction might not be completed for reasons other than technical failure or lack of full Issuer approval; for example:

- a. When the Cardholder will be offered the choice at a later time to complete the Transaction with another payment means (such as when checking out of a hotel or returning a rental car);
- b. When the products ordered by the Cardholder might be later found to be out of stock;
- c. If the mobile phone number for which the Cardholder has requested a top-up is later found not to exist.

The risk of technical failures, such as telecommunications failure or Terminal failure, should not be taken into account when determining whether preauthorization coding is appropriate. All clearing messages corresponding to a preauthorization must be presented within 30 calendar days of the authorization approval date.

NOTE: An addition to this Rule appears in the "Asia/Pacific Region" section at the end of this chapter.

# 2.5.2 Preauthorizations - Maestro POS Transactions

A Maestro POS Transaction preauthorization is performed to obtain the Issuer's approval of an estimated or Cardholder-requested Transaction amount, prior to submission of a request for authorization of the final amount.

1. The Acquirer must ensure that preauthorizations (in the physical environment) are initiated using a Card reader, and Cardholder verification method (including "No CVM" for Contactless Transactions not exceeding the CVM limit).
2. The Issuer must accept all preauthorization completions provided the actual amount of the completion is less than or equal to the amount approved in the preauthorization. A preauthorization completion is generated from the original preauthorization response and without use of the Card reader or a CVM.
3. If the Issuer does not receive a preauthorization completion within 20 minutes of the preauthorization, the preauthorization approval is void, except as provided for in Rule 4.14 Merchant-approved Maestro POS Transactions or in Rule 2.10.2 Maestro Transactions.
4. The Acquirer is not responsible for preauthorization completions that occurred within two hours of the initial Transaction that were stored and forwarded because of technical problems between the Acquirer and the Interchange System, or the Interchange System and the Issuer.

NOTE: Modifications to this Rule appear in the "Europe Region," "Latin America and the Caribbean Region," "United States Region," and "Additional U.S. Region and U.S. Territory Rules" sections at the end of this chapter.

# 2.5.3 Preauthorizations - ATM and Manual Cash Disbursement Transactions

NOTE: A Rule on this subject appears in the "Europe Region" section at the end of this chapter.


# Authorization and Clearing Requirements

# 2.6 Undefined Authorizations

NOTE: This Rule does not apply for China domestic Transactions or in the Asia/Pacific, Europe, or Middle East/Africa Regions.

A Processed Transaction authorization request is identified as undefined when DE 61 (Point–of–Service [POS] Data), subfield 7 (POS Transaction status) contains a value of 0 and DE 48, subelement 61 (POS Data Extended Condition Codes), subfield 5 (Final Authorization Indicator) contains a value of 0 or is not present.

A Mastercard POS Transaction authorization request may be identified as undefined if:

1. Authorization is requested for an amount greater than zero; and
2. The final Transaction amount may differ from the authorized amount; and
3. The Transaction is not expected to be cancelled after the authorization request is approved in full by the Issuer (excluding non–completion for technical reasons such as telecommunications failure or Terminal failure).

All clearing messages corresponding to an undefined authorization must be presented within seven calendar days of the authorization approval date.

If an Acquirer submits at least 100,000 Domestic Transaction authorization requests per month to the Interchange System, then the number of undefined Domestic Transaction authorization requests submitted by the Acquirer in any one month must not exceed 20 percent of its total Domestic Transaction authorization requests submitted in the same month.

# 2.7 Final Authorizations

A Processed Transaction authorization request is properly identified as a final authorization when DE 61 (Point-of-Service [POS] Data), subfield 7 (POS Transaction Status) contains a value of 0 and DE 48 (Additional Data), subelement 61 (POS Data Extended Condition Codes), subfield 5 contains a value of 1.

When an Acquirer or Merchant uses the final authorization, then in a dual message environment:

1. Any Transaction corresponding to an authorization identified as a final authorization must be presented for clearing within seven calendar days of the authorization approval date; and
2. The presented Transaction amount must equal the authorized amount.

An Acquirer is advised to identify a Mastercard POS Transaction authorization request as a final authorization if:

1. Authorization is requested for the final Transaction amount; and
2. The Transaction is not expected to be cancelled after the authorization request is approved in full by the Issuer, except upon Cardholder request or when non-completion is unavoidable for technical reasons such as telecommunications failure or POS Terminal failure.


# Authorization and Clearing Requirements

# 2.8 Message Reason Code 4808 Chargeback Protection Period

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," "Europe Region," and "Middle East/Africa Region" sections at the end of this chapter.

# 2.8 Message Reason Code 4808 Chargeback Protection Period

A message reason code 4808 (Authorization–related Chargeback) chargeback protection period applies to each Mastercard POS Transaction as follows.

|Each Mastercard POS Transaction identified as a...|Has a message reason code 4808 chargeback protection period of...|
|---|---|
|Preauthorization|30 calendar days from the authorization approval date|
|Undefined authorization|Seven calendar days from the authorization approval date|
|Final authorization|Seven calendar days from the authorization approval date for purchase and purchase with cash back Transactions and effective 12 April 2024, five calendar days from the authorization approval date for refund Transactions|

The Issuer must release any hold placed on the Cardholder’s Account after the expiration of the message reason code 4808 chargeback protection period for a particular Transaction, at the latest. The total authorized amount of a Transaction does not include any amount for which the message reason code 4808 chargeback protection period has expired. The approved amount of any authorization with an expired message reason code 4808 chargeback protection period is deemed to be zero. No fraud–related or other chargeback rights or Transaction processing requirements are affected by the message reason code 4808 chargeback protection period, unless otherwise indicated.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region" and "Europe Region" sections at the end of this chapter.

# 2.9 Multiple Authorizations

NOTE: This Rule does not apply for China Domestic Transactions.

3 The message reason code 4808 chargeback protection for a properly identified preauthorization of an Acquirer–financed or Merchant–financed installment billing payment arrangement is not limited in time. Refer to Chapter 4 for Contactless Transit Aggregated Transaction processing procedures.



49
# Authorization and Clearing Requirements

# 2.9 Multiple Authorizations

To extend the duration of the message reason code 4808 chargeback protection period afforded by an approved preauthorization of a Transaction, a Merchant may later submit an additional preauthorization request for the same Transaction.

The following requirements apply to Mastercard POS Transactions that are Processed Transactions when multiple authorizations are processed for a single Transaction:

1. The Acquirer must use a unique identifier from the initial approved authorization of a Transaction in any additional authorizations requested in connection with the same Transaction, by populating:
1. DE 48, subelement 63 (Trace ID) of each additional authorization request with the DE 63 (Network Data), subfield 1 (Financial Network Code) and subfield 2 (Banknet Reference Number) and DE 15 (Date, Settlement) data from the initial approved Authorization Request Response/0110 message; and
2. Effective 17 October 2025, DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID]) of each additional authorization request with the same value populated in this field in the initial approved Authorization Request Response/0110 message.

These unique identifiers must also be included in the Transaction clearing record.
2. Upon receipt of the Transaction clearing record, the Issuer must use the unique identifier to match the original and any additional approved authorizations to the Transaction.
3. Upon matching all authorizations to the clearing record, the Issuer must release any hold placed on the Cardholder's account in connection with the original and any additional approved authorizations that is in excess of the Transaction amount.

The use of multiple authorizations for the aggregation of separate Cardholder-initiated purchases into a single Transaction must only occur as set forth in Rule 5.10, "Mastercard Micropayment Solution - United States Region Only."

If the additional preauthorization request is for a zero amount, it extends the duration of the message reason code 4808 chargeback protection period with no change in the total authorized Transaction amount. If the preauthorization request is for an amount higher than zero, it both extends the duration of the message reason code 4808 chargeback protection period and incrementally increases, by the amount of the new preauthorization request, the total authorized Transaction amount. If the message reason code 4808 chargeback protection period has already expired, the new preauthorization request must be for the full Transaction amount rather than an incremental amount.

This option is not available to a Single Message System Acquirer.

NOTE: An addition to this Rule appears in the "Europe Region," "Latin America and the Caribbean Region," and "Additional U.S. Region and U.S. Territory Rules" sections at the end of this chapter.


# Authorization and Clearing Requirements

# 2.10 Multiple Clearing or Completion Messages

# 2.10.1 Mastercard and Debit Mastercard Transactions

A Mastercard Dual Message System Acquirer has the option of linking multiple presentments with partial amounts to one approved authorization identified as either a preauthorization or final authorization. The following requirements apply to Mastercard and Debit Mastercard Transactions acquired in the Mastercard Dual Message System:

1. In the First Presentment/1240 message, the Acquirer may populate DE 25 (Message Reason Code) with either of the following values:
1. 1403 (Previously approved authorization - partial amount, multi-clearing); or
2. 1404 (Previously approved authorization - partial amount, final clearing). This value indicates that the original authorization is closed; no subsequent clearing messages may be submitted. If the final first presentment message submitted for a preauthorized Transaction contains a value of 1403 in DE 25, and the total authorized amount has not been fully cleared, then the Acquirer or Merchant must initiate an authorization reversal so that the Issuer may release any excess hold on funds in the Cardholder's Account.
2. Effective 17 October 2025, the Acquirer must populate DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID]) of each First Presentment/1240 message with the same TLID value received in the original Authorization Request Response/0110 message or other original message response.
3. Upon receipt of a clearing message containing a value of 1403 or 1404, the Issuer must match the clearing message to the authorization message by comparing the data contained in the following fields:
1. DE 63 (Transaction Life Cycle ID), subfield 2 (Trace ID) of the First Presentment/1240 message;
2. DE 63 (Network Data), subfield 2 (Banknet Reference Number) and DE 15 (Date, Settlement) of the Authorization Request/0100 message; and
3. Effective 17 October 2025, DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID]) of each lifecycle message for the same Transaction.

NOTE: A Debit Mastercard Issuer may receive the value of 1403 or 1404 in DE 60 (Advice Reason Code), subfield 2 (Advice Reason Detail Code) of a Mastercard Single Message System-generated Financial Transaction Advice/0220 message.
4. Upon matching a clearing message to an authorization message, the Issuer must adjust any hold on the availability of funds in the Cardholder's Account in accordance with its standard Account management practice for cleared amounts:


# Authorization and Clearing Requirements

# 2.10.2 Maestro Transactions

|If the clearing message contains a value of...|Then the Issuer is advised to...|
|---|---|
|1403|Release the hold placed on the Cardholder's Account in connection with the approved authorization by the amount in DE 6 (Amount, Cardholder Billing).|
|1404|Release any unused funds in connection with the approved authorization.|

All multi-clearing messages must be presented within the applicable clearing time frame, in order to avoid an Authorization-related or Late Presentment chargeback. Refer to Rule 2.8 regarding Authorization-related chargeback time frames and Rule 3.15.1 regarding Late Presentment chargeback time frames.

# 2.11 Full and Partial Reversals

An authorization reversal message is used to reduce the original approved Transaction amount. A full reversal (where DE 95 [Replacement Amounts], when present, contains a value of zero) cancels the original authorization request. A partial reversal has a DE 95 value that is less than the original approved Transaction amount, including in the case of a partial approval. For example, if a USD 100 authorization request is partially approved for USD 75, then the DE 95 value in a subsequent reversal must not exceed USD 75.

NOTE: Modifications to this Rule appear in the "Europe Region" section at the end of this chapter.

# 2.11.1 Full and Partial Reversals - Acquirer Requirements

# POS Transactions

An Acquirer must support reversals (automatic or otherwise) for the full amount of the original Transaction authorization request whenever the Acquirer host system is unable to communicate an authorization response to the POS Terminal.

An Acquirer must ensure that each Reversal Request/0400 or Acquirer Reversal Advice/0420 message submitted that originates from a Merchant corresponds to an original authorization request message. Effective 17 October 2025, the Acquirer must populate DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID]) of each Reversal Request/0400 and Acquirer Reversal Advice/0420 message with the same TLID value.


# Authorization and Clearing Requirements

# 2.11.2 Full and Partial Reversals - Issuer Requirements

received in the original Authorization Request Response/0110 or other original message response.

The Acquirer must ensure that a Merchant submits a Reversal Request/0400 message to the Issuer within 24 hours of:

- The cancellation of a previously authorized Transaction (for example, the sale was voided or the Merchant accepted another form of payment); or
- The finalization of a Transaction with a lower amount than previously approved.

The reversal may be a full or partial reversal, as appropriate. In the case of finalization of a Transaction with a lower amount, a partial reversal is not required if the First Presentment/1240 message is submitted within 24 hours of finalization of the Transaction.

The reversal requirement does not apply to automated fuel dispenser (MCC 5542) Transactions or to Contactless transit aggregated or transit debt recovery Transactions.

Notwithstanding the above reversal requirement, the Acquirer must ensure that if a Merchant cancels a Transaction or finalizes a Transaction for a lower amount than previously approved, no reversal is submitted if such event occurs:

- More than 30 calendar days after the authorization date for a preauthorization; or
- More than seven calendar days after the authorization date for any other authorization message.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," "Europe Region," and "United States Region" sections at the end of this chapter.

# Refund Transactions

A refund Transaction authorized on the Dual Message System that is not reversed by means of an Authorization Reversal Request/0400 message must be submitted for clearing within five (5) days.

A clearing reversal or Single Message System adjustment of a refund Transaction must only be submitted to correct a documented clerical error and upon agreement of the Issuer. In such an event, the error must be reversed or adjusted no later than one calendar day after submission of the Financial Transaction/0200 or First Presentment/1240 message for the refund Transaction.

Reversible clerical errors include, by way of example and not limitation, the erroneous capture of Transaction data, a duplicate Transaction, or an error caused by the transposition of data.

# ATM Transactions

An Acquirer must not automatically generate a full or partial reversal of an authorized ATM Transaction when the ATM Terminal indicates that the Transaction was not completed because the Cardholder failed to collect some or all of the cash dispensed.

# 2.11.2 Full and Partial Reversals - Issuer Requirements

An Issuer receiving a Reversal Request/0400 message or an Acquirer Reversal Advice/0420 message must release any hold placed on funds in the Mastercard or Maestro Account in the



53
# Authorization and Clearing Requirements

# 2.11.3 Reversal for Conversion of Approval to Decline

amount specified within 60 minutes of matching the reversal message to the original authorization request message.

To match the reversal to the original approved authorization, the Issuer should use:

- The original authorization trace ID, as populated in DE 48, subelement 63 (Trace ID);
- The original switch serial number, as populated in DE 48, subelement 59, subfield 1 (Original Switch Serial Number); or
- Effective 17 October 2025, the original authorization TLID, as populated in DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID]).

NOTE: Modifications to this Rule appear in the "Europe Region" and "United States Region" sections at the end of this chapter.

# 2.11.3 Reversal for Conversion of Approval to Decline

An Acquirer or Merchant may convert an approval authorization request response (herein, an “Issuer-approved authorization”) into a decline for a Card-not-present (CNP) Mastercard or Maestro POS Transaction believed, in good faith, by the Acquirer or Merchant to be fraudulent solely in accordance with the following procedure:

1. The Acquirer or Merchant must determine whether to proceed with a Transaction believed, in good faith, to be fraudulent within 72 hours of sending the original authorization request message.
2. Upon deciding not to proceed with the Transaction and still within 72 hours of the original authorization request, the Acquirer or Merchant must:
1. Generate a reversal message for the full transaction amount that includes a reason code indicating that the Transaction was declined by the Acquirer or the Merchant due to perceived fraud,
2. Disclose to the Cardholder that the transaction cannot be completed at that time, and provide the Cardholder with valid customer service contact information (phone number or email address) to respond to Cardholder calls or email messages related to the cancelled order.

The contact information should be that of the Acquirer or Merchant that made the decision not to proceed with the Transaction. Sharing the specific reasons for the decline is not recommended or required.

The likelihood that a Transaction is fraudulent typically is determined through fraud screening and fraud scoring services that involve the storage, transmission or processing of Card or Transaction data in compliance with the Payment Card Industry Data Security Standard (PCI DSS). The Acquirer must register any third party provider of such services as a Third Party Processor (TPP) as described in Chapter 7 of the Mastercard Rules. The systematic decline by an Acquirer or Merchant of CNP Transactions arising from particular Cards, Issuers, or geographic locations is a violation of section 5.11.1, "Honor All Cards" of the Mastercard Rules.


# Authorization and Clearing Requirements

# 2.11.4 Reversal to Cancel Transaction

A single message POS Transaction may be cancelled prior to its completion by use of a “CANCEL” or “STOP” key on the POS Terminal. If either the Cardholder or Merchant cancels the Transaction, or a technical failure occurs involving a magnetic stripe Transaction, either before or after the authorization request has been forwarded to the Issuer, the Cardholder and Merchant must be informed; there must be no record of a Transaction; and a reversal advice message must be sent to the Issuer.

If after sending an authorization request, the POS Terminal does not receive a response, the POS Terminal must ‘time-out’ and send an automatic reversal. In such event, the Cardholder and Merchant must be informed; the attempted Transaction must be recorded; and a reversal advice message must be sent to the Issuer with a response code.

# 2.12 Full and Partial Approvals

The Acquirer and each of its Merchants that support partial approvals must establish an education program for Merchant staff, including but not limited to POS Terminal operators, relating to the acceptance of multiple payment methods for a single purchase. A Merchant's support of partial approvals is indicated with a value of 1 in DE 48, subelement 61, subfield 1 (Partial Approval Terminal Support Indicator) of the authorization request (0100 or 0200) message.

An Issuer must not respond to a cash withdrawal or purchase with cash back Transaction authorization request with a partial approval. A cash withdrawal Transaction must be approved or declined for the amount requested. A purchase with cash back Transaction must be either approved or declined for the total amount requested (purchase plus cash) or approved for the purchase amount only.

A Customer must support partial approval as follows:

1. An Issuer must support partial approval for all prepaid Mastercard, all Debit Mastercard (including prepaid), and all Maestro Account ranges.
2. For each Merchant identified with any of the MCCs listed below, an Acquirer must support partial approval on Mastercard and Maestro branded prepaid and debit Account ranges. This requirement applies to Card-present Transactions occurring at attended Terminals and at Cardholder-activated Terminals (CATs) identified with MCC 5542 (Fuel Dispenser, Automated) or MCC 5552 (Electric Vehicle Charging).

|MCC|Description|
|---|---|
|5310|Discount Stores|
|5311|Department Stores|
|5411|Grocery Stores, Supermarkets|
|5541|Service Stations (with or without Ancillary Services)|


# Authorization and Clearing Requirements

# 2.12 Full and Partial Approvals

|MCC|Description|
|---|---|
|5542|Fuel Dispenser, Automated (if authorization occurs prior to fueling)|
|5552|Electric Vehicle Charging (if authorization occurs prior to charging)|
|5621|Women’s Ready to Wear Stores|
|5691|Men’s and Women’s Clothing Stores|
|5732|Electronic Sales|
|5812|Eating Places, Restaurants|
|5814|Fast Food Restaurants|
|5912|Drug Stores, Pharmacies|
|5999|Miscellaneous and Specialty Retail Stores|

3. For an Acquirer in a Region indicated below, the partial approval support requirement in item 2 includes the following additional MCCs.

|MCC|Description|Acquirer Region|
|---|---|---|
|4111|Transportation: Suburban and Local Commuter Passenger, including Ferries|U.S.|
|4812|Telecommunication Equipment including Telephone Sales|Canada, U.S.|
|4814|Telecommunication Services|Canada, U.S.|
|4816|Computer Network/Information Services|Canada, U.S.|
|4899|Cable, Satellite, and Other Pay Television and Radio Services|U.S.|
|5111|Stationery, Office Supplies|U.S.|
|5200|Home Supply Warehouse Stores|Canada, U.S.|
|5300|Wholesale Clubs|U.S.|
|5331|Variety Stores|Canada, U.S.|
|5399|Miscellaneous General Merchandise Stores|U.S.|
|5499|Miscellaneous Food Stores: Convenience Stores, Markets, Specialty Stores|Canada, U.S.|
|5631|Women's Accessory and Specialty Stores|Canada|
|5641|Children's And Infant's Wear Stores|Canada|
|5651|Family Clothing Stores|Canada|
|5661|Shoe Stores|Canada|
|5734|Computer Software Stores|Canada, U.S.|
|5735|Record Shops|Canada, U.S.|


# Authorization and Clearing Requirements

# 2.13 Refund Transactions and Corrections

|MCC|Description|Acquirer Region|
|---|---|---|
|5921|Package Stores, Beer, Wine, and Liquor|Canada, U.S.|
|5941|Sporting Goods Stores|Canada, U.S.|
|5942|Book Stores|Canada, U.S.|
|5943|Office, School Supply and Stationery Stores|U.S.|
|5945|Game, Toy, and Hobby Shops|Canada|
|5947|Gift, Card, Novelty, and Souvenir Shops|Canada|
|5977|Cosmetic Stores|Canada|
|7399|Business Services: not elsewhere classified|Canada|
|7829|Motion Picture and Video Tape Production and Distribution|U.S.|
|7832|Motion Picture Theaters|U.S.|
|7841|Video Entertainment Rental Stores|U.S.|
|7996|Amusement Parks, Carnivals, Circuses, Fortune Tellers|U.S.|
|7997|Clubs: Country Clubs, Membership (Athletic, Recreation, Sports), Private Golf Courses|U.S.|
|7999|Recreation Services: not elsewhere classified|U.S.|
|8011|Doctors: not elsewhere classified|U.S.|
|8021|Dentists, Orthodontists|U.S.|
|8041|Chiropractors|U.S.|
|8042|Optometrists, Ophthalmologists|U.S.|
|8043|Opticians, Optical Goods, and Eyeglasses|U.S.|
|8062|Hospitals|U.S.|
|8099|Health Practitioners, Medical Services: not elsewhere classified|U.S.|
|8999|Professional Services: not elsewhere classified|Canada, U.S.|
|9399|Government Services: not elsewhere classified|Canada, U.S.|

NOTE: Modifications to this Rule appear in the "Asia/Pacific," "Canada Region," "Europe Region," and "Middle East/Africa Region" sections at the end of this chapter.

A refund Transaction is a payment processed by a Merchant to a Cardholder’s Account upon the return of goods or cancellation of services previously purchased by the Cardholder from the


# Authorization and Clearing Requirements

# 2.13.1 Refund Transactions - Acquirer Requirements

Merchant. A refund Transaction may be a dual or single message Transaction and contains a value of 20 in DE 3 (Processing Code), subfield 1 (Cardholder Transaction Type Code). A refund Transaction must only be reversed for the purchase Transaction amount or adjusted for an amount less than the purchase Transaction amount to correct a clerical error. The reversal or adjustment must occur within one calendar day of the refund Transaction. The Settlement Date of the Financial Transaction Request/0200 or Central Site Business Date of the First Presentment/1240 message of the refund Transaction is counted as day zero. Reversible clerical errors include, by way of example and not limitation, the erroneous capture of Transaction data, a duplicate Transaction, or an error caused by the transposition of data.

A correction is a single message authorization request containing a value of 20 in DE 3 (Processing Code), subfield 1 (Cardholder Transaction Type Code) that is used in a Card-present environment following a single message POS Transaction approval to remedy a Merchant or Cardholder error. A correction must be performed as a Card-read Transaction initiated by or on behalf of the Cardholder; the Transaction may be completed without a Cardholder verification method.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# 2.13.1 Refund Transactions - Acquirer Requirements

Effective 12 April 2024, an Acquirer must support the online authorization of Mastercard, Debit Mastercard, and Maestro refund Transactions acquired on the Dual Message System (with the exception of refunds for Contactless transit aggregated Transactions) and enable refund Transaction authorization service for a Merchant upon request. The Acquirer must forward each refund Transaction authorization request to the Issuer at the time of the Transaction, rather than in a batch, so that the Merchant receives the Issuer's response while the Cardholder is at the POS and before offering the Cardholder a refund Transaction receipt.

The Acquirer must identify a refund Transaction authorization request as a final authorization, as described in Rule 2.7.

The First Presentment/1240 message of a refund Transaction must be submitted for clearing within five calendar days of the refund Transaction date, and if authorized, contain refund Transaction authorization data in DE 63, subfield 2 (Trace ID).

Effective 12 April 2024, an authorized refund Transaction has a message reason code 4808 chargeback protection period of five calendar days from the refund Transaction authorization approval date.

Effective 18 October 2024, the Acquirer must perform online authorization for refund Transactions acquired through the Dual Message System.

NOTE: Modifications to this Rule appear in the "Canada Region" and "United States Region" sections at the end of this chapter.


# Authorization and Clearing Requirements

# 2.13.2 Refund Transactions - Issuer Requirements

Original Purchase Identifier

When possible, the Acquirer is recommended to populate DE 48, subelement 63 (Trace ID) of the refund Transaction authorization request message with a unique identifier from the original purchase Transaction, consisting of the values in DE 63 (Network Data), subfield 1 (Financial Network Code); DE 63, subfield 2 (Banknet Reference Number); and DE 15 (Date, Settlement) of the purchase Transaction authorization approval response message. The presence of this identifier may assist the Issuer in linking the refund to a prior purchase and help to avoid Credit Not Processed disputes.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region" and "Europe Region" sections at the end of this chapter.

# 2.13.2 Refund Transactions - Issuer Requirements

For all Mastercard Cards except non-reloadable prepaid Cards, an Issuer must be able to receive and respond to an Authorization Request/0100 or Financial Transaction Request/0200 message for a refund Transaction.

# Response Code Values

An Issuer is advised to provide a value of 00 (Approved or completed successfully) in DE 39 (Response Code) if the Account is open, so that the refund Transaction can be completed. The following DE 39 values are invalid for refund Transactions and must not be used in the Issuer's response to a refund Transaction authorization request:

- 10 (Partial approval)
- 51 (Insufficient funds/over credit limit)

An Issuer may only use a value of 57 (Transaction not permitted to issuer/cardholder) in DE 39 for a non-reloadable Prepaid Card Program. An Issuer is advised to register the Prepaid Card Program as non-reloadable using the Prepaid Card Program registration process on Mastercard Connect before using this response code value. An Issuer must not decline a refund Transaction solely due to a message format error, the absence of a PIN, or the absence of chip-related data.

# Posting of Funds to the Cardholder's Account

Within one day of the Issuer's receipt of the First Presentment/1240 message or Financial Transaction Advice/0220 message for a refund Transaction, the Issuer must post the funds to the Cardholder's Account or adjust the Account’s "open-to-buy", as applicable. The Issuer may place a temporary hold on the funds to the extent allowed under applicable law if the Issuer determines that the circumstances or account history warrant the delay. With respect to dual message online authorization requests for refund Transactions, the Issuer is advised:


# Authorization and Clearing Requirements

# 2.14 Balance Inquiries

- to ensure that the refund Transaction amount is treated and displayed to the Cardholder as a pending credit, until the clearing record has been received and matched to the authorization;
- to clearly communicate that the funds due as a result of a refund Transaction will only be deposited to the Cardholder's Account upon receipt of such funds by the Issuer; and
- not to release the funds to the Cardholder until the clearing record is received.

# Pending Refund Transaction Information

An Issuer must make information about pending refund Transactions available to Cardholders upon through at least one delivery channel, such as in its online banking or other Cardholder-facing applications or by means of Transaction alerts. The pending refund information must be displayed in a manner similar to that used for a pending purchase Transaction.

NOTE: Modifications to this Rule appear in the "Europe Region" section at the end of this chapter.

# 2.14 Balance Inquiries

The balance inquiry functionality of a Terminal allows a Cardholder to check the available balance of funds in an Account. Balance inquiries are identified with a value of 30 in DE 3, subfield 1 of authorization messages.

All Terminals that offer a balance inquiry functionality to debit cardholders of Competing EFT POS Networks and other competing networks must offer the same balance inquiry functionality to debit Cardholders.

A Terminal that offers balance inquiry must provide the Cardholder an opportunity to receive a receipt reflecting (and may also display) Account balance information. Each ATM Terminal and Bank Branch Terminal must display, as part of the screen information, or must print on the receipt, the currency symbol of the local currency or three-character alpha ISO country code in which the balance amount is given, beside each balance inquiry amount.

NOTE: Additions to this Rule appear in the “Europe Region” and “United States Region” sections at the end of this chapter.

# 2.15 CVC 2 Verification for POS Transactions

A Merchant must not prompt or otherwise require a Mastercard Cardholder to enter CVC 2 information when a Chip Card or Contactless Payment Device is used to complete a Chip Transaction at a POS Terminal or MPOS Terminal. This Rule also applies to Mastercard Consumer-Presented QR Transactions.

Refer to Chapter 3 of the Security Rules and Procedures manual for CVC 2 requirements.

NOTE: An addition to this Rule appears in the “Europe Region” section at the end of this chapter.


# Authorization and Clearing Requirements

# 2.16 CVC 3 Verification for Maestro Magnetic Stripe Mode Contactless Transactions—Brazil Only

NOTE: A Rule on this subject pertaining to Brazil appears in the “Latin America and the Caribbean Region” section at the end of this chapter.

# 2.17 Euro Conversion—Europe Region Only

NOTE: A Rule on this subject appears in the “Europe Region” section at the end of this chapter.

# 2.18 Transaction Queries, Disputes, and Errors

A Customer must have the facilities and ensure the support of processes to handle Transaction queries, disputes, and chargebacks.

NOTE: A modification to this Rule appears in the “United States Region” section at the end of this chapter.

# 2.18.1 Compliance with Dispute Procedures

The Corporation administers procedures set forth in the Chargeback Guide that enable a Customer to seek redress against another Customer for failure to comply with the Standards applicable to a Transaction. Any filing by or on behalf of a Customer related to an arbitration procedure (including any chargeback or re-presentment cycle) or pre-compliance or compliance procedure must be made in good faith and only after careful review of both the Standards and available information pertinent to the dispute.

# 2.19 Chargebacks for Reissued Cards

Upon reissuing a Card with the same primary account number (PAN) and a new expiration date, the Issuer must include the expiration date in all Transaction chargeback records.

# 2.20 Correction of Errors

If a Customer has been unjustly enriched because of an error, the Customer must reimburse the amount with which it has been enriched to the Customer or Customers that have suffered the corresponding loss.


# Authorization and Clearing Requirements

# 2.21 Merchant Payment Gateway Identifier (MPG ID)

An Acquirer must populate the MPG ID field (DE 48, subelement 37 [Additional Merchant Data], subfield 5 [Merchant Payment Gateway ID] with the MPG ID assigned by the Corporation at the time of registration of the MPG as a Service Provider, in authorization and advice messages for all Card-not-present Transactions (excluding MO/TO Transactions) identified with a value of 09, 10, or 81 in DE 22, subfield 1 that are received from the particular MPG. The value 999998 must be populated in the MGP ID field if the MPG is wholly owned by the Acquirer and so not registered as a Service Provider. The value 999997 must be populated in the MPG ID field if the Merchant uses no gateway and connects directly to the Acquirer. This requirement applies to purchase Transactions, refund Transactions, and Payment Transactions initiated by Merchants (for example, Gaming Payment Transactions).

If multiple MPGs are involved, the Acquirer must provide the MPG ID of the MPG that sends to that Acquirer the Transaction data that the Acquirer uses to generate the authorization or advice message.

Population of the MPG ID in authorization and advice messages for Card-present Transactions is recommended but not required.

An Issuer must technically support the population of the MPG ID field in authorization and advice messages for both Card-not-present and Card-present Transactions. No Issuer response to or handling of the MPG ID is required.

NOTE: A modification to this Rule appears in the "Middle East/Africa Region" section at the end of this chapter.

# 2.22 Co-badged Cards - Acceptance Brand Identifier

NOTE: A Rule on this subject appears in the "Europe Region" section at the end of this chapter.


# Authorization and Clearing Requirements

# Variations and Additions by Region

The remainder of this chapter provides modifications to the Standards set out in this chapter. The modifications are organized by region or country and by applicable subject title.

# Asia/Pacific Region

The following modifications to the Rules apply in the Asia/Pacific Region or in a particular Region country or countries. Refer to Appendix A for the Asia/Pacific Region geographic listing.

# 2.1 Acquirer Authorization Requirements

In the Asia/Pacific Region, the Rule on this subject is modified as follows. An Acquirer must ensure that any authorization request for an amount greater than zero is identified as either a preauthorization or as a final authorization. An Acquirer must support Maestro POS Transactions that access the primary account and may also allow the Cardholder to select a checking or savings account (“account selection”). In China, the Rule on this subject is modified as follows. An Acquirer must be able to transmit a PIN in Preauthorization Request/0100 and Financial Transaction Request/0200 messages for China Domestic Transactions.

# 2.1.1 Acquirer Host System Requirements

An Acquirer in the Asia/Pacific Region must ensure that its host systems and those of its Service Providers support online PIN:

- For China Domestic Transactions occurring at POS Terminals, including MPOS Terminals; and
- Effective 1 April 2023, for Transactions occurring at contactless-enabled POS Terminals in all other Asia/Pacific Region countries and territories except Japan, Republic of Korea, and Taiwan.

The following Rule applies to China domestic Transactions only. An Acquirer and each of its Merchants must support POS Transactions, Payment Transactions, Refund Transactions, and full reversals when performed to cancel a POS Transaction that the Acquirer cannot complete due to a technical problem. The Acquirer may also support the below payment or transfer type transactions:

- China Funds Transfer Transactions
- China Deposit Transactions

An Acquirer must not discriminate.


# Authorization and Clearing Requirements

# 2.2 Issuer Authorization Requirements

In the Asia/Pacific Region, the Rule on this subject is modified as follows. An Issuer may decline authorization of a Transaction when technical fallback from chip to magnetic stripe occurred.

For China Domestic Transactions, the Rule on this subject is modified as follows. In China, when a Chip Card is used to transact at a Hybrid Terminal, the Transaction must be routed by means of the chip payment application.

# 2.2.1 Issuer Host System Requirements

In the Asia/Pacific Region, the Rule on this subject is modified as follows. An Issuer that chooses to enable the purchase with cash back Transaction type for Debit Mastercard (including prepaid) or Maestro (including prepaid) Account ranges must support the purchase with cash back Transaction type on its host system interfaces. A Maestro Card Issuer’s host system interfaces must support POS balance inquiry.

In China, the Rule on this subject is modified as follows. For China Domestic Transactions, an Issuer’s host system interface must support the online processing of:

- POS Transactions
- Payment Transactions
- Refund Transactions
- Full Reversal
- Cash withdrawals at ATM Terminals
- Funds Transfer Transactions; and
- Deposit Transactions.

For China Domestic Transactions, in the event that an Issuer does not offer a particular Transaction message type to its Cardholders, the Issuer must provide a value of 57 indicating “transaction not permitted to issuer/cardholder” in DE 39 (Response Code) of the online authorization message. An Issuer must not discriminate against or discourage the above transaction types in favor of any other acceptance brand or switch network.

# 2.3 Authorization Responses

For China Domestic Transactions, the Rule on this subject is modified as follows. An Acquirer must comply with the authorization response wait time requirements set forth in "Maximum Response Times" in Chapter 2 of the China Switch Specifications. An Issuer must comply with the authorization response requirements set forth in "Maximum Response Times" in Chapter 2 of the China Switch Specifications.

# 2.5 Preauthorizations


# Authorization and Clearing Requirements

# 2.5.1 Preauthorizations - Mastercard POS Transactions

For China Domestic POS Transactions, the Rule on this subject is modified as follows. All preauthorization completion corresponding to a preauthorization must be initiated within 30 calendar days of the authorization approval date. The preauthorization completion amount must be less than or equal to the amount approved in the corresponding preauthorization. The Issuer must accept all preauthorization completions provided the actual amount of the completion is less than or equal to the amount approved in the preauthorization.

# 2.5.2 Preauthorizations—Maestro POS Transactions

In the Asia/Pacific Region, the Rule on this subject is modified as follows. The Acquirer is not liable for preauthorization completions that occurred within 20 minutes of the initial Maestro POS Transaction but were subsequently stored and forwarded because of technical problems between the Interchange System and the Issuer.

# 2.7 Final Authorization

In China, a domestic final authorization request is identified in the Financial Transaction Request/0200 message when DE 61 (Point-of-Service [POS] Data), subfield 7 (POS Transaction Status) contains a value of 0 and DE 48 (Additional Data), 61 (POS Data), subfield 5 (Final Authorization Indicator) contains a value of 1. Effective 3 April 2024 for India Domestic Transactions, the Rule on this subject is modified as follows. When an Acquirer or Merchant uses the final authorization, then in a dual message environment:

1. Any Transaction corresponding to an authorization identified as a final authorization must be presented for clearing within four calendar days of the authorization approval date; and
2. The presented Transaction amount must equal the authorized amount.

# 2.8 Message Reason Code 4808 Chargeback Protection Period

Effective 3 April 2024 for India Domestic Transactions, the Rule on this subject is modified as follows. A message reason code 4808 (Authorization–related Chargeback) chargeback protection period applies to each Mastercard POS Transaction as follows.

|Each Mastercard POS Transaction|Has a message reason code 4808 chargeback protection period of…|
|---|---|
|Preauthorization|30 calendar days from the authorization approval date|
|Final authorization|Four calendar days from the authorization approval date|


# Authorization and Clearing Requirements

# 2.11.1 Full and Partial Reversals—Acquirer Requirements

# POS Transactions

Effective 3 April 2024 for India Domestic Transactions, the Rule on this subject is modified as follows. Notwithstanding the above reversal requirement, the Acquirer must ensure that if a Merchant cancels a Transaction or finalizes a Transaction for a lower amount than previously approved, no reversal is submitted if such event occurs:

- More than 30 calendar days after the authorization date for a preauthorization; or
- More than four calendar days after the authorization date for any other authorization message.

# 2.12 Full and Partial Approvals

In the Asia/Pacific Region, the Rule on this subject is modified as follows. Issuers and Acquirers are not required to support partial approvals.

# 2.13 Refund Transactions and Corrections

In China, the China Switch allows the Customer to use the China Dispute Resolution Platform to manually initiate a refund for a processed domestic Transaction. The Standards in this manual applicable to a refund Transaction will also apply to a domestic manual refund Transaction.

# 2.13.1 Refund Transactions - Acquirer Requirements

For China Domestic Transactions, the Rule on this subject is modified as follows. Effective 12 April 2024, an Acquirer must support the online authorization of Mastercard, Debit Mastercard, and Maestro refund Transactions acquired on the Dual Message System (with the exception of refunds for Contactless transit aggregated Transactions) and enable refund Transaction authorization service for a Merchant upon request. The Acquirer must forward each refund Transaction authorization request to the Issuer at the time of the Transaction, rather than in a batch, so that the Merchant receives the Issuer’s response while the Cardholder is at the POS and before offering the Cardholder a refund Transaction receipt.

# Original Purchase Identifier

The Acquirer must follow the requirements as per the table below for population of the Original Purchase Identifier. The presence of this identifier may assist the Issuer in linking the refund to a prior purchase and help to avoid Credit Not Processed disputes.


# Authorization and Clearing Requirements

# Canada Region

If the online refund Transaction occurs…

| |Within 180 days from the original Transaction date|After 180 days from the original Transaction date|
|---|---|---|
|The Acquirer…|The Acquirer must populate DE 48, subelement 59 (Original Network Reference Number) of the refund Transaction authorization request message with unique identifier from the original purchase Transaction, consisting of the values in DE 63 (Network Data), subfield 3 (Network Reference Number); and DE 15 (Date, Settlement) of the purchase of the Transaction authorization approval response message.|The Acquirer is strongly recommended to populate DE 48, subelement 59 (Original Network Reference Number) of the refund Transaction authorization request message with unique identifier from the original purchase Transaction, consisting of the values in DE 63 (Network Data), subfield 3 (Network Reference Number); and DE 15 (Date, Settlement) of the purchase of Transaction authorization approval response message.|

# Canada Region

The following modifications to the Rules apply in the Canada Region. Refer to Appendix A for the Canada Region geographic listing.

# 2.1 Acquirer Authorization Requirements

# 2.1.1 Acquirer Host System Requirements

The Acquirer of a Merchant located in the Canada Region must ensure that its host system and those of its Service Providers:

- Are capable of processing Domestic Debit Mastercard Transactions; and
- Populates the value of Y in DE 48 (Additional Data—Private Use), subelement 18 (Service Parameters), subfield 01 (Canada Domestic Indicator) of the Authorization Request/0100 message for each Mastercard Transaction initiated at Merchants that have provided consent to accept domestically issued Debit Mastercard Cards.

Initiating a Domestic Debit Mastercard Transaction that contains the Y, a Canada Region Acquirer affirms that the Merchant has agreed to accept domestically issued Debit Mastercard Cards.

# 2.2 Issuer Authorization Requirements

In the Canada Region, the Rule on this subject is modified as follows.

An Issuer must decline authorization of a Transaction conducted in the Canada Region when technical fallback from chip to magnetic stripe occurred.



67
# Authorization and Clearing Requirements

# 2.12 Full and Partial Approvals

In the Canada Region, the Rule on this subject is modified as follows.

1. An Issuer must support partial approval for all prepaid Mastercard and all Debit Mastercard Accounts.
2. An Acquirer must support partial approval for Card-present Transactions occurring at a Merchant in a category listed in Rule 2.12 with a Debit Mastercard or prepaid Mastercard Account range.

# 2.13 Refund Transactions and Corrections

# 2.13.1 Refund Transactions - Acquirer Requirements

In the Canada Region, the requirement for an Acquirer to perform online authorization for refund Transactions acquired through the Dual Message System does not apply.

# Europe Region

The following modifications to the Rules apply in the Europe Region or in a particular Region country or countries. Refer to Appendix A for the Europe Region, Non-Single European Payments Area (Non-SEPA) and Single European Payments Area (SEPA) geographic listing.

# 2.1 Acquirer Authorization Requirements

In the Europe Region, the Rule on this subject is modified as follows.

An Acquirer must ensure that any authorization request for an amount greater than zero is identified as either a preauthorization or as a final authorization. The reference to the Single Message System does not apply in the EEA.

# Strong Customer Authentication (SCA) Requirements

If the Issuer and the Acquirer are located in an SCA Country, but the Merchant is not, EMV 3DS authentication requests must include the Mastercard "Merchant Data" EMV 3DS Message Extension, with Field 3 containing the Acquirer country code. In other cases, it is recommended to provide the Acquirer country code in the Mastercard "Merchant Data" EMV 3DS Message Extension Field 3.

The Issuer and its Access Control Server are advised to use the Acquirer country code in the Mastercard "Merchant Data" EMV 3DS Message Extension Field 3 to determine if SCA is required. If the Acquirer country is not provided, the Issuer is advised to use the Merchant country to determine if SCA is required.

# Authentication Outage Exception

The following Rules apply to Intracountry and Cross-border Transactions within and between SCA Countries.


# Authorization and Clearing Requirements

# 2.1 Acquirer Authorization Requirements

An Acquirer may permit a Merchant to use the Authentication Outage Exception flag in authorization request messages. The Merchant must first attempt use of a suitable exemption (subject to the Acquirer's approval) before resorting to the Authentication Outage Exception. The Acquirer must ensure that the Merchant does not misuse the Authentication Outage Exception as a means to bypass authentication. Authentication failure must persist for at least five minutes, leading all authentications to fail (i.e., no attempt responses provided) before the Authentication Outage Exception is used. Authentication must be resumed as soon as the outage is resolved. The Acquirer must promptly provide full and clear evidence of the outage upon the Corporation's request.

The Authentication Outage Exception must in no case be used for a Transaction or an Account status inquiry that sets up Merchant-initiated Transactions or recurring payment arrangements. A Transaction completed using the Authentication Outage Exception is not protected from fraud-related chargebacks.

For the authorization of a Remote Electronic Transaction, authentication using EMV 3DS and Identity Check is required and may be omitted only if an Acquirer exemption to SCA applies or if another SCA compliant method is used (e.g., alternative technical SCA solution delegation to the Merchant), or exemption under Article 17 of the PSD2 RTS (or corresponding legislation) applied with the Merchant's knowledge.

When SCA by the Issuer is not required, or when it has been delegated, or when SCA has been omitted, the Merchant must provide to the Acquirer the reason for omitting authentication (e.g., exemption or exclusion). The Merchant must not forward a Remote Electronic Transaction without providing the reason for omitting authentication. The Acquirer must indicate the reason for the exemption or exclusion in the appropriate field of the authorization message as specified by the registered switch of its choice. The Acquirer must not submit the authorization request without indicating the reason for omitting authentication.

An Acquirer which allows its e-commerce Merchants to request a Transaction Risk Analysis (TRA) exemption must set the TRA exemption flag for such Merchants when registering them for the Identity Check Program in the Identity Solutions Services Management (ISSM) tool. In order to optimize authorization approval rates for Transactions that benefit from an Acquirer exemption, a Merchant is advised to send an EMV 3DS authentication request with the Acquirer exemption flag.

Both Acquirers and Issuers must support the Acquirer exemption flag in EMV 3DS authentication requests as follows:

- In EMV 3DS version 2.1, Challenge Indicator value 02/No Challenge and Mastercard "Merchant Data" EMV 3DS Message Extension Field 1 (SCA Exemptions) with value 05/No SCA Requested, Transaction Risk Analysis performed.
- Effective with EMV 3DS version 2.2, Challenge Indicator value 05/No SCA Requested, Transaction Risk Analysis performed.

An Acquirer of e-commerce Merchants that accept corporate Cards, and an Issuer of such Cards must support the Mastercard "Merchant Data" EMV 3DS Message Extension flag in EMV 3DS authentication requests. This flag indicates if the conditions for the exemption under Article 17 of the PSD2 RTS (or corresponding legislation) are met, so that this exemption can be applied.


# Authorization and Clearing Requirements

# 2.2 Issuer Authorization Requirements

by the Issuer. The flag is in the Mastercard "Merchant Data" EMV 3DS Message Extension Field 4 (Secure Corporate Payment).

# Account Status Inquiry (ASI) Requests

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. References to ASI request messages and data fields are replaced by the corresponding message type and data fields of the registered switch of the Customer's choice.

# Echoing of Transaction Link ID

In the EEA, UK, and Gibraltar, the Rule on this subject is modified as follows. References to authorization messages and data fields are replaced by the corresponding message types and data fields of the registered switch of the Customer's choice.

# 2.2 Issuer Authorization Requirements

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. An Issuer must indicate that the Transaction type is not permitted to the Cardholder in the field of the authorization response and using the values specified by the registered switch of the Issuer's choice.

# SCA Requirements

The following Rules apply to Intracountry and Cross-border Transactions within and between SCA Countries. An Issuer must be able to process the Low Risk Merchant Indicator in authorization request messages, as specified by the registered switch of the Customer's choice.

If the Low Risk Merchant Indicator is present and populated in the authorization message, then the Issuer must neither automatically decline the authorization request nor require the Cardholder to authenticate the Transaction unless: a) its Transaction monitoring suggests a high risk of fraud, or b) in the case of a low-value payment, the Transaction counters are exceeded.

If an authentication request contains the Acquirer exemption flag or the delegation flag, the Issuer must neither automatically decline the authentication request nor require the Cardholder to authenticate the Transaction unless: a) its Transaction monitoring suggests a high risk of fraud, or b) in the case of a low-value payment, the Transaction counters are exceeded.

An Issuer that requires authentication for more than 10% of authorization requests which indicate the application of an Acquirer exemption or SCA delegation will be automatically enrolled in the Smart Authentication Direct for Acquirer Exemption (SADAE) service.

# Authentication Outage Exception

An Issuer must be able to receive and process the Authentication Outage Exception flag in authorization messages. It is recommended that the Issuer indicate clearly in the authorization.


# Authorization and Clearing Requirements

# 2.2.2 Stand-In Processing Service

response whether or not the Merchant should attempt authentication at a later time when the outage is resolved.

# Account Status Inquiry (ASI) Requests

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. References to ASI request messages and data fields are replaced by the corresponding message type and data fields of the registered switch of the Customer's choice.

# 2.2.2 Stand-In Processing Service

In the Europe Region, the Rule on this subject is modified as follows. For all of its Maestro and Cirrus Card Programs, an Issuer must use the Stand-In Processing Service. This requirement does not apply if the Issuer commenced its use of an alternative on-behalf authorization service before 17 September 2008 and such service meets the Corporation’s performance standards as set forth in Rule 2.4.2. Stand-In Parameters for Maestro and Cirrus Card Programs must be set at or above the Corporation's default limits. The requirement to use CVC 1 Verification in Stand-In service, does not apply to Maestro Chip-only Cards, as such term is defined in section 6.11, "Maestro Chip-only Card Programs," Chapter 13 of the Mastercard Rules.

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. An Issuer is not required to participate in the Stand-in Processing Service unless so required by the registered switch of the Issuer's choice. The registered switch of the Issuer's choice must provide a back-up service that is able to approve authorization requests on the Issuer's behalf. The Stand-in Processing Service may be used for this purpose. The Issuer must set its parameters in the back-up service of its chosen switch at or above the default limits established by the Corporation for Mastercard, Maestro and Cirrus Card Programs.

# Smart Authentication Stand-In

An Issuer in Armenia, Azerbaijan, Belarus, Israel, Georgia, Kazakhstan, Kyrgyzstan, Tajikistan, Russian Federation (except domestic authentication processed by NSPK), Switzerland, Turkey, Turkmenistan, or Uzbekistan must participate in Smart Authentication Stand-In. Issuers in all other Europe Region countries must participate in Smart Authentication Stand-In or an alternative authentication stand-in solution.

# 2.2.3 ATM Transaction Requirements for Mastercard Credit Card Issuers

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. The decline reason codes in the table in this Rule are replaced by the corresponding reason codes specified by the registered switch of the Issuer's choice.

# 2.3 Authorization Responses

In the Europe Region, the Rule on this subject is modified as follows.


# Authorization and Clearing Requirements

# 2.4 Performance Standards

An Issuer must comply with the authorization response requirements set forth in “Routing Timer Values” in Chapter 5 of the Authorization Manual. If the Issuer’s response is not received within the required time frame, then the Transaction will time out and be forwarded via the Stand-In Processing System or, when permitted under Rule 2.2.2, another alternate authorization provider as specified by the Issuer.

# 2.4 Performance Standards

# 2.4.2 Performance Standards—Issuer Requirements

In the Europe Region, the Rule on this subject is replaced with the following. For all Transactions, an Issuer authorization failure rate that exceeds one percent for two months in any six-month period is deemed to be substandard performance. The Issuer failure rate is not applied until after the Issuer’s fourth calendar month of operation or upon the Issuer’s processing of 5,000 Transactions in a calendar month, whichever occurs first. The Issuer failure rate is calculated by taking the sum of ISO 8583 response codes 31—issuer signed off, 82—time out at Issuer host, and 96—system malfunction, and dividing by the total number of Transactions processed through the Issuer connection to the Interchange System.

An Issuer that has been designated as having substandard performance:

1. May be subject to noncompliance assessments as set forth in Rule 2.4; and
2. Will be mandated to implement the Stand-In Processing Service. Chip Issuers mandated to implement the Stand-In Processing Service will also be required to register for M/Chip Cryptogram Validation in Stand-In.

# 2.5 Preauthorizations

In the Europe Region, the Rule on this subject is modified as follows. In a dual message environment, the Acquirer must identify each Processed Transaction authorization request as either a preauthorization or a final authorization. Preauthorizations occurring at an automated fuel dispenser and identified with MCC 5542 (Automated Fuel Dispenser) must be performed as described in Rule 4.10.1. Preauthorizations occurring at an electric vehicle charging station and identified with MCC 5552 (Electric Vehicle Charging) must be performed as described in Rule 4.10.2.

In the EEA, UK and Gibraltar the Rule on this subject is modified as follows. The authorization request must be identified as a preauthorization in the field and with the value specified by the registered switch of the Issuer’s choice.

# 2.5.2 Preauthorizations—Maestro POS Transactions

In the Europe Region, the Rule on this subject is modified as follows. Preauthorizations are permitted for Card-not-present Maestro POS Transactions when completed in accordance with the requirements set forth below. Preauthorizations are not permitted for Maestro POS Transactions conducted in any Card-present environment, with the


# Authorization and Clearing Requirements

# 2.5.3 Preauthorizations—ATM and Manual Cash Disbursement Transactions

exception of automated fuel dispenser Transactions, electric vehicle charging Transactions, and Contactless transit aggregated Transactions.

As an exception to the preceding Rule, preauthorizations for an estimated maximum amount are permitted for Maestro POS Transactions conducted in a Card-present environment, at vending machines located in the Netherlands and Switzerland that are identified with MCC 5499 (Miscellaneous Food Stores—Convenience Stores, Markets, Specialty Stores). The Acquirer must inform the Issuer of the final Transaction amount via an advice message, which must be sent to the Issuer within 20 minutes of the authorization response message.

Issuers in the Netherlands and Switzerland, respectively, must be able to receive the advice message and must post the Transaction to the Cardholder’s Account on the basis of the advice message, rather than the preauthorization response. Support of Maestro preauthorizations at vending machines in the Netherlands and Switzerland is optional for Issuers in other countries.

The Acquirer must ensure that the authorization request for a Card–not–present Maestro POS Transaction for an amount greater than zero is identified as a preauthorization if:

1. Authorization is requested for an estimated amount; or
2. The Transaction might not be completed for reasons other than technical failure or lack of full issuer approval; for example:

The risk of technical failures, such as telecommunications failure or Terminal failure, should not be taken into account to determine if an authorization must be coded as a preauthorization.

Any Card–not–present Maestro POS Transaction clearing message corresponding to a preauthorization must be presented within seven calendar days of the authorization approval date. The presented Transaction amount must equal the approved amount.

# 2.5.3 Preauthorizations—ATM and Manual Cash Disbursement Transactions

In the Europe Region, the Acquirer must ensure that any ATM Transaction or Manual Cash Disbursement Transaction authorization request for an amount greater than zero is identified as a preauthorization if:

1. Authorization is requested for an estimated amount; or
2. The Transaction might not be completed for reasons other than technical failure or lack of full issuer approval; for example, if the mobile phone number for which the Cardholder has requested a top–up is later found not to exist.

The risk of technical failures, such as telecommunications failure or Terminal failure, should not be taken into account to determine if an authorization must be coded as a preauthorization.



73
# Authorization and Clearing Requirements

# 2.7 Final Authorizations

Any ATM Transaction or Manual Cash Disbursement Transaction corresponding to an authorization identified as a preauthorization must be presented within seven calendar days of the authorization approval date. The presented Transaction amount must equal the authorized amount.

# 2.7 Final Authorizations

In the Europe Region, the Rule on this subject is modified as follows. The Acquirer must ensure that when an authorization request for an amount greater than zero is identified as a final authorization:

1. The Transaction may no longer be cancelled and must not be reversed after the authorization request is approved in full by the Issuer, except upon Cardholder request or when non-completion is unavoidable for technical reasons such as telecommunications failure or POS Terminal failure;
2. The authorization being requested is for the final Transaction amount.

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. The authorization request must be identified as a final authorization in the field and with the value specified by the registered switch of the Issuer's choice.

# 2.8 Message Reason Code 4808 Chargeback Protection Period

In the Europe Region, the Rule on this subject is modified as follows. The following message reason code 4808 (Authorization–related Chargeback) chargeback protection periods apply with respect to each approved authorization.

|Each approved…|Has a message reason code 4808 chargeback protection period of…|
|---|---|
|Preauthorization of a Mastercard POS Transaction|Thirty (30) calendar days from the authorization approval date|
|Preauthorization of a Maestro POS Transaction, ATM Transaction, or Manual Cash Disbursement Transaction|Seven (7) calendar days from the authorization approval date|
|Final authorization|Seven (7) calendar days from the authorization approval date|

4 The message reason code 4808 chargeback protection for a properly identified preauthorization of an Acquirer-financed or Merchant-financed installment billing payment arrangement is not limited in time. Refer to Chapter 4 for Contactless Transit Aggregated Transaction processing procedures.


# Authorization and Clearing Requirements

# 2.9 Multiple Authorizations

In the Europe Region, the Rule on this subject applies to both Mastercard POS Transactions and Maestro POS Transactions.

Upon receipt of the Transaction clearing record, the Issuer must use the unique identifier to match the initial and any additional approved preauthorizations to the Transaction.

In the EEA, UK and Gibraltar, the Rule on this subject is additionally modified as follows. The Acquirer must populate a unique identifier from the initial approved authorization of a Transaction in the appropriate field of additional authorizations and of the Transaction clearing record, in accordance with the specifications of the registered switch of the Acquirer’s choice.

# 2.11 Full and Partial Reversals

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. References to Reversal Request/0440 and Acquirer Reversal Advice/0420 messages are replaced by the corresponding message types of the registered switch of the Customer’s choice.

# 2.11.1 Full and Partial Reversals - Acquirer Requirements

In the Europe Region, the Rule on this subject is modified as follows. With respect to POS Transactions and Merchandise Transactions, the Acquirer or Merchant must submit a reversal message to the Issuer within 24 hours of:

- The cancellation of a previously authorized Transaction, or
- The finalization of a Transaction with a lower amount than previously approved.

The reversal may be a full or partial reversal, as appropriate. In the case of finalization of a Transaction with a lower amount, a partial reversal is not required if the clearing message is submitted within 24 hours of finalization of the Transaction.

The reversal requirement does not apply to Transactions occurring at a Merchant identified with MCC 5542 (Fuel Dispenser, Automated) or to Contactless transit aggregated Transactions or transit debt recovery Transactions.

The requirement for the Acquirer to ensure that a Merchant submits a reversal within 30 calendar days for a preauthorization or seven calendar days for a final authorization does not apply in the Europe Region.

The Acquirer of a Merchant located in Italy that is identified with an MCC listed in the table below and that accepts Mastercard or Debit Mastercard Cards must support full and partial reversals performed at the POI and whenever, for technical reasons, the Acquirer is unable to communicate the authorization response to the Merchant, for all prepaid Debit Mastercard and all prepaid Mastercard Card Account ranges:

|MCC|Description|
|---|---|
|5310|Discount Stores|


# Authorization and Clearing Requirements

# 2.11.2 Full and Partial Reversals—Issuer Requirements

|MCC|Description|
|---|---|
|5311|Department Stores|
|5411|Grocery Stores, Supermarkets|
|5541|Service Stations (with or without Ancillary Services)|
|5542|Fuel Dispenser, Automated|
|5621|Women’s Ready to Wear Stores|
|5691|Men’s and Women’s Clothing Stores|
|5732|Electronic Sales|
|5812|Eating Places, Restaurants|
|5814|Fast Food Restaurants|
|5912|Drug Stores, Pharmacies|
|5999|Miscellaneous and Specialty Retail Stores|

In Italy, the Rule on this subject is modified as follows. An Issuer in Italy must support full and partial reversals for all prepaid Mastercard and all prepaid Debit Mastercard Card Account ranges.

# 2.12 Full and Partial Approvals

In the Europe Region, the Rule on this subject is modified as follows. A Customer must support partial approvals at Merchants identified with MCC 5542 (Fuel Dispenser, Automated) for all Mastercard Account ranges if the Customer supports partial approvals for Maestro or any other debit brand, as described in Rule 4.10.1. A Customer must support partial approvals on Mastercard and Maestro if it supports them on other brands, for the same product types and Merchant types as on the other brands. To the extent that support for partial approvals is not required on other brands, then it is not required on Mastercard or Maestro, with the exception of support at Merchants identified with MCC 5542 as set out in the preceding paragraph.

In Ukraine, the Rule on this subject is modified as follows: Effective 1 July 2023, all Issuers must support and participating Acquirers may offer partial approval on Mastercard, Debit Mastercard, and Maestro Account ranges. This requirement applies to Card-present Transactions occurring at attended POS Terminals and Card-not present Transactions.

In Moldova, the Rule on this subject is modified as follows:


# Authorization and Clearing Requirements

# 2.13 Refund Transactions and Corrections

Effective 1 January 2024, all Issuers must support and participating Acquirers may offer partial approvals on Mastercard, Debit Mastercard, and Maestro Account ranges, for Card-present Transactions occurring at attended POS Terminals and Card-not present (CNP) Transactions.

# 2.13.1 Refund Transactions—Acquirer Requirements

In the EEA, UK, and Gibraltar, the Rule on this subject is modified as follows. References to First Presentment/1240 messages are replaced by the corresponding message type of the registered switch of the Customer’s choice.

# 2.13.2 Refund Transactions—Issuer Requirements

In the EEA, UK, and Gibraltar, the Rule on this subject is modified as follows. References to Authorization Request/0100 messages and data fields are replaced by the corresponding message type and data fields of the registered switch of the Customer’s choice.

# 2.14 Balance Inquiries

In the Europe Region, the Rule on this subject is modified as follows. It is strongly recommended that an Issuer in the Europe Region support domestic, inter-European, and intra-European balance inquiries conducted at ATM Terminals. If an Issuer provides balance inquiries for its Cardholders at its own ATM Terminals, it must also support balance inquiries at the ATM Terminals of other Customers in the Europe Region. An Issuer may distinguish among Cards according to their category (for example, debit, credit). In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A balance inquiry must be identified in the message type and field and with the value specified by the registered switch of the Customer's choice.

# 2.15 CVC 2 Verification for POS Transactions

In Ireland and France, the following applies to Maestro Intracountry POS Transactions: If an Issuer receives CVC 2 data in the authorization request and it is invalid (for example, the CVC 2 field is not blank and the data does not match the data held on the Issuer’s records), the authorization request must be declined. The Issuer cannot use a fraud-related message reason code to charge back a Transaction after approving an authorization request for the Transaction that contained invalid CVC 2 data. In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. The value indicating a non-match of the CVC 2 must be populated in the field and with the value specified by the registered switch of the Customer’s choice.



77
# Authorization and Clearing Requirements

# 2.17 Euro Conversion

In the Europe Region, Transactions submitted into interchange that take place in countries that convert to the euro must be submitted in the euro. To allow a grace period for exceptional cases, the Interchange System will not reject Transactions submitted in currencies that have been replaced by the euro within six months after the transition period. Within this six-month period, an Issuer may not reject or charge back Transactions submitted in currencies that the euro has replaced exclusively on grounds that such Transactions have not been submitted in euro.

# 2.22 Co-badged Cards - Acceptance Brand Identifier

The following Rules apply for Intracountry POS Transactions in Serbia, Bosnia and Herzegovina, North Macedonia, Gibraltar, the United Kingdom, and EEA countries and for Cross-border POS Transactions between Serbia, Bosnia and Herzegovina, North Macedonia, Gibraltar, the United Kingdom and an EEA country, and for Intra-EEA POS Transactions completed on Cards that are co-badged with another payment scheme than Mastercard or Maestro at Merchants that accept the other payment scheme as well as Mastercard and/or Maestro.

# All Transactions

When the acceptance brand is Mastercard or Maestro, the Customer must ensure that the acceptance brand selected by the Cardholder at the POI is accurately captured and recorded for each Transaction. If the acceptance brand selected by the Cardholder is not transported or available, then the Transaction must be identified as Mastercard or Maestro if the Card or Account was issued under a BIN or BIN range assigned to the Corporation. The Corporation has the right to review the selected acceptance brand when auditing a Customer's Transaction records, for example if reported volumes seem to be inaccurate.

# Chip Transactions

A Chip Transaction is a Mastercard or Maestro Transaction when an acceptance brand identifier that uniquely relates to Mastercard or Maestro is sent by the Terminal to the Acquirer. The acceptance brand identifier is transmitted in the Dedicated File Name (DF Name). All chip-capable Terminals must capture and transmit the DF Name when the Chip Transaction is a Mastercard or Maestro Transaction. An Acquirer must itself transport, and must ensure that the registered switch of its choice transports, the DF Name to the Issuer in the authorization and clearing message for a Mastercard or Maestro Chip Transaction. Each Customer must store the DF Name along with other Transaction data and must rely on the DF Name to identify that a Chip Transaction is a Mastercard or Maestro Transaction.


# Authorization and Clearing Requirements

# Latin America and the Caribbean Region

# Electronic Commerce Transactions

The Acquirer and Merchant must rely on the acceptance brand selected by the Cardholder to identify that a Transaction is a Mastercard or Maestro Transaction. An Acquirer must itself transport, and must ensure that the registered switch of its choice transports, the acceptance brand to the Issuer in the authorization and clearing message for a Mastercard or Maestro Transaction. Each Customer must store the acceptance brand along with other Transaction data and must rely on the acceptance brand to identify that a Transaction is a Mastercard or Maestro Transaction.

# Latin America and the Caribbean Region

The following modifications to the Rules apply in the Latin America and the Caribbean Region. Refer to Appendix A for the Latin America and the Caribbean Region geographic listing.

# 2.2 Issuer Authorization Requirements

# 2.2.1 Issuer Host System Requirements

In Colombia and Venezuela, an Issuer that chooses to enable the purchase with cash back Transaction type for Debit Mastercard (including prepaid) or Maestro (including prepaid) Account ranges must support the purchase with cash back Transaction type on its host system interfaces.

# 2.5 Preauthorizations

# 2.5.2 Preauthorizations - Maestro POS Transactions

In Brazil, the Rule on this subject is modified as follows. Each Card-not-present Maestro POS Transaction preauthorization initiated with a debit Card issued in Brazil and used at a Merchant located in Brazil is valid for a period of seven (7) calendar days from the preauthorization approval date. Additional preauthorization requests may be submitted to extend the validity period or increase the authorized amount, as described in Rule 2.9 Multiple Authorizations of this Latin America and the Caribbean Region section.

# 2.9 Multiple Authorizations

In Brazil, the Rule on this subject is modified as follows with respect to Card-not-present Maestro POS Transactions initiated with a debit Card issued in Brazil at a Merchant located in Brazil. Following Issuer approval of the initial preauthorization request, a Merchant may submit one or more additional preauthorization requests for the same Card-not-present Maestro POS Transaction, subject to the following conditions:


# Authorization and Clearing Requirements

# 2.9 Multiple Authorizations

1. The original and each additional preauthorization request for the same Transaction is valid for a period of seven (7) calendar days from the authorization approval date.
2. Each additional approved preauthorization:
1. If submitted for a zero amount, extends the authorization validity period with no change to the total authorized Transaction amount; and
2. If submitted for a non-zero amount, both extends the authorization validity period and incrementally increases the total authorized Transaction amount.
3. If an additional preauthorization request is declined, then the most recent previously approved preauthorization remains valid. For example, if the Issuer approved the original BRL 100 preauthorization request on June 1 and declined an additional BRL 25 preauthorization request on June 7, then the Transaction must be completed by June 8 (when the original preauthorization expires) for BRL 100 (the original approved amount).
4. If any preauthorization request expires before the Transaction completion message is sent, then the Merchant or Acquirer must initiate a new original preauthorization request for the Transaction.

The processing of multiple preauthorization requests for the same Maestro POS Transaction must occur as follows.

|Preauthorization Message (0200/0210)|Preauth1 (original preauthorization message)|
|---|---|
| |Preauth2 (first additional preauthorization message for the same Transaction)|

# The Mastercard Network

The Acquirer provides:

- In DE 4 (Amount, Transaction), the original preauthorization request amount
- In DE 4, the additional amount being authorized, or a zero amount (to extend the authorization validity without increasing the authorized amount)
- In DE 15 and DE 63, the same values as received in the Preauth1 0210 message

populates:

- The authorization date in DE 15 (Date, Settlement) and the switch serial number [SSN] in DE 63 (Network Data)
- Preauth2 authorization date in DE 15
- Preauth2 SSN in DE 63
- Preauth1 SSN in DE 48 subelement 59 (Original Switch Serial Number)
- In DE 54 (Amounts, Additional), subfield 2 (Amount Type), the value of 92 and in subfield 5 (Amount), the total cumulative authorized amount


# Authorization and Clearing Requirements

# 2.10 Multiple Clearing or Multiple Completion Messages

# Preauthorization Message

(0200/0210) The Acquirer provides:

- In DE 4, the additional amount being authorized, or a zero amount
- In DE 15 and DE 63, the same values as received in the Preauth2 0210 message
- In DE 54, subfield 2, the value of 92 and in subfield 5, the total cumulative authorized amount

• Preauth3 (second additional preauthorization message for the same Transaction)

- Preauth3 authorization date in DE 15
- Preauth3 SSN in DE 63
- Preauth2 SSN in DE 48 subelement 59

# 2.10 Multiple Clearing or Multiple Completion Messages

# 2.10.2 Maestro Transactions

An Acquirer of a Maestro Merchant located in Brazil that processes a Maestro Card-not-present Transaction involving a debit Card issued in Brazil has the option to submit one or more linked completion messages within a period of seven days from the settlement date.

# Acquirer Requirements

1. At the time of the Cardholder's purchase of goods or services, an Acquirer that supports this processing option must populate the following values in the Financial Transaction Request/0200: multiple completion message.

|Field|Value|
|---|---|
|DE 4 (Amount, Transaction)|The total purchase amount|
|DE 61 (Point of Service [POS] Data), subfield 7 (POS Transaction Status)|4 (Preauthorization Request)|
|DE 61, subfield 12 (POS Authorization Life Cycle)|07 (Partial completion processing supported)|

2. Within seven days of the date contained in DE 15 (Date, Settlement) of the Financial Transaction Request Response/0210: multiple completion message, the Acquirer may submit either one or several Financial Transaction Advice/0220: multiple completion messages. Each completion message must contain the following values.


# Authorization and Clearing Requirements

# 2.10.2 Maestro Transactions

|Field|Value|
|---|---|
|DE 4 (Amount, Transaction)|The Transaction amount being fulfilled with this completion message; which may be all or a portion of the total purchase amount|
|DE 15 (Date, Settlement)|The same value received in DE 15 of the Financial Transaction Request Response/0210: multiple completion message|
|DE 60 (Advice Reason Code), subfield 1 (Advice Reason Code)|290 (APS approved transaction; preauthorized by issuer)|
| |– 1403 (Previously approved authorization: partial amount, multiple completions)|
| |– 1404 (Previously approved authorization: partial amount, final completion)|
|DE 61, subfield 7 (POS Transaction Status)|4 (Preauthorization request)|
|DE 61, subfield 12 (POS Authorization Life Cycle)|07 (Partial completion processing supported)|

# Issuer Requirements

Upon receiving a Financial Transaction Advice/0220: multiple completion message containing a value of 1403 or 1404, the Issuer should:

1. Match the completion message to the original Financial Transaction Request/0200 message by comparing the data contained in DE 48, subelement 59 (Original Switch Serial Number) to the original Switch Serial Number (SSN) in the original 0210: multiple completion message from DE 63 (Network Data); and
2. Adjust any hold on the availability of funds in the Cardholder's Account in accordance with its standard Account management practice. In any event, the Issuer should release any remaining unused amount still held after seven days from the settlement date of the Financial Transaction Request/0200: multiple completion message.

# If the completion message contains a value of…

Then the Issuer is advised to…

|Value|Advice|
|---|---|
|1403|Reduce the hold placed on the Cardholder's Account in connection with the approved Financial Transaction Advice/0220: multiple completion message by the amount in DE 4 (Amount, Transaction).|
|1404|Release any unused funds in connection with the approved Financial Transaction Request/0200: multiple completion message.|


# Authorization and Clearing Requirements

# 2.16 CVC 3 Verification for Maestro Magnetic Stripe Mode Contactless—Brazil Only

In Brazil, for each Maestro Magnetic Stripe Mode Contactless Transaction, the Issuer must verify the dynamic CVC 3 value in the authorization request and provide the result in the response message.

# Middle East/Africa Region

The following modifications to the Rules apply in the Middle East/Africa Region or in a particular Region country or countries. Refer to Appendix A for the Middle East/Africa Region geographic listing.

# 2.1 Acquirer Authorization Requirements

In the Middle East/Africa Region, the Rule on this subject is modified as follows. An Acquirer must ensure that any authorization request for an amount greater than zero is identified as either a preauthorization or as a final authorization.

# 2.7 Final Authorizations

In the Middle East/Africa Region, the Acquirer must ensure that any authorization request is identified as a final authorization only if:

- The Transaction may no longer be cancelled and must not be reversed after the authorization request is approved in full by the Issuer, except upon Cardholder request or when non-completion is unavoidable for technical reasons such as telecommunications failure or POS Terminal failure; and
- The authorization being requested is for the final Transaction amount.

# 2.12 Full and Partial Approvals

In the Middle East/Africa Region, the Rule on this subject is modified as follows. An Issuer and an Acquirer in Jordan or South Africa is not required to support partial approval.

# 2.21 Merchant Payment Gateway Identifier (MPG ID)

The Rule on this subject does not apply in the following countries: Jordan, Nigeria and Pakistan.

# United States Region

The following modifications to the Rules apply in the United States (U.S.) Region. Refer to Appendix A for the U.S. Region geographic listing.


# Authorization and Clearing Requirements

# 2.1 Acquirer Authorization Requirements

In the U.S. Region, the Rule on this subject is modified as follows. An Acquirer must support POS balance inquiry for all prepaid Debit Mastercard and prepaid Maestro Accounts.

# 2.1.1 Acquirer Host System Requirements

An Acquirer in the U.S. Region must ensure that its POS Terminal host systems and those of its Service Providers:

1. Are capable of processing Contact Chip Transactions and Contactless Transactions (including both EMV Mode Contactless Transactions and Magnetic Stripe Mode Contactless Transactions);
2. Support the transmission of Contact Chip Transaction and Contactless Transaction messages in accordance with the Standards;
3. Support all valid CVM options for Chip Transactions, including but not limited to PIN (both offline and online), regardless of whether each Hybrid POS Terminal connected to the Acquirer host system supports all of these options;
4. Support all mandatory and applicable conditional data subelements within DE 55 (Integrated Circuit Card [ICC] System-Related Data); and
5. Have been approved by the Corporation, with respect to each Interchange System network interface, as enabled for Contact Chip Transaction and Contactless Transaction processing.

# 2.2 Issuer Authorization Requirements

In the U.S. Region, the Rule on this subject is modified as follows. A Maestro Card Issuer must also support:

- Partial approval from primary account, checking account, savings account, and pooled account;
- Full and partial reversal;
- POS balance response for prepaid Accounts.

Each Maestro and Cirrus Card Issuer must offer cash withdrawal from a savings account and from a checking account, and may optionally offer Shared Deposit to a savings account and to a checking account. An Issuer may decline authorization of a Transaction when technical fallback from chip to magnetic stripe occurred.

# 2.2.1 Issuer Host System Requirements

In the U.S. Region, the Rule on this subject is modified as follows. A Maestro Card Issuer’s host system interfaces must support POS balance inquiry.

# 2.2.2 Stand-In Processing Service

In the U.S. Region, the following requirements apply with respect to Mastercard Card Programs.


# Authorization and Clearing Requirements

# 2.2.2 Stand-In Processing Service

For all Mastercard Card Programs, an Issuer must use the Stand-In Processing Service. For all Mastercard Card Programs except Debit Mastercard Card Programs, Stand-In Parameters must be set at or above the Corporation’s default limits.

In the event that fraudulent activity is detected with respect to a BIN or BIN range, the Corporation, in its sole discretion and judgment, may take such action as the Corporation deems necessary or appropriate to safeguard the goodwill and reputation of the Corporation’s Marks. Such action may include, by way of example and not limitation, declining some or all Transaction authorization requests received by the Stand-in Processing Service relating to the use of Cards issued under such BIN or BIN range.

For Debit Mastercard Card Programs, the following requirements apply:

1. For all Transactions identified with a TCC of C, P, T, U, or Z, the Transaction category code (TCC) limit may be set below the Corporation’s default value.
2. For all Card-not-present Transactions, the TCC limit may be set below the Corporation’s default value.
3. For Card-present Transactions identified with a TCC of A, F, H, O, R, or X and effected with a Debit Mastercard Card (standard), the TCC limit may be set below the Corporation’s default value to an amount no less than USD 50.
4. For Card-present Transactions identified with a TCC of A, F, H, O, R, or X and effected with a Debit Mastercard Card (enhanced), the TCC limit may be set below the Corporation’s default value to an amount no less than USD 100.
5. For Card-present Transactions identified with a TCC of A, C, F, H, O, R, or X and effected with a Debit Mastercard BusinessCard Card or Debit Mastercard Professional Card, the TCC limit may be set below the Corporation’s default value to an amount no less than USD 400.
6. For Debit Mastercard Card (standard) Programs, the accumulative limits may be set below the Corporation’s default values as follows.

|Day|Minimum Transaction Count|Recommended Transaction Count|Minimum Transaction Amount|
|---|---|---|---|
|1|4|6|USD 50|
|2|6|12|USD 100|
|3|6|18|USD 150|
|4|6|24|USD 200|

7. For Debit Mastercard Card (enhanced) Programs, the accumulative limits may be set below the Corporation’s default values as follows.

|Day|Minimum Transaction Count|Recommended Transaction Count|Minimum Transaction Amount|
|---|---|---|---|
|1|4|6|USD 100|
|2|6|12|USD 200|


# Authorization and Clearing Requirements

# 2.4 Performance Standards

|Day|Minimum Transaction Count|Recommended Transaction Count|Minimum Transaction Amount|
|---|---|---|---|
|3|6|18|USD 300|
|4|6|24|USD 400|

8. For Debit Mastercard BusinessCard Card and Debit Mastercard Professional Card Programs, the accumulative Limits may be set below the Corporation’s default values as follows.

|Day|Minimum Transaction Count|Recommended Transaction Count|Minimum Transaction Amount|
|---|---|---|---|
|1|4|4|USD 750|
|2|6|6|USD 1,000|
|3|6|6|USD 1,000|
|4|6|6|USD 1,000|

# 2.4 Performance Standards

# 2.4.2 Performance Standards—Issuer Requirements

In the U.S. Region, the Rule on this subject is replaced with the following. An Issuer authorization failure rate for Maestro POS Transactions and ATM Transactions that exceeds two percent (2%) in any given calendar month is deemed to be substandard performance. The Issuer failure rate is not applied until after the Issuer’s fourth calendar month of operation or upon the Issuer’s processing of 5,000 Transactions in a calendar month, whichever occurs first. Refer to “Calculation of the Issuer Failure Rate” in this chapter for the formula used to calculate the Issuer authorization failure rate.

# 2.5 Preauthorizations

# 2.5.2 Preauthorizations—Maestro POS Transactions

In the U.S. Region, the Rule on this subject is modified as follows. The Acquirer is not liable for preauthorization completions that occurred within 20 minutes of the initial Maestro POS Transaction but were subsequently stored and forwarded because of technical problems between the Acquirer and the Interchange System, or the Interchange System and the Issuer. No CVM is required for a PIN-less Single Message Transaction preauthorization.


# Authorization and Clearing Requirements

# 2.11 Full and Partial Reversals

# 2.11.1 Full and Partial Reversals—Acquirer Requirements

In the U.S. Region, the Rule on this subject is modified as follows. An Acquirer must ensure that a Merchant accepting Debit Mastercard Cards supports full and partial reversals performed at the POI and whenever, for technical reasons, the Acquirer is unable to communicate the authorization response to the Merchant. This requirement applies with respect to all MCCs for which the Acquirer is required to support partial approvals, as listed in Rule 2.12.

# 2.11.2 Full and Partial Reversals—Issuer Requirements

In the U.S. Region, the Rule on this subject is modified as follows. For all Debit Mastercard Card Account ranges, an Issuer must support full and partial reversals.

# 2.13 Refund Transactions and Corrections

# 2.13.1 Refund Transactions - Acquirer Requirements

In the United States Region, the requirement for an Acquirer to perform online authorization for refund Transactions acquired through the Dual Message System does not apply.

# 2.14 Balance Inquiries

In the U.S. Region, the Rule on this subject is modified as follows. The Acquirer must ensure that a balance inquiry is initiated through the use of a PIN and a magnetic stripe reader and is performed only at Cardholder-operated Terminals.

# 2.18 Transaction Queries, Disputes, and Errors

In the U.S. Region, the Rule on this subject is modified as follows. The Acquirer of a U.S. Region Merchant participating in the substantiation of certain tax-qualified purchases (for example, medical-related, prescription drug, and vision care purchases) must be prepared to respond to an Issuer’s request for the retrieval of documentation for a Transaction effected with an eligible U.S. Region-issued Card. The Acquirer must provide the requested documentation within 30 calendar days of the Central Site Business Date of the Issuer’s request.

# Additional U.S. Region and U.S. Territory Rules

The following variations and additions to the Rules apply in the United States Region and in American Samoa, Guam, Northern Mariana Islands, Puerto Rico, and the U.S. Virgin Islands (herein, "the U.S. Territories"). These Rules apply in addition to any that apply within the Asia/Pacific Region, with respect to Customers located in American Samoa, Guam, and Northern Mariana Islands; the Latin America.


# Authorization and Clearing Requirements

# 2.2 Issuer Authorization Requirements

and the Caribbean Region, with respect to Customers located in Puerto Rico and the U.S. Virgin Islands; and the United States Region, with respect to U.S. Region Customers.

# 2.2.2 Stand-In Processing Service

In the U.S. Region and U.S. Territories, the following additional requirements apply. An Issuer must use the Stand-In Processing Service for all of its debit cards that provide Maestro functionality. The Stand-In Parameters may be set below the Corporation's default TCC limit for Non-Mastercard BIN Maestro card-not-present debit card Transactions. In the event that fraudulent activity is detected, the Corporation, in its sole discretion and judgment, may take such action as the Corporation deems necessary or appropriate to safeguard the goodwill and reputation of the Corporation's Marks. Such action may include, by way of example and not limitation, declining some or all Transaction authorization requests received by the Stand-in Processing Service relating to Non-Mastercard BIN Maestro card-not-present debit card Transactions.

# 2.5 Preauthorizations

# 2.5.2 Preauthorizations—Maestro POS Transactions

In the U.S. Region and U.S. Territories, the Rule on this subject is modified as follows. Each Maestro card-not-present (CNP) POS Transaction preauthorization initiated with a Non-Mastercard BIN Maestro card-not-present (CNP) debit card is valid for a period of seven (7) calendar days from the preauthorization approval date, when the preauthorization request message contains a value of 07 in DE 61, subfield 12 (POS Authorization Life Cycle). Additional preauthorization requests may be submitted to extend the validity period or increase the authorized amount, as described in Rule 2.9 Multiple Authorizations of this Additional U.S. Region and U.S. Territories section. The Authorization-related Chargeback described in Chapter 4 Single Message System Chargebacks for Non-Mastercard BIN Maestro Card-Not-Present (CNP) Debit Transactions of the Chargeback Guide may apply if the Transaction amount in the preauthorization completion message was not fully authorized.

# 2.9 Multiple Authorizations

In the U.S. Region and U.S. Territories, the Rule on this subject is modified as follows with respect to Maestro card-not-present (CNP) POS Transactions effected with Non-Mastercard BIN Maestro card-not-present (CNP) debit cards. Following Issuer approval of the initial preauthorization request, a Merchant may submit one or more additional preauthorization requests for the same card-not-present (CNP) Maestro POS Transaction, subject to the following conditions:


# Authorization and Clearing Requirements

# 2.9 Multiple Authorizations

1. The original and each additional preauthorization request for the same Transaction is valid for a period of seven (7) calendar days from the authorization approval date, when the preauthorization request message contains a value of 07 in DE 61, subfield 12 (POS Authorization Life Cycle).

2. Each additional approved preauthorization:

a. If submitted for a zero amount, extends the authorization validity period with no change to the total authorized Transaction amount.

b. If submitted for a non-zero amount, both extends the authorization validity period and incrementally increases the total authorized Transaction amount.

3. If an additional preauthorization request is declined, then the most recent previously approved preauthorization remains valid. For example, if the Issuer approved the original USD 100 preauthorization request on 1 June and declined an additional USD 25 preauthorization request on 7 June, then the Transaction must be completed by 8 June (when the original preauthorization expires) for USD 100 (the original approved amount).

4. If any preauthorization request expires before the Transaction completion message is sent, then the Merchant or Acquirer must initiate a new original preauthorization request for the Transaction.

The processing of multiple preauthorization requests for the same Maestro POS Transaction must occur as follows.

Preauthorization message (0200/0210)
Preauth1 (original preauthorization message)
Preauth2 (first additional preauthorization message for the same Transaction)

# The Mastercard Network

The Acquirer provides:

- In DE 4 (Amount, Transaction), the original preauthorization request amount
- In DE 4, the additional amount being authorized, or a zero amount (to extend the authorization validity without increasing the authorized amount)
- In DE 15 and DE 63, the same values as received in the Preauth1 0210 message
- In DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID]), the same value as received in the Preauth1 0210 message

populates:

- The authorization date in DE 15 (Date, Settlement) and the switch serial number [SSN] in DE 63 (Network Data)
- Preauth2 authorization date in DE 15
- Preauth2 SSN in DE 63
- Preauth1 SSN in DE 48, subelement 59 (Original Switch Serial Number)
- In DE 54 (Amounts, Additional), subfield 2 (Amount Type), the value of 92 and in subfield 5 (Amount), the total cumulative previously authorized and currently requested amount


# Authorization and Clearing Requirements

# 2.10 Multiple Clearing and Multiple Completion Messages

# Preauthorization message

(0200/0210) The Acquirer provides:

- In DE 4, the additional amount being authorized, or a zero amount
- In DE 15 and DE 63, the same values as received in the Preauth2 0210 message
- In DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID]), the same value as received in the Preauth2 0210 message

The Mastercard Network populates:

- Preauth3 authorization date in DE 15
- Preauth3 SSN in DE 63
- Preauth1 SSN in DE 48, subelement 59
- In DE 54, subfield 2, the value of 92 and in subfield 5, the total cumulative previously authorized and currently requested amount

The Authorization-related Chargeback described in Chapter 4 Single Message System Chargebacks for Non-Mastercard BIN Maestro Card-Not-Present (CNP) Debit Transactions of the Chargeback Guide may apply if the Transaction amount in the preauthorization completion message was not fully authorized.

# 2.10 Multiple Clearing and Multiple Completion Messages

# 2.10.2 Maestro Transactions

An Acquirer of a Maestro Merchant located in the U.S. Region or U.S. Territories that processes a Maestro "back of card" (non-Mastercard BIN) card-not-present Transaction involving a debit card issued in the U.S. Region or U.S. Territories has the option to submit one or more linked completion messages within a period of seven days from the settlement date.

# Acquirer Requirements

1. An Acquirer that supports this processing option must populate the following values in the Financial Transaction Request/0200 message initiated at the time of the Cardholder's purchase of goods or services.

|Field|Value|
|---|---|
|DE 4 (Amount, Transaction)|The total purchase amount|
|DE 61 (Point of Service [POS] Data), subfield 7 (POS Transaction Status)|4 (Preauthorization Request)|


# Authorization and Clearing Requirements

# 2.10.2 Maestro Transactions

|Field|Value|
|---|---|
|DE 61, subfield 12 (POS Authorization Life Cycle)|07|

2. Within seven days of the date contained in DE 15 (Date, Settlement) of the Financial Transaction Request Response/0210 message, the Acquirer may submit either one or several Financial Transaction Advice/0220 completion messages. Each completion message must contain the following data.

# Table 4: Financial Transaction Advice/0220 completion message(s)

|Field|Value|
|---|---|
|DE 4 (Amount, Transaction)|The Transaction amount being fulfilled with this completion message, which may be all or a portion of the total purchase amount|
|DE 15 (Date, Settlement)|The same value received in DE 15 of the Financial Transaction Request Response/0210 message|
|DE 60 (Advice Reason Code), subfield 1 (Advice Reason Code)|290 (APS approved transaction; preauthorized by issuer)|
|DE 60, subfield 2 (Advice Reason Detail Code)|One of the following: – 1403 (Previously approved authorization - partial amount, multiple completions) – 1404 (Previously approved authorization - partial amount, final completion)|
|DE 61, subfield 7 (POS Transaction Status)|4 (Preauthorization request)|
|DE 61, subfield 12 (POS Authorization Life Cycle)|07|
|DE 105 (Multi-Use Transaction Identification Data), subelement 001 (Transaction Link Identifier [TLID])|Effective 17 October 2025, the same value received in DE 105, subelement 001 of the Financial Transaction Request Response/0210 message|

# Issuer Requirements

Upon receiving a Financial Transaction Advice/0220 completion message containing a value of 1403 or 1404, the Issuer should:

1. Match the completion message to the original Financial Transaction Request/0200 message by comparing the data contained in DE 48, subelement 59 (Original Switch Serial Number) to the original Switch Serial Number (SSN) in the original 0200 message from DE 63 (Network Data) and effective 17 October 2025, the data contained in DE 105, subelement.


# Authorization and Clearing Requirements

# 2.10.2 Maestro Transactions

001 (Transaction Link Identifier [TLID]) to the DE 105, subelement 001 value in the original 0200 message.

2. Adjust any hold on the availability of funds in the Cardholder's Account in accordance with its standard Account management practice. In any event, the Issuer should release any remaining unused amount still held after seven days from the settlement date of the Financial Transaction Request/0200 message.

|If the completion message contains a value of...|Then the Issuer is advised to...|
|---|---|
|1403|Reduce the hold placed on the Cardholder's Account in connection with the approved Financial Transaction Advice/0220 message by the amount in DE 4 (Amount, Transaction)|
|1404|Release any unused funds in connection with the approved Financial Transaction Request/0200 message.|