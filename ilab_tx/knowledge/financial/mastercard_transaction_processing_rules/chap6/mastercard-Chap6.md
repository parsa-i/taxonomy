# Payment Transactions and Funding Transactions

# 6.1 Payment Transactions

A Payment Transaction is a transfer of funds to an Account via the Corporation System. Each Payment Transaction must comply with all requirements set forth herein, in Appendix C, and in the technical specifications for authorization messages. If a Payment Transaction is conducted pursuant to a Customer-to-Customer, intracountry, or intercountry business service arrangement, the business service arrangement must be approved by the Corporation in writing, in advance of the effecting of a Payment Transaction. The Corporation reserves the right to audit or to monitor any Payment Transaction Program at any time.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# 6.1.1 Payment Transactions—Acquirer and Merchant Requirements

The following requirements apply to an Acquirer and any Merchant that conducts Payment Transactions:

1. An Acquirer must submit an authorization request to the receiving Issuer (either an Authorization Request/0100 or Financial Transaction Request/0200 message, as applicable) for each Payment Transaction.
2. Each Payment Transaction must be authorized, cleared and settled separately and distinctly. Two or more funds transfers or payments must not be aggregated into a single Payment Transaction, nor may one Payment Transaction be separated into two or more Payment Transactions.
3. A Payment Transaction must be effected on the date agreed to with the Cardholder whose Account is to be funded.
4. A Payment Transaction must not be effected:
1. To “authenticate” an Account or a Cardholder; for example, by effecting or attempting to effect a Payment Transaction for a nominal amount.
2. For any illegal purpose or any other purpose deemed by the Corporation to be impermissible.
3. For the purchase of goods or services, unless that Payment Transaction is expressly permitted by the Standards.
5. Funds for the Payment Transaction must be deemed collected and in the control of the Acquirer before the Payment Transaction is submitted to the Interchange System.
6. In a dual message environment, the Acquirer must submit a clearing message to the Interchange System within one calendar day of the Issuer’s approval of the authorization request. The Acquirer must ensure that the amount of the Payment Transaction in the clearing message matches the amount in the authorization request.
7. A reversal of a Payment Transaction (other than a MoneySend Payment Transaction) must only be submitted to correct a documented clerical error and upon agreement of the Issuer. In such an event, the error must be reversed within one calendar day of the date the
# Payment Transactions and Funding Transactions

# 6.1.2 Payment Transactions—Issuer Requirements

Payment Transaction was submitted to the Interchange System (as a Financial Transaction/0200 message or First Presentment/1240 message, as applicable) for posting to an Account. Reversible clerical errors include, by way of example and not limitation, the erroneous capture of Payment Transaction data, a duplicate Payment Transaction, or an error caused by the transposition of data.

8. A reversal of a MoneySend Payment Transaction must only be submitted for reasons of (a) timeout when the Acquirer’s time-out limit has been exceeded for receiving the authorization request response message, or (b) incorrectly formatted response messages where the response received by the Acquirer is not properly formatted as defined for the request response messages in Dual Message System or Single Message System specifications. In such an event, the error must be reversed within sixty (60) seconds of when the original authorization message related to a MoneySend Payment Transaction was submitted to the Dual Message System or the Single Message System (as an Authorization Request/0100 message or a Financial Transaction/0200 message, as applicable) for posting to an Account, and must include Data Element (DE) 90 (subfields when available). Any other adjustment of a MoneySend Payment Transaction must be in accordance with the Mastercard MoneySend and Funding Transactions Program Standards.

9. The Acquirer or Merchant that offers the Payment Transaction service must not request or require that a Cardholder disclose his or her PIN. If the Payment Transaction service is provided via a web page, the Merchant must not design that web page in any way that might lead the Cardholder to believe that he or she must provide his or her PIN. Similarly, if the Cardholder is asked to complete a form in order to conduct a Payment Transaction, the contents of that form must not lead the Cardholder to believe that he or she must provide his or her PIN. The Acquirer must ensure that the Merchant is following these procedures. The Corporation will also, from time to time, perform audits on these Merchants to ensure that they are compliant with this and all other requirements.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# 6.1.2 Payment Transactions—Issuer Requirements

The following requirements apply to an Issuer that receives Payment Transactions, excluding MoneySend Payment Transactions.

An Issuer that offers the Payment Transaction must make either the PAN or a pseudo PAN available to the Cardholder. If the Issuer provides the Cardholder with a pseudo PAN, the Issuer must be able to link the pseudo PAN to the Cardholder’s actual PAN.

An Issuer must receive, process, and provide a valid authorization response to each Payment Transaction authorization request received.

