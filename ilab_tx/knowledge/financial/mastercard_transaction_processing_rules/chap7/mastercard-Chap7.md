# Terminal Requirements

# 7.1 Terminal Eligibility

The following types of terminals, when compliant with the applicable technical requirements and other Standards, are eligible to be Terminals:

1. Any ATM Terminal or Bank Branch Terminal that is owned, operated or controlled by a Customer;
2. Any ATM Terminal that is owned, operated or controlled by an entity that is ineligible to be a Customer, provided that such ATM Terminal is connected to the Interchange System by a Principal or Affiliate;
3. Any POS Terminal (including an MPOS Terminal) that is owned, operated or controlled by a Merchant and is in the Merchant’s physical possession, provided that such POS Terminal is connected to the Interchange System by a Principal or Association;
4. Any other type of terminal which the Corporation may authorize.

A terminal that dispenses scrip is ineligible to be a Terminal.

NOTE: A modification to this Rule appears in the “Europe Region” section at the end of this chapter.

# 7.2 Terminal Requirements

Each Terminal must:

1. Have an online connection to the Acquirer host system for the authorization of Transactions, except where offline-only processing is specifically permitted by the Standards. If online PIN is a supported CVM, the Terminal must be able to encrypt PINs at the point of entry and send them to the Acquirer host system in encrypted form in accordance with the PIN security Standards;
2. Accept any Card that conforms with the encoding Standards, including but not limited to the acceptance of all valid PAN lengths, major industry identifier numbers and BINs/IINs, effective and expiration dates, chip application effective dates, service code values, and characters encoded in the discretionary data;
3. Support all required Transaction types and valid Transactions in accordance with the Standards;
4. Have a magnetic stripe reader capable of reading Track 2 data encoded on the magnetic stripe of a Card, and transmit all such data for authorization;
5. Not perform tests or edits on Track 1 data for the purpose of disqualifying Cards from eligibility for Interchange System processing;
6. For magnetic stripe Transactions, perform a check (either at the Terminal or in the Acquirer host system) of the track layout, limited to the start sentinel, separator, end sentinel, and Longitudinal Redundancy Check (LRC), to ensure that the Card conforms to the technical specifications set forth in Appendix A of the Security Rules and Procedures manual. If an LRC error occurs or the track data cannot be interpreted correctly or verified, the Transaction must not be processed or recorded;


# Terminal Requirements

# 7.2.1 Terminal Function Keys for PIN Entry

7. Prevent additional Transactions from being entered into the system while a Transaction is being processed.

A Cardholder-facing or unattended Terminal additionally must:

1. Ensure privacy of PIN entry to the Cardholder (where PIN processing is required and/or supported);
2. Provide Cardholder operating instructions in English as well as the local language, as selected by the Cardholder. Two or more languages may be displayed simultaneously. In the Europe Region, operating instructions in French and German must also be available whenever technically feasible, and Spanish and Italian are recommended;
3. Have a screen that clearly displays to the Cardholder:
1. The Transaction amount;
2. Any Transaction data entered into the Terminal by the Cardholder; and
3. The response received as the result of the Cardholder’s Transaction request, including the application labels or preferred names on a multi-application Card.

Refer to the Security Rules and Procedures for additional requirements related to Terminal security, PIN processing, and use of service codes. Refer to Rule 3.9 for requirements relating to Terminal-generated Transaction receipts, including truncation of the primary account number (PAN).

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region" and "Europe Region" sections at the end of this chapter.

# 7.2.1 Terminal Function Keys for PIN Entry

A PIN-capable Terminal must have a numeric keyboard to enable the entry of PINs, with an ‘enter key’ function to indicate the completion of entry of a variable length PIN.

In all Regions except the Canada and United States Regions, a Terminal’s PIN entry device (PED) or encrypting PIN pad (EPP) must accept PINs having four to six numeric characters. In the Canada and United States Regions, each PED and EPP must support PINs of up to 12 alphanumeric characters. It is recommended that all PEDs and EPPs support the input of PINs in letter-number combinations as follows:

|1|Q, Z|6|M, N, O|
|---|---|---|---|
|2|A, B, C|7|P, R, S|
|3|D, E, F|8|T, U, V|
|4|G, H, I|9|W, X, Y|
|5|J, K, L| | |

The support of the following PED function keys is recommended:
# Terminal Requirements

# 7.2.2 Terminal Responses

1. A key used to restart the process of PIN entry or entry of the Transaction amount. The preferred color is yellow, and the preferred label is CORR or CANCEL.
2. A key used to complete the process of PIN entry or entry of the Transaction amount. The preferred color is green, and the preferred label is OK.
3. A key used to terminate a Transaction. The preferred color is red, and the preferred label is STOP or CANCEL. In the Europe Region, this key is mandatory. The key must allow the Cardholder to cancel a Transaction prior to the final step that results in the submission of an authorization request.

# 7.2.2 Terminal Responses

A Terminal must be able to display or print the response required in the applicable technical specifications. The Acquirer or Merchant must provide an appropriate message to the Cardholder whenever the attempted Transaction is rejected, either with a specific reason or by referring the Cardholder to the Issuer.

# 7.2.3 Terminal Transaction Log

The Acquirer must maintain a Terminal Transaction log. The log must include, at a minimum, the same information provided on the Cardholder receipt, including the Card sequence number, if present. The log must include the full PAN, unless otherwise supported by supplementary reported data, and must not include the PIN or any discretionary data from the Card’s magnetic stripe or chip. Only the data necessary for research should be recorded. An Issuer may request a copy of this information.

The Terminal must not electronically record a Card’s full magnetic stripe or chip data for the purpose of allowing or enabling subsequent authorization requests, after the initial authorization attempt. The only exception to this Rule is for Merchant-approved Maestro POS Transactions, which may be logged until either the Transaction is authorized or the end of the 13-day period during which the Merchant may make attempts to obtain an authorization pursuant to the Standards, whichever occurs first.

When an attempted Transaction is rejected, an indication or reason for the rejection must be included on the Terminal Transaction log.

# 7.2.4 Contactless-enabled Terminals and Contactless Reader Requirements

For purposes of this chapter, “contactless-enabled” means a Terminal with a contactless reader that is activated and that accepts Cards and Access Devices based on contactless chip technology (“EMV Mode”) and optionally magnetic stripe technology (“Magnetic Stripe Mode”). The reader of a contactless-enabled Terminal must:

- Comply with Mastercard Contactless Reader Specification Version 3.0 (MCL 3.0) or EMV CL Book C-2; and
- For POS Terminals only (including MPOS Terminals), be configured to support Consumer Device Cardholder Verification Method (CDCVM) and the processing of Contactless Transactions that exceed the applicable Cardholder verification method (CVM) limit amount up to the amount that the same POS Terminal supports on its contact interface.



