# Acceptance Procedures

# 3.1 Card-Present Transactions

A Card-present Transaction occurs when the Cardholder has presented a Card or Access Device to a Merchant or Customer representative in a face-to-face environment, or uses a Card or Access Device to initiate a Transaction at an ATM Terminal or unattended POS Terminal. A Card-present Transaction conducted at a Terminal should be processed using the highest level of technology supported by both the Card or Access Device and the Terminal, as follows:

1. If a Chip Card or Access Device is presented at a Card-reading Hybrid Terminal, complete the Transaction in accordance with the technical specifications set forth in the M/Chip Requirements for Contact and Contactless; or
2. If a Card is presented at a magnetic stripe-reading Terminal that is not chip-enabled, ensure that the Card’s magnetic stripe is “read” by the Terminal.

Each Transaction must be authorized as described in Rule 3.3.

# 3.1.1 Mastercard Card Acceptance Procedures

A Mastercard Card is not required to be accepted if neither the magnetic stripe nor the contact or contactless chip on the Card can be read for any reason. The manual completion of a Transaction, whether by means of a manual imprinter, electronic key entry of the Card information, or both, does not provide sufficient proof of Card presence in a fraud-related dispute.

The following steps may be performed in a face-to-face environment to determine the validity of a Mastercard Card (but not an Access Device):

- Check for the presence of the Mastercard or Debit Mastercard hologram, as applicable, or the Premium Brand Mark.
- If the POS Terminal displays the PAN encoded on the magnetic stripe and if the PAN is present on the Card, then compare the last four digits of the PAN on the Card with the four-digit truncated PAN displayed on the POS Terminal.

The following steps may be performed for all face-to-face unique Transactions (TCC of U) and Manual Cash Disbursement Transactions, unless PIN or CDCVM is used as the CVM:

- Request personal identification in the form of an unexpired, official government document (for example, a passport, identification document, or driver’s license).
- If a photograph is present on the personal identification, compare the photograph with the person presenting the Card.

The personal identification type and number must not be recorded on the Transaction receipt.

# Suspicious Cards

When suspicious that a presented Mastercard Card may not be valid, the Merchant or Customer accepting the Card should follow the Acquirer’s “Code 10” (suspicious Card) procedures, which


# 3.1.2 Maestro Card Acceptance Procedures

may include placing a value of 1 (Suspected fraud [merchant suspicious—code 10]) in DE 61, subfield 8 (Transaction Security) of the authorization request message.

NOTE: A modification to this Rule appears in the “Europe Region” section at the end of this chapter.

# 3.1.2 Maestro Card Acceptance Procedures

A Maestro Card must not be accepted if neither the magnetic stripe nor the contact or contactless chip on the Card can be read for any reason.

Electronic key entry of Maestro Card information into a POS Terminal is permitted only for refund Transactions. An Issuer is not responsible for a Maestro POS Transaction if the PAN was manually entered into the POS Terminal and the approved Transaction was subsequently determined to have arisen through use of a fraudulent Card and/or unauthorized use of a PIN.

# 3.2 Card-Not-Present Transactions

The physical presentation of a Card or Access Device is not required and must not be requested to complete a Transaction conducted in a Card-not-present environment, including any e-commerce, mail order, phone order, or Credential-on-file Transaction.

A Merchant must not refuse to complete a Mastercard e-commerce Transaction solely because the Cardholder does not have a digital certificate or other secured protocol.

NOTE: A Rule variation on this subject appears in the “Europe Region” section at the end of this chapter.

# 3.3 Obtaining an Authorization

With respect to securing authorizations, an Acquirer must treat all Transactions at a Merchant in the same manner.

# 3.3.1 Mastercard POS Transaction Authorization Procedures

A Merchant must inform the Cardholder of any estimated amount for which authorization will be requested and must obtain the Cardholder's consent to the amount before initiating the authorization request. This requirement does not apply to:

- Contactless transit aggregated or transit debt recovery Transactions;
- Automated fuel dispenser (AFD) Transactions (MCC 5542); or
- An authorization requested for an amount otherwise approved by the Cardholder as the final Transaction amount.

Refer to Chapter 2 for requirements relating to the proper identification of a Processed Transaction authorization request for an amount greater than zero as a preauthorization (in all Regions), undefined authorization (in all Regions except the Asia/Pacific, Middle East/Africa, and Europe Regions), or final authorization (in all Regions).


# Acceptance Procedures

# Authorization of Lodging, Cruise Line, and Vehicle Rental Transactions

A Merchant must obtain an online authorization from the Issuer for all Transactions, with the following exceptions:

1. Transactions at a CAT 3 device.
2. Chip Transactions authorized offline by the EMV chip, including both Contact Chip and EMV mode Contactless Transactions, when the Transaction amount is equal to or less than USD 200, or EUR 200 for a Merchant in the Europe Region.
3. Refund Transactions. Effective 18 October 2024, this exception is limited to refunds conducted by airline Merchants and for contactless transit aggregated Transactions.
4. Transit First Ride Risk (FRR) claim Transactions that are less than or equal to the FRR limit amount applicable in the Merchant's country, as described in Rule 5.6.1.

NOTE: Modifications to this Rule appear in the "Canada Region" and "United States Region" sections at the end of this chapter.

Terminal offline chip authorization limits are published in Chapter 5 of the Quick Reference Booklet.

A Merchant or its Acquirer may obtain a voice authorization from the Issuer, with the understanding that the authorization code obtained in a voice authorization is not a valid remedy to an authorization-related chargeback.

For additional authorization message requirements, including how a Merchant or Acquirer may convert an Issuer's approval of a Card-not-present Transaction believed in good faith to be fraudulent to a decline, refer to Chapter 2.

NOTE: A modification to this Rule appears in the "Europe Region" section at the end of this chapter.

# Authorization of Lodging, Cruise Line, and Vehicle Rental Transactions

Lodging, cruise line, and vehicle rental Merchants may request an authorization for an estimated Transaction amount, and may submit subsequent authorization requests for any additional estimated amounts as needed. For more information, refer to Rule 2.9.

Vehicle rental Merchants:

1. May not include any charge in a Transaction that represents either the vehicle insurance deductible amount or an amount to cover potential or actual damages when the Cardholder waives insurance coverage at the time of the rental; and
2. Before the Cardholder enters into a rental agreement, the Merchant must disclose to the Cardholder the amount of the authorization request to be sent to the Issuer.

Charges for loss, theft, or damage must be processed separately.

The Transaction amount of a lodging, cruise line, or vehicle rental Processed Transaction must not exceed the authorized amount. If the Merchant obtains a preauthorization for an estimated amount, and the Transaction amount exceeds the authorized amount, the Merchant may request an incremental authorization. In connection with such Transactions, the Issuer must not place a hold on the Cardholder’s Account in excess of the authorized amount.


# Acceptance Procedures

# Authorization When the Cardholder Adds a Gratuity

NOTE: A modification to this Rule appears in the “Europe Region” section at the end of this chapter.

# Authorization When the Cardholder Adds a Gratuity

When a preauthorization or an undefined authorization (in all Regions except the Asia/Pacific, Europe, and Middle East/Africa Regions) is obtained:

- If the Transaction is a Card-Not-Present Transaction, Chip/PIN Transaction, Contactless Transaction, or Mastercard Consumer-Presented Quick Response (QR) Transaction, any gratuity must be included in the authorization request. A gratuity must not be added after authorization is obtained.
- For all other Transaction types, a gratuity may be added after authorization is obtained.
- If the gratuity does not exceed 20 percent of the authorized amount, then no additional authorization is needed.
- If the gratuity exceeds 20 percent of the authorized amount, then the Merchant may request an incremental authorization for the amount in excess of the authorized amount.