Upon receiving a Payment Transaction, the Issuer, at its discretion, may:

1. Approve (and receive remuneration for costs incurred) or decline any requests by the Acquirer to correct a clerical error;
2. Establish a maximum Payment Transaction amount; and
3. Determine when to make the transferred funds available to the recipient—immediately or after a period of time defined by the Issuer.


# Payment Transactions and Funding Transactions

# 6.2 Gaming Payment Transactions

A Payment Transaction must be effected in a way that does not conflict with Cardholder agreements or instructions.

NOTE: An addition to this Rule appears in the “Europe Region” section at the end of this chapter.

# 6.2 Gaming Payment Transactions

The Gaming Payment Transaction is a transaction that may be used to transfer winnings or value usable for gambling or gaming to a Mastercard or Maestro Account.

NOTE: Rules on this subject appear in the “Europe Region,” “Middle East/Africa Region,” and “United States Region” sections at the end of this chapter.

# 6.3 MoneySend Payment Transactions

Each Issuer and Acquirer and each MoneySend Payment Transaction must comply with all requirements set forth in the Standards applicable to MoneySend, including but not limited to those herein and in Appendix C, in the technical specifications for authorization messages, and in the Mastercard MoneySend and Funding Transactions Program Standards.

An Issuer of a consumer Card Program or Eligible Commercial Card Program (excluding anonymous prepaid and gift Card Accounts) must be able to receive, process, authorize (meaning making an individual authorization decision with respect to each MoneySend Payment Transaction), and post MoneySend Payment Transactions in compliance with the Standards applicable to MoneySend. Refer to the Mastercard MoneySend and Funding Transactions Program Standards for a list of Eligible Commercial Card Program types.

NOTE: A modification to this Rule appears in the “Europe Region” section at the end of this chapter.

# 6.4 China Deposit Transactions – China Only

NOTE: A Rule on this subject appears in the “Asia/Pacific Region” section at the end of this chapter.

# 6.5 China Funds Transfer Transactions – China Only

NOTE: A Rule on this subject appears in the “Asia/Pacific Region” section at the end of this chapter.



236
# Payment Transactions and Funding Transactions

# 6.6 Funding Transactions

Each Issuer and Acquirer and each Funding Transaction must comply with all requirements set forth in the Standards applicable to Funding Transactions, including but not limited to those in the Mastercard MoneySend and Funding Transactions Program Standards.

As set forth and as from the effective dates set forth in the Mastercard MoneySend and Funding Transactions Program Standards, the following requirements apply with respect to Funding Transactions identified with MCC 4829 (Money Transfer), MCC 6538 (Funding Transactions for MoneySend), or MCC 6540 (Funding Transactions):

- Before submitting Funding Transactions using any of these MCCs, an Acquirer must first register itself and each Merchant proposing to initiate such Funding Transactions with Mastercard.
- The Acquirer must use the appropriate Transaction Type Indicator (TTI) value in DE 48, subelement 77 (Transaction Type Identifier) of authorization request messages and in DE 48, PDS 0043 (Transaction Type Identifier) of clearing messages.
- The Acquirer must ensure that each Merchant and each Funding Transaction complies with all applicable legal and operational requirements and that the Funding Transaction includes any required reference data in DE 108 (Additional Transaction Reference Data) of authorization request messages.
- The Issuer must comply with requirements regarding internal controls for AML compliance and information retention for each Funding Transaction received.

# Variations and Additions by Region

The remainder of this chapter provides modifications to the Standards set out in this chapter. The modifications are organized by region or country and by applicable subject title.

# Asia/Pacific Region

The following modifications to the Rules apply in the Asia/Pacific Region or in a particular Region country or countries. Refer to Appendix A for the Asia/Pacific Region geographic listing.

# 6.4 China Deposit Transactions – China Only

This Rule 6.4 and its subsections apply to China domestic Transactions only. Each Issuer and Acquirer must comply with all requirements set forth in the Standards applicable to China Deposit Transactions, including the technical specifications for authorization messages and the China Interbank ATM Deposit Program Guide.

An Acquirer may choose to participate in China Deposit Transactions; provided that if an Acquirer deploys ATM Terminals that participate in domestic deposit transactions of other scheme brands or networks, such Acquirer’s ATM Terminals must participate in China Deposit Transactions.



237
# Payment Transactions and Funding Transactions

# 6.4.1 Non-discrimination Regarding Maximum Transaction Amount Limit

An Acquirer may impose a maximum amount limit on China Deposit Transactions accepted at an ATM Terminal provided that the limit imposed on Cardholders is the same or more favorable than the limits imposed on cardholders of other scheme brands or networks. This Rule does not limit the application of other non-discrimination provisions contained in the Standards.