248
# Terminal Requirements

# 7.3 POS Terminal Requirements

Support of CDCVM is required only for Transactions that exceed the CVM limit.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# 7.3 POS Terminal Requirements

Each POS Terminal must comply with Rule 7.2, except contactless-only POS Terminals as described below and Mastercard Consumer-Presented QR-only POS Terminals. Each Merchant is responsible for the maintenance arrangements of its POS Terminals, unless the Acquirer undertakes this function.

For unattended POS Terminal requirements, refer to Rule 4.11. An unattended POS Terminal that accepts Mastercard Cards must comply with the Cardholder-Activated Terminal (CAT) requirements set forth in Appendix D.

All POS Terminals must be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality. This requirement includes CATs and excludes contactless-only acceptance as described in Rule 4.7 of this manual.

NOTE: Modifications to this Rule appear in the “Asia/Pacific Region,” “Canada Region,” “Europe Region,” and “United States Region” sections at the end of this chapter.

# 7.3.1 Contactless–enabled POS Terminals

A contactless-enabled POS Terminal must comply with the following.

|If the contact interface of the POS Terminal…|Supports online PIN|
|---|---|
|Then for Transactions exceeding the CVM limit ("high-value Transactions"), the contactless interface of the POS Terminal…|- Must support both online PIN and CDCVM; and
- If Mastercard is accepted, must support signature CVM. Signature collection is optional.
|
|Does not support online PIN|1. A high-value Transaction can only occur when a Mobile Payment Device is used and CDCVM was successful. For this configuration, CDCVM is the only CVM supported.
2. A high-value Transaction can occur with signature CVM when Mastercard is accepted, and may also be able to occur when a Mobile Payment Device is used and CDCVM was successful. For this configuration, both signature CVM and CDCVM must be supported. Signature collection is optional.
|



249
# Terminal Requirements

# 7.3.2 Contactless-only POS Terminals

Mastercard Rule 5.12.3, "Minimum/Maximum Transaction Amount Prohibited" applies to both the contact and contactless payment functionalities of a Dual Interface POS Terminal (whether attended or unattended).

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," "Canada Region," "Middle East/Africa Region," "Europe Region," "Latin America and the Caribbean Region," and "United States Region" sections at the end of this chapter.

# 7.3.2 Contactless-only POS Terminals

A POS Terminal that utilizes only contactless payment functionality, as permitted in accordance with Rule 4.7, must comply with all of the requirements set forth in Rule 7.3 except those applicable to contact magnetic stripe or chip functionality. In addition, such a POS Terminal must:

1. Request a cryptogram for all Contactless Transactions, and if the Transaction is approved, transmit an application cryptogram and related data;
2. If Cards and Access Devices with contactless chip payment functionality are accepted, support both online and offline authorization.
3. Support online PIN, if required for contactless-enabled POS Terminals in the Merchant’s Region or country.

# 7.4 Mobile POS (MPOS) Terminal Requirements

Any Merchant and any Customer or cash disbursement agent conducting Manual Cash Disbursement Transactions may use a Mobile POS (MPOS) Terminal that complies with the POS Terminal Standards.

Any Merchant may use an MPOS Terminal that cannot print a paper Transaction receipt at the time the Transaction is conducted, provided the Merchant has a means by which to provide a receipt to the Cardholder upon request (for example, in an email or text message).

Only a Merchant with less than USD 100,000 in annual Mastercard POS Transaction Volume may use an MPOS Terminal with any of the following characteristics, for Mastercard POS Transaction processing only:

1. Has a contact chip reader and magnetic stripe-reading capability but does not support PIN as a CVM for Contact Chip Transactions; or
2. Is a Chip-only MPOS Terminal.

All MPOS Terminals (including Chip-only MPOS Terminals) must be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality. This requirement applies regardless of Merchant Transaction Volume and excludes contactless-only acceptance as described in Rule 4.7.

NOTE: A modification to this provision of the Rule appears in the "Asia/Pacific Region" section at the end of this chapter.



250
# Terminal Requirements

# 7.4 Mobile POS (MPOS) Terminal Requirements

# MPOS Terminal Identification

All authorization and clearing messages for Transactions occurring at an MPOS Terminal must contain the MPOS acceptance device indicator, as follows:

- A value of 9 in DE 61 (Point-of-Service Data), subfield 10 (Cardholder-Activated Terminal Level) of the Authorization Request/0100 or Financial Transaction Request/0200 message; and
- A value of CT9 in PDS 0023 (Terminal Type) of the First Presentment/1240 message.

PIN verification, if supported by an MPOS Terminal, must be conducted by means of a PIN entry device (PED) that complies with section 4.10 of the Security Rules and Procedures manual. A Chip Transaction that occurs at an MPOS Terminal must be authorized online by the Issuer, resulting in the generation of a unique Authorization Request Cryptogram (ARQC).

# Chip-only MPOS Terminal Identification

A Chip-only MPOS Terminal must use the following values:

- A value of 9 in DE 61 (Point-of-Service Data), Subfield 11 (POS Card Data Terminal Input Capability Indicator) in the Authorization Request/0100 or Financial Transaction Request/0200 message, as described in the Customer Interface Specification and Single Message System Specifications manuals; and
- A value of E in DE 22 (Point of Service Data Code), Subfield 1 (Terminal Data: Card Data Input Capability) of the First Presentment/1240 message, as described in the IPM Clearing Formats manual.

A software-based Chip-only MPOS Terminal must use the following values:

- In the Authorization Request/0100 or Financial Transaction Request/0200 message, a value of:
- 2 (Terminal does not have PIN entry capability) or 3 (MPOS Software-based PIN Entry Capability) in DE 22 (Point of Service Data Code), Subfield 2 (POS Terminal PIN Entry Mode)
- 0 (Dedicated MPOS Terminal with PCI compliant dongle [with or without key pad]) or 1 (Off the Shelf Mobile Device) in DE 48 (Additional Data—Private Use), subelement 21 (Acceptance Data), subfield 1 (MPOS Acceptance Device Type)
- In the First Presentment/1240 message, a value of:
- 2 (Terminal does not have PIN entry capability) or 3 (MPOS Software-based PIN Entry Capability) in DE 22 (Point of Service Data Code), Subfield 2 (Terminal Data: Card Data Input Capability)
- 0 (Dedicated MPOS Terminal with PCI compliant dongle [with or without key pad]) or 1 (Off the Shelf Mobile Device) in PDS 0018 (Acceptance Data), subfield 1 (MPOS Acceptance Device Type)

The Acquirer must comply with the MPOS Terminal requirements set forth in the M/Chip Requirements manual, the EMV chip specifications, and section 4.10 of the Security Rules and Procedures manual.


# Terminal Requirements

# 7.5 ATM Terminal and Bank Branch Terminal Requirements