NOTE: Modifications to this Rule appear in the “United States Region” section at the end of this chapter.

For all Transactions, if the authorization request message contains the Partial Approval Terminal Support Indicator, and the authorization request response message contains a value of 10 (Partial Approval) in DE 39 and a partial approval amount in DE 6, the Transaction amount must not exceed the authorized amount.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

The Issuer must not place a hold on the Cardholder’s Account in excess of the total authorized amount (inclusive of the 20 percent tolerance, if applicable, or any incremental authorization).

NOTE: Modifications to this Rule appear in the “United States Region” section at the end of this chapter.

# Card-Not-Present Transaction Declines

If a Merchant initiates an authorization request for a Card-not-present Transaction and the Acquirer receives any one of the following declined responses in DE 39 (Response Code) of the Issuer’s authorization request response message, the Merchant must not initiate any additional authorization requests for the same Transaction with the same PAN and expiration date at any time.

|Response Code Value|Description|
|---|---|
|04|Capture card|
|14|Invalid card number|
|15|Invalid issuer|


# Acceptance Procedures

# Use of Card Validation Code (CVC) 2

|Response Code Value|Description|
|---|---|
|41|Lost card|
|43|Stolen card|
|54|Expired card|

In a Card-not-present environment, a Merchant may request a Card validation code (CVC) 2 verification from the Issuer, as a means to check the validity of a Mastercard Card. CVC 2 data must not be stored by the Merchant, its Acquirer, or any Service Provider. Refer to section 3.12 of the Security Rules and Procedures manual for additional CVC 2 requirements.

# Capture Card Response

If the Merchant receives a “capture card” or “pick-up-card” response to an authorization request, the Merchant must not complete the Transaction. In a face-to-face Transaction environment, the Merchant should attempt to retain the Card by reasonable and peaceful means. The Card retention requirement does not apply when an Access Device has been presented. Upon recovering a Card, the Merchant must notify its Acquirer and ask for further instructions.

# 3.3.2 Maestro POS Transaction Authorization Procedures

A Merchant must obtain an online authorization from the Issuer or its agent for all Maestro magnetic stripe POS Transactions. With respect to Maestro Chip Transactions, the Terminal offline chip authorization limits published in Chapter 5 of the Quick Reference Booklet apply. A Merchant must obtain an online authorization for a Chip Transaction that exceeds the published Terminal offline chip authorization limit and whenever the Card or the Hybrid POS Terminal requires online authorization. Before completing a Chip Transaction for which online authorization is required or requested, the Merchant must obtain a Transaction Certificate (TC) and related data. For additional authorization message requirements, including how a Merchant or Acquirer may convert an Issuer's approval of a Card-not-present Transaction believed in good faith to be fraudulent to a decline, refer to Chapter 2.

NOTE: An addition to this Rule appears in the “Europe Region” section at the end of this chapter.

# 3.4 Mastercard Cardholder Verification Requirements

In a face-to-face Transaction environment, the Merchant Terminal must support signature as a Cardholder verification method (CVM) for a Mastercard POS Transaction. Signature collection is optional.


# Acceptance Procedures

# 3.4 Mastercard Cardholder Verification Requirements

If PIN, Consumer Device CVM (CDCVM), successful Cardholder authentication on a Mastercard Biometric Card, or "No CVM" is used as the CVM in accordance with the Standards, the Merchant must not request that the Cardholder sign the Merchant's copy of the Transaction receipt.

|For a Mastercard Contactless Transaction that…|Then…|
|---|---|
|Is less than or equal to the applicable contactless CVM limit|"No CVM" is the only CVM option. The Merchant must not request that the Cardholder sign the Merchant’s copy of the Transaction receipt.|
|Exceeds the applicable contactless CVM limit|The CVM may be any of the following, provided both the Card or Access Device and the POS Terminal support the CVM:|

- Signature - When signature is selected as the CVM, the Merchant may optionally request the Cardholder's signature
- Online PIN
- Consumer Device CVM (CDCVM)

With respect to Mastercard POS Transactions conducted by a Merchant using an MPOS Terminal or a Chip-only MPOS Terminal, PIN is not required if:

1. the Merchant has less than USD 100,000 in annual Transaction volume; and
2. the MPOS Terminal has a contact chip reader and magnetic stripe-reading capability but does not support PIN as a CVM for Contact Chip Transactions.

(The use of an MPOS Terminal or Chip-only MPOS Terminal lacking such capabilities confers no chargeback protection. Refer to Rule 7.4 regarding restrictions on the use of certain MPOS Terminal types.)

In a Card-not-present Transaction environment, the Merchant may complete the Transaction without using a CVM.

Refer to Appendix D for CVM requirements at unattended POS Terminals.

NOTE: Modifications to this Rule appear in the "Latin America and the Caribbean Region" section at the end of this chapter.


# Acceptance Procedures

# CVM Not Required for Refund Transactions

No CVM is required for a refund Transaction. However, when a PIN is used as the CVM for a refund Transaction conducted at a Hybrid POS Terminal, the Merchant must obtain a successful PIN validation.

# Use of PIN for Mastercard Magnetic Stripe Transactions

Each PIN-capable POS Terminal must meet specific requirements for PIN processing wherever an approved implementation of PIN for magnetic stripe Transactions takes place. Refer to chapter 4 of the Security Rules and Procedures for more information. An Issuer should refer to the Authorization Manual for information about optional PIN verification during Stand-In Processing.

# 3.5 Maestro Cardholder Verification Requirements

For each Card-present Maestro POS Transaction, PIN must be used as the CVM, whether magnetic stripe or chip is used to initiate the Transaction, except in the case of:

1. A properly presented Contactless Transaction for which no CVM is required or when Consumer Device CVM (CDCVM) has been successfully completed;
2. No-CVM Transactions conducted in the Europe Region; and
3. A Transaction occurring at a Hybrid POS Terminal in a country in which the Corporation has consented to the use of offline PIN as the minimum CVM for a Chip Transaction and signature as the CVM for a magnetic stripe Transaction. Signature collection is optional.

At present, the Corporation has given such consent to Customers in:

1. Finland
2. France
3. Ireland
4. Israel
5. Monaco
6. United Kingdom

As of 31 December 2023, Finland, France, and Monaco will be removed from the above list. An Issuer must not decline authorization of a Transaction solely because the PIN was verified in an offline mode or because the Transaction occurred in a country where the Corporation has granted Customers a waiver allowing the use of a signature-based CVM instead of a PIN-based CVM. An Issuer must accept and properly process (by performing an individual risk assessment on) each Transaction verified using a signature-based CVM in the same manner as the Issuer would if the Transaction had been verified using a PIN-based CVM.

NOTE: Modifications to this Rule appear in the “Europe Region,” “Latin America and the Caribbean Region” and “United States Region” sections at the end of this chapter.


# Acceptance Procedures

# 3.6 Use of a PIN for Transactions at ATM Terminals and Bank Branch Terminals

The following requirements apply with respect to Transactions occurring at ATM Terminals and Bank Branch Terminals.

1. At an ATM Terminal and when a Maestro or Cirrus Card or PIN-preferring Mastercard Card is accepted at a Bank Branch Terminal, the Cardholder must be verified by a PIN, whether magnetic stripe or chip is used to initiate the Transaction.
2. For magnetic stripe Transactions, PIN verification must be online.
3. For a Cardless ATM Transaction, the Cardholder must be verified by Consumer Device CVM (CDCVM) and may also be verified by PIN.
A Cardless ATM Transaction is identified in Authorization Request/0100 and Financial Transaction Request/0200 messages with:

- Data Element (DE) 22 (POS Entry Mode), subfield 1 (POS Terminal PAN Entry Mode) = 09 (PAN/Token entry via electronic commerce containing DSRP cryptogram in DE 55 (Integrated Circuit Card [ICC] System-Related Data)
- DE 18 (Merchant Type) = 6011 (Automated Cash Disbursements—Customer Financial Institution)
- DE 48 (Additional Data—Private Use), Transaction Category Code = Z (Automated Cash Disbursement)
- DE 48, subfield 28 (Cardless ATM Order ID) = a 10-digit order ID provided by Mastercard Cardless engine
4. The Issuer must ensure that Chip Cards support online PIN for these Transactions and decline Transaction attempts where the PIN is entered incorrectly. For Chip Transactions, the Payment Application or Card may also be blocked if the Cardholder exceeds the number of PIN attempts permitted by the Issuer.

# 3.7 Use of a Consumer Device CVM

A Consumer Device CVM (CDCVM) may only be used as a CVM for Transactions if:

1. The CDCVM has been qualified by Mastercard, as set forth in Chapter 3 of the Security Rules and Procedures; and
2. The person authenticated has been identified and verified as an authorized Cardholder in accordance with Issuer-approved parameters.

When a CVM is requested or required for a Transaction and a CDCVM is used, the Issuer must either perform CDCVM verification or confirm that CDCVM verification was successful.


# 3.8 POI Currency Conversion

For purposes of these POI currency conversion Rules, billing currency is the currency in which the Card was issued.

POI currency conversion is a service that may be offered by a Merchant or Acquirer. The service enables a Cardholder to decide whether a Transaction should be completed in either the local currency or the billing currency. POI currency conversion is also referred to as dynamic currency conversion, or DCC. If POI currency conversion is used for a Transaction, the foreign exchange rate is applied by the Merchant or Acquirer.

When POI currency conversion is offered, the Transaction currency is the currency selected by the Cardholder at the Point-of-Sale (POS) Terminal, ATM Terminal, or Bank Branch Terminal. An Acquirer that intends to acquire Transactions on which POI currency conversion has been performed first must register with the Corporation to do so.

POI currency conversion must not be offered, as follows:

- On a Contactless Transaction (including any Contactless transit aggregated Transaction) that is equal to or less than the applicable CVM limit. POI currency conversion optionally may be offered on a Contactless Transaction that exceeds the CVM limit.
- On any Card or Account identified in the Mastercard Parameter Extract (MPE) as ineligible for POI currency conversion, including but not limited to:
- Any ATM or face-to-face Transaction effected with Mastercard and Maestro Prepaid Cards that have single or multi-currency features;
- Any Mastercard and Maestro branded debit Card that is a multi-currency Card where the Issuer’s associated account range for all cross-border Card-present Transaction Volume of a full calendar year is equal to or greater than fifty percent of its total Card-present Transaction Volume in the same year.
- On a Virtual Account used to purchase travel services pursuant to the Mastercard Enterprise Solution Wholesale Travel Program.

POI currency conversion may be offered, subject to all of the following conditions:

- No specific currency conversion method may be implemented as the default option, except that when POI currency conversion is offered on the Internet, a currency conversion option may be pre-selected. When POI Currency Conversion is offered for an e-commerce Transaction and the currency conversion option is pre-selected, the Cardholder must be informed of the pre-selection and provided with the means to decline the currency conversion;
- A Cardholder may not be required or encouraged (i.e., “steered”) in any manner to use POI currency conversion. For example, a POS Terminal must not ask or require a Cardholder to choose to have the Transaction completed in a particular currency, whether by selecting “YES” or “NO” or by displaying different currency selections in red and green colors, or otherwise;


# Acceptance Procedures

# 3.8.1 Cardholder Disclosure Requirements

- The offer must be presented in a clear manner and must not use biased or misleading language that may influence the Cardholder's currency selection; and
- In addition to meeting any requirement under applicable local law or regulation, the offer must comply with the following Cardholder disclosure requirements, as applicable.

NOTE: A modification to this Rule appears in the “Europe Region” section at the end of this chapter.

# 3.8.1 Cardholder Disclosure Requirements

Before an authorization or preauthorization request for the Transaction is submitted, and before the Cardholder decides the currency in which the Transaction is to be completed:

- The Cardholder must be clearly informed that the Cardholder has the right to choose the currency in which the Transaction will be completed;
- The Cardholder must be clearly informed of each of the following:
- Transaction amount in the local currency;
- Transaction amount in the billing currency;
- Currency conversion rate to be applied should the Transaction be completed in the billing currency;
- Any other fee that can be charged in the event the cardholder selects POI currency conversion;
- The Merchant and Terminal must honor Cardholder's currency selection;

# Each Terminal or Merchant Environment identified as a…

# Unattended POS Terminal

Must include the following message to the Cardholder when POI Currency Conversion is offered…

Before the Cardholder is asked to select a currency in which the Transaction is to be completed, the unattended POS Terminal must clearly disclose the following language, verbatim, to the Cardholder: "MAKE SURE YOU UNDERSTAND THE COSTS OF CURRENCY CONVERSION AS THEY MAY BE DIFFERENT DEPENDING ON WHETHER YOU SELECT YOUR HOME CURRENCY OR THE TRANSACTION CURRENCY."

If an unattended POS Terminal cannot comply with the Cardholder disclosure requirements set forth above, the Merchant must satisfy the requirements by some alternative means designed to ensure that the Cardholder understands the POI currency conversion before the Cardholder is asked to decide the currency the Transaction is to be completed in.

# ATM Terminal

Before the Cardholder is asked to select a currency in which the Transaction is to be completed, the ATM Terminal must clearly disclose the following language, verbatim, to the Cardholder: "MAKE SURE YOU UNDERSTAND THE COSTS OF CURRENCY CONVERSION AS THEY MAY BE DIFFERENT DEPENDING ON WHETHER YOU SELECT YOUR HOME CURRENCY OR THE TRANSACTION CURRENCY."


# Acceptance Procedures

# 3.8.2 Cardholder Disclosure - Transaction Receipt Information

Each Terminal or Merchant Environment identified as a… E-commerce Transaction

Must include the following message to the Cardholder when POI Currency Conversion is offered… Before the Cardholder is asked to select a currency in which the Transaction is to be completed, the Merchant's website must clearly disclose the following language, verbatim, to the Cardholder during the checkout process:

"MAKE SURE YOU UNDERSTAND THE COSTS OF CURRENCY CONVERSION AS THEY MAY BE DIFFERENT DEPENDING ON WHETHER YOU SELECT YOUR HOME CURRENCY OR THE TRANSACTION CURRENCY."

In its sole discretion, the Corporation may approve or reject the presentation or display of cardholder disclosure at the POI.

# 3.8.2 Cardholder Disclosure - Transaction Receipt Information

Refer to section 3.13 Transaction Receipts, 3.13.1 POS and Mastercard Manual Cash Disbursement Transaction Receipt Requirements, and section 3.13.2 ATM and Bank Branch Terminal Transaction Receipt Requirements regarding provision of Transaction receipts and the information that must be disclosed on a Transaction receipt when the Cardholder has chosen to use the POI currency conversion service to complete the Transaction.

# 3.8.3 Priority Check-Out

Before initiating POI Currency Conversion for a priority check-out Transaction, a Merchant must complete a written agreement with the Cardholder that specifies all of the following:

- The Cardholder has been offered a choice of currencies for payment, whether a Transaction should be completed in either the local currency or the billing currency;
- The Cardholder has agreed that POI Currency Conversion will take place;
- The specific Transaction currency agreed by the Cardholder;
- That the Cardholder expressly agrees to POI Currency Conversion;
- Any currency conversion commission, fees, or mark-up on the exchange rate; and
- If applicable, that the exchange rate will be determined by the Merchant at a later time, without additional consultation with the Cardholder.

If the Cardholder actively chooses POI Currency Conversion, the Transaction receipt must include the same disclosures previously provided to the Cardholder in addition to all other required information that is described in detail in Rule 3.8.2 Cardholder Disclosure —Transaction Receipt Information.

# 3.8.4 Transaction Processing Requirements

The currency chosen by the Cardholder must be indicated as the Transaction currency in DE 49 of Transaction messages.


# Acceptance Procedures

# 3.9 Multiple Transactions—Mastercard POS Transactions Only

The POI currency conversion indicator, pre-conversion currency, and amount must be provided in DE 54 of Financial Transaction/0200 messages and First Presentment/1240 messages. If the Cardholder does not choose to have the Transaction completed in the Cardholder’s billing currency, the Transaction must be completed and processed in the local currency. A refund Transaction must be processed in the same currency used when the returned goods or canceled services were purchased. Before offering POI currency conversion at an ATM Terminal, the Acquirer must either submit the proposed screen messages and a sample receipt to the Corporation for review and potential approval or implement screen messages and receipts in the form shown in Appendix F.

NOTE: The Mastercard standard disclaimer is shown in the Model Screen Offering POI Currency Conversion, Appendix F.

# 3.9 Multiple Transactions—Mastercard POS Transactions Only

All products and services purchased in a single Transaction must be included in one total amount on a single Transaction receipt and reflected in a single Transaction record, with the following exceptions:

- A Merchant may accept more than one payment method for a single purchase, provided that the Transaction record and receipt reflects only the portion of the purchase to be paid by means of an Account.
- A Merchant may complete a consumer’s purchase of multiple products or services by individually billing the products or services in separate Transactions to the same Account, in accordance with the acceptance procedures.

# 3.10 Partial Payment—Mastercard POS Transactions Only

A Merchant is prohibited from effecting a Transaction where only a part of the total purchase amount is included on the Transaction record and receipt, except in the following circumstances:

- The customer pays a portion of the total purchase amount by means of an Account and pays the remaining balance by another payment method, such as cash or check.
- The products or services will be delivered or performed after the Transaction date, one Transaction receipt represents a deposit, and the second Transaction receipt represents payment of the balance. The Merchant must note the words “deposit” and “balance” on the Transaction receipts as appropriate. The second Transaction receipt is contingent on the delivery or performance of the products or services, and must not be presented until after the products or services are delivered or performed.
- The Cardholder has agreed in writing to be billed by the Merchant in installments, and has specified the installment payment schedule and/or each installment payment amount to be billed to the Account.


# Acceptance Procedures

# 3.11 Specific Terms of a Transaction

The Merchant may impose specific terms governing a Transaction by, for example:

1. Legible printing of the specific terms on the Transaction receipt; or
2. Disclosing the specific terms by other means, such as by signage or literature, provided the disclosure is sufficiently prominent and clear so that a reasonable person would be aware of and understand the disclosure before the Transaction is completed.

Specific Transaction terms may include, for example, such words as “No Refunds,” “Exchange Only,” “In-Store Credit Only,” or “Original Packaging Required for Returns.” Specific terms may address such matters as late delivery, delivery charges, or insurance charges.

The specific terms printed on the Transaction receipt offered to the Cardholder will govern in the event of a dispute, subject to compliance with other Standards.

# 3.11.1 Specific Terms of an E-commerce Transaction

In an e-commerce Transaction:

1. A Cardholder may accept specific Transaction terms by electronic means (for example, by checking a box or clicking a “Submit” button indicating the acceptance of terms and conditions); and
2. A Merchant must clearly communicate, and the Cardholder must specifically accept, any terms concerning a recurring payment or installment billing Transaction arrangement separately from any other terms (for example, by checking a box or clicking a “Submit” button indicating the acceptance of recurring payment or installment billing terms and conditions).

The specific Transaction terms will govern in the event of a dispute, subject to compliance with other Standards, provided that such specific terms were disclosed to and accepted by the Cardholder before completion of the Transaction.

# 3.12 Charges for Loss, Theft, or Damage—Mastercard POS Transactions Only

A charge for loss, theft, or damage must be processed as a separate Transaction from the underlying rental, lodging, or other Transaction.

The Merchant must provide a reason for the charge and a reasonable estimate of the cost of repairs to the Cardholder. After gaining the Cardholder’s authorization of the charge and the estimated cost, the Merchant must process the Transaction as one of the following:

- A Card-present Transaction. For CVM requirements, see Rule 3.4.
- A fully authenticated e-commerce Transaction


# Acceptance Procedures

# 3.13 Transaction Receipts

The Transaction receipt must include a statement indicating that the estimated amount charged for repairs will be adjusted upon completion of the repairs and submission of the invoice for such repairs.

The final amount of a Transaction relating to repairs must not exceed the Merchant’s estimated amount. If the Merchant obtains a preauthorization for an estimated amount, and the Transaction amount exceeds the authorized amount, the Merchant may request an additional authorization. In connection with such Transactions, the Issuer must not place a hold on the Cardholder’s Account in excess of the authorized amount.

# 3.13 Transaction Receipts

A Transaction receipt (also called a Transaction Information Document, or TID) must be offered to the Cardholder upon completion of a Transaction as required by and in a form that is compliant with the Standards and applicable law or regulation.

All products and services purchased or cash disbursed in the same Transaction must be included on a single Transaction receipt. A Transaction receipt must also be offered for a refund Transaction.

# At POS Terminals

At a POS Terminal (including any MPOS or CAT device unless otherwise stated), a paper Transaction receipt must be offered to the Cardholder. A POS Terminal may also offer the Cardholder the option of receiving a Transaction receipt electronically in digital form, such as through email, text, Merchant website, or other electronic means. The offer of a Transaction receipt may be made verbally by the Merchant or electronically by the POS Terminal (such as a Cardholder-facing screen asking "Receipt? Press YES or NO" or "Paper receipt? Email receipt? No receipt?").

The following exceptions to the above Standard apply:

- A Transaction receipt is not required to be offered if the Transaction is a Contactless Transaction (including a Contactless transit aggregated Transaction) that is equal to or less than the CVM limit but must be provided (on paper or digitally) upon Cardholder request.
- The following POS Terminal types are not required to provide a Transaction receipt at the time the Transaction is conducted, provided the Merchant has a means by which to provide a Transaction receipt at a later date upon Cardholder request and clearly displayed the method for such request at the Merchant location:
- A POS Terminal identified as a CAT 1, CAT 2, or CAT 3 device and using MCC 5499 (Miscellaneous Food Stores - Convenience Stores, Markets, Specialty Stores); and
- An unattended contactless-only POS Terminal (see Rule 4.7 for information about contactless-only acceptance).


# Acceptance Procedures

# 3.13.1 POS and Mastercard Manual Cash Disbursement Transaction Receipt Requirements

If the means by which the Merchant will provide a Transaction receipt involves the storage, transmission, or processing of Card data, then the Acquirer must ensure such means comply with the Payment Card Industry Data Security Standard (PCI DSS).

- A contactless-only POS Terminal identified as a CAT 1, CAT 2, or CAT 3 device and using MCC 8398 (Organizations, Charitable and Social Service) offering a Transaction equal to or less than USD 15 (or local currency equivalent) may be deployed without the capability to provide a Transaction receipt at the time the Transaction is conducted or at a later date. The inability to provide a receipt must be clearly displayed on the CAT device prior to the Transaction being completed.
- An in-flight POS Terminal identified as a CAT 4 device must offer a Transaction receipt, as described in Appendix D.

# At ATM and Bank Branch Terminals

A Transaction receipt must be offered for a cash withdrawal or other financial Transaction occurring at an ATM or, if technically feasible, a Bank Branch Terminal.

A Transaction receipt may be paper or electronic, such as a digital receipt through email, text, Merchant website, or other electronic means. The offer of a Transaction receipt may be made verbally or electronically (such as a Cardholder-facing screen asking "Receipt? Press YES or NO" or "Paper receipt? Email receipt? No receipt?").

ATM cash withdrawals without paper receipts are allowed when the device is out of paper, the Cardholder being duly advised.

NOTE: A variation to this Rule provision appears in the "Europe Region" section at the end of this chapter.

# Card-not-present Transactions

A receipt must be provided for each Card-not-present Transaction. For each completed e-commerce Transaction, a printable receipt page must be displayed after the Cardholder confirms a purchase. With respect to an e-commerce Transaction, non-face-to-face recurring payment Transaction, or any other Card-not-present Transaction upon Cardholder request, a receipt may be sent to the Cardholder by email or other electronic means.

# 3.13.1 POS and Mastercard Manual Cash Disbursement Transaction Receipt Requirements

All of the following information must be included on a Transaction receipt (no other information is required):

1. The “doing business as” (DBA) Merchant name, city, state/province, and country, or the financial institution location as provided in DE 43 (Card Acceptor Name/Location).
2. The Transaction type (retail sale, cash disbursement, refund).
3. The primary account number (PAN), in compliance with Rule 3.13.3. When an Access Device is presented, the Transaction receipt must display the PAN (in truncated form) for the Account accessed by means of that Contactless Payment Device, which may differ from the


# Acceptance Procedures

# 3.13.2 ATM and Bank Branch Terminal Transaction Receipt Requirements

PAN on a Card linked to the same Account. If available, the truncated Card PAN may also be displayed for informational purposes.

1. A description and the price of each product and service purchased or returned, including applicable taxes, in detail sufficient to identify the Transaction.
2. The total Transaction amount and Transaction currency. If no currency is identified on the Transaction receipt, the Transaction is deemed to have taken place in the currency that is legal tender at the POI. If the Cardholder has chosen to use a POI currency conversion service to complete the Transaction as described in section 3.8 POI Currency Conversion, the Transaction receipt must disclose all of the following:
- The total Transaction amount in the local currency;
- The total Transaction amount in the converted currency as agreed to by the Cardholder;
- The currency symbol or code of each; and
- The currency conversion rate used.
3. The Transaction date. (For Transaction date requirements, see Appendix C.)
4. For Card-present Mastercard POS Transactions completed with a manual imprinter, a legible imprint of the Card (unless the Card is unembossed).
5. The authorization approval code, if obtained from the Issuer. If multiple authorizations are obtained over the course of the Transaction (as may occur for lodging, cruise line, or vehicle rental Transactions), all authorization numbers, the amounts authorized, and the date of each authorization must be included.
6. For a Chip Transaction, the application identifier (AID) and the application preferred name or application label.
7. For signature-based Transactions occurring at a Merchant that chooses to perform or is required by applicable law or regulation to perform signature collection, adequate space for the Cardholder’s signature on the Merchant’s copy (and optionally on the Cardholder’s copy). A space for the Cardholder’s signature should be omitted from the Transaction receipt if the Transaction is completed with a PIN or Consumer Device CVM (CDCVM) as the CVM or no CVM is used. The Transaction receipt may optionally indicate that successful PIN or CDCVM verification has occurred.

If personal identification is requested for a face-to-face unique Transaction or Manual Cash Disbursement Transaction, the personal identification type and number must not be recorded on the Transaction receipt (refer to Rule 3.1.1).

If a receipt is produced following an unsuccessful Transaction attempt, the receipt must indicate the response or failure reason.

NOTE: An addition to this Rule appears in the “Europe Region” section at the end of this chapter.

# 3.13.2 ATM and Bank Branch Terminal Transaction Receipt Requirements

All of the following information must be included on a Transaction receipt (no other information is required):

1. Identification of the Acquirer (for example, the institution name or logotype).
2. The ATM or Bank Branch Terminal location.


# Acceptance Procedures

# 3.13.3 Primary Account Number (PAN) Truncation and Expiration Date Omission

3. The Transaction amount (in a dual currency environment, the Transaction currency must be identified on the receipt; in all other environments, the Transaction currency symbol is recommended). If the Cardholder has chosen to use a POI currency conversion service to complete the Transaction as described in section 3.8 POI Currency Conversion, the Transaction receipt must disclose all of the following:

- The total Transaction amount in the local currency;
- The total Transaction amount in the converted currency as agreed to by the Cardholder;
- The currency symbol or code of each; and
- The currency conversion rate used.

4. The Transaction time and date.

5. The primary account number (PAN), in compliance with Rule 3.13.3. When an Access Device is presented, the Transaction receipt must display the PAN (in truncated form) for the Account accessed by means of that Contactless Payment Device, which may differ from the PAN on a Card linked to the same Account. If available, the truncated Card PAN may also be displayed for informational purposes.

6. The Transaction type (cash disbursement).

7. The Transaction sequence number.

8. An electronic recording of the magnetic stripe-read or chip-read Card data.

9. For a Chip Transaction, the application label and, at the Acquirer’s discretion, the Transaction certificate (in its entirety) and related data.

10. For Merchandise Transactions only, a statement that the Transaction was for the purchase of products or services.

An ATM or Bank Branch Terminal must clearly describe, by receipt, screen information, or both, the action taken by the Issuer in response to a Cardholder’s request (approved or rejected).

# 3.13.3 Primary Account Number (PAN) Truncation and Expiration Date Omission

A Transaction receipt generated by an electronic Terminal, whether attended or unattended, must not include the Card expiration date. In addition, a Transaction receipt generated for a Cardholder by an electronic Terminal, whether attended or unattended, must reflect only the last four digits of the primary account number (PAN). All preceding digits of the PAN must be replaced with fill characters, such as “X,” “*,” or “#,” that are neither blank spaces nor numeric characters.

The Corporation strongly recommends that if an electronic POS Terminal generates Merchant copies of Transaction receipts, the Merchant copies should also reflect only the last four digits of the PAN, replacing all preceding digits with fill characters, such as “X,” “*,” or “#,” that are neither blank spaces nor numeric characters.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# 3.13.4 Prohibited Information

The Transaction receipt or any other Acquirer or Merchant document must not reflect:


# Acceptance Procedures

# 3.13.5 Standard Wording for Formsets

- The PIN, any part of the PIN, or any fill characters representing the PIN; or
- The Card validation code 2 (CVC 2).

# 3.13.5 Standard Wording for Formsets

A formset is a Transaction receipt produced by a manual imprinter. The following wording, in English, the local language, or both (or words to similar effect) should appear on the Cardholder copy of a formset:

“IMPORTANT—retain this copy for your records.”
In addition, the following wording (or words to similar effect) should appear on each copy of a formset for the specified Transaction type.

- Retail Sale and Manual Cash Disbursement Transactions—“The Issuer of the Card identified on this receipt is authorized to pay the amount shown as ‘total’ upon proper presentation. I promise to pay such total (together with any other charges due thereon) subject to and in accordance with the agreement governing the use of such Card.”
- Refund Transactions—“I request that the above Cardholder account be credited with the amount shown as ‘total’ because of the return of, or adjustments on, the goods, services, or other items of value described.”

# 3.14 Returned Products and Canceled Services

A Merchant is required to accept the return of products or the cancellation of services unless specific disclosure was provided at the time of the Transaction.

Upon the return in full or in part of products or the cancellation of a service purchased with a Card, or if the Merchant agrees to a price adjustment on a purchase made with a Card, the following applies:

- If a Mastercard Card was used, the Merchant may not provide a price adjustment by any means other than a credit to the same Card Account used to make the purchase (or a Card reissued by the same Issuer to the same Cardholder).
- If a Maestro Card was used, a Merchant may offer a price adjustment by means of a credit, provided the credit is posted to the same Card Account used to make the purchase (or a Card reissued by the same Issuer to the same Cardholder).

In a Card-present environment, the Merchant should ask the Cardholder for a Transaction receipt identifying (by means of a truncated PAN) the payment card used for the original purchase Transaction (but be aware that if an Access Device was used, the PAN on a Card linked to the same Account may not match the PAN on the receipt).

In the case of involuntary refunds by airlines or other Merchants as required by law, or if the Card used to make the purchase is not available, or the Merchant’s refund Transaction authorization request is declined, the Merchant must act in accordance with its policy for adjustments, refunds, returns, or the like, which may include providing a cash, check, or prepaid card refund.


# Acceptance Procedures

# 3.14.1 Refund Transactions

Upon Mastercard approval, a Merchant may offer Cardholders the option of a “fast refund” using the MoneySend Payment Transaction, as described in the Mastercard MoneySend and Funding Transactions Program Standards. The fast refund using the MoneySend Payment Transaction may be submitted to the same Account used in the original purchase (as identified on the purchase Transaction receipt) or to a different Account, for example when the Issuer of the Card or Access Device used in the original purchase declines a refund Transaction authorization request. A Merchant enabled for the fast refund using the MoneySend Payment Transaction must continue to support and offer the refund Transaction.

NOTE: A modification to this Rule appears in the “Europe Region” section at the end of this chapter.

# 3.14.1 Refund Transactions

A Merchant must process a refund Transaction only for the purpose of crediting funds to a Cardholder for returned products, canceled services, or a price adjustment related to a prior purchase.

The refund Transaction:

- must be processed in the same currency as used in the related purchase Transaction; and
- must not exceed the authorized amount of the related purchase Transaction, except as may occur due to currency value fluctuations or when the Merchant agrees to credit return shipping costs.

Key entry of Card data is not permitted for Maestro refund Transactions conducted in a Card-present environment. For information about chip-based refund Transactions, refer to the M/Chip Requirements for Contact and Contactless manual.

# When the original purchase was…

# A Chip Transaction

Then the refund Transaction…

May be completed without Chip Card authentication, Cardholder verification (CVM), or online authorization from the Issuer. No Transaction cryptogram will be produced for a refund Transaction unless online authorization occurs. Refer to the M/Chip Requirements for Contact and Contactless manual for details. Authorization may occur at the Merchant's option but PIN data is not required; an Issuer must not decline a refund Transaction solely because of the absence of PIN data.

# A dual message magnetic stripe Transaction

May be completed without CVM or online authorization from the Issuer.

# A single message magnetic stripe Transaction

May be completed without CVM. In a Card-present environment, the Card must be read by the POS Terminal; in a Card-not-present environment, the Card data may be key-entered. Authorization must occur but PIN data is not required; an Issuer must not decline a refund Transaction solely because of the absence of PIN data.


# Acceptance Procedures

# 3.15 Transaction Records

The Cardholder must be provided a copy of the refund Transaction receipt containing:

- The date of the refund;
- A description of the returned products, canceled services, or adjustment made; and
- The amount of the refund.

NOTE: Modifications to this Rule appear in the "Europe Region," "Middle East/Africa Region," and "Additional U.S. Region and U.S. Territory Rules" sections at the end of this chapter.

# 3.15 Transaction Records

Each Transaction record must reflect a valid and accurate Transaction date, as defined in Appendix C. A Merchant must provide all products and services included in a Transaction record to the Cardholder at the time of the Transaction unless, prior to completion of the Transaction, the Cardholder agrees to a delayed delivery of products or performance of services.

The following applies with respect to Mastercard POS Transactions:

1. The Merchant must submit each purchase and refund Transaction record to its Acquirer no later than three business days after the Transaction date.
2. Upon providing a full or partial refund for returned products or canceled services, the Merchant must submit the refund Transaction record to its Acquirer within 15 days of the refund Transaction receipt date, in order to avoid a Credit Not Processed chargeback.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region" section at the end of this chapter.

# 3.15.1 Transaction Presentment Time Frames

Upon receiving the Transaction record, the Acquirer must present the Transaction within the applicable presentment time frame in order to avoid an Expired Chargeback Protection Period chargeback.

The Acquirer must present a Transaction to the Issuer within the following presentment time frames:

- The authorization was identified as a preauthorization (DE 61 [Point-of-Service (POS) Data], subfield 7 (POS Transaction Status) contains a value of 4 [Preauthorized request]) and the transaction was presented or completed more than 30 calendar days after the latest authorization approval date.
- The authorization was not identified as a preauthorization and the transaction was presented more than seven-calendar days after the authorization approval date.
- For a Mastercard purchase Transaction, no later than 30 calendar days after the latest authorization approval date for a preauthorization or no later than seven calendar days after the authorization approval date for any other authorization, or for an offline chip-approved purchase Transaction or other Transaction not requiring online authorization by the Issuer, seven calendar days after the Transaction date.
- Seven calendar days after the Transaction date of a Maestro purchase Transaction;


# Acceptance Procedures

# 3.15.2 Retention of Transaction Records

- Seven calendar days after the Transaction date of an ATM Transaction;
- Within one calendar day of the authorization date of a Payment Transaction;
- Within 14 calendar days of the authorization date of a Contactless transit aggregated Transaction; and
- Within five calendar days of the Transaction date of a refund Transaction (the date on the Transaction receipt, or if the refund Transaction was authorized by the Issuer, then the authorization date).

An Issuer must accept Transactions submitted beyond the applicable time frame if the Cardholder's Account is in good standing or the Transaction can be otherwise honored and posted.

# 3.15.2 Retention of Transaction Records

The Acquirer must retain a record of each Transaction it receives or sends for a minimum of 13 months, or such longer period as may be required by applicable law or regulation.

# Variations and Additions by Region

The remainder of this chapter provides modifications to the Standards set out in this chapter. The modifications are organized by region or country and by applicable subject title.

# Asia/Pacific Region

The following modifications to the Rules apply in the Asia/Pacific Region or in a particular Region country or countries. Refer to Appendix A for the Asia/Pacific Region geographic listing.

# 3.14 Returned Products and Canceled Services

# 3.14.1 Refund Transactions

In Australia, the Rule on this subject is modified as follows. When the original purchase Transaction includes a surcharge, the refund Transaction must include the full or prorated surcharge amount.

# 3.15 Transaction Records

Effective 3 April 2024 for India Domestic Transactions, the Rule on this subject is modified as follows:

1. A purchase Transaction must be submitted to its Acquirer in accordance with its Merchant Agreement and in compliance with all applicable laws and regulations.
2. Upon providing a full or partial refund for returned products or canceled services, the Merchant must submit the refund Transaction record to its Acquirer in accordance with its Merchant Agreement and in compliance with all applicable laws and regulations.


# Acceptance Procedures

# 3.15.1 Transaction Presentment Time Frames

Effective 3 April 2024 for India Domestic Transactions, the Rule on this subject is modified as follows.

The Acquirer must present a Transaction to the Issuer within the following presentment time frames:

- Within one calendar day of the authorization approval date of a Payment Transaction;
- Within four calendar days of the final authorization approval date for all other Transactions.

# Canada Region

The following modifications to the Rules apply in the Canada Region. Refer to Appendix A for the Canada Region geographic listing.

# 3.3 Obtaining an Authorization

# 3.3.1 Mastercard POS Transaction Authorization Procedures

The requirement to obtain online authorization from the Issuer for a refund Transaction does not apply to Merchants in the Canada Region.

# Europe Region

The following modifications to the Rules apply in the Europe Region or in a particular Region country or countries. Refer to Appendix A for the Europe Region, Non-Single European Payments Area (Non-SEPA) and Single European Payments Area (SEPA) geographic listing.

# 3.1 Card-Present Transactions

# 3.1.1 Mastercard Card Acceptance Procedures

# Suspicious Cards

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A suspicious Card must be identified in the field of the authorization message and with the value specified by the registered switch of the Customer's choice.

# 3.2 Card-Not-Present Transactions

The following Rule variation applies with respect to Merchants located in the Europe Region. A Merchant must not refuse to complete a Remote Electronic Transaction solely because the Issuer does not request Strong Customer Authentication (SCA), as Issuer exemptions from SCA may apply.


# Acceptance Procedures

# 3.3 Obtaining an Authorization

A Merchant must not refuse to complete a Remote Electronic Transaction solely because the Issuer does not support the Mastercard Identity Check Program, given that the Issuer may use alternative technical solutions for SCA. The liability shift applies equally to EMV 3DS as to 3DS 1.0.2. Refer to the Chargeback Guide for more information.

# 3.3 Obtaining an Authorization

# 3.3.1 Mastercard POS Transaction Authorization Procedures

In the EEA, UK and Gibraltar, Contactless transit aggregated and transit debt recovery Transactions and automated fuel dispenser (AFD) Transactions (MCC 5542) are not excluded from the requirement for a Merchant to inform the Cardholder of any estimated amount for which authorization will be requested and to obtain the Cardholder's consent to the amount before initiating the authorization request. As an example, a Merchant may comply with this information requirement by allowing the Cardholder to select the preauthorization amount at the Terminal or via a clearly readable sticker or other notice placed at the Point-of-Interaction (POI).

At an unattended POS Terminal, the Cardholder may express consent to the amount by continuing with the Transaction.

# Authorization of Lodging, Cruise Line, and Vehicle Rental Transactions

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A partial approval must be identified in the field and with the value specified by the registered switch of the Customer's choice.

# Authorization When the Cardholder Adds a Gratuity

In the EEA, the Rule on this subject is modified as follows. A partial approval must be identified in the field and with the value specified by the registered switch of the Customer's choice.

# 3.3.2 Maestro POS Transaction Authorization Procedures

In the Europe Region, the Rule on this subject is modified as follows. A Merchant must inform the Cardholder of any estimated amount for which authorization will be requested and must obtain the Cardholder's consent to the amount before initiating the authorization request. This requirement does not apply to:

- Contactless transit aggregated Transactions and transit debt recovery Transactions,
- Automated fuel dispenser (AFD) Transactions (MCC 5542), or
- An authorization requested for an amount otherwise confirmed by the Cardholder to be the final Transaction amount.

In the EEA, UK and Gibraltar, the above Rule is modified as follows.


# Acceptance Procedures

# 3.5 Maestro Cardholder Verification Requirements

A Merchant must inform the Cardholder of any estimated amount for which authorization will be requested and must obtain the Cardholder's consent to the amount before initiating the authorization request also for Contactless transit aggregated or transit debt recovery Transactions and for automated fuel dispenser (AFD) Transactions (MCC 5542). As an example, a Merchant may comply with this information requirement by allowing the Cardholder to select the preauthorization amount at the Terminal or via a clearly readable sticker or other notice placed at the Point of Interaction.

At an unattended POS Terminal, the Cardholder may express consent to the amount by continuing with the Transaction.

To extend the duration of the reason code 4808 chargeback protection period afforded for each approved authorization, the Merchant may submit additional authorization requests for the same Transaction on later dates, as described in Rule 2.1.

# 3.5 Maestro Cardholder Verification Requirements

In the Europe Region, the Rule on this subject is modified as follows. The Cardholder must be verified by a PIN for each Contactless Transaction conducted in the Europe Region with a Card issued in the Europe Region that exceeds the applicable Contactless Transaction CVM limit amount.

# 3.8 POI Currency Conversion

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. The currency chosen by the Cardholder and the pre-conversion currency and amount must be identified in the fields specified by the registered switch of the Customer's choice. The POI currency conversion indicator must be populated in the field and with the value specified by the registered switch of the Customer's choice.

# 3.13 Transaction Receipts

In the Europe Region, the Rule on this subject is modified as follows.

# At POS Terminals

The Merchant is not required to automatically offer a paper Transaction receipt to the Cardholder. If the Cardholder expressly requests a receipt, one must be provided, either on paper or digitally.

In the following specific cases, a paper Transaction receipt must be automatically offered:

- A Merchant that requires a paper receipt for a refund must offer the Cardholder a paper receipt;
- A Merchant that applies an exchange or return policy must offer a paper receipt on which the policy is stated, in accordance with Rule 3.11 Specific Terms of a Transaction.
- If a paper receipt is otherwise required by applicable law or regulation (e.g., to document a warranty).


# Acceptance Procedures

# 3.13.1 POS and Mastercard Manual Cash Disbursement Transaction Receipt Requirements

If the Merchant provides a paper cash register receipt, tax invoice, or other type of receipt for a Transaction, it is not required to additionally offer a paper POS Terminal receipt. Provision of the Transaction receipt by digital (non-paper) means is strongly recommended. When the Merchant offers a Transaction receipt by digital means, it must clearly inform the Cardholder how to access the receipt and whether the Merchant needs to process any additional Personal Data, such as Cardholder contact details, to enable access to the receipt. The Merchant must limit the processing of the Cardholder's additional Personal Data only for the purpose of making the receipt available to the Cardholder. The Merchant must ensure that the digital receipt is promptly available. The Merchant's copy of the Transaction receipt need not be on paper and may be stored and provided in digital form.

At a POS Terminal in France, a paper Transaction receipt must not be automatically provided. A paper Transaction receipt must be provided in the following cases:

- if the Cardholder expressly requests one,
- in case of cancellation of the Transaction,
- if the Transaction is for a refund,
- if the purchase is of durable goods for which a legal guarantee applies, and
- in any other case specified in applicable law, as amended from time to time.

When a paper Transaction receipt is not provided to the Cardholder, the Merchant is permitted to provide a digital receipt.

# At ATM Terminals

ATM Terminals that do not have receipt-printing capability may be deployed in the Europe Region. For every completed Transaction, an ATM Terminal with receipt printing capability must make a receipt available to the Cardholder, either automatically or upon the Cardholder's request. A cash withdrawal without a printed receipt is allowed only if the ATM Terminal does not have receipt-printing capability or is out of paper. The Cardholder must be advised prior to the Transaction that a printed receipt is not available.

As an exception to this Rule, an ATM Terminal in France must have receipt-printing capability and must not automatically provide a paper Transaction receipt. A paper Transaction receipt must be provided in the following cases:

- upon Cardholder request,
- in case of cancellation of the Transaction, and
- in any other case specified in applicable law, as amended from time to time.

# 3.13.1 POS and Mastercard Manual Cash Disbursement Transaction Receipt Requirements

In the Europe Region, the Rule on this subject is modified as follows.


# Acceptance Procedures

# 3.13.3 Primary Account Number (PAN) Truncation and Expiration Date Omission

A Terminal may print the Transaction amount in the Transaction currency and a maximum of one different currency on the Transaction receipt. The Transaction amount printed in a different currency must appear at the bottom of the receipt with a clear indication that it is being provided only for information purposes.

In the Netherlands, the Rule on this subject is replaced with the following: A Transaction receipt generated by an electronic Terminal, whether attended or unattended, must not include the Card expiration date. In addition, a Transaction receipt generated for a Cardholder by an electronic Terminal, whether attended or unattended, must reflect a maximum of four of the last seven digits of the PAN. All non-reflected digits of the PAN must be replaced with fill characters, such as “X,” “*,” or “#.” The Corporation strongly recommends that if a POS Terminal generates a Merchant copy of the Transaction receipt, the Merchant copy should also reflect a maximum of four of the last seven digits of the PAN, replacing all non-reflected digits with fill characters that are neither blank spaces nor numeric characters, such as “X,” “*,” or “#.”

# 3.14 Returned Products and Canceled Services

For intra-European and inter-European Transactions, the Rule on this subject is modified as follows: If a Merchant agrees to provide a refund or price adjustment, it may provide the refund or price adjustment by any means.

# 3.14.1 Refund Transactions

For intra-European and inter-European Transactions, the Rule on this subject is modified as follows:

1. For each refund Transaction, a service fee is paid by the Issuer to the Acquirer. Such fee is independent of the interchange fee associated with the corresponding POS Transaction.
2. The refund Transaction may be used to return the unused gambling value to the Cardholder, up to the amount of the original purchase occurring on a Maestro Card. The Gaming Payment Transaction must be used to transfer gambling winnings to the Cardholder.
3. A refund of a Maestro Transaction may be processed to a Card as a MO/TO Transaction using manual key entry of the PAN and without reading the magnetic stripe or chip on the Card. An Issuer must technically support Maestro refund Transactions processed as MO/TO Transactions.
4. A Transaction printout must be generated for a refund Transaction, with the exception of a refund processed as a MO/TO Transaction.


# Acceptance Procedures

# Latin America and the Caribbean Region

The following modifications to the Rules apply in the Latin America and the Caribbean Region. Refer to Appendix A for the Latin America and the Caribbean Region geographic listing.

# 3.4 Mastercard Cardholder Verification Requirements

In Peru, the Rule on this subject is modified as follows. A Merchant Terminal located in Peru may be configured so that “No CVM” is the only CVM supported for Chip Transactions conducted with a Chip Card issued in Peru, provided the Transaction amount is equal to or less than PEN 80. In this Terminal configuration, “No CVM” replaces both signature and PIN in the Terminal’s list of supported CVMs. The Acquirer must only use this Terminal configuration for Domestic Peru Transactions.

# 3.5 Maestro Cardholder Verification Requirements

In the Latin America and the Caribbean Region, the Rule on this subject is modified as follows. The Cardholder must be verified by a PIN for:

- Each Maestro Contactless Transaction conducted in Brazil, Chile, or Colombia with a Card issued in Brazil, Chile, or Colombia that exceeds the applicable Contactless Transaction CVM limit amount, and
- Each Maestro Magnetic Stripe Mode Contactless Transaction conducted in Brazil with a Card issued in Brazil that exceeds BRL 50. A CVM is not required for a Magnetic Stripe Mode Contactless Transaction that is less than or equal to BRL 50.

# Middle East/Africa Region

The following modifications to the Rules apply in the Middle East/Africa Region. Refer to Appendix A for the Middle East/Africa Region geographic listing.

# 3.14 Returned Products and Canceled Services

# 3.14.1 Refund Transactions

In Angola, Botswana, Comoros, Democratic Republic of the Congo, Djibouti, Eritrea, Ethiopia, Ghana, Gambia, Lesotho, Liberia, Madagascar, Malawi, Mauritius, Mozambique, Namibia, Nigeria, Rwanda, Seychelles, Sierra Leone, Somalia, South Sudan, Swaziland, Tanzania, Uganda, Zambia, and Zimbabwe, the Rule on this subject is modified as follows with respect to Maestro POS Transaction refunds: The refund Transaction may be used to return the unused gambling value to the Cardholder, up to the amount of the original purchase occurring on a Maestro Card. The Gaming Payment Transaction must be used to transfer gambling winnings to the Cardholder.


# Acceptance Procedures

# United States Region

The following modifications to the Rules apply in the United States (U.S.) Region. Refer to Appendix A for the U.S. Region geographic listing.

# 3.3 Obtaining an Authorization

# 3.3.1 Mastercard POS Transaction Authorization Procedures

The requirement to obtain online authorization from the Issuer for a refund Transaction does not apply to Merchants in the U.S. Region.

# Authorization When the Cardholder Adds a Gratuity

In the U.S. Region, the Rule on this subject is modified as follows. For Mastercard POS Transactions effected at a U.S. Region Merchant with a Mastercard Card issued in the U.S. Region, when a preauthorization or an undefined authorization is obtained:

- If the Transaction is a Chip/PIN Transaction, Contactless Transaction, Mastercard Consumer-Presented QR Transaction, or Card-not-present Transaction identified other than as described below, any gratuity must be included in the authorization request. A gratuity must not be added to the authorized amount.
- If the Transaction is a Card-not-present Transaction identified with MCC 5812 (Eating Places, Restaurants) or MCC 5814 (Fast Food Restaurants), a gratuity may be added after authorization is obtained, as follows:
- If the gratuity does not exceed 30 percent of the authorized amount, then no additional authorization is needed.
- If the gratuity exceeds 30 percent of the authorized amount, then the Merchant may request an incremental authorization for the amount in excess of the authorized amount.
- For all other Transaction types, a gratuity may be added after authorization is obtained, as follows:
- If the gratuity does not exceed 30 percent of the authorized amount, then no additional authorization is needed.
- If the gratuity exceeds 30 percent of the authorized amount, then the Merchant may request an incremental authorization for the amount in excess of the authorized amount.

The Issuer must not place a hold on the Cardholder’s Account in excess of the total authorized amount or implied authorized amount (inclusive of the 30 percent tolerance, when applicable).

# 3.5 Maestro Cardholder Verification Requirements

In the U.S. Region, the Rule on this subject is modified as follows. The Cardholder must be verified by a PIN for each Maestro Contactless Transaction that exceeds the applicable Contactless Transaction CVM limit amount.



123
# Acceptance Procedures

# Additional U.S. Region and U.S. Territory Rules

No PIN is required when a POS Transaction is conducted as described in “PIN-less Single Message Transactions” in Chapter 4, or for e-commerce Transactions (including Non-Mastercard BIN Maestro card-not-present debit card Transactions).

# Additional U.S. Region and U.S. Territory Rules

The following variations and additions to the Rules apply in the United States Region and in American Samoa, Guam, Northern Mariana Islands, Puerto Rico, and the U.S. Virgin Islands (herein, “the U.S. Territories”). These Rules apply in addition to any that apply within the Asia/Pacific Region, with respect to Customers located in American Samoa, Guam, and Northern Mariana Islands; the Latin America and the Caribbean Region, with respect to Customers located in Puerto Rico and the U.S. Virgin Islands; and the United States Region, with respect to U.S. Region Customers.

# 3.14 Returned Products and Canceled Services

# 3.14.1 Refund Transactions

In the U.S. Region and U.S. Territories, the Rule on this subject is modified as follows. The refund Transaction must include a full or prorated Brand-Level Surcharge or Product-Level Surcharge amount, as the terms Brand-Level Surcharge and Product-Level Surcharge are defined in section 5.12.2, "Charges to Cardholders" of the Mastercard Rules, when the original purchase Transaction included a Brand-Level Surcharge or Product-Level Surcharge.