# 6.4.2 ATM Access Fee

The Acquirer may charge an ATM Access Fee or other fee types imposed, or advised of, at an ATM Terminal, in connection with a Deposit Transaction. The Acquirer must follow the requirements for Rule 4.18.3 ATM Access Fee Requirements in Chapter 4 of this manual.

# 6.4.3 Account Verification

The Acquirer may submit an account verification message to verify the validation of the deposit account prior to initiating the China Deposit Transaction. The Issuer must return the deposit account Cardholder name with surname truncated via the account verification response message if the Account is valid.

# 6.4.4 Failed Transaction

The ATM Terminal must be able to notify the depositor and return the cash if the Deposit Transaction fails.

# 6.5 China Funds Transfer Transactions – China Only

This Rule 6.5 and its subsections apply to China domestic Transactions only. Each Issuer and Acquirer must comply with all requirements set forth in the Standards applicable to the China Funds Transfer Transaction, including in the technical specifications for authorization messages, and in the China Interbank ATM Funds Transfer Program Guide.

# 6.5.1 China Funds Transfer Transaction Terms

Key terms used in this section are defined in the following table for purposes of this section only.

|Terms|Description|
|---|---|
|Funding Account|The funding source of the Originating Account Holder, from where funds are acquired by the Originating Institution to initiate a PTA Transaction.|
|Funding Institution|The issuer of funding account. The Funding Institution and Originating Institution will be the same entity if the funding institution originates the China Funds Transfer Transaction. Funding Institution is also referred as Funding Issuer.|


# Payment Transactions and Funding Transactions

# 6.5.2 Non-discrimination Regarding Maximum Amount Limit

|Terms|Description|
|---|---|
|Originating Institution|The Customer that notifies the China Switch to originate a China Funds Transfer Funding Transaction (optional) or a China Funds Transfer Payment Transaction. Also referred to as an Acquirer.|
|Receiving Account|The Account held by a Receiving Account Holder and to which the Receiving Customer must ensure receipt of a China Domestic Funds Transfer Transaction.|
|Receiving Institution|The Customer that receives and approves a China Funds Transfer Payment Transaction. Also referred to as the Issuer of Receiving Account in funds transfer transactions.|

A Funding Institution or Receiving Institution may impose a maximum amount limit on China Funds Transfer Transactions provided that the limit imposed on Cardholders is the same or more favorable than the limits imposed on cardholders of other scheme brands or networks. This Rule does not limit the application of other non-discrimination provisions contained in the Standards.

# 6.5.3 ATM Access Fee

The Originating Institution may charge an ATM Access Fee or other fee types imposed, or advised of, at an ATM Terminal, in connection with a China Funds Transfer Transactions. The Acquirer must follow the requirements in Rule 4.18.3 ATM Access Fee Requirements in Chapter 4 of this manual.

# 6.5.4 Account Verification

The Originating Institution may submit an account verification message to verify the validation of the receiving account prior to initiating the China Funds Transfer Transaction. The Receiving Institution must return the receiving account Cardholder name with Surname truncated via the account verification response message if the account is valid.

# 6.5.5 Funds Availability

For a China Funds Transfer Transaction that occurs at an ATM Terminal, the Receiving Institution must post the funds to the Receiving Account immediately after the approval of the China Funds Transfer Transaction. Reversal is not allowed for a China Funds Transfer Transaction.



239
# Payment Transactions and Funding Transactions

# Europe Region

The following modifications to the Rules apply in the Europe Region or in a particular Region country or countries. Refer to Appendix A for the Europe Region, Non-Single European Payments Area (Non-SEPA) and Single European Payments Area (SEPA) geographic listing.

# 6.1 Payment Transactions

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A Payment Transaction may be processed via any switch of the Customer’s choice that is registered with the Corporation. Each type of Payment Transaction must be identified in authorization and clearing messages as specified by the registered switch of the Customer’s choice.

In Russia, the Rule on this subject is modified as follows. Payment Transactions in Russia may be processed through a domestic switching service.

# 6.1.1 Payment Transactions—Acquirer and Merchant Requirements

In the Europe Region, the Rule on this subject is modified as follows. With respect to an interregional Payment Transaction involving a Europe Region Acquirer and an Issuer located in another Region, if the Acquirer does not submit a clearing message to the Interchange System within seven days of the authorization request, the Corporation collects the Payment Transaction amount and any additional fees charged from the Acquirer by means of a Fee Collection/1740 message.

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. Funds for the Payment Transaction must be deemed collected and in the control of the Acquirer before the Payment Transaction is submitted to the registered switch of the Customer’s choice. The Acquirer must submit a clearing message to the registered switch of its choice within one calendar day of the Issuer’s approval of the authorization request. A clerical error must be reversed or adjusted within three calendar days of the date the Payment Transaction was submitted to the registered switch of the Acquirer’s choice for posting to a Mastercard Account, or within one calendar day if submitted for posting to a Maestro or Cirrus Account.