NOTE: A modification to this Rule appears in the "Asia/Pacific Region," "Canada Region," "Europe Region," and "United States Region" sections at the end of this chapter.

# 7.5 ATM Terminal and Bank Branch Terminal Requirements

In addition to complying with Rule 7.2, each ATM Terminal and Bank Branch Terminal must:

1. Offer cash withdrawals from an Account;
2. Offer balance inquiry functionality to Cardholders, if balance inquiry functionality is offered to cardholders of any other network accepted at that ATM Terminal or Bank Branch Terminal;
3. During Account selection, include the word “Savings” when offering a cash withdrawal or transfer from a savings account, and the word “Checking” or “Chequing” when offering a cash withdrawal or transfer from a checking account;
4. Not automatically generate an online reversal for the full or partial amount of any authorized cash withdrawal or disbursement when the ATM Terminal or Bank Branch Terminal indicates that such Transaction was not completed because the Cardholder failed to collect some or all of the cash dispensed;
5. Have an online connection to the Acquirer host system;
6. Encrypt the PIN at the point of entry and send the PIN to the Acquirer host system in encrypted form, in accordance with the PIN security Standards;
7. Process each Transaction in the currency dispensed by the Terminal during that Transaction. Terminals may process Transactions in other currencies only if done in accordance with “POI Currency Conversion” in Chapter 3, except that a withdrawal of foreign currency may be processed in the issuing currency of the Card if it is the same as the currency of the country where the Terminal is located. The amount of currency dispensed, Transaction amount, and conversion rate must be shown on the screen before the Cardholder completes the Transaction and must also be included on the Transaction receipt.

Both single-line and multi-line screens that have a screen width of at least 16 characters are acceptable. A minimum screen width of 40 characters is recommended.

An ATM Terminal or Bank Branch Terminal also:

1. May offer Merchandise Transactions from no account specified; and
2. May offer MoneySend Payment Transactions.

Refer to Chapter 4 of the Security Rules and Procedures manual for PIN entry device and PIN security requirements.

NOTE: Additions and/or variations to this Rule appear in the “Asia/Pacific Region,” “Canada Region,” “Europe Region,” and “United States Region” sections at the end of this chapter.



252
# Terminal Requirements

# 7.5.1 ATM Terminals

In addition to complying with Rule 7.5, an ATM Terminal must permit the Cardholder to obtain the equivalent of USD 100 in the currency in use at the ATM Terminal per Transaction, subject to authorization of the Transaction by the Issuer. Refer to Chapter 4 for additional requirements.

# 7.5.2 Bank Branch Terminals

In addition to complying with Rule 7.5, a Bank Branch Terminal must:

1. Be approved in writing by the Corporation to have access to the Interchange System;
2. With respect to Maestro and Cirrus acceptance, accept all Maestro and Cirrus Cards. A bank branch offering the service must display the Maestro and Cirrus Acceptance Marks on the door or window, and at the counter where the service is provided. With respect to Mastercard acceptance, refer to Rule 4.14.4, Mastercard Acceptance Mark Must be Displayed;
3. Clearly describe by Transaction receipt, screen information, or both the action taken in response to a Cardholder's request. It is recommended that the bank branch address also be included on the Transaction receipt;
4. With respect to Maestro and Cirrus acceptance, permit the Cardholder to obtain the equivalent of USD 200 in the currency in use at the Bank Branch Terminal per Transaction, subject to authorization of the Transaction by the Issuer. With respect to Mastercard acceptance, refer to Rule 4.14.2, Maximum Cash Disbursement Amounts. The currency may be dispensed in local currency or another currency, provided the Cardholder is informed of the currency that will be dispensed before the Transaction is performed. The Transaction receipt, if provided, must identify the currency dispensed.

NOTE: Refer to Rule 4.15 for additional Mastercard Manual Cash Disbursement Transaction requirements. An addition to this Rule appears in the "Europe Region" section at the end of this chapter.

# 7.5.3 Contactless-enabled ATM and Bank Branch Terminals

Online PIN must be the only CVM supported for Contactless Transactions effected:

- At a contactless-enabled ATM Terminal with a Mastercard, Maestro, or Cirrus Card or Access Device; or
- At a contactless-enabled Bank Branch Terminal with a Maestro or Cirrus Card or Access Device.

NOTE: Modifications to this Rule appear in the "Canada Region" and "Europe Region" sections at the end of this chapter.


# Terminal Requirements

# 7.6 Hybrid Terminal Requirements

In addition to complying with Rule 7.2, a Hybrid Terminal must:

1. Read required data from the chip when present in Chip Cards, and either transmit or process, as appropriate, all required data for authorization processing. Effective 1 April 2024, this includes when a magnetic stripe is not present on the Chip Card;
2. Complete the Transaction using the EMV chip if present;
3. Read and process EMV-compliant Payment Applications for each of the Corporation’s brands accepted at that location when a Card containing any such Payment Application is presented, if the Hybrid Terminal reads and processes any other EMV-compliant payment application;
4. Request a cryptogram for all chip-read Transactions; if the Transaction is approved, transmit an application cryptogram and related data.

A chip-capable Terminal that does not satisfy all of the requirements to be a Hybrid Terminal is deemed by the Corporation to be a magnetic stripe-only Terminal, and must be identified in Transaction messages as such.

Chip Transactions must be processed in accordance with the M/Chip Requirements for Contact and Contactless manual, the Security Rules and Procedures manual, and other applicable technical specifications. In particular, refer to:

- The Security Rules and Procedures manual for Hybrid Terminal security and PIN processing requirements;
- The M/Chip Requirements for Contact and Contactless manual for technical fallback, Cardholder verification method (CVM) fallback, and Card authentication method (CAM) support requirements;
- The Chargeback Guide for information about Intracountry Transaction and Intraregional Transaction chip liability shifts and the Global Chip Liability Shift Program for Interregional Transactions.

NOTE: Modifications to this Rule appear in the “Asia/Pacific Region,” “Europe Region,” and “United States Region” sections at the end of this chapter.

# 7.6.1 Hybrid POS Terminal Requirements

In addition to complying with Rule 7.6, a Hybrid POS Terminal must:

1. At a minimum, support online authorization.
2. If Maestro Cards are accepted, support both online and offline PIN as the CVM. On a country-by-country basis, Mastercard may permit Acquirers to, at a minimum, support offline PIN as the CVM as outlined in Rule 3.5.
3. Perform Terminal offline chip authorization limit and Card velocity checking. Transactions above the Terminal offline chip authorization limit programmed in the POS Terminal must be routed online to the Issuer, as indicated by the authorization request cryptogram (ARQC).


# Terminal Requirements

# Hybrid POS Terminal and Chip-only MPOS Terminal Displays

1. Support online mutual authentication (OMA) and script processing if connected to a debit acquiring network.
2. If offline Transactions are supported, identify all offline Transactions as such to the Issuer when submitted for clearing and settlement.

A Hybrid POS Terminal is identified in Transaction messages with the following values:

- A value of 3, 5, 8, or 9 in DE 61 (Point-of-Service Data), Subfield 11 (POS Card Data Terminal Input Capability Indicator) in the Authorization Request/0100 or Financial Transaction Request/0200 message, as described in the Customer Interface Specification and Single Message System Specifications manuals; and
- A value of 5, C, D, E, or M in DE 22 (Point of Service Data Code), Subfield 1 (Terminal Data: Card Data Input Capability) of the First Presentment/1240 message, as described in the IPM Clearing Formats manual.

A PIN-capable Hybrid POS Terminal is indicated when in addition, DE 22, Subfield 2 (Terminal Data: Cardholder Authentication Capability), of the First Presentment/1240 message contains a value of 1.

A chip-capable POS Terminal that does not satisfy all of the requirements to be a Hybrid POS Terminal is deemed by the Corporation to be a magnetic stripe-only POS Terminal and must be identified in Transaction messages as such.

NOTE: Additions to this Rule appear in the "Asia/Pacific Region," "Europe Region," and "Middle East/Africa Region" sections at the end of this chapter.

# Hybrid POS Terminal and Chip-only MPOS Terminal Displays

A Hybrid POS Terminal (including any Hybrid MPOS Terminal) and a Chip-only MPOS Terminal must:

1. Display to the Cardholder all mutually supported application labels or preferred names. Multiple matching applications must be displayed in the Issuer’s priority sequence.
2. Allow the Cardholder to select the application to be used when multiple matching applications exist.
3. Display to the Cardholder the Transaction amount and Transaction currency, if different from the Merchant’s or cash disbursement agent’s local currency.

NOTE: A modification to this Rule appears in the "Additional U.S. Region and U.S. Territory Rules" section at the end of this chapter.

# 7.6.2 Hybrid ATM Terminal and Bank Branch Terminal Requirements

In addition to complying with Rule 7.6, each Hybrid ATM Terminal and Hybrid Bank Branch Terminal must:

1. Obtain online authorization from the Issuer for each Transaction, whether the magnetic stripe or the chip of the Card is used to initiate the Transaction. Offline authorization by means of the chip, for a technical or any other reason, is not permitted;


# Terminal Requirements

# 7.7 Mastercard Consumer-Presented QR Functionality

2. Support online PIN as the CVM for all ATM Transactions and for all Manual Cash Disbursement Transactions effected with a Maestro or Cirrus Card;

3. Support full use of the multi-application capabilities of Chip Cards by:

- a. Maintaining a complete list of all Application Identifiers (AIDs) for all products they accept;
- b. Receiving and retaining updates of AIDs for all products they accept;
- c. Attempting to match all AIDs contained in the ATM Terminal or Bank Branch Terminal with those on any EMV-compliant Chip Card used;
- d. Displaying all matching application labels or preferred names to the Cardholder, except when the Standards permit a compatible product or application to take priority;
- e. Allowing the Cardholder to select the application to be used when multiple matching applications exist, except when the Standards permit a compatible product or application to take priority; and
- f. Providing the Cardholder the option of approving or canceling a Merchandise Transaction before the products are dispensed or the services are performed.

NOTE: An addition to this Rule appears in the “Europe Region” section at the end of this chapter.

# 7.7 Mastercard Consumer-Presented QR Functionality

A Terminal may be deployed with Mastercard Consumer-Presented QR payment functionality. For the purpose of this Rule, a "Mastercard Consumer-Presented QR-enabled" Terminal is any attended or unattended POS Terminal (including any MPOS Terminal) with a QR Code reader that is activated and can effect a Transaction through the presentment of a QR Code by the Cardholder and capture of the QR Code by the Merchant to initiate a Transaction.

Mastercard Consumer-Presented QR-enabled POS Terminals must comply with the following:

- • Must support purchase and refund Transactions. The requirement to support refunds using Mastercard Consumer-Presented QR payment is only applicable to attended Terminals.
- • Each Mastercard Consumer-Presented QR Transaction must be sent for online authorization by the Issuer.
- • Terminal CVM processing is not supported for Mastercard Consumer-Presented QR Transactions.
- • Must operate in accordance with the M/Chip Requirements for Contact and Contactless manual and other Terminal-related specifications as provided by Mastercard.

The Acquirer must comply with the Mastercard Consumer-Presented QR Transaction requirements set forth in the M/Chip Requirements for Contact and Contactless manual and the EMV QR Code Specification for Payments Systems-Consumer-Presented Mode specifications.

An Acquirer may sponsor a Merchant that deploys POS Terminals that utilize only Mastercard Consumer-Presented QR functionality with the condition that, should the Merchant accept other forms of payment (e.g., contactless) for competing brands, the Merchant will also accept those forms of payment for Mastercard.


# Terminal Requirements

# Variations and Additions by Region

NOTE: A modification to this Rule appears in the "Canada Region" and "United States Region" sections at the end of this chapter.

# Variations and Additions by Region

The remainder of this chapter provides modifications to the Standards set out in this chapter. The modifications are organized by region or country and by applicable subject title.

# Asia/Pacific Region

The following modifications to the Rules apply in the Asia/Pacific Region or in a particular Region country or countries. Refer to Appendix A for the Asia/Pacific Region geographic listing.

# 7.2 Terminal Requirements

In Australia, the Rule on this subject is modified as follows. For a Debit Mastercard Card Chip Transaction, a Terminal must not display the application label "Credit" or any other term or abbreviation that may be construed to mean or refer to a credit instrument. In accordance with the Standards, the Terminal must display the application preferred name or application label corresponding to the Mastercard-branded Application Identifier (AID).

# 7.3 POS Terminal Requirements

In the Asia/Pacific Region, the Rule on this subject is modified as follows. Effective 1 April 2023, all POS Terminals may be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality. This requirement includes CATs and excludes contactless-only acceptance as described in Rule 4.7.

In Japan, the Rule on this subject is modified as follows. Effective 1 January 2024, all newly deployed POS Terminals must be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality. This requirement includes CATs and excludes contactless-only acceptance as described in Rule 4.7.

In China, the Rule on this subject is modified as follows. All POS Terminals, including CATs and MPOS Terminals and excluding contactless-only acceptance as described in Rule 4.7, may be Dual Interface Hybrid Terminals that support and enable:

- both EMV contact and EMV Mode contactless payment functionality; and
- both PBoC contact and PBoC mode contactless payment functionality for China domestic Transactions.


# Terminal Requirements

# 7.3.1 Contactless-enabled POS Terminals

An attended POS Terminal, including any MPOS Terminal, must support online PIN for all China Domestic Transactions, whether conducted using a magnetic stripe reader, a contact chip reader, or a contactless reader. Refer to Rule 3.4 for requirements relating to the use of PIN for Mastercard magnetic stripe Transactions.