# 6.1.2 Payment Transactions—Issuer Requirements

In Italy, the Rule on this subject is modified as follows:

1. An Issuer must support, process, and provide a valid authorization response to each Payment Transaction authorization request received, for all prepaid Mastercard, Debit Mastercard (including prepaid), and Mastercard charge Card Programs (revolving credit Card Programs are excluded); and


# Payment Transactions and Funding Transactions

# 6.2 Gaming Payment Transactions

Except with respect to non-reloadable prepaid Cards, an Issuer must not automatically decline Payment Transactions.

# 6.2 Gaming Payment Transactions

In the Europe Region, in addition to the requirements for Payment Transactions, the requirements contained in the Mastercard Gaming and Gambling Payments Program Standards apply to Gaming Payment Transactions.

# 6.3 MoneySend Payment Transactions

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A MoneySend Payment Transaction may be processed via any switch of the Customer’s choice that is registered with the Corporation.

# Middle East/Africa Region

The following modifications to the Rules apply in the Middle East/Africa Region. Refer to Appendix A for the Middle East/Africa Region geographic listing.

# 6.2 Gaming Payment Transactions

In the Middle East/Africa Region, in addition to the requirements for Payment Transactions, the following requirements apply to Gaming Payment Transactions:

1. The Gaming Payment Transaction may only be used to transfer winnings or unspent chips or other value usable for gambling to the same Card that the Cardholder used to place the bet or purchase value used or usable for gambling.
2. The Gaming Payment Transaction must be properly identified in authorization and clearing messages using MCC 7995, a Transaction type value of 28, and a Payment Transaction program type value of C04.
3. The Gaming Payment Transaction must not exceed USD 50,000 or the local currency equivalent.
4. Mail order and telephone order (MO/TO) Merchants may not process Gaming Payment Transactions.
5. Gaming Payment Transactions must not be processed to any type of Mastercard Corporate Card, Maestro Card, or prepaid Card. In Kenya, a Gaming Payment Transaction may be processed to a consumer prepaid Card (excluding anonymous prepaid Cards).
6. The following Anti-Money-Laundering (AML) requirements apply:
1. The Acquirer must consider its Merchants that submit Gaming Payment Transactions as higher risk under its anti-money laundering compliance program.
2. In addition to any requirement of applicable local law or regulation, the Acquirer must conduct enhanced customer due diligence reviews of any Merchant that submits Gaming Payment Transactions.



241
# 6.2 Gaming Payment Transactions

c. The Acquirer must ensure that each Merchant that submits Gaming Payment Transactions has appropriate controls in place to identify legitimate customers and to block suspicious activities, Cards, or Payment Transactions.

d. The Acquirer must have robust procedures and ongoing controls in place to monitor Transactions and Payment Transactions conducted by Merchants that submit Gaming Payment Transactions and to detect and report any potentially suspicious activity.

# 7. A Gaming Payment Transaction may be effected if not prohibited by applicable law or regulation and only for Cards issued in the following countries.

|Country Code|Country|Country Code|Country|
|---|---|---|---|
|024|Angola|480|Mauritius|
|072|Botswana|508|Mozambique|
|174|Comoros|516|Namibia|
|180|Democratic Republic of the Congo|566|Nigeria|
|262|Djibouti|646|Rwanda|
|232|Eritrea|690|Seychelles|
|230|Ethiopia|694|Sierra Leone|
|270|Gambia|706|Somalia|
|288|Ghana|728|South Sudan|
|404|Kenya|748|Swaziland|
|426|Lesotho|834|Tanzania|
|430|Liberia|800|Uganda|
|450|Madagascar|894|Zambia|
|454|Malawi|716|Zimbabwe|

# 8. In Nigeria, an Issuer must support the Gaming Payment Transaction in authorization and clearing messages.

# 9. Gaming Payment Transactions will not be authorized by the Stand-In Processing Service. Authorization is entirely under the control of the Issuer.



242
# Payment Transactions and Funding Transactions

# United States Region

The following modifications to the Rules apply in the United States (U.S.) Region. Refer to Appendix A for the U.S. Region geographic listing.

# 6.2 Gaming Payment Transactions

In the United States Region, in addition to the requirements for Payment Transactions, the requirements contained in the Mastercard Gaming and Gambling Payment Program Standards apply to Gaming Payment Transactions.