In Indonesia and Republic of Korea, the Rule on this subject is modified as follows. All newly deployed POS Terminals must be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality. This requirement includes CATs, excludes MPOS Terminals, and excludes contactless-only acceptance as described in Rule 4.7.

# 7.3.1 Contactless-enabled POS Terminals

In the Asia/Pacific Region, the Rule on this subject is modified as follows. Except as stated below, a contactless-enabled Terminal may support:

- Contactless magnetic stripe technology ("Magnetic Stripe Mode") only;
- Both contactless magnetic stripe and contactless chip technology ("EMV Mode"); or
- EMV mode only.

Any contactless-enabled POS Terminal submitted to the Corporation for MTIP testing as a new project must only support EMV Mode Contactless Transactions and must not support Magstripe Mode Contactless Transactions.

The following requirements apply to online PIN support on the contact and contactless interface of a Dual Interface POS Terminal and on the contactless interface of a contactless-only POS Terminal:

- In China, all POS Terminals (including MPOS Terminals) that accept China Domestic Transactions must support online PIN. For Cross-border Transactions, online PIN must be enabled in accordance with the below Asia/Pacific Region schedule.
- In all other Asia/Pacific Region countries and territories except Japan, Republic of Korea, and Taiwan:
- Effective 1 April 2023, all contactless-enabled POS Terminals submitted to the Corporation for MTIP testing as a new project must support online PIN.
- Effective 1 April 2024, all newly deployed contactless-enabled POS Terminals must support online PIN.

Support of online PIN is optional at MPOS Terminals, except in China, as stated above.

# 7.4 Mobile POS (MPOS) Terminal Requirements

In the Asia/Pacific Region, the Rule on this subject is modified as follows. Effective 1 April 2023, all MPOS Terminals may be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality.

In Japan, the Rule on this subject is modified as follows.


# Terminal Requirements

# 7.5 ATM Terminal and Bank Branch Terminal Requirements

Effective 1 January 2024, all newly deployed MPOS Terminals must be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality.

In Indonesia and Republic of Korea, the Rule on this subject is modified as follows. All newly deployed MPOS Terminals must be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality. This requirement applies regardless of Merchant Transaction Volume.

# 7.5 ATM Terminal and Bank Branch Terminal Requirements

In the Asia/Pacific Region, the Rule on this subject is modified as follows. An Acquirer must ensure that each of its ATM Terminals and Bank Branch Terminals offer:

1. Cash withdrawals from savings accounts and checking accounts;
2. Cash advances from a credit card; and
3. Balance inquiry for checking accounts, savings accounts, and credit cards.

# 7.6 Hybrid Terminal Requirements

In the Asia/Pacific Region, the Rule on this subject is modified as follows. All new Terminals deployed by Region Customers and capable of accepting Chip Cards (credit or debit) must be EMV-compliant.

For China domestic Transactions, the Rule on this subject is modified as follows. For a Transaction that occurs at a Hybrid Terminal, if the Card also supports Mastercard chip technology, the Transaction must be completed using the chip. Technical fallback to magnetic stripe is not permitted.

# 7.6.1 Hybrid POS Terminal Requirements

In Australia, the Rule on this subject is modified as follows. For a Debit Mastercard Card Chip Transaction, a Hybrid POS and Chip-only MPOS Terminal must not display the application label “Credit” or any other term or abbreviation that may be construed to mean or refer to a credit instrument. In accordance with the Standards, the Terminal must display the application preferred name or application label corresponding to the Mastercard-branded Application Identifier (AID).


# Terminal Requirements

# Canada Region

Canada Region

The following modifications to the Rules apply in the Canada Region. Refer to Appendix A for the Canada Region geographic listing.

# 7.3 POS Terminal Requirements

In the Canada Region, the Rule on this subject is modified as follows. All POS Terminals, including CATs, may be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality.

# 7.3.1 Contactless–enabled POS Terminals

In the Canada Region, the Rule on this subject is modified to add the following: All contactless-enabled POS Terminals, including any contactless-enabled Terminal submitted to the Corporation for MTIP testing as a new project, must only support EMV Mode Contactless Transactions and must not support Magnetic Stripe Mode Contactless Transactions.

All newly-deployed contactless-enabled POS Terminals, including any contactless-enabled POS Terminal submitted to the Corporation for MTIP testing as a new project, must transmit the device type indicator in DE 48, subelement 23 (Payment Initiation Channel), subfield 1 (Device Type) of authorization messages when present in the Card or Access Device used to effect a Transaction. The Acquirer must also include the device type indicator, when present, in PDS 0198 (Device Type Indicator) of First Presentment/1240 messages.

# 7.4 Mobile POS (MPOS) Terminal Requirements

In the Canada Region, the Rule on this subject is modified as follows. All MPOS Terminals may be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality.

# 7.5 ATM Terminal and Bank Branch Terminal Requirements

In the Canada Region, the Rule on this subject is modified as follows. An Acquirer must ensure that each of its ATM Terminals and Bank Branch Terminals:

1. Offer cash withdrawal from a savings and checking (or chequing) accounts;
2. Offer cash advances from a credit card.
3. If offered via a Competing ATM Network, offer balance inquiry to a savings account, checking account, and/or credit card account, and transfers from checking to savings and from savings to checking accounts.
4. If cash withdrawals not requiring account selection are performed, convert the Transaction to a withdrawal from no account specified.

An ATM Terminal or Bank Branch Terminal may offer cash withdrawals from no account specified.



260
# 7.5.3 Contactless-enabled ATM and Bank Branch Terminals

All contactless-enabled ATM and Bank Branch Terminals, including any contactless-enabled Terminal submitted to the Corporation for MTIP testing as a new project, must only support EMV Mode Contactless Transactions and must not support Magnetic Stripe Mode Contactless Transactions.

# 7.7 Mastercard Consumer-Presented QR-enabled POS Terminals

In the Canada Region, the Rule on this subject is modified to add the following: An Acquirer must transmit the device type indicator in DE 48, subelement 23 (Payment Initiation Channel), subfield 1 (Device Type) of the Authorization Request/0100 message when present in the Access Device used to effect a Transaction. The Acquirer must also include the device type indicator when present in PDS 0198 (Device Type Indicator) of the First Presentment/1240 message.

# Europe Region

The following modifications to the Rules apply in the Europe Region or in a particular Region country or countries. Refer to Appendix A for the Europe Region, Non-Single European Payments Area (Non-SEPA) and Single European Payments Area (SEPA) geographic listing.

# 7.1 Terminal Eligibility

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. Terminals may be connected to any switch of the Customer’s choice that is registered with the Corporation.

# 7.2 Terminal Requirements

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A Terminal must not perform tests or edits on Track 1 data for the purpose of disqualifying Cards from eligibility for processing by the registered switch of the Acquirer’s choice.

# 7.2.4 Contactless-enabled Terminals and Contactless Reader Requirements

All contactless-enabled Terminals, including MPOS Terminals, deployed in a Europe Region country must support Mastercard Contactless Reader Specification version 3.0 (MCL 3.0) or above. In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A POS Terminal that is required to support Mastercard Contactless Reader Specification version 3.0 (MCL 3.0) or above pursuant to this Rule must support a level of contactless functionality equivalent to MCL 3.0 or above.


# 7.3 POS Terminal Requirements

The following requirements apply in Greece:

1. A POS Terminal must be configured to require entry of the Transaction amount before the Card or Access Device is swiped, dipped, or tapped.
2. A POS Terminal deployed at a Merchant location where a gratuity may be added (such as a bar, restaurant, hotel, or taxi) must contain an automated prompt to the Cardholder to add the gratuity before the authorization request is submitted. This requirement applies for the addition of a gratuity to all types of Transactions.

The following requirements apply in Hungary:

An Acquirer that has deployed at least 250 POS Terminals in Hungary, or that has at least two percent (2%) of the domestic POS acquiring Volume, must technically support the selection of the different voucher types for government-defined employee benefit programs, such as accommodation, catering, and recreation voucher types, at Merchant locations offering the types of goods and/or services that may be purchased under the employee benefit program. The voucher types apply for prepaid Cards issued under a meal/food voucher product code, such as MRJ. The Volume percentage must be calculated by the Acquirer twice per year on the basis of the Hungarian National Bank half-yearly report.

# 7.3.1 Contactless-enabled POS Terminals

In the Europe Region, the Rule on this subject is modified as follows.

# Contactless Enablement

The Acquirer of a Merchant located in the Europe Region must ensure that all POS Terminals (including MPOS Terminals) are contactless-enabled.

All contactless-enabled POS Terminals must support EMV Mode Contactless Transactions.

All newly deployed contactless-enabled POS Terminals, including any contactless-enabled Terminal submitted to the Corporation for MTIP testing as a new project, must only support EMV Mode Contactless Transactions and must not support Magnetic Stripe Mode Contactless Transactions.

Effective 1 January 2024, all contactless-enabled POS Terminals must only support EMV Mode Contactless Transactions and must not support Magnetic Stripe Mode Contactless Transactions.

The Acquirer of a Merchant located in Italy and identified with one of the following Card acceptor business codes (MCCs) must ensure that all POS Terminals at the Merchant's locations are contactless-enabled.

|MCC|Description|
|---|---|
|5310|Discount Stores|
|5311|Department Stores|


# Terminal Requirements

# 7.3.1 Contactless-enabled POS Terminals

|MCC|Description|
|---|---|
|5411|Grocery Stores, Supermarkets|
|5499|Miscellaneous Food Stores - Convenience Stores, Markets, Specialty Stores|
|5541|Service Stations (with or without Ancillary Services)|
|5651|Family Clothing Stores|
|5661|Shoe Stores|
|5691|Men's and Women's Clothing Stores|
|5699|Accessory and Apparel Stores - Miscellaneous|
|5719|Miscellaneous House Furnishing Specialty Shops|
|5722|Household Appliance Stores|
|5812|Eating Places, Restaurants|
|5813|Bars, Cocktail Lounges, Discotheques, Nightclubs, and Taverns - Drinking Places (Alcoholic Beverages)|
|5814|Fast Food Restaurants|
|5912|Drug Stores, Pharmacies|
|5942|Book Stores|
|5977|Cosmetic Stores|
|7230|Barber and Beauty Shops|
|7523|Automobile Parking Lots and Garages|
|7832|Motion Picture Theaters|

Online PIN Support

POS Terminals deployed in Ireland and the United Kingdom may either support or not support online PIN on the contactless interface.

In Ireland and the United Kingdom, all new POS Terminals that are submitted to the Corporation for M-TIP testing on or after 1 April 2023 must support online PIN on the contactless interface if they support online PIN on the contact interface.

All newly deployed POS Terminals in France must support online PIN on the contactless interface.

Prior to 31 December 2023, POS Terminals deployed in Finland may either support or not support online PIN on the contactless interface.

Effective 1 May 2024, POS Terminals deployed in Israel may either support or not support online PIN on the contactless interface.


# 7.4 Mobile POS (MPOS) Terminal Requirements

In Israel, it is strongly recommended that all new POS Terminals submitted to the Corporation for M-TIP testing on or after 1 May 2024 support online PIN on the contactless interface if the POS Terminal supports online PIN on the contact interface.

# 7.4 Mobile POS (MPOS) Terminal Requirements

In the Europe Region, the Rule on this subject is modified as follows. A Merchant may use an MPOS Terminal that supports only Contact Chip Transactions and Contactless Transactions and does not support magnetic stripe Transactions. The following Rule applies in the EEA, UK and Gibraltar: An MPOS Terminal, including any Chip-only MPOS Terminal, must be identified in authorization and clearing messages as specified by the registered switch of the Customer’s choice.

# 7.5 ATM Terminal and Bank Branch Terminal Requirements

In the Europe Region, the Rule on this subject is modified as follows.

1. Each ATM Terminal and Bank Branch Terminal must be capable of dispensing, without limit per Transaction, the authorized amount requested by the Cardholder unless for technical and/or security considerations/constraints, the amount per Transaction is limited to at least the equivalent of EUR 200 in local currency.
2. Transfers from one account to another and account selection are not currently supported in the Europe Region.
3. It is strongly recommended that an Acquirer in the Europe Region support and offer domestic, inter-European, and intra-European balance inquiry and PIN change and unblock functionality at all of its ATM Terminals. The Acquirer must ensure that the balance amount is not provided by the ATM Terminal before the Cardholder’s PIN has been entered. The recommendation to support PIN change and unblock functionality applies in relation to Chip Cards only. An Acquirer must offer balance inquiry and/or PIN change/unblock functionality to Cardholders if it offers these services to the cardholders of any other network accepted at the ATM Terminal, ensuring equal treatment according to the Card category (for example, debit, credit).
4. Except when a Transaction was not completed because the Cardholder failed to collect some or all of the cash dispensed, the Acquirer must send a reversal or partial reversal within 60 seconds of receiving the authorization response at the Acquirer host system when a Transaction fails to complete.

# 7.5.2 Bank Branch Terminals

In the Europe Region, the Rule on this subject is modified as follows. An Issuer is required to support and an Acquirer may optionally support Transactions effected with a Bank Branch Terminal.


# 7.5.3 Contactless-enabled ATM and Bank Branch Terminals

All contactless-enabled ATM and Bank Branch Terminals must support EMV Mode Contactless Transactions.

All newly-deployed contactless-enabled ATM and Bank Branch Terminals, including any contactless-enabled Terminal submitted to the Corporation for MTIP testing as a new project, must only support EMV Mode Contactless Transactions and must not support Magnetic Stripe Mode Contactless Transactions.

Effective 1 January 2024, all contactless-enabled ATM and Bank Branch Terminals must only support EMV Mode Contactless Transactions and must not support Magnetic Stripe Mode Contactless Transactions.

# 7.6 Hybrid Terminal Requirements

In the Europe Region, the Rule on this subject is modified as follows.

1. At a Hybrid ATM Terminal, if the Card also supports EMV chip technology, the Transaction must be completed using the chip. Technical fallback to magnetic stripe is not permitted.
2. Technical fallback is permitted at Hybrid POS Terminals and Hybrid Bank Branch Terminals. When technical fallback occurs, PIN must be used as the CVM. An Acquirer may withdraw support for technical fallback at attended POS Terminals and Bank Branch Terminals when the Acquirer is content that technical fallback support is no longer required to ensure good customer service. Upon doing so, the Acquirer must ensure that the POS Terminal or Bank Branch Terminal continues to support magnetic stripe Card acceptance.
3. All Terminals deployed within SEPA must support both magnetic stripe and EMV chip technology.
4. All Terminals deployed in Albania, Bosnia and Herzegovina, Kosovo, Moldova, Montenegro, North Macedonia, or Serbia must support both magnetic stripe and EMV chip technology.

# 7.6.1 Hybrid POS Terminal Requirements

In the Europe Region, the Rule on this subject is modified as follows.

1. CVM fallback from PIN CVM to signature CVM on a Chip Transaction conducted with a Maestro Card is not permitted.
2. All Hybrid POS Terminals deployed within SEPA must support the use of PIN as the CVM for intra-SEPA Chip Transactions conducted with Mastercard Cards.

All Hybrid POS Terminals deployed in Albania, Bosnia and Herzegovina, Kosovo, Moldova, Montenegro, North Macedonia, and Serbia must support the use of PIN as the CVM for Chip Transactions conducted with a Mastercard Card.

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A Hybrid POS Terminal and a PIN-capable Hybrid POS Terminal must be identified in authorization and clearing messages as specified by the registered switch of the Customer’s choice.


# 7.6.2 Hybrid ATM Terminal and Bank Branch Terminal Requirements

In the Europe Region, the Rule on this subject is modified as follows. ATM Terminals must be contactless-enabled in the following countries by the dates specified.

|Countries|Effective date|
|---|---|
|Bosnia and Herzegovina|Requirement already in effect for newly deployed ATM Terminals|
|Czech Republic|19 January 2024 for all ATM Terminals in Czech Republic|
|Montenegro| |
|Poland| |
|Serbia| |
|Albania|19 July 2024 for newly deployed ATM Terminals and for ATM Terminals that are already contactless-enabled for another acceptance brand|
|Austria| |
|Bulgaria|19 July 2028 for all ATM Terminals|
|Croatia| |
|Cyprus| |
|Germany| |
|Greece| |
|Hungary| |
|Kosovo| |
|Liechtenstein| |
|Malta| |
|North Macedonia| |
|Romania| |
|Slovakia| |
|Slovenia| |
|Switzerland| |

Where a Hybrid ATM Terminal or Hybrid Bank Branch Terminal supports more than one payment application residing on a Chip Card (for example, the Cirrus Payment Application and a stored value payment application), the Cardholder must be permitted to choose the preferred payment application.


# Terminal Requirements

# Latin America and the Caribbean Region

Latin America and the Caribbean Region

The following modifications to the Rules apply in the Latin America and the Caribbean Region. Refer to Appendix A for the Latin America and the Caribbean Region geographic listing.

# 7.3 POS Terminal Requirements

In the Latin America and the Caribbean Region, the Rule on this subject is modified as follows. All newly-deployed integrated POS Terminals must be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality. For the purposes of this Rule, an integrated POS Terminal refers to acceptance architectures where the Merchant’s POS solution is integrated with the Card-reading technology. They are typically deployed by large Merchant chains and stores. This definition may include automated fuel dispenser Terminals that have integrated payment functionality, although it does not include any devices that can be deployed as stand-alone payment Terminals.

# 7.3.1 Contactless–enabled POS Terminals

In the Latin America and the Caribbean Region, the Rule on this subject is modified as follows. All contactless-enabled Terminals, including a contactless-enabled Terminal submitted to the Corporation for MTIP testing as a new project, must only support EMV Mode Contactless Transactions and must not support Magnetic Stripe Mode Contactless Transactions. All newly-deployed integrated POS Terminals must be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality. For the purposes of this Rule, an integrated POS Terminal refers to acceptance architectures where the Merchant's POS solution is integrated with the Card-reading technology. They are typically deployed by large Merchant chains and stores. This definition may include automated fuel dispenser Terminals that have integrated payment functionality, although it does not include any devices that can be deployed as stand-alone payment Terminals.

# Online PIN Support

The following requirements apply to online PIN support on the contact and contactless interfaces of a Dual Interface POS Terminal and on the contactless interface of a contactless-only POS Terminal. MPOS Terminals are excluded from the above requirements.

In Brazil, the following requirements apply:

1. A contactless-enabled POS Terminal must support online PIN as the CVM for a Maestro Magnetic Stripe Mode Contactless Transaction that exceeds BRL 50; and
2. For Domestic Transactions, if the Cardholder selects the "debit" option when using a Mastercard Card or Access Device to initiate a Contactless Transaction, Mastercard® Single Message System processing requirements and the chargeback procedures in Chapter 4 of the Chargeback Guide will apply. The resulting Transaction is referred to as a Maestro Magnetic Stripe Mode Contactless Transaction.



267
# Terminal Requirements

# 7.6 Hybrid Terminal Requirements

Online PIN support is required for:

|All newly deployed contactless-enabled POS Terminals except integrated POS (iPOS) Terminals|Effective as of:|
|---|---|
| |• 1 June 2022 except in Mexico|
| |• 1 June 2024 in Mexico|
|All newly deployed contactless-enabled integrated POS (iPOS) Terminals|Effective as of:|
| |• 1 March 2023 except in Mexico|
| |• 1 March 2025 in Mexico|
|All contactless-enabled POS Terminals|Effective as of:|
| |• 1 January 2024 except in Mexico|
| |• 1 December 2025 in Mexico|

A contactless-enabled POS Terminal deployed in Brazil, Chile, or Colombia must minimally support online PIN and may also support Consumer Device CVM (CDCVM) as the CVM for a Maestro Contactless Transaction that exceeds the applicable contactless CVM limit.

# 7.6 Hybrid Terminal Requirements

In the Latin America and the Caribbean Region, the Rule on this subject is modified as follows. All Terminals that are newly deployed within the Region must be EMV-compliant.

# Middle East/Africa Region

The following modifications to the Rules apply in the Middle East/Africa Region. Refer to Appendix A for the Middle East/Africa Region geographic listing.

# 7.3 POS Terminal Requirements

# 7.3.1 Contactless-enabled POS Terminals

In the Middle East/Africa Region, the Rule on this subject is modified as follows. All contactless-enabled Terminals, including a contactless-enabled Terminal submitted to the Corporation for MTIP testing as a new project, must only support EMV Mode Contactless Transactions and must not support Magnetic Stripe Mode Contactless Transactions. All contactless-enabled POS Terminals deployed in the Region must support online PIN. This requirement applies to the contact and contactless interfaces of a Dual Interface POS Terminal and the contactless interface of a contactless-only POS Terminal. MPOS Terminals are excluded from this requirement.


# Terminal Requirements

# 7.6 Hybrid Terminal Requirements

# 7.6.1 Hybrid POS Terminal Requirements

In the Middle East/Africa Region, the Rule on this subject is modified as follows. All new or retrofitted Terminals deployed by Region Customers must be capable of upgrade to EMV compliance.

# United States Region

The following modifications to the Rules apply in the United States (U.S.) Region. Refer to Appendix A for the U.S. Region geographic listing.

# 7.3 POS Terminal Requirements

In the United States Region, the Rule on this subject is modified as follows.

- All POS Terminals, including CATs, may be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality.
- A POS Terminal that accepts Mastercard and Maestro as well as supports contactless acceptance for competing brands, must enable Mastercard and Maestro on the contactless interface.
- A newly-deployed POS Terminal that supports contactless acceptance must support only EMV mode contactless. Magstripe mode contactless must not be supported.
- Effective 1 April 2023, all POS Terminals that support contactless acceptance must support only EMV mode contactless. Magstripe mode contactless must not be supported.

# 7.3.1 Contactless–enabled POS Terminals

In the U.S. Region, the Acquirer of a Merchant that uses a contactless–enabled POS Terminal must comply with all of the following:

1. MCL Version 3.0—The contactless reader of a newly deployed contactless-enabled POS Terminal must support MCL version 3.0 or later.
2. Device Type Indicator—An Acquirer must ensure that any newly deployed contactless-enabled POS Terminal transmits the device type indicator in DE 48, subelement 23 (Payment Initiation Channel), subfield 1 (Device Type) of authorization messages when present in the Card or Access Device used to effect a Transaction. The Acquirer must also include the device type indicator, when present, in PDS 0198 (Device Type Indicator) of First Presentment/1240 messages.
3. CVM Support—A contactless–enabled POS Terminal deployed in the U.S. Region must minimally support online PIN as the CVM for a Maestro Contactless Transaction that exceeds the applicable contactless CVM limit. Any newly deployed or replacement contactless-enabled POS Terminal must also support Consumer Device CVM (CDCVM).


# 7.4 Mobile POS (MPOS) Terminal Requirements

In the United States Region, the Rule on this subject is modified as follows. All MPOS Terminals may be Dual Interface Hybrid Terminals that support and enable both EMV contact and EMV Mode contactless payment functionality.

# 7.5 ATM Terminal and Bank Branch Terminal Requirements

In the U.S. Region, the Rule on this subject is modified as follows:

1. An ATM Terminal or Bank Branch Terminal must:
1. Offer cash withdrawals from savings and checking accounts and cash advances from credit cards;
2. Offer balance inquiry for checking accounts, savings accounts, and credit cards;
3. Offer transfers from checking to savings accounts and from savings to checking accounts;
4. Offer Shared Deposit to savings accounts and checking accounts if the ATM Terminal or Bank Branch Terminal accepts shared deposits for any other shared deposit service;
5. Convert a cash withdrawal performed without account selection to a withdrawal from no account specified.
2. An ATM Terminal or Bank Branch Terminal may offer:
1. Cash withdrawals from no account specified; and
2. Shared Deposit to savings and checking accounts if the Terminal does not accept shared deposits for any other shared deposit service.

# 7.6 Hybrid Terminal Requirements

In the U.S. Region, the Rule on this subject is modified as follows. A Hybrid Terminal deployed in the U.S. Region must be configured as online-only or online-preferring for both Contact Chip Transaction and Contactless Transaction processing. “Online-only” means that the Hybrid Terminal seeks online authorization for all Transactions. “Online-preferring” means that the Hybrid Terminal seeks an online authorization for all Transactions, but may approve a Transaction that does not exceed the applicable Terminal offline chip authorization limit when in the “unable to go online” mode. This may occur when the Terminal temporarily loses online connectivity or does not receive an authorization response from the Issuer. For more information, refer to M/Chip Requirements for Contact and Contactless.

# 7.7 Mastercard Consumer-Presented QR-enabled POS Terminals

In the U.S. Region, the Rule on this subject is modified to add the following: An Acquirer must transmit the device type indicator in DE 48, subelement 23 (Payment Initiation Channel), subfield 1 (Device Type) of the Authorization Request/0100 message or the Financial Transaction Request/0200 message when present in the Access Device used to effect a Transaction. The Acquirer must also include the device type indicator, when present, in PDS 0198 (Device Type Indicator) of the First Presentment/1240 message.


# Terminal Requirements

# Additional U.S. Region and U.S. Territory Rules

The following modifications to the Rules apply in the United States Region and in American Samoa, Guam, Northern Mariana Islands, Puerto Rico, and the U.S. Virgin Islands (herein, “the U.S. Territories”).
These Rules apply in addition to any that apply within the Asia/Pacific Region, with respect to Customers located in American Samoa, Guam, and Northern Mariana Islands; the Latin America and the Caribbean Region, with respect to Customers located in Puerto Rico and the U.S. Virgin Islands; and the United States Region, with respect to U.S. Region Customers.

# 7.6 Hybrid Terminal Requirements

# 7.6.1 Hybrid POS Terminal Requirements

Hybrid POS Terminal and Chip-only MPOS Terminal Displays
In the U.S. Region and U.S. Territories, the Rule on this subject is replaced with the following:
A Hybrid POS Terminal (including any Hybrid MPOS Terminal) and a Chip-only MPOS Terminal must:

1. For each debit Account (including any prepaid debit Account) on a Card, display to the Cardholder at least one mutually supported application label or preferred name, which the Merchant may select.
2. For each credit Account on a Card, display all mutually supported application labels or preferred names. Multiple matching applications must be displayed in the Issuer's priority sequence.
3. Display to the Cardholder the Transaction amount and Transaction currency, if different from the Merchant's or cash disbursement agent's local currency.

For more information, refer to the U.S. Region section in Chapter 2 of the M/Chip Requirements for Contact and Contactless manual.
