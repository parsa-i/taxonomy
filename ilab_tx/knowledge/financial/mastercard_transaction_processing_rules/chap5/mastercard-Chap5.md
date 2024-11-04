# Card-Not-Present Transactions

# 5.1 Electronic Commerce Transactions

An electronic commerce (“e-commerce”) Transaction must be authorized by the Issuer, in accordance with the authorization requirements described in Chapter 2. An e-commerce Transaction must not be effected using contactless payment, contactless payment or Mastercard Consumer-Presented QR payment functionality, or as a purchase with cash back Transaction.

NOTE: Additions to this Rule appear in the “Asia/Pacific Region” and “Europe Region,” and “Middle East/Africa Region” sections at the end of this chapter.

# 5.1.1 Acquirer and Merchant Requirements

Each Acquirer and Merchant conducting any e-commerce Transactions must comply with the following requirements:

1. The Merchant must display the appropriate Acceptance Marks on its website where payment methods are listed, in accordance with the Standards set forth in Chapters 4 and 5 of the Mastercard Rules.
2. The Merchant must provide a mailing address and a contact telephone number or email address for customer queries. This information may be displayed on any page within the Merchant’s website, but must be readily accessible to a Cardholder, and remain displayed for at least 90 calendar days after the last day on which a Transaction was performed.
3. The Merchant must clearly display price information, including currency, and the details of the timing of billing and fulfillment of Transactions, and provide a function for Cardholders to confirm a purchase before the completion of the sale.
4. For each Merchant and each 3-D Secure Service Provider (as defined in Chapter 7 of the Mastercard Rules) transacting under the Mastercard® Identity Check program, the Acquirer must ensure the Merchant is assigned a Merchant ID and uses the Mastercard Directory Server to complete the authentication if the Transaction is submitted for authorization and clearing (unless such Transaction is submitted via an alternate switch due to regulatory reasons), and ensure that the Merchant correctly populates all UCAF fields with required data elements and complies with the Mastercard Identity Check Standards. Refer to the Mastercard Identity Check Program for more information.
5. The Transaction amount used in the authorization message for a CIT must match the value of the products and services in the Cardholder’s purchase order, including any additional charges for posting and packing, etc.
6. If the purchase will be delivered in multiple shipments, the Merchant must notify the Cardholder and ensure that the combined amount of all shipments does not exceed the total purchase amount agreed with the Cardholder. The Merchant must obtain the Cardholder’s agreement to any increase in the purchase amount as a result of multiple or partial deliveries. Each shipment, and any increase to the original agreed purchase amount, must be processed by the Merchant as a separate authorized Transaction. Each subsequent authorization request initiated by the Merchant after the initial CIT must be identified with.


# Card-Not-Present Transactions

# 5.1.1 Acquirer and Merchant Requirements

the MIT value of M205 (Partial Shipment) in DE 48, subelement 22 (Multi-purpose Merchant Indicator), subfield 5 (Cardholder/Merchant Initiated Transaction Indicator).

1. If the products or services purchased are not available at time of the Transaction, the Merchant must inform the Cardholder and obtain the Cardholder’s agreement to a delayed delivery (specifying the anticipated delivery date) before proceeding with the Transaction.
2. The Merchant must advise the Cardholder if the products or services ordered will not be delivered within the time frame originally disclosed to and agreed with the Cardholder. The Cardholder must be notified of the new anticipated delivery timeframe and given an opportunity to cancel the Transaction.
3. The information provided on any email acknowledgment of the Cardholder’s order must comply with the Transaction receipt requirements described in Chapter 3.
4. For a physical or digital product or a sample of the physical or digital product provided to a Cardholder by a negative option billing Merchant for a trial period, the trial period begins on the date that the Cardholder receives the product. For purposes of this Rule 5.1.1, a trial period means a preset length of time during which the Cardholder may evaluate the characteristics of the product such as its quality or usefulness to determine whether the Cardholder wants to either:
5. - Purchase the product on a one-time basis or recurring basis; or
- Return the product (if possible) to the negative option billing Merchant.

If the Merchant is a negative option billing Merchant, then the Merchant must provide a direct link to an online cancellation procedure for recurring payment Transactions on the website on which the Cardholder initiated an agreement with the Merchant to bill the Cardholder on a recurring basis for one or more physical or digital products provided by the Merchant through the Merchant’s website.

In addition, with respect to Maestro e-commerce Transactions:

1. The Acquirer and Merchant must be capable of accepting PANs between 13 and 19 digits in length and sending the full unaltered PAN and the expiration date (in MMYY format) to the Interchange System. Transactions must not be declined by the Merchant or Acquirer as a result of edits or validations performed on the BIN/IIN or expiration date;
2. The Merchant must support Mastercard Identity Check;
1. For the EMV 3D Secure 2.0 specification, a Merchant must support both browser and in-app Transactions;
2. For the 3D Secure 1.0 specification, a Merchant must support browser Transactions and may support in-app Transactions;
3. The Acquirer and Merchant must support the passing of authentication data in the Universal Cardholder Authentication Field (UCAF);
4. The Acquirer must support the 3D Secure Merchant Plug-in, and be capable of handling Transactions within a 3D Secure environment;
5. The Merchant must provide a set of “help” functions to help Cardholders that have not yet been enabled by their Issuers for transacting via the Internet; and
6. On an ongoing basis, the Acquirer must educate its Merchants to ensure that each Merchant has an understanding of the special risks and responsibilities associated with accepting Transactions in an e-commerce environment.



176
# Card-Not-Present Transactions

# 5.1.2 Issuer Requirements

NOTE: Modifications to this Rule appear in the “Asia/Pacific Region,” "Europe Region," "Latin America and the Caribbean Region," "Middle East/Africa Region," and the "Additional U.S. Region and U.S. Territory Rules" sections at the end of this chapter.

An Issuer must approve or decline each e-commerce Transaction authorization request. Call referrals are not permitted.

A Region that previously implemented an intraregional Merchant-only liability shift for e-commerce Transactions may agree to require Issuers in that Region to implement Mastercard Identity Check.

An Issuer that uses Mastercard Identity Check to verify its Cardholders must:

- Use the Mastercard Secure Payment Application (SPA) algorithm to generate the Accountholder Authentication Value (AAV); and
- Verify the validity of the AAV when present in DE 48, subelement 43 of the authorization request message, or participate in the Mastercard Identity Check AAV Verification Service.

Mastercard Identity Check liability shifts applicable to e-commerce Transactions conducted with a Mastercard Card are described in the Chargeback Guide.

Refer to the Chargeback Guide for information about using message reason code 4841 (Cancelled Recurring Transactions and Digital Goods Purchases Under USD 25) to charge back a Transaction under USD 25 involving the purchase of Digital Goods.

The following applies with respect to a Maestro Card Program:

1. The Issuer is encouraged but not required to permit a Maestro Cardholder to engage in e-commerce Transactions. An Issuer that permits its Maestro Cardholders to perform e-commerce Transactions must be capable of recognizing and processing these Transactions when presented by an Acquirer.
2. The Issuer should provide a registration and set-up process for Cardholders wishing to engage in e-commerce Transactions.
3. The Issuer must provide a Cardholder wishing to engage in e-commerce Transactions with a PAN of between 13 and 19 digits in length and an expiration date in MMYY format. The PAN must start with a Maestro BIN/IIN, which may be a BIN that is currently used by the Issuer. The Issuer may optionally use a PAN that is different from the PAN displayed on the Card (a “pseudo PAN”). If a pseudo PAN is used, it must be static and have an expiration date that does not exceed five years from the PAN issuance date.
4. The Issuer must implement security techniques between the Cardholder interface device and the Issuer server to guard against unauthorized Transactions.
5. The Issuer is responsible for deciding which CVMs are acceptable for the completion of e-commerce Transactions, and may choose to request that a Cardholder use a chip/hardware authentication device.
6. An Issuer should educate Cardholders of the risks of releasing Card details and PINs into open networks and entering PINs into public terminals without using the approved methods.


# Card-Not-Present Transactions

# 5.1.3 Use of Static AAV for Card-not-present Transactions

7. An Issuer may directly implement Mastercard Identity Check and register its Cardholders and each Cardholder’s authentication information, or delegate a specific implementation and registration function to a designated Service Provider, in accordance with the set-up requirements provided to the Corporation by the Issuer. The Issuer must ensure that Cardholders are properly identified if issuing certificates.

8. The Issuer must perform an appropriate risk assessment on any Transaction for which the UCAF field (data element 48, subelement 43) contains a Corporation-assigned static AAV.

9. The Issuer is responsible for fraud in connection with any e-commerce Transaction that the Issuer has approved, unless it can be proved that the Merchant and/or Acquirer participated in the fraud or the Merchant Website does not support the passing of UCAF data. However, the Issuer will have a chargeback right for fraudulent Transactions containing the Corporation-assigned static AAV in the UCAF field.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," "Europe Region," "Latin America and the Caribbean Region," "Middle East/Africa Region," and the "Additional U.S. Region and U.S. Territory Rules" sections at the end of this chapter.

# 5.1.3 Use of Static AAV for Card-not-present Transactions

NOTE: A Rule on this subject appears in the “Europe Region” section of this chapter.

# 5.1.4 Debit Small-Ticket Digital Transaction Program: Brazil Only

NOTE: A Rule on this subject appears in the “Latin America and the Caribbean Region” section of this chapter.

# 5.2 Mail Order and Telephone Order (MO/TO) Transactions

The following requirements apply to mail order and telephone (“phone”) order (MO/TO) Transactions effected with a Mastercard Account, and where supported, a Maestro Account, including phone order Transactions conducted with Integrated Voice Response (IVR) technology. MO/TO Transactions are supported for Maestro in some of the Europe Region countries, India, and the United States Region and U.S. Territories only.

1. MO/TO Transactions must not be effected using contactless payment, Mastercard Consumer-Presented QR payment, or as purchase with cash back Transactions. Manual key entry of the PAN is the normal method of performing a MO/TO Transaction. Online authorization is required.
2. The Issuer must approve or decline each authorization request. A call referral is an invalid response to a MO/TO Transaction authorization request and must be treated by the Acquirer and the Merchant as a decline.
3. There is no Cardholder verification procedure for MO/TO Transactions; however, an Acquirer and Merchant may choose to support Mastercard SecureCode or Identity Check for.


# Card-Not-Present Transactions

# 5.3 Credential-on-File Transactions

Mastercard phone order Transactions conducted with Integrated Voice Response (IVR) technology.

4. The Merchant must not request an authorization, in a single message environment, or submit a Transaction to the Acquirer for presentment, in a dual message environment, until the products and services are available for delivery.

NOTE: Additions to this Rule appear in the “Europe Region” section and, pertaining to India, in the “Asia/Pacific” sections at the end of this chapter.

# 5.3 Credential-on-File Transactions

A Credential-on-file Transaction occurs when a Cardholder expressly authorizes a Merchant to store the Cardholder’s Mastercard or Maestro Account data (meaning PAN and expiration date) for subsequent use in connection with one or more later Transaction(s) with that Merchant and subsequently authorizes that Merchant to use the stored Mastercard or Maestro Account data in one or more Transaction(s).

For authorization, a Credential-on-file Transaction must contain the Credential-on-file indicator, which is a value of 10 (Credential on File) in DE 22 (Point-of-Service Entry Mode), subfield 1 (POS Terminal PAN Entry).

For clearing, a Credential-on-file Transaction must contain the Credential-on-file indicator, which is a value of 7 (Credential on File) in DE 22 (Point-of-Service Entry Mode), subfield 7 (Card Data Input Mode).

A Transaction must contain the Credential-on-file indicator (in addition to a CIT or MIT indicator, as applicable) when:

- the Cardholder previously authorized the Merchant to store the Account data for use in future Transactions, and
- the Cardholder agreed to the Merchant’s use of the stored Account data to conduct the Transaction being submitted.

Refer to Rule 5.9 for more information about Merchant-initiated Transactions (MITs) and to Appendix C regarding the use of CIT and MIT indicators.

The Acquirer should:

- ensure that the Merchant retains the Cardholder's written agreement to the terms of a Credential-on-file Transaction arrangement; and
- advise the Merchant not to place Account data on file as a Stored Credential if the Issuer provides a Merchant advice code value of 40 (Consumer non-reloadable prepaid card) or 41 (Consumer single use virtual card number) in an authorization response (0110 or 0210) message.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region" and "Europe Region" sections at the end of this chapter.



179
# 5.4 Recurring Payment Transactions

A recurring payment Transaction is a Transaction made pursuant to an agreement between a Cardholder and a Merchant, whereby the Cardholder authorizes the Merchant to store and use the Cardholder’s Mastercard Account or (where supported) Maestro Account data periodically and on an ongoing basis, with no specified end date. Use may occur periodically, such as on a monthly, quarterly, or annual basis, or as needed to “top up” the Cardholder’s account with the Merchant. A recurring payment Transaction may be for a variable or a fixed amount, as specified in the agreement. A recurring payment Transaction differs from an installment Transaction in that the number of installment Transaction payments is specified.

By way of example and not limitation, the following are Merchant categories that frequently process recurring payment Transactions:

- MCC 4814 (Telecommunication Services including but not limited to prepaid phone services and recurring phone services)
- MCC 4816 (Computer Network/Information Services)
- MCC 4899 (Cable, Satellite, and Other Pay Television and Radio Services)
- MCC 4900 (Utilities—Electric, Gas, Heating Oil, Sanitary, Water)
- MCC 5192 (Books, Periodicals, and Newspapers)
- MCC 5968 (Direct Marketing—Continuity/Subscription Merchants)
- MCC 6300 (Insurance Sales, Underwriting, and Premiums)

The Acquirer must identify the first Cardholder-initiated Transaction of a recurring payment series with the following values.

|Data Element|Subfield|
|---|---|
|61 (Point-of-Service [POS] Data)|1 (POS Terminal Attendance)|

Value

- One of the following:
- 0 (Attended Terminal)
- 1 (Unattended Terminal [Cardholder-activated Terminal {CAT}, home PC, mobile phone, personal digital assistant {PDA}])
- 2 (No Terminal used [voice/audio response unit {ARU} authorization; server])


# Card-Not-Present Transactions

# 5.4 Recurring Payment Transactions

|Data Element|Subfield|
|---|---|
|61 (Point-of-Service [POS] Data)|4 (POS Cardholder Presence)|

Value

One of the following:

•   0 (Cardholder present)

•   1 (Cardholder not present, unspecified)

•   2 (Mail/facsimile order)

•   3 (Phone/ARU order)

•   5 (Electronic order [home PC, Internet, mobile phone, PDA])

Effective 7 June 2022 in the U.S. Region and 14 October 2022 in all other Regions (unless an earlier effective date applies), the value of 4 must be used when the first payment in a recurring payment series occurs in a Card-not-present environment.

61 (Point-of-Service [POS] Data)
5 (POS Card Presence)
One of the following:

•   0 (Card present)

•   1 (Card not present)

48 (Additional Data—Private Use)
5 (Cardholder/Merchant Initiated Transaction Indicator)
One of the following:

•   C101 (Credential-on-file [ad hoc])

•   C102 (Standing Order [variable amount/fixed frequency])

•   C103 (Subscription [fixed amount/fixed frequency])

An Acquirer must identify each subsequent Merchant-initiated recurring payment Transaction with the following values, including when a Stored Credential has been replaced with a Token at the Merchant’s request.

|Data Element|Subfield|Value|
|---|---|---|
|22 (Point-of-Service [POS] Entry Mode)|1 (POS Terminal PAN Entry Mode)|• 10 (Credential on File)|


# Card-Not-Present Transactions

# 5.4 Recurring Payment Transactions

|Data Element|Subfield|
|---|---|
|61 (Point-of-Service [POS] Data)|1 (POS Terminal Attendance)|
|Value|One of the following:|
| |• 1 (Unattended Terminal [Cardholder-activated Terminal {CAT}, home PC, mobile phone, personal digital assistant {PDA}])|
| |• 2 (No Terminal used [voice/audio response unit {ARU} authorization; server])|
|61 (Point-of-Service [POS] Data)|4 (POS Cardholder Presence)|
|61 (Point-of-Service [POS] Data)|5 (POS Card Presence)|
|61 (Point-of-Service [POS] Data)|10 (Cardholder-activated Terminal Level)|
|61 (Point-of-Service [POS] Data)|11 (POS Card Data Terminal Input Capability Indicator)|
|48 (Additional Data—Private Use)|5 (Cardholder/Merchant Initiated Transaction Indicator)|
| |4 (Standing order/recurring Transactions)|
| |1 (Card not present)|
| |0 (Not a CAT Transaction)|
|6 (Key entry only)| |
| |One of the following:|
| |• M101 (Unscheduled Credential-on-file)|
| |• M102 (Standing Order [variable amount/fixed frequency])|
| |• M103 (Subscription [fixed amount/fixed frequency])|

The recurring payment indicator must not appear in installment billing Transactions.

An Issuer should provide a Merchant advice code in DE 48, subelement 84 of the authorization response message when declining a recurring payment Transaction authorization request. The Acquirer and the Merchant should be able to receive and act on the Merchant advice code when present.

The Acquirer should ensure that the Merchant retains the Cardholder’s written agreement to the terms of a recurring payment Transaction arrangement. The Merchant must not deliver products or perform services pursuant to a recurring payment Transaction arrangement after receiving notification of its cancellation by the Cardholder or Issuer or that the Account on file is not to be honored.

NOTE: Additions to this Rule appear in the “Europe Region” section at the end of this chapter.



182
# Card-Not-Present Transactions

# 5.4.1 Subscription Billing Merchants

The following Standards apply to recurring payment Transactions initiated by a Merchant performing subscription billing in which the Cardholder has agreed for the Merchant to provide ongoing and/or periodic delivery of a service, membership, physical products or Digital Goods. Refer to Rule 5.4.1.1 regarding the applicability of these Standards to certain Merchant categories.

1. The Merchant must disclose the subscription terms simultaneously with a request for Card credentials. The disclosure must include the price that will be billed and the frequency of the billing (for example, "You will be billed USD 9.95 per month until you cancel the subscription). Merchants that utilize a negative option billing model must also disclose the terms of the trial, including any initial charges, the length of the trial period, and the price and frequency of the subsequent subscription (for example, You will be billed USD 2.99 today for a 30-day trial. Once the trial ends, you will be billed USD 19.99 each month thereafter until you cancel.").

An e-commerce Merchant must:

1. Clearly and prominently display the subscription terms on any payment and order summary webpages; and
2. Capture a Cardholder's affirmative acceptance of the subscription terms before completing the subscription order.

Providing a link to another webpage or requiring the Cardholder to expand a message box or scroll down the webpage to view the subscription terms does not satisfy this requirement.
2. Immediately after the Cardholder completes the subscription order, the Merchant must promptly send a subscription order confirmation to the Cardholder through an email message or other electronic communication method that includes the subscription terms. The confirmation message must include or provide access to instructions for account management capabilities, including instructions for canceling the subscription (and thereby withdrawing permission for any subsequent recurring payment).
3. Each time that the Merchant receives an approved authorization request, it is recommended that the Merchant provide the Cardholder with a Transaction receipt through an e-mail message or other electronic communication method that includes the amount and reason for the billing and includes or provides access to instructions for account management capabilities, including instructions for canceling the subscription (and thereby withdrawing permission for any subsequent recurring payment Transactions). Cardholders may choose to opt-out of receiving these notices.

This Standard becomes a requirement when a Merchant that utilizes a recurring payment plan is identified for four months or more in the Acquirer Chargeback Monitoring Program (ACMP) as an Excessive Chargeback Merchant (ECM), a High Excessive Chargeback Merchant (HECM) and/or an Excessive Fraud Merchant (EFM) within the same audit period (refer to Chapter 8 Acquirer Chargeback Monitoring Program of the Data Integrity Monitoring Program for more information). The Acquirer of a Merchant that has been identified in ACMP for four months or more and has not implemented these requirements may be subject to Category A assessments for each month of noncompliance, in addition to the assessments applicable under the Acquirer Chargeback Monitoring Program.



183
# Card-Not-Present Transactions

# 5.4.1 Applicability of Standards

4. The Merchant must provide an online or electronic cancellation method (similar to unsubscribing from email messages or any other electronic method) or clear instructions on how to cancel that are easily accessible online (such as a “Manage Subscription” or “Cancel Subscription” link on the merchant’s home page).

5. For any subscription where the billing frequency is every six months (180 days) or less (i.e., billing occurs every six months, every year, every other year, etc.), the Merchant must send an electronic reminder to the Cardholder at least seven days but no more than 30 days prior to the next billing date that includes the subscription terms and includes or provides access to instructions for account management capabilities, including instructions for canceling the subscription (and thereby withdrawing permission for any subsequent recurring payment). The communication must clearly reference in the subject line that it relates to upcoming charges to the Cardholder (for example, "Important Information About Upcoming Charges to Your Account") and the message must be distinct from marketing communications that are otherwise sent to the Cardholder.

# 5.4.1.1 Applicability of Standards

The Standards in this Rule 5.4.1 do not apply to payments for utilities (i.e., gas, electric, sanitation, heating oil, water), telecommunications, insurance policies, or existing debt (for example, vehicle loan or mortgage payments).

The Standards in this Rule 5.4.1 are only best practice recommendations for any not-for-profit/charity Merchant that utilizes a recurring payment plan. However, all five Standards (including, for the avoidance of doubt, item three) become requirements when a not-for-profit/charity Merchant that utilizes a recurring payment plan is identified for four months or more in the Acquirer Chargeback Monitoring Program (ACMP) as an Excessive Chargeback Merchant (ECM), a High Excessive Chargeback Merchant (HECM) and/or an Excessive Fraud Merchant (EFM) within the same audit period (refer to Chapter 8 Acquirer Chargeback Monitoring Program of the Data Integrity Monitoring Program for more information). The Acquirer of a Merchant that has been identified in ACMP for four months or more and has not implemented these requirements may be subject to Category A assessments for each month of noncompliance, in addition to the assessments applicable under the Acquirer Chargeback Monitoring Program.

# 5.4.2 Negative Option Billing Merchants

A negative option billing Merchant offers a Cardholder the opportunity to purchase a subscription service to automatically receive one or more physical products (such as cosmetics, health-care products, or vitamins), Digital Goods or services on a recurring basis (such as weekly, monthly, semi-annually, or annually). As used in this section, the term "product" means or a physical product or a Digital Good.

The subscription service may be initiated by an agreement between the Cardholder and the Merchant whereby the Cardholder agrees to receive from the Merchant a sample of the product or services (either complimentary or at a nominal price) for a trial period. The sample may be larger, equal to, or smaller than the product provided by the Merchant during the subscription period. For the purposes of this Rule 5.4.2, a trial period means a preset length of time during


# Card-Not-Present Transactions

# 5.4.2 Negative Option Billing Merchants

which the Cardholder may evaluate the characteristics of the product or service such as its quality or usefulness to determine whether the Cardholder wants to either:

- Purchase the product or service on a one-time basis or recurring basis; or
- Return the product (if possible) to the Merchant.

After the trial period has expired, the Merchant may use Account credentials provided to the Merchant by the Cardholder to submit Transactions on a recurring basis each time that the product is shipped, delivered, or otherwise made available to the Cardholder, until either:

- The Cardholder takes action to terminate the agreement with the Merchant (for example, notifying the Merchant to cancel the subscription);
- The Merchant terminates the agreement; or
- The subscription expires.

The following Standards apply to recurring payment Transactions associated with a negative option billing Merchant:

1. For Digital Goods and services offering a trial period longer than seven days: No less than three days and no more than seven days prior to end of trial period, the Merchant must send a reminder notification to the Cardholder that the subscription plan will commence if the Cardholder does not cancel, or whenever terms and conditions will change. This notification must include the basic terms of the subscription and clear instructions on how to cancel. This reminder can be completed by email or any other electronic methods.
2. For physical products:
1. The Acquirer must process all subsequent recurring payment Transactions using the same Merchant ID in DE 42 (Card Acceptor ID Code) and Merchant name in DE 43, subfield 1 (Card Acceptor Name) as the Acquirer used for the initial Transaction.
2. After the trial period has expired, the Merchant must provide the following information to the Cardholder and receive the Cardholder’s explicit consent in relation to this information before the Merchant may submit an authorization request for the initial recurring payment Transaction for the full-size or regular price product:
- The date the subscription period begins
- The Transaction amount
- The payment date of the Transaction
NOTE: After the Cardholder has provided consent, the Merchant may not change this date; however, a later payment date may be offered by the Merchant prior to consent, if the authorization request results in a declined response from the Issuer due to insufficient funds in the Cardholder’s Account.
- The Merchant name as it will appear on the Cardholder’s statement
- Instructions for terminating the recurring payment Transaction cycle (for example, canceling the subscription service) at the Cardholder’s discretion
3. Each time that the Merchant receives an approved authorization request, the Merchant must provide the Cardholder with a Transaction receipt through an e-mail message or other electronic communication method (such as an SMS “text message”) including instructions for terminating the recurring payment Transaction cycle (such as canceling the subscription).


# 5.4.3 China Domestic Recurring Payment Transactions

If the Merchant provides the Cardholder with a Transaction receipt after a declined authorization request, the Transaction receipt must state the reason for the decline response.

4. The Merchant must provide the Cardholder with written confirmation in either hard copy or electronic format at least seven (7) days in advance when any of the following events occur:

- The Merchant is revising the subscription billing terms
- The recurring payment Transaction cycle has been terminated by either the Merchant or the Cardholder, in which case the notice must be sent no more than seven days after the Cardholder's decision to cancel.

For more information about registration requirements for negative option billing Merchants selling physical goods, refer to section 9.4.10 of the Security Rules and Procedures manual.

# 5.5 Installment Billing

Installment billing consists of payments by an Issuer to an Acquirer on behalf of a Cardholder who authorizes a Merchant to bill the Cardholder’s Account on a continued, periodic basis (typically based on the Transaction date, and on a monthly basis) until the total amount due for the goods or services purchased from the Merchant or other retailer is paid. The amount of each payment is a fixed amount determined by the total number of installments specified and the value of goods or services purchased.

Installment billing differs from recurring payments in that there is a specified end date. For example, a Cardholder contracted to pay BRL 500 on a monthly basis for one year for membership in a health club. This would not qualify as a recurring payment arrangement because there is a beginning and ending time specified for the membership.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# Applicability of Rules

The Standards in Rule 5.5.1 and in message reason code 4850—Installment Billing Disputes in the Chargeback Guide apply to an Acquirer-financed and Merchant-financed installment billing where the Acquirer processes a single authorization request containing installment information for the full Transaction amount. Upon Issuer approval, the Acquirer submits multiple clearing records for the installment payments, in accordance with the terms agreed by the Cardholder at the POI. The first installment billing may occur in a Card-present or Card-not-present environment; all subsequent installment billings are processed as Card-not-present Transactions.

Mastercard also supports Issuer-financed installment billing, which differs in that upon Issuer approval of the authorization request containing installment information, the Acquirer submits.


# Card-Not-Present Transactions

# 5.5.1 Single-Authorization Installment Billing

A single clearing record for the full Transaction amount. The Issuer then bills the Cardholder for the installments in accordance with the terms agreed by the Cardholder at the POI. Mastercard supports single-authorization installment billing in participating countries only. The Standards in Rule 5.5.2 apply when a Merchant or Installment Provider offers installment billing to Cardholders, and each installment payment Transaction is submitted individually for authorization by the Issuer, in accordance with the terms agreed by the Cardholder at the POI. Upon Issuer approval, the Acquirer submits a separate clearing record for each installment payment. For more information about Installment Providers, refer to Chapter 7 of the Mastercard Rules.

# 5.5.1 Single-Authorization Installment Billing

This section applies to installment billing Transactions whereby information about the installment plan agreed between the Merchant and the Cardholder is transmitted in the Merchant's authorization request message for Issuer approval.

# 5.5.1.1 Definitions

Solely for the purposes of the installment billing Rules set forth herein and in “Message Reason Code 4850—Installment Billing Dispute” in the “Domestic Chargebacks” section of the Chargeback Guide, the following terms have the meanings set forth below:

- Installment billing: An arrangement agreed between a Merchant and a Cardholder at the POI whereby a fixed number of periodic payments will be processed to complete a total payment for goods or services purchased.
- Installment: One of a fixed number of periodic payments processed by a Merchant and submitted by its Acquirer as a separate clearing record in accordance with an installment billing arrangement between the Merchant and the Cardholder.
- Installment acceleration: Acceleration of the processing of remaining installments for a Transaction. When installment acceleration is requested by the Issuer, the Acquirer must immediately process all remaining installments for the Transaction.

# 5.5.1.2 Transaction Processing Procedures

The Authorization Request/0100 message of a Transaction to be billed in installments must contain the following information, and must not contain the recurring payment indicator:

- The appropriate installment billing indicator code in DE 48, subelement 95 (Promotion Code), and
- The installment plan type and the number of installments requested by the Cardholder at the time of purchase in DE 112 (Additional Data, National Use).


# Card-Not-Present Transactions

# 5.5.2 Multiple-Authorization Installment Billing

The Authorization Request/0100 message must be submitted for the total value of the Transaction. The Acquirer must ensure that the Authorization Request Response/0110 message contains the same number of installments indicated in DE 112 of the Authorization Request/0100 message.

The Transaction receipt must include the number of installments agreed between the Cardholder and the Merchant at the time of the Transaction.

Each installment payment is cleared and settled separately upon the processing of each installment. The Acquirer may process each installment payment clearing record upon receipt from the Merchant as the installment becomes due. The Acquirer must ensure that each installment payment clearing record contains information identifying the original approved authorization, as follows:

- The values contained in DE 63 (Network Data) and DE 15 (Settlement Date) from the authorization request response message must be placed in DE 63, subfield 2 (Trace ID) of each clearing record, and
- The value contained in DE 38 (Approval Code) from the authorization request response message must be placed in DE 38 of each clearing record.

For Transactions completed with electronically recorded Card information (whether Card-read or key-entered), the first installment must be presented within seven calendar days of the Transaction date. For Transactions completed with manually recorded Card information (whether imprinted or handwritten), the first installment must be processed within 30 days of the Transaction date.

Unless otherwise agreed between the Cardholder and the Merchant, the period between installments must be 30 calendar days. Acceleration of the processing of installments is permitted when authorized by the Issuer.

The Issuer is responsible for ensuring that each installment is processed accurately and for identifying each installment number on the Cardholder’s billing statement (for example, installment one of six).

NOTE: Modifications to this Rule appear in the "Asia/Pacific" and "Europe Region" sections at the end of this chapter.

# 5.5.2 Multiple-Authorization Installment Billing

This section describes Transaction processing procedures for Merchants and Installment Providers offering installment billing arrangements to Cardholders in connection with a retail purchase, in which each installment payment is processed as an individually authorized and cleared Transaction. The following requirements apply:

- The installment billing arrangement terms and conditions must be fully and clearly disclosed in advance to the Cardholder. This includes but is not limited to the total number of installment payments, the payment schedule, the amount of each payment, and any fees that may apply;


# Card-Not-Present Transactions

# 5.5.2 Multiple-Authorization Installment Billing

- The installment billing arrangement must be conducted in accordance with the terms and conditions offered to and agreed by the Cardholder;
- The Acquirer must properly identify each installment payment Transaction as described in the “Installment Payment Information” section; and
- The Transaction receipt for each installment Transaction must include the installment number as it corresponds to the total number of installments (for example, "Payment 2 of 4").

# Installment Payment Information

An installment payment Transaction is properly identified as described in the following table.

|In This Data Field:|If submitted by a Merchant, each Transaction must contain:|If submitted by an Installment Provider, each Transaction must contain:|
|---|---|---|
|DE 43 (Acceptor Name and Address)|The Merchant’s name and address|The full or abbreviated name of the Installment Provider in combination with the retailer name, separated by an asterisk (for example, Installment Provider*Retailer)|
|DE 18 (Merchant Type)|The MCC that best describes the primary business of the Merchant, or the nature of the purchase|The MCC that best describes the primary business of the retailer, or the nature of the purchase|
|DE 48, subelement 32 (Mastercard-assigned ID)|Optional; if present, the Mastercard-assigned ID of the Merchant|The Mastercard-assigned ID of the Installment Provider|
|DE 48, subelement 77 (Transaction Type Identifier)|Not Required|P10 (Purchase Repayment)|
|DE 48, subelement 22 (Multi-Purpose Merchant Indicator), subfield 5 (Cardholder/Merchant Initiated Transaction Indicator)|C104 for the initial CIT and M104 for each subsequent MIT|C104 for the initial CIT and M104 for each subsequent MIT|

The following First Presentment/1240 message fields must be populated with the same information as provided in the corresponding Authorization Request/0100 message field:

- DE 43 (Acceptor Name/Location)
- DE 26 (Acceptor Business Code [MCC])
- PDS 0176 (Mastercard-assigned ID)
- PDS 0043 (Transaction Type Identifier)


# Card-Not-Present Transactions

# 5.6 Transit Transactions Performed for Debt Recovery

The Credential-on-file Transaction indicator must be present in authorization and clearing messages as described in Rule 5.3 for each installment payment Transaction subsequent to the initial payment. The value of C104 or M104, as appropriate, may also be provided in PDS 0218 (Cardholder/Merchant Initiated Transaction Indicator).

If space allows, a message describing the installment being paid may optionally be provided in authorization and clearing messages at the end of DE 43, subfield 1 (Card Acceptor Name); for example, “PYMT 2 of 4”.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# Customer Service Information

The Acquirer is recommended to provide the following information in PDS 0170 (Card Acceptor Inquiry Information) of each First Presentment/1240 message:

- A customer service phone number for the retailer in subfield 1 (Customer Service Phone Number);
- A customer service phone number for the Installment Provider in subfield 2 (Card Acceptor Phone Number); and
- The installment number and total number of installments in subfield 3 (Additional Contact Information) (for example, “PAYMENT 2 of 4”).

# 5.6 Transit Transactions Performed for Debt Recovery

A transit Merchant may use the transit debt recovery Transaction to recover a Cardholder’s debt resulting from one or more contactless taps for entry to the transit system, if the Issuer has declined the Contactless transit aggregated Transaction authorization request (0100 or 0200) message. A transit debt recovery Transaction is an MIT that is properly identified with:

- A value of 07 (Debt Recovery) in DE 48, subelement 64 (Transit Program), subfield 1 (Transit Transaction Type Indicator) in Authorization Request/0100 and Financial Transaction Request/0200 messages and in PDS 0210 (Transit Program), subfield 1 (Transit Transaction Type Indicator) of First Presentment/1240 messages; and
- An amount in DE 4 (Amount, Transaction) that does not exceed the applicable Mastercard Contactless transit aggregated Transaction CVM limit.

Effective 14 October 2022, a transit debt recovery Transaction may also contain the MIT value of M208 (Resubmission) in DE 48, subelement 22 (Multi-purpose Merchant Indicator), subfield 5 (Cardholder/Merchant Initiated Transaction Indicator) of Authorization Request/0100 and Financial Transaction Request/0200 messages.

An Issuer of Maestro Cards that allows its Cardholders to perform Maestro Contactless transit aggregated Transactions must be able to accept and must make an individual authorization decision for each transit debt recovery Transaction identified as a Card-not-present Transaction (for example, as a PAN key-entered, e-commerce, or mail order or telephone order (MO/TO) Transaction).


# Card-Not-Present Transactions

# 5.6.1 Transit First Ride Risk Framework

NOTE: A modification to this Rule appears in the “Europe Region” section at the end of this chapter.

A transit Merchant that initiates the authorization of Contactless transit aggregated Transactions submitted via the Mastercard Dual Message System and is located in a country implementing the First Ride Risk (FRR) framework may qualify to collect payment for first ride debt incurred by the Cardholder. First ride debt is the amount owed by the Cardholder to the transit Merchant for one or more rides taken upon using a Contactless tap to enter the transit system (such as at a gate or turnstile), if the Issuer declines the Contactless transit aggregated Transaction authorization request. The FRR framework applies solely with respect to the use of a Card or Access Device issued in the Merchant's country, unless otherwise specified.

Under the FRR framework, a Merchant that meets all the FRR framework criteria can collect payment for first ride debt in an amount not exceeding the FRR limit applicable in the Merchant's country, as follows.

# Submit this Transaction type:

- A transit debt recovery Transaction
- A Transit FRR claim Transaction

# Under these conditions:

1. The Issuer declined the Contactless transit aggregated Transaction using a response code value categorized in Table 7 as "Recoverable" or "Temporarily Recoverable." The transit debt recovery Transaction amount must not exceed the applicable Contactless transit aggregated Transaction CVM limit.
2. The Issuer declined the Contactless transit aggregated Transaction or a subsequent transit debt recovery Transaction using a response code value categorized in Table 7 as "Unrecoverable." In such event, the FRR claim Transaction can be submitted immediately; or
3. The Merchant made at least nine transit debt recovery Transaction attempts for a period of 45 calendar days from the date of the original Contactless Transit aggregated Transaction decline, with the last attempt occurring on day 45, and the Issuer declined each attempt for a "Recoverable" or "Temporarily Recoverable" reason. The Merchant must make no more than one attempt per 24-hour period.

An FRR claim Transaction does not require authorization by the Issuer. The FRR claim Transaction is properly identified in the First Presentment/1240 message with:

- A value of 08 (First Ride Risk Claim) in PDS 0210 (Transit Program), subfield 1 (Transit Transaction Type Indicator) for Post Authorized Aggregation (PAA), Authorized Aggregated Split Clearing (AASC) or PAA-Maestro transit model only; and
- An amount in DE 4 (Amount, Transaction) that does not exceed the FRR limit applicable in the Merchant's country, as specified in Chapter 5 of the Quick Reference Booklet.


# Card-Not-Present Transactions

# 5.6.1 Transit First Ride Risk Framework

The Acquirer must not submit an FRR claim Transaction if the Issuer used a response code value categorized in this table as "Not Claimable" when declining the original Contactless transit aggregated Transaction or a subsequent transit debt recovery Transaction.

|Temporarily Recoverable|Unrecoverable|Recoverable|Not Claimable|
|---|---|---|---|
|51 (Insufficient funds/over credit limit)|03 (Invalid merchant)|01 (Refer to card issuer)|15 (Invalid issuer)|
|55 (Invalid PIN)|04 (Capture card)|05 (Do not honor)5|30 (Format error)|
|61 (Exceeds withdrawal amount limit)|12 (Invalid transaction)|70 (Contact card issuer)|54 (Expired card)|
|65 (Exceeds withdrawal count limit)|13 (Invalid amount)|86 (PIN validation not possible)|57 (Transaction not permitted to issuer/cardholder)|
|71 (PIN not changed)|14 (Invalid card number)|87 (Purchase amount only; no cash back allowed)|92 (Unable to route transaction)|
|75 (Allowable number of PIN tries exceeded)|41 (Lost card)|91 (Authorization system or issuer system inoperative)|94 (Duplicate transmission detected)|
|76 (Invalid/nonexistent "To Account" specified)|43 (Stolen card)| |96 (System error)|
|77 (Invalid/nonexistent "From Account" specified)|58 (Transaction not permitted to acquirer/terminal)| | |
|78 (Invalid/Nonexistent account specified)|62 (Restricted card)| | |
| |63 (Security violation)| | |
| |88 (Cryptographic failure)| | |

The terms used in the headings of the preceding table are defined here.

Recoverable: For response codes that are recoverable, the transit acquirer must use the debt recovery Authorization Request/0100 message to attempt debt recovery from the issuer or cardholder.

5 Unrecoverable if DE 48, subelement 84 (Merchant Advice Code) contains a value of 03 (Do not try again).


# Card-Not-Present Transactions

# 5.7 Use of Automatic Billing Updater

# Unrecoverable

Authorization requests receiving response codes that are deemed unrecoverable will be eligible for unrecoverable debt claims by the merchant's acquirer to the issuer. The claim is submitted as a First Presentment/1240 clearing message without a valid authorization approval. The transit acquirer submitting a first presentment to make an FRR claim due to reason code 14 (Invalid card number) may be rejected with an error code 2358 (DE2 PRIMARY ACCOUNT NUMBER [PAN] INVALID. THE PAN MAPPING SERVICE CANNOT MAP DE2 TO ANOTHER ACCOUNT NUMBER) from the Global Clearing Message System (GCMS) if the authorization request was initiated from a digitized card associated with a closed account. The transit acquirer may submit a Fee Collection/1740 message to claim the debt for reason code 14 (invalid card number) after the first presentment was rejected with error code 2358 when making an FRR claim.

# Temporarily Recoverable

Upon receiving a response code that indicates a temporary situation that the cardholder may potentially be able to resolve by working with the issuer, the transit merchant must make at least nine attempts at debt recovery from the cardholder within 45 calendar days from the date on which the temporarily recoverable decline response code was initially received, until the last attempt occurring no later than day 45. When all debt recovery attempts are exhausted, the debt becomes unrecoverable, and the transit merchant may submit an FRR claim directly to the issuer. The claim is submitted as a First Presentment/1240 clearing message without a valid authorization approval.

# Not Claimable

Transit merchants must deny access to expired cards and cards that do not support deferred authorization (bit 8 of byte 3 set to 1b) in the transit product data (an extension of third-party data defined in the M/Chip Requirements for Contact and Contactless announced in December 2020) at the point of entry, and will be fully liable for declines due to reason codes 54 (Expired card) and 57 (Transaction not permitted to issuer/cardholder). Merchants cannot claim the debt using the FRR framework or submit a debt recovery authorization upon receiving an expired card decline or card that does not support deferred authorization. Transit merchants also cannot claim the outstanding debt for response codes that indicate formatting or network issues.

# 5.7 Use of Automatic Billing Updater

The Automatic Billing Updater (ABU) is used by a Customer to communicate changes to Account information to Merchants that participate in Account-on-file and recurring payment.



193
# Card-Not-Present Transactions

# 5.8 Authentication Requirements—Europe Region Only

Transactions. For information about ABU, refer to the Mastercard Automatic Billing Updater Reference Guide, available in the Technical Resource Center on Mastercard Connect. When applicable, an Issuer of Mastercard Cards and each Acquirer that accepts Mastercard Cards must participate in ABU and be able to send, receive, and process Automatic Billing Updater (ABU) data.

To participate in ABU, an Issuer must take all of the following actions:

- Complete the Automatic Billing Updater Customer Enrollment Form available on Mastercard Connect™. Regarding a newly assigned ICA or BIN, an Issuer has six months from the date of the assignment to comply with this requirement.
- Provide to ABU a one-time upload plus six months of historic ICA and BIN data changes, up to a maximum of 50 months’ data, and all newly issued and reissued activated Accounts.
- Submit to ABU all of the types of Account changes defined in the Mastercard Automatic Billing Updater Reference Guide, excluding any such Account changes to Cards issued under exempt Mastercard Card Programs.

The following Card Programs and Accounts are exempt from ABU participation requirements:

- A non-reloadable prepaid Card Program, provided that the Issuer does not allow the prepaid Cards to be used to enter into recurring payment arrangements;
- Remote Transaction Accounts issued for a single use or other predefined purpose; and
- A Commercial Card Program, except that ABU participation requirements apply to Cards issued for use by a small business (for a list of small business Card Programs, see www.Mastercardbusiness.com and select “Cards” under “Small Business”).

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," "Canada Region," "Europe Region," "Latin America and the Caribbean Region," "Middle East/Africa Region," and "United States Region" sections at the end of this chapter.

# 5.8 Authentication Requirements—Europe Region Only

NOTE: Rules on this subject appear in the “Europe Region” section at the end of this chapter.

# 5.9 Merchant-initiated Transactions

A Merchant-initiated Transaction (MIT) is a Card-not-present Transaction that a Merchant initiates based on a prior agreement with the Cardholder, and in which the Cardholder does not actively participate. An MIT is often preceded by an Account Status Inquiry authorization request or CIT.

MITs are classified as follows. Recurring payment and installment MITs are Credential-on-file Transactions initiated by a Merchant or Installment Provider based on the Cardholder’s agreement to be billed on a



194
# Card-Not-Present Transactions

# 5.10 Mastercard Micropayment Solution—United States Region Only

scheduled or unscheduled basis for goods or services purchased from the Merchant, or for a single purchase to be paid in several installments.

Industry Practice MITs are initiated by the Merchant based on the Cardholder’s agreement to the terms and conditions of a single purchase of goods or services. Industry practice MITs may be performed with credentials that the Merchant does not store permanently on file, but only temporarily retains for purposes of completing the purchase. An industry practice MIT may be one of the following:

- “Partial shipment” occurs when items that were out of stock when originally ordered in a CIT are later shipped and billed separately by the Merchant as an MIT.
- “Related/delayed charge” occurs when the Merchant submits an MIT to bill the Cardholder for additional items or fees associated with an initial CIT, in accordance with the original Transaction terms.
- “No-show” is a fee billed by a Merchant in accordance with the Merchant’s guaranteed reservation service policy, when the Cardholder fails to cancel a reservation within the time frame disclosed at the time of the booking.
- “Resubmission” occurs when the original CIT authorization request was declined by the Issuer for a reason that does not preclude the Merchant from resubmitting the request after a reasonable period (for example, in 24 hours).

An Acquirer must properly identify in Authorization Request/0100 and Financial Transaction Request/0200 messages:

- All Merchant-initiated Transactions (MITs); and
- Any Cardholder-initiated Transaction (CIT) that occurs in an e-commerce environment and is used to place a credential on file for future MITs.

This requirement takes effect 14 October 2022, except that the requirement is in effect for recurring payment, installment, related/delayed charge, and partial shipment MITs occurring in the U.S. Region. Refer to Appendix C for MIT and CIT identification requirements.

NOTE: Additions to this Rule appear in the “Europe Region” section and modifications to this Rule appear in the “Asia/Pacific Region” section at the end of this chapter.

# 5.10 Mastercard Micropayment Solution—United States Region Only

A Rule on this subject appears in the “United States Region” section at the end of this chapter.


# Card-Not-Present Transactions

# Variations and Additions by Region

The remainder of this chapter provides modifications to the Standards set out in this chapter. The modifications are organized by region or country and by applicable subject title.

# Asia/Pacific Region

The following modifications to the Rules apply in the Asia/Pacific Region or in a particular Region country or countries. Refer to Appendix A for the Asia/Pacific Region geographic listing.

# 5.1 Electronic Commerce Transactions

In the Asia/Pacific Region, the Rule on this subject is modified as follows. A Customer that participates as an Issuer in another international cardholder authentication program must certify that it has enabled its Cardholders and its e-commerce Merchants for Mastercard Identity Check.

In India, the Rule on this subject, as it applies to Mastercard Intracountry e-commerce Transactions, is modified as follows:

1. Electronic commerce Transactions occurring at a Merchant located in India with a Mastercard Card issued in India must be authenticated. An authenticated Transaction occurs when:
1. The Merchant is Universal Cardholder Authentication Field (UCAF)-enabled;
2. The Issuer provided the UCAF data for that Transaction;
3. All other authorization and clearing requirements applicable to the Transaction were satisfied; and
4. The Authorization Request Response/0110 message reflected the Issuer’s approval of the Transaction.
2. Each Issuer and e-commerce Transaction Acquirer must participate in the Activation During Shopping (ADS) method of Cardholder enrollment in Mastercard Identity Check. Cardholders must complete enrollment on the first attempt, and the Issuer must not permit a Cardholder to opt-out of the enrollment process.
3. Each Issuer and e-commerce Transaction Acquirer participating in the Mastercard Assurance Service must register with the Corporation. Each e-commerce Transaction enabled using the Mastercard Assurance Service must contain a value of 6 (UCAF Control Byte) in DE 48, subelement 43, position 1, and a value of MAS in DE 124 of the Authorization Request/0100 message. For additional information, please contact south_asia_ops@mastercard.com.

A refund for a Maestro Intracountry e-commerce Transaction must be processed as a Payment Transaction.


# Card-Not-Present Transactions

# 5.1.1 Acquirer and Merchant Requirements

An Acquirer must technically support in authorization and clearing the data fields and values described in Appendix C (Transaction Identification Requirements) for e-commerce Transactions and Digital Secure Remote Payment Transactions containing UCAF data.

In India, Bangladesh, and Malaysia, the Rule on this subject is modified as follows. Each Acquirer and each Merchant must request Cardholder authentication using EMV 3DS and comply with the requirements set forth in the Identity Check authentication program.

In Australia, the Rule on this subject is modified as follows. An Acquirer must ensure that each of its Merchants:

- Prominently and clearly discloses to the Cardholder the Merchant’s participation in least cost routing prior to the request to capture or for authorization to store the Cardholder’s Debit Mastercard Account data. To maintain visual parity, such disclosure must be at least as prominent as, and appear in at least the same size as surrounding content.
- Present Mastercard as a payment option to the Cardholder in accordance with the Standards, irrespective of whether the Transaction is routed or processed through the Interchange System.

# 5.1.2 Issuer Requirements

An Issuer must technically support in authorization and clearing the data fields and values described in Appendix C (Transaction Identification Requirements) for e-commerce Transactions and Digital Secure Remote Payment Transactions containing UCAF data.

The requirement either to verify the validity of the AAV when present in DE 48, subelement 43 of the authorization request message or to participate in the Mastercard Identity Check AAV Verification Service does not apply to an Issuer in China.

In India, Singapore, Bangladesh, and Malaysia, the Rule on this subject is modified as follows. An Issuer must support EMV 3DS and respond to a Cardholder authentication request using a solution that is compliant with the Identity Check authentication program requirements.

# 5.2 Mail Order and Telephone Order (MO/TO) Transactions

In India, the Rule on this subject, as it pertains to Intracountry mail order and phone order (including Integrated Voice Response or IVR) Transactions (“MO/TO” Transactions), is modified as follows.

1. Mail order and phone order Transactions effected at a Merchant located in India with a Mastercard Card issued in India must be authenticated. An authenticated Transaction occurs when:


# Card-Not-Present Transactions

# 5.3 Credential-on-File Transactions

1. The Authorization Request Response/0110 message reflected the Issuer’s approval of the Transaction.
2. Each IVR Transaction enabled using Mastercard Identity Check must contain a value of 2 (Identity Check phone order) in DE 61 (point-of-service [POS] Data), subfield 7 (POS Transaction Status) of the Authorization Request/0100 message.
3. Each Issuer and MO/TO Transaction Acquirer participating in the Mastercard Assurance Service must register with the Corporation. Each mail order and phone order (including IVR) Transaction enabled using the Mastercard Assurance Service must contain a value of 6 (UCAF Control Byte) in DE 48, subelement 43, position 1, and a value of MAS in DE 124 of the Authorization Request/0100 message. For additional information, please contact south_asia_ops@mastercard.com.
4. An Issuer may not use message reason codes 4837, 4849 or 4863 to charge back a mail order or phone order (including IVR) Transaction that occurs at a Merchant located in India, if:
1. The Merchant is UCAF-enabled;
2. The Issuer provided the UCAF for that Transaction;
3. All other phone order authorization and clearing requirements were satisfied, including the presence of:
1. A value of 2 (Identity Check phone order) in DE 61 (Point-of-Service [POS] Data), subfield 7 (POS Transaction Status) of the Authorization Request/0100 message for IVR Transactions enabled with Mastercard Identity Check; or
2. A value of 6 (UCAF Control Byte) in DE 48, subelement 43, position 1, and a value of MAS in DE 124 of the Authorization Request/0100 message for mail order, phone order, or IVR Transactions enabled with the Mastercard Assurance Service.
4. The Authorization Request Response/0110 message reflected the Issuer’s approval of the Transaction.
5. Each Issuer and IVR Transaction Acquirer must participate in the Activation During Shopping (ADS) method of cardholder enrollment in Mastercard Identity Check. Cardholders must complete enrollment on the first attempt, and the Issuer must not permit a Cardholder to opt-out of the enrollment process.
6. Each Issuer and mail order and phone order (including IVR) Transaction Acquirer that wishes to participate in the Mastercard Assurance Service must register with the Corporation.

# 5.3 Credential-on-File Transactions

In Japan, the Rule on this subject is modified as follows. For Acquirers in Japan, for authorization, a Credential-on-file Transaction may contain the Credential-on-file indicator, which is a value of 10 (Credential on File) in DE 22 (Point-of-Service Entry Mode), subfield 1 (POS Terminal PAN Entry). For Acquirers in Japan, for clearing, a Credential-on-file Transaction may contain the Credential-on-file indicator, which is a value of 7 (Credential on File) in DE 22 (Point-of-Service Entry Mode), subfield 7 (Card Data Input Mode).

In Australia, the Rule on this subject is modified as follows.


# Card-Not-Present Transactions

# 5.4 Credential-on-File Transactions

An Acquirer must ensure that each of its Merchants:

- Prominently and clearly discloses to the Cardholder the Merchant’s participation in least cost routing prior to the request to capture or for authorization to store the Cardholder’s Debit Mastercard Account data. To maintain visual parity, such disclosure must be at least as prominent as, and appear in at least the same size as surrounding content.
- Present Mastercard as a payment option to the Cardholder in accordance with the Standards, irrespective of whether the Transaction is routed or processed through the Interchange System.
- Must give at least 7 days notice to the Cardholder to exercise consumer choice in the event that the recurring transaction routing option is different from the Cardholder's last confirmation of checkout choice.

An Acquirer must ensure, within 30 days of when a Merchant begins participating in least cost routing, subsequent to the time of the Merchant’s initial request for authorization to store the Cardholder’s Debit Mastercard Account data, that the Merchant prominently and clearly discloses to the Cardholder the Merchant’s participation in least cost routing as set forth above.

# 5.4 Credential-on-File Transactions

# 5.4.2 China Domestic Recurring Payment Transactions

Each Acquirer of China domestic Transactions must comply with all requirements set forth in the Standards applicable to recurring payment Transactions, including the requirements in this manual, in the China Switch Specifications for authorization messages, and in the China Recurring Transaction Program Guide.

# 5.4.2.1 Transaction Requirements for Acquirers

# Adding a New Recurring Payment Series

The Acquirer must secure approval from Issuer for the recurring payment series prior to the initial recurring payment Transaction via the entrusted relation related messages as described in China Switch Specifications.

The Acquirer must include the China Recurring Payment Transaction – Recurring Payment Terms via Data Element 112 (Additional Data [China Use]) Subelement 37 (Delegated Business Information) when requesting to add a new recurring payment series.

The Acquirer may only put a credential on file for recurring payment Transactions if the Issuer approves the request to add a new recurring payment series. The Acquirer must not submit the recurring payment Transaction if the Issuer declines the request to add a new recurring payment series.

The Acquirer must identify each request to add a new recurring payment series with the following values:


# Card-Not-Present Transactions

# 5.4.2.1 Transaction Requirements for Acquirers

|Data Elements|Subelement|
|---|---|
|4 (Amount, Transaction)| |
|25 (Point of Service Condition Code)| |
|61 (Point-of-Service [POS] Data)|1 (POS Terminal Attendance)|
|Value|0|
|98 (Entrusted Relation Establishment)|One of the following:|
| |• 0 (Attended Terminal)|
| |• 1 (Unattended Terminal (Cardholder-activated Terminal [CAT], home PC, mobile phone, personal digital assistant [PDA]))|
| |• 2 (No Terminal used (voice/audio response unit [ARU] authorization); server)|
|61 (Point-of-Service [POS] Data)|4 (POS Cardholder Presence)|
| |One of the following:|
| |• 0 (Cardholder present)|
| |• 5 (Cardholder not present (Electronic order [home PC, Internet, mobile phone, PDA]))|
|61 (Point-of-Service [POS] Data)|5 (POS Card Presence)|
| |One of the following:|
| |• 0 (Card present)|
| |• 1 (Card not present)|
|61 (Point-of-Service [POS] Data)|7 (POS Transaction Status)|
|8 (Account Verification Service)| |
|112 (Additional Data [China Use])|37 (Delegated Business Information)|
| |All subfields must appear|

Processing of Recurring Payment Transactions

The Acquirer must verify the China Recurring Payment Transaction – Recurring Payment Terms before sending a recurring payment Transaction to the China Switch. If the China Recurring Payment Transaction – Recurring Payment Terms are not consistent with the Cardholder consent, the Acquirer must not submit the Transaction to the China Switch. If the Recurring Payment Terms are consistent with the Cardholder consent, the Acquirer must populate the China Recurring Payment Transaction – Recurring Payment Terms in Data Element 112 (Additional Data [China Use]) Subelement 37 (Delegated Business Information).

The Acquirer must identify each recurring payment Transaction with the following values:


# Card-Not-Present Transactions

# 5.4.2.2 Transaction Requirement for Issuers

|Data Elements|Subfield|
|---|---|
|22 (Point-of-Service [POS] Entry Mode)|1 (POS Terminal PAN Entry Mode)|
|61 (Point-of-Service [POS] Data)|1 (POS Terminal Attendance)|
|Value|10 (Credential on File)|
|One of the following:|- (Unattended Terminal (Cardholder-activated Terminal [CAT], home PC, mobile phone, personal digital assistant [PDA]))
- 2 (No Terminal used (voice/audio response unit [ARU] authorization; server))
|
|61 (Point-of-Service [POS] Data)|4 (POS Cardholder Presence)|
|61 (Point-of-Service [POS] Data)|5 (POS Card Presence)|
|61 (Point-of-Service [POS] Data)|7 (POS Transaction Status)|
|61 (Point-of-Service [POS] Data)|10 (Cardholder-activated Terminal Level)|
|61 (Point-of-Service [POS] Data)|11 (POS Card Data Terminal Input Capability Indicator)|
|112 (Additional Data [China Use])|37 (Delegated Business Information)|
|4 (Standing order/recurring Transactions)|1 (Card Not Present)|
|0 (Normal Request)|0 (Not a CAT Transaction)|
|6 (Key entry only)|Subfields 01, 02, 03, 04, 05 and 11 must appear|

# 5.4.2.2 Transaction Requirement for Issuers

# Adding a New Recurring Payment Series

The Issuer must secure Cardholder consent for the below China Recurring Payment Transaction – Recurring Payment Terms before the completion of the initial recurring payment Transaction:

- Card Acceptor Name
- Merchandise or service
- Payment account
- Recurring frequency or condition
- End date (if applicable)

The Issuer must provide a service to the Cardholder to query and manage the consented recurring payment series.

# Processing of Recurring Payment Transactions

The Issuer must verify the China Recurring Payment Transaction – Recurring Payment Terms for each recurring payment Transaction. The Issuer must decline the recurring payment Transaction.



201
# Card-Not-Present Transactions

# 5.5 Installment Billing

If the China Recurring Payment Transaction – Recurring Payment Terms is inconsistent with the Cardholder consent.

# 5.5 Installment Billing

# 5.5.1 Single-Authorization Installment Billing

# 5.5.1.2 Transaction Processing Procedures

Effective 3 April 2024 for India Domestic Transactions, the Rule on this subject is modified as follows. For Transactions completed with electronically recorded Card information (whether Card-read or key-entered) or manually recorded Card information (whether imprinted or handwritten), the first installment must be processed within four days of the Transaction date.

# 5.7 Use of Automatic Billing Updater

In the Asia/Pacific Region, each Issuer must comply and each Acquirer may comply with the ABU requirements set forth in this chapter.

# 5.9 Merchant-initiated Transactions

In Japan, the Rule on this subject is modified as follows. For Acquirers in Japan, a Merchant-initiated Transaction may contain the applicable MIT indicator value as described in Appendix C.

# Canada Region

The following modifications to the Rules apply in the Canada Region. Refer to Appendix A for the Canada Region geographic listing.

# 5.7 Use of Automatic Billing Updater

Each Issuer and Acquirer in the Canada Region must comply with the ABU requirements set forth in this chapter.

# Europe Region

The following modifications to the Rules apply in the Europe Region or in a particular Region country or countries. Refer to Appendix A for the Europe Region, Non-Single European Payments Area (Non-SEPA) and Single European Payments Area (SEPA) geographic listing.

# 5.1 Electronic Commerce Transactions


# Card-Not-Present Transactions

# 5.1.1 Acquirer and Merchant Requirements

In the EEA, the Rule on this subject is modified as follows. An Acquirer must technically support the authorization and clearing of the data fields and values described in Appendix C, Transaction Identification Requirements, for e-commerce Transactions and Digital Secure Remote Payment Transactions containing UCAF data, if the Transactions are processed via the Interchange System. If the Transactions are processed via an alternative switch, the Acquirer must populate the corresponding data fields in authorization and clearing messages with the values specified by the alternative switch.

For Maestro e-commerce Transactions, the Acquirer and Merchant must be capable of sending the full unaltered PAN to the registered switch of the Acquirer’s choice.

In Hungary, the following additional Rule applies. An Acquirer of e-commerce Merchants located in Hungary must ensure that 90% of its e-commerce Intracountry Transactions originate from Merchants that provide Cardholders the option to save Mastercard and Maestro Account data on file, and to use the previously saved Account data to perform a Credential-on-file (COF) Transaction. Tokenized and non-tokenized data storage solutions qualify to show compliance with this requirement.

Compliance is calculated on a quarterly basis and is measured at authorization level. Effective from 1 January 2023, in any given quarter, 65% of an Acquirer’s e-commerce Intracountry Transactions must originate from Merchants that are COF-enabled. From 30 June 2023 in any given quarter, 90% of an Acquirer’s e-commerce Intracountry Transactions must originate from Merchants that are COF-enabled. A Merchant is COF-enabled if it has at least one Transaction in the corresponding quarter that carries the Credential-on File indicator or a WID of 327.

An Acquirer must ensure that its e-commerce Merchants in Hungary offer to Cardholders a method to provide the initial consent to the Merchant and/or its agent to store the Mastercard or Maestro Account data on file, either in advance of or when carrying out the first Transaction with the Merchant. The Merchant must also provide a process for deleting and updating previously saved credentials.

# SCA Requirements

The following Rules apply to Intracountry and Cross-border Transactions within and between SCA Countries.

# Authentication Amount

The authentication amount for a Remote Electronic Transaction must be an amount that the Cardholder would reasonably expect and the authentication must use the same currency as the authorization.

As a best practice, in the UK and Gibraltar, the total Transaction amount of all authorizations that relate to a Remote Electronic Transaction should not exceed the authentication amount for the Transaction by more than 20 percent (20%). If the Transaction amount is not known in advance, the authentication amount must be an amount that the Cardholder would reasonably expect (e.g., within a tolerance of 20 percent [20%]). In this case, if the authorization amount exceeds the authenticated amount by more than 20 percent (20%), it is recommended that the


# Card-Not-Present Transactions

# 5.1.2 Issuer Requirements

Merchant treat the incremental amount compared to the authenticated amount as a separate Transaction. Transactions will require separate SCA unless an exemption applies or unless they are handled as Merchant-initiated Transactions. If the Transaction amount exceeds the Cardholder’s reasonable expectations, the refund right for authorized transactions may apply as provided for in applicable legislation.

This Rule does not apply to recurring payment Transactions.

# Attempt to Authenticate Following Soft Decline

In response to a decline of a Remote Electronic Transaction in which the Issuer indicates that SCA is required, a Merchant must attempt EMV 3DS authentication with the 3DS Requestor Challenge Indicator set to 04 (Challenge requested: Mandate) or use an alternative technical SCA solution. Until such time as all Issuers support the response code that indicates that SCA is required, a Merchant is advised always to send an authentication request following an authorization that is declined for non-financial and non-technical reasons.

# Secure Corporate Payments

When an authentication or an authorization is flagged as a Secure Corporate Payment, the Acquirer must ensure that the Transaction meets the requirements set out in applicable regulation for application of the Secure Corporate Payment exemption.

# 5.1.2 Issuer Requirements

In the Europe Region, the Rule on this subject is modified as follows.

1. An Issuer must allow its Cardholders to engage in Maestro e-commerce Transactions on any Maestro Card except a prepaid Card.
2. An Issuer in Italy or San Marino must allow its Cardholders to engage in e-commerce Transactions using a Debit Card bearing the Debit Mastercard brand or the Maestro brand.
3. An Issuer in Albania, Austria, Bosnia, Bulgaria, Croatia, Czech Republic, Hungary, Israel, Kosovo, Montenegro, North Macedonia, Poland, Romania, Serbia, Slovakia, or Slovenia must not participate in the Activation During Shopping (ADS) method of Cardholder enrollment in Mastercard Identity Check in a manner that would require the Cardholder to manually input any personal data, including a user name and/or password. An Issuer may require a Cardholder to confirm acceptance of Mastercard Identity Check terms and conditions and/or acknowledgment of service activation by clicking a button. This Cardholder confirmation must be limited to a single click and a single screen in the whole process.
4. An Issuer must technically support the authorization and clearing of the data fields and values described in Appendix C, Transaction Identification Requirements, for e-commerce Transactions and Digital Secure Remote Payment Transactions containing UCAF data, if the Transactions are processed via the Interchange System. If the Transactions are processed via an alternative switch, the Issuer must technically support the corresponding data fields and values specified by the alternative switch.

In the EEA, UK, and Gibraltar, the Rule on this subject is modified as follows. The UCAF field must be identified as specified by the registered switch of the Customer's choice.


# Card-Not-Present Transactions

# 5.1.3 Use of Static AAV for Card-not-present Transactions

# SCA Requirements

The following Rule applies for Intracountry and Cross-border Transactions within and between SCA Countries.

An Issuer located in an SCA Country must decline authorization of a Remote Electronic Transaction using the "soft decline" response code defined by the registered switch of its choice, if SCA is required and is missing. In response to a CNP authorization request, an Issuer must not use the "soft decline" response code for any reason other than requesting SCA. An Issuer must not use this response code if an authorization request is flagged as "fully authenticated." An Issuer must not challenge more than 5 percent of all authentication requests carrying an Acquirer exemption or exclusion flag unless there is material risk of fraud, and an Issuer that has not opted out of the Authentication Express program must not challenge more than 5 percent of all authentication requests carrying a SCA delegation flag unless there is material risk of fraud.

# 5.1.3 Use of Static AAV for Card-not-present Transactions

In Belgium, an Issuer of Maestro Cards must technically support Card-not-present Transactions that contain a value of 3 in DE 48 (Additional Data - Private Use), subelement 43 (Static AAV), position 1 of Authorization Request/0100 messages. The Issuer must make individual authorization decisions and must not automatically decline authorization of Card-not-present Transactions containing these values. In Belgium, an Issuer must technically support the DOLM Program coding included in AN 4727 Revised Standards for the Withdrawal of Special Maestro Recurring Payments Programs in Europe Region and Introduction of DOLM in Belgium. The static AAV must be provided in authorization messages in the field and with the values specified by the registered switch of the Customer's choice.

# 5.2 Mail Order and Telephone Order (MO/TO) Maestro Transactions

In the Europe Region, the Rule on this subject is modified as follows.

# 5.2.1 Definitions

Solely within the Europe Region, the following terms have the meanings set forth below:

- Address Verification Service (AVS): A process whereby the Issuer checks the address given for a Card-not-present Transaction. For more information on AVS participation and message requirements, refer to Chapter 5 of the Customer Interface Specification manual and Chapter 8 of the Authorization Manual.
- Cardholder Authority: A Cardholder’s instructions requesting a Merchant to perform a CNP Transaction.
- CVC 2/AVS Check: Automated verification by the Issuer of the Card Validation Code (CVC) 2 and address details provided for a CNP Transaction.
- Mail Order Transaction: A CNP Transaction for which the Cardholder provides a written Cardholder Authority.


# Card-Not-Present Transactions

# 5.2.2 Intracountry Maestro MO/TO Transactions—Cardholder Authority

Phone Order Transaction, Telephone Order Transaction: A CNP Transaction for which the Cardholder provides a Cardholder Authority through the telephone system.

An Acquirer in Ireland or France that acquires intracountry MO/TO transactions under other debit brands must also acquire MO/TO Transactions under the Maestro brand.

Merchants located in Europe Region countries designated by the Corporation may at their option offer MO/TO Transactions on Maestro Cards issued in the same country. Merchants in Ireland, Turkey, and France may offer this option.

The Rules for Maestro MO/TO Transactions are the same as those for Maestro face-to-face POS Transactions except that:

1. A MO/TO Transaction must have its own unique Cardholder Authority.
2. Merchants must collect and transmit CVC 2 for all MO/TO Transactions. AVS checking is optional.
3. Merchants must not present the Transaction until the products or services are ready to be dispatched.
4. If the Merchant does not give the Cardholder the Transaction receipt or the products and/or services upon completion of the Transaction, then they must be either delivered to the Cardholder by a method chosen at the Merchant’s discretion or collected by the Cardholder.

# 5.2.2 Intracountry Maestro MO/TO Transactions—Cardholder Authority

For a Maestro Mail Order Transaction, a document signed by the Cardholder or a document which the Acquirer considers to be acceptable in lieu of a signed document (for example, an authority sent by facsimile transmission).

For a Maestro Telephone Order Transaction:

1. Either instructions given over the telephone by the Cardholder to the Merchant, either to the Merchant’s staff or to equipment operated by the Merchant (for example, an interactive voice system), or instructions given over the telephone by means of a text message from the Cardholder to the Merchant, via equipment operated by the Merchant; and
2. The date on which the Cardholder gave her/his authority.

# 5.2.3 Intracountry Maestro MO/TO Transactions—Transactions Per Cardholder Authority

A Cardholder Authority must contain:

1. The Card’s PAN, expiry date, and CVC 2;
2. The Cardholder’s name and home address (including postcode);
3. The Transaction amount (including postage and packaging);
4. If products or services are to be delivered, the delivery address, and if the goods/services are to be delivered to or collected by a third party, the third party’s name.

# 5.2.4 Intracountry Maestro MO/TO Transactions—CVC 2/AVS Checks

The following applies where the Merchant carries out AVS checking and for CVC 2 checks:

1. The Cardholder authority must include the CVC 2 shown on the Cardholder’s Card.



206
# Card-Not-Present Transactions

# 5.3 Credential-on-File Transactions

2. When entering the Transaction, the Merchant must key in the CVC 2 and numeric data in the Cardholder’s address and postcode.

3. Online authorization must be sought for the Transaction.

4. The Acquirer must attempt to send the authorization request to the Issuer accompanied by the data referred to in paragraph 2 above.

When the Issuer’s authorization response is an approval, the Issuer must accompany its response with an indication as to whether:

- The address, postcode, and CVC 2 data provided matches information held in its own records;
- The address, postcode, and CVC 2 data does not match information held in its own records;
- The address and postcode data provided have not been checked; or
- The address, postcode, and CVC 2 data has not been supplied.

When the Acquirer sends a response to the authorization request to the Merchant’s POS Terminal, the message must include the Issuer’s CVC 2 and AVS responses.

The Merchant must not re-use the CVC 2 or retain the CVC 2 in any manner for any purpose.

The CVC 2 on a Cardholder authority for a Mail Order Transaction must be rendered unreadable prior to storage.

# 5.3 Credential-on-File Transactions

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. Credential-on-file Transactions must be identified in authorization and clearing messages as specified by the registered switch of the Customer's choice.

# 5.4 Recurring Payment Transactions

In Belgium, the Rule on this subject is modified as follows. A Merchant with Transactions processed by an Acquirer located in the EEA, UK, or Gibraltar may submit Maestro recurring payment Transactions on a Card issued under a Maestro BIN assigned for Belgium, using a risk-based authentication approach in accordance with the Debit Online Low Risk Merchant (DOLM) program requirements.

The Acquirer located in the EEA, UK, or Gibraltar must ensure that the Merchant is properly registered for DOLM before using a Mastercard-assigned Merchant ID and static AAV on Transactions completed on Maestro Cards issued in Belgium.

An Acquirer must ensure that a Merchant not registered for DOLM does not use the DOLM Transaction coding set out in DOLM program documentation.

An Issuer must:

1. Permit its Cardholders to perform recurring payment Transactions on all Maestro Cards except prepaid Maestro Cards. For prepaid Maestro Cards, it is strongly recommended that an Issuer allow its Cardholders to perform recurring payment Transactions;


# Card-Not-Present Transactions

# 5.4 Recurring Payment Transactions

2. Recognize all properly identified recurring payment Transactions, including the identification of the first payment as either a face-to-face recurring payment Transaction or as an e-commerce recurring payment Transaction, depending on the environment in which the recurring payment arrangement is initiated.

In France, Germany, Hungary, Ireland, Poland, Romania, Ukraine, and the United Kingdom, the Rule on this subject, as it applies to Domestic recurring payment Transactions, is modified as follows:

1. It is recommended that an Acquirer ensure that a Merchant only includes the Card expiration date in the first Transaction of a recurring payment arrangement involving a particular Mastercard or Maestro Account number. Mastercard further recommends that the Card's expiration date not be included in any subsequent recurring payment Transaction authorization requests involving the same PAN. An Issuer must not decline a non-face-to-face recurring payment Transaction from a Merchant solely on the basis of missing Card expiration date information.
2. If a recurring payment Transaction authorization request is declined by the Issuer, the Acquirer must ensure that the Merchant resubmits the Transaction no more than once per day for a maximum of 31 consecutive days until the Transaction is approved by the Issuer.

For recurring payment Transactions relating to a bill invoiced to the Cardholder, it is recommended that in the First Presentment/1240 message, the Merchant name in DE 43 subfield 1 be followed by a space, the word "BILL" or the local language equivalent, a space, and the bill reference number.

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. Recurring payment Transactions must be identified in authorization messages as specified by the registered switch of the Customer’s choice. If provided, the Merchant advice code must be provided in the field and with the value specified by the registered switch of the Customer's choice.

# SCA Requirements

The following Rules apply to Intracountry and Cross-border Transactions within and between SCA Countries.

SCA is required on the initial authorization in a recurring payment arrangement, unless the initial authorization takes place as MO/TO (if allowed by local authorities).

The initial authorization (either authorization request or account status inquiry) in a recurring payment arrangement must be identified as a recurring payment using the appropriate values in the fields specified by the registered switch of the Customer’s choice. As an exception to the preceding Rule, if the initial authorization is a MO/TO transaction, it must be identified as either mail order or telephone order, and not as a recurring payment.

An Acquirer must provide the unique Trace ID from the initial recurring payment authorization response in the appropriate field of a subsequent recurring payment authorization request, as specified by the registered switch of its choice.


# Card-Not-Present Transactions

# 5.5 Installment Billing

If the initial authorization took place as MO/TO (if allowed by local authorities), or occurred before 14 September 2020, then the Trace ID may be populated with a default value as specified by the registered switch of the Acquirer's choice. Alternatively, if the initial authorization occurred before 14 September 2020, the Acquirer may provide the Trace ID of any other authorization belonging to that same recurring payment arrangement, provided that this authorization took place before 14 September 2020. The Trace ID will be considered the reference to the first transaction of that series of recurring transactions mandate that the Cardholder authenticated. The Issuer must be able to use the Trace ID provided in the authorization message of a subsequent recurring payment to retrieve and confirm the original recurring payment transaction.

# 5.5 Installment Billing

In the Europe Region countries where the Mastercard installment billing service is supported, the Rule on this subject is modified as follows. In participating countries in the Europe Region, installment billing is not limited to Domestic Transactions only. As an exception to the foregoing, installment billing in Russia is initially limited to Domestic Transactions. Acquirers and Issuers that wish to support installment billing on Cross-border Transactions are advised to carry out all necessary and appropriate legal verifications before implementing the service.

Within a single country, only one option may be supported, either Issuer-financed installment billing or Acquirer-financed installment billing, unless otherwise noted. The Rules in this section apply to both options unless otherwise specified. Merchant-financed installment billing is in place in Greece. Refer to the Domestic Rules folder on Mastercard Connect® for further information.

Issuer-financed installment billing is in place in the following countries:

- Czech Republic
- Hungary
- Ireland
- Poland
- Romania
- Russia
- Slovakia
- Slovenia
- Ukraine
- United Kingdom

The installment billing service is available in both face-to-face and non-face-to-face environments and for Mastercard, Debit Mastercard, and Maestro Card payments, except in the Czech Republic, Hungary, Ireland, Poland, Russia and Ukraine, where support of installment billing on Maestro is not required.


# Card-Not-Present Transactions

# 5.5 Installment Billing

# Issuer-financed Installment Billing

A participating Issuer must clearly inform its Cardholders of the terms and conditions applicable to installment billing, the Card products that are eligible for installment billing, installment transaction fees, and outstanding amounts in connection with installment transactions performed by a Cardholder.

In the Czech Republic, Hungary, Poland, Russia, Slovakia, Slovenia, Ukraine, and the United Kingdom, an Issuer that wishes to participate in the installment billing service must register for "Mastercard POS Enabled Installments" via Mastercard Connect. Except in Russia, where there is no impact to the authorization message, the Issuer must be able to support the enhanced authorization request and response messages aimed at receiving and sending sufficient information on payment options and installment parameters to the POI. A participating Issuer must be able to split and post the billing of the Transaction amount to the Cardholder's Account according to the option selected at the POI.

# Acceptance Mark

The Acquirer must ensure that a Merchant in the Czech Republic, Hungary, Poland, Romania, Russia, Slovakia, Slovenia, or Ukraine that participates in the Mastercard installment billing service displays the special MC Installments mark at the POI.

# Merchant Support - Czech Republic, Hungary, Poland, and Ukraine

The Acquirer of a Merchant identified with an MCC not contained in the Merchant Exclusions section must ensure that the Mastercard installment billing service is supported at all POS Terminals and Card-not-present acceptance locations of the Merchant in the specific country, as applicable. At Cardholder-activated Terminals, support for the Mastercard installment billing service is a recommendation and not a requirement.

# Merchant Support - Romania Only

The Acquirer of a Merchant in Romania identified with an MCC in the following list must ensure that the Mastercard installment billing service is supported at all newly deployed POS Terminals and new Card-not-present acceptance locations of the Merchant, as applicable. The Acquirer of a Merchant in Romania identified with an MCC in the following list must ensure that the Mastercard installment billing service is supported at all POS Terminals and Card-not-present acceptance locations of the Merchant, as applicable.

MCC and Description0742 Veterinary Services0780 Horticultural and Landscaping Services1711 Air Conditioning, Heating, and Plumbing Contractors1731 Electrical ContractorsMCC and Description5732 Electronic Sales5733 Music Stores - Musical Instruments, Pianos, Sheet Music5734 Computer Software Stores5921 Package Stores, Beer, Wine, Liquor



210
# Card-Not-Present Transactions

# 5.5 Installment Billing

|MCC and Description|MCC and Description|
|---|---|
|1750 Carpentry Contractors|5932 Antique Shops - Sales, Repairs, and Restoration Services|
|1771 Concrete Work Contractors|5940 Bicycle Shops - Sales and Service|
|3297 Tarom Romanian Air Transport|5941 Sporting Goods Stores|
|4511 Air Carriers, Airlines - not elsewhere classified|5944 Clock, Jewelry, Watch, and Silverware Store|
|4722 Travel Agencies and Tour Operators|5945 Game, Toy, and Hobby Shops|
|4812 Telecommunication Equipment Including Telephone Sales|5946 Camera and Photographic Supply Stores|
|4816 Computer Network/Information Services|5948 Leather Goods and Luggage Stores|
|5013 Motor Vehicle Supplies and New Parts|5965 Direct Marketing - Combination Catalog and Retail Merchants|
|5021 Office and Commercial Furniture|5969 Direct Marketing - Other Direct Marketers - not elsewhere classified|
|5039 Construction Materials - not elsewhere classified|5971 Art Dealers and Galleries|
|5044 Office, Photographic, Photocopy, and Microfilm Equipment|5975 Hearing Aids - Sales, Service, Supply Stores|
|5045 Computers, Computer Peripheral Equipment, Software|5976 Orthopedic Goods - Artificial Limb Stores|
|5047 Dental/Laboratory/Medical/Ophthalmic Hospital Equipment and Supplies|5977 Cosmetic Stores|
|5065 Electrical Parts and Equipment|5983 Fuel Dealers - Coal, Fuel Oil, Liquified Petroleum, Wood|
|5072 Hardware Equipment and Supplies|5999 Miscellaneous and Specialty Retail Stores|
|5074 Plumbing and Heating Equipment|6300 Insurance Sales, Underwriting, and Premiums|
|5094 Precious Stones and Metals, Watches and Jewelry|7032 Recreational and Sporting Camps|
|5111 Stationery, Office Supplies, Printing and Writing Paper|7298 Health and Beauty Spas|
|5137 Men's, Women's, and Children's Uniforms and Commercial Clothing|7372 Computer Programming, Data Processing, and Integrated Systems Design Services|
|5139 Commercial Footwear|7379 Computer Maintenance, Repair, and Services - not elsewhere classified|
|5198 Paints, Varnishes, and Supplies|7395 Photo Developing, Photofinishing Laboratories|
|5200 Home Supply Warehouse Stores|7531 Automotive Body Repair Shops|


# Card-Not-Present Transactions

# 5.5 Installment Billing

|MCC and Description|MCC and Description|
|---|---|
|5211 Building Materials, Lumber Stores|7534 Tire Retreading and Repair Shops|
|5231 Glass, Paint, Wallpaper Stores|7538 Automotive Service Shops|
|5251 Hardware Stores|7622 Electronic Repair Shops|
|5511 Automobile and Truck Dealers - Sales, Service, Repairs, Parts, and Leasing|7699 Miscellaneous Repair Shops and Related Services|
|5521 Automobile And Truck Dealers - (Used Only) - Sales|7991 Tourist Attractions and Exhibits|
|5532 Automotive Tire Stores|7997 Clubs - Country Clubs, Membership (Athletic, Recreation, Sports), Private Golf Courses|
|5533 Automotive Parts, Accessories Stores|7999 Recreation Services - not elsewhere classified|
|5571 Motorcycle Shops and Dealers|8011 Doctors - not elsewhere classified|
|5599 Miscellaneous Automotive, Aircraft, and Farm Equipment Dealers - not elsewhere classified|8021 Dentists, Orthodontists|
|5611 Men's and Boy's Clothing And Accessories Stores|8042 Optometrists, Ophthalmologists|
|5621 Women's Ready To Wear Stores|8043 Opticians, Optical Goods, and Eyeglasses|
|5631 Women's Accessory And Specialty Stores|8049 Chiropodists, Podiatrists|
|5641 Children's and Infant's Wear Stores|8050 Nursing and Personal Care Facilities|
|5651 Family Clothing Stores|8062 Hospitals|
|5655 Sports Apparel, Riding Apparel Stores|8071 Dental and Medical Laboratories|
|5661 Shoe Stores|8099 Health Practitioners, Medical Services - not elsewhere classified|
|5681 Furriers and Fur Shops|8211 Schools, Elementary and Secondary|
|5691 Men's and Women's Clothing Stores|8220 Colleges, Universities, Professional Schools, and Junior Colleges|
|5699 Accessory and Apparel Stores - Miscellaneous|8249 Schools, Trade and Vocational|
|5712 Equipment, Furniture, and Home Furnishings Stores (except Appliances)|8299 Schools and Educational Services - not elsewhere classified|
|5713 Floor Covering Stores|8351 Child Care Services|
|5714 Drapery, Upholstery, and Window Coverings Stores|9222 Fines|
|5719 Miscellaneous House Furnishing Specialty Shops|9311 Tax Payments|
|5722 Household Appliance Stores| |



212
# Card-Not-Present Transactions

# 5.5 Installment Billing

# Merchant Support - Slovakia and Slovenia Only

The Acquirer of a Merchant in Slovakia or Slovenia identified with an MCC not contained in the
Merchant Exclusions section must ensure that the Mastercard installment billing service is
supported at all POS Terminals and Card-not-present acceptance locations of the Merchant, as
applicable. At Cardholder-activated Terminals (CATs), support for the Mastercard installment
billing service is a recommendation and not a requirement.

# Merchant Support – Russia

In Russia, a Merchant that wishes to participate in installment billing must provide a minimum
of two months of free installments.

# Exclusions

The Mastercard installment billing service is permitted only for purchases of goods and services.
It must not be offered on purchase with cash back Transactions.
Installments must not be offered if the clearing amount might not match the authorization
amount, for example in the case of a preauthorization or an incremental authorization, or if the
Transaction type does not require Cardholder involvement, such as a Merchant-initiated
Transaction or a recurring payment Transaction.
An Acquirer must not deploy installments-capable POS applications in an acceptance location
identified with one of the following MCCs:

- 4829 (Money Transfer - Merchant)
- 6010 (Manual Cash Disbursements - Customer Financial Institution)
- 6050 (Quasi-Cash - Customer Financial Institution)
- 6051 (Quasi-Cash - Merchant)
- 6532 (Payment Transaction - Customer Financial Institution)
- 6533 (Payment Transaction - Merchant)
- 6536 (MoneySend Intracountry)
- 6537 (MoneySend Intercountry)
- 6538 (MoneySend Funding)
- 6540 (POI Funding Transaction)
- 7995 (Gambling Transactions)

In Russia, the following additional MCCs are also excluded:

- 9311 Tax payments
- 9399 Government services - Not Elsewhere Classified
- 9211 Court Costs including Alimony and Child Support
- 9222 Fines
- 9223 Bail and Bond Payments
- 9402 Postal services - government only
- 8211 Schools, Elementary and Secondary
- 8220 Colleges, Universities, Professional Schools, and Junior Colleges


# Card-Not-Present Transactions

# 5.5 Installment Billing

- 8398 Charities
- 7995 Gambling Transactions

In the United Kingdom, the following additional MCCs are also excluded:

- 6011 (Automated Cash Disbursements - Customer Financial Institution)
- 8999 (Professional Services - not elsewhere classified)
- 9311 (Tax Payments)

In the Czech Republic and Hungary, the following additional MCCs are also excluded:

- 6011 (Automated Cash Disbursements - Customer Financial Institution)
- 9406 (Government-owned Lottery)

In addition, in Hungary, support for installment billing at Merchants identified with any of the following MCCs is neither excluded nor mandatory:

|MCC|Description|
|---|---|
|3000-3350|Airlines, Air Carriers|
|4111|Transportation-Suburban and Local Commuter Passenger, including Ferries|
|4112|Passenger Railways|
|4121|Limousines and Taxicabs|
|4225|Public Warehousing|
|4789|Transportation Services - Not Elsewhere Classified|
|5310|Discount Stores|
|5422|Freezer, Locker Meat Provisioners|
|5441|Candy, Nut, Confectionery Stores|
|5451|Dairy Products Stores|
|5462|Bakeries|
|5499|Miscellaneous Food Stores|
|5811|Caterers|
|5812|Eating Places, Restaurants|
|5813|Bars, Cocktail Lounges, Discotheques, Nightclubs and Taverns|
|5814|Fast Food Restaurants|
|5935|Salvage and Wrecking Yards|
|5942|Book Stores|
|5947|Gift Card, Novelty and Souvenir Shops|
|5963|Door-to-Door Sales|


# Card-Not-Present Transactions

# 5.5 Installment Billing

|MCC|Description|
|---|---|
|5964|Direct Marketing-Catalog Merchants|
|5992|Florists|
|5993|Cigar Stores and Stands|
|5994|News Dealers and Newsstands|
|6012|Merchandise and Services - Customer Financial Institution|
|6211|Securities-Brokers/Dealers|
|7210|Cleaning, Garment, and Laundry Services|
|7211|Laundry Services-Family and Commercial|
|7216|Dry Cleaners|
|7273|Dating and Escort Services|
|7342|Exterminating and Disinfecting Services|
|7523|Automobile Parking Lots and Garages|
|7542|Car Washes|
|7829|Motion Picture and Video Tape Production and Distribution|
|7832|Motion Picture Theaters|
|7998|Aquariums, Dolphinariums, Zoos and Seaquariums|
|8041|Chiropractors|
|8241|Schools, Correspondence|

In Poland, the following additional MCCs are also excluded:

|MCC|Description|
|---|---|
|4784|Bridge and Road Fees, Tools|
|5541|Service Stations with or without Ancillary Service|
|5542|Fuel Dispenser, Automated|
|5812|Eating Places, Restaurants|
|5813|Bars, Cocktail Lounges, Discotheques, Nightclubs and Taverns|
|5814|Fast Food Restaurants|
|5933|Pawn Shops|
|5960|Direct Marketing - Insurance Services|
|5962|Direct Marketing-Travel Related Arrangement Services|



215
# Card-Not-Present Transactions

# 5.5 Installment Billing

|MCC|Description|
|---|---|
|5964|Direct Marketing - Catalog Merchants|
|5965|Direct Marketing - Combination Catalog and Retail Merchants|
|5966|Direct Marketing - Outbound Telemarketing Merchants|
|5967|Direct Marketing - Inbound Telemarketing Merchants|
|5968|Direct Marketing - Continuity/Subscription Merchants|
|5969|Direct Marketing - Other Direct Marketers - Not Elsewhere Classified|
|6011|Automated Cash Disbursements - Customer Financial Institution|
|6012|Merchandise Services - Customer Financial Institutions|
|6211|Securities-Brokers/Dealers|
|7523|Automobile Parking Lots and Garages|
|9405|Intra-Government Purchases - Government Only|
|9406|Government-Owned Lottery (including totalizator sportowy in Poland)|

In addition, in Poland, support for installment billing at Merchants identified with the following MCCs is neither excluded nor mandatory:

|MCC|Description|
|---|---|
|3000-3350|Airlines|
|4511|Air Carriers, Airlines - Not Elsewhere Classified|

In Ukraine, the following additional MCCs are also excluded:

|MCC|Description|
|---|---|
|5811|Caterers|
|5812|Eating Places, Restaurants|
|5813|Bar Lounge Disco Nightclub Tavern-Alcoholic Drinks|
|5814|Fast Food Restaurants|
|6011|Automated Cash Disbursements - Customer Financial Institution|
|6012|Merchandise and Services – Customer Financial Institution|
|6211|Securities-Brokers/Dealers|
|9311|Tax Payments|



216
# Card-Not-Present Transactions

# 5.5 Installment Billing

|MCC|Description|
|---|---|
|9399|Government Services - Not Elsewhere Classified|
|9402|Postal Services - Government Only|
|9405|Intra-Government Purchases - Government Only|
|9406|Government-Owned Lottery (Non–U.S.)|

# Transaction Amount

In Hungary, an Acquirer must enable the installment billing option only for Transaction amounts above HUF 20,000.

In Poland, an Acquirer must enable the installment billing option only for Transaction amounts above PLN 400. An Issuer must not set a different minimum amount.

In Ukraine, an Acquirer must enable the installment billing option only for Transaction amounts above UAH 500. An Issuer may set a minimum above this amount, but not lower than this amount.

In the United Kingdom, the minimum purchase amount above which installment billing may be offered is GBP 150. An Issuer may set a minimum above this amount.

In the Czech Republic, the minimum purchase amount above which installment billing may be offered is CZK 1500. An Issuer may set a minimum above this amount.

In Slovakia and Slovenia, the minimum purchase amount above which installment billing may be offered is EUR 50. An Issuer may set a minimum above this amount.

# Information Requirements

The Cardholder must be informed clearly of the installment terms before agreeing to the installment billing arrangement. The required information includes the number, frequency, and amount of the installments and any associated fees. The information may be provided via screen messages on the POS terminal, or in another manner, provided that it is clear to the Cardholder.

The POS terminal or electronic commerce payment page of a participating Merchant must display both payment options - full payment and installment billing. If no selection is made then "full payment" is the default option. In the installments section of the menu, the cardholder may have the option to choose the number and/or frequency of installments (for example, between two and 24 installments).

Model POS Terminal and e-commerce displays are provided in Appendix F of this manual.

In Russia, the Cardholder will be provided repayment options between 2 and 12 months.

In Poland, the Cardholder will be provided repayment options of 3, 6, or 12 months.

In Ukraine, the Issuer must present to the Cardholder a maximum of three repayment options, for example, 3, 6, and 9 months, or 6, 9, and 12 months.



217
# Card-Not-Present Transactions

# 5.5 Installment Billing

In Hungary, the authorization request must not contain the installments indicator if the currency is not HUF.

The authorization request response message must contain the following information, at a minimum:

- Total amount due
- Installment amount
- Interest rate
- Installment fee or annual percentage rate (APR)

In Slovenia, the authorization request response message must contain the following information, at a minimum:

- Total amount due
- Interest rate
- Installment fee
- Call center number

In Poland, the authorization request response message must contain three occurrences of the following installment payment data, for each of 3, 6, and 12 months payments options:

- Number of installments (optional)
- Interest rate (optional)
- Installment fee (optional)
- Annual percentage rate (optional)
- First installment amount (mandatory)
- Subsequent installment amount (optional)
- Total amount due (must include data on the total cost of funding provided to the Cardholder)

# Transaction Receipt Contents

Transaction receipt contents must be in the local language, if the Card is issued in the Merchant's country, and in English if the Card is issued in a different country.

In Russia, the receipt must be in Russian as installments are offered only on Domestic Transactions.

The Transaction receipt or e-mail confirmation page must contain the additional information listed below if the Cardholder has chosen installment billing and the authorization request has been approved:

- Transaction type (Installment).
- If applicable, installment fee charged to the Cardholder for the transaction Total amount charged to the cardholder (price of the product or service plus if applicable, installment Transaction fee).
- Payment plan (information summarizing the number of installments and the amount of each installment. If the amount of the first installment is different from the subsequent)


# Card-Not-Present Transactions

# 5.5 Installment Billing

Installment amounts, this must be clearly stated on the Transaction receipt or electronic commerce payment page).

In Poland, the above information may be provided by the Issuer. In this case, the Transaction receipt or e-mail confirmation page must contain a statement advising the Cardholder to contact the Issuer for more information.

In Hungary, the Transaction receipt or e-mail confirmation page must additionally contain a legend inviting the Cardholder to contact the Issuer for more information and a contact telephone number.

In the Czech Republic and Slovakia, the Transaction receipt or e-mail confirmation page must additionally contain a legend inviting the Cardholder to contact the Issuer for more information.

In Slovenia, the Transaction receipt or e-mail confirmation page must additionally contain the interest rate and a contact telephone number.

In Ukraine, the Transaction receipt or e-mail confirmation page must additionally contain the address of the Issuer's website.

# Support for Transaction Identification

Each Issuer and Acquirer must technically support the proper coding for installment Transaction authorization and clearing messages, as must each participating Merchant.

As an exception to the preceding Rule, in Ireland each Acquirer must support the offering of installments by integrating with the Mastercard Installment Payment Service APIs, available through the Mastercard Developer Zone. Support for installments is optional for Issuers and Merchants in Ireland.

In Russia, the requirement to support proper coding applies only for clearing messages, which must contain the installment data in PDS 181. This requirement applies to participating Issuers, Acquirers and Merchants. Effective 1 January 2023, Issuers of more than 500,000 Mastercard Credit Cards in the preceding year must technically support the offering of the installment billing service.

In Slovakia and Slovenia, this requirement applies to all Acquirers, to all Merchants apart from excluded Merchants and to participating Issuers.

In the Czech Republic, Hungary, Poland, Ukraine, and the United Kingdom, this requirement applies to all Acquirers and to participating Issuers and Merchants.

If an Acquirer's Transaction volume in the country is below a threshold determined by the local country management, support by that Acquirer for the Mastercard installment billing service is recommended rather than required.

The requirement to technically support the proper coding of installment Transactions does not apply to any Acquirer that acquires only Merchants at which support for installment billing is excluded.

In participating countries in the EEA, the Rule on this subject is modified as follows.


# Card-Not-Present Transactions

# 5.5.1 Single-Authorization Installment Billing

Installment billing Transactions must be identified in authorization and clearing messages as specified by the registered switch of the Customer's choice. If provided, the Merchant advice code must be provided in the field and with the value specified by the registered switch of the Customer's choice.

# Chargeback Rules

For Issuer-financed installment billing, chargeback message reason code 4850 does not apply.

# Authorization Processing

Offline processing is not allowed for installment Transactions. Installment Transactions are not eligible for Stand-in or X-Code authorization processing. All installment authorization requests must be approved or declined only by the Issuer. In the EEA, UK or Gibraltar, the Rule on this subject is modified as follows. The decline reason codes in the table contained in this Rule are replaced by the corresponding reason codes specified by the registered switch of the Issuer's choice. The Issuer must use the following decline response codes when appropriate, and the relevant description must be reflected on the screen of the POS Terminal or the webpage for the declined Transaction.

|DE 39 (Response Code)|Description|Reason|
|---|---|---|
|57|Transaction not permitted to Cardholder|Invalid number of installments, issuer does not offer Installment Transactions at all, or not for this specific Cardholder|
|58|Transaction not permitted to Merchant|Installment Transactions must not be initiated by this Merchant (see "Excluded Transactions")|

# 5.5.1 Single-Authorization Installment Billing

# 5.5.1.2 Transaction Processing Procedures

In the EEA, UK or Gibraltar, the Rule on this subject is modified as follows. Installment billing Transactions must contain the required data in authorization and clearing messages in accordance with the specifications of the registered switch of the Customer’s choice.

# 5.5.2 Multiple-Authorization Installment Billing

# Installment Payment Information

In the Europe Region, the Rule on this subject is modified as follows.


# Card-Not-Present Transactions

# 5.6 Transit Transactions Performed for Debt Recovery

With respect to installment payments submitted by an Installment Provider, the MCC selected by the Acquirer may describe the installment payment service rather than the primary business of the retailer or the nature of the purchase.

In the EEA, UK or Gibraltar, the Rule on this subject is modified as follows. Transit Transactions performed for debt recovery must be identified in authorization messages as specified by the registered switch of the Customer’s choice.

# 5.7 Use of Automatic Billing Updater

# 5.7.1 Issuer Requirements

ABU must be used for Mastercard and Maestro Cards issued under a BIN or BIN range assigned for:

- Ireland
- United Kingdom
- Italy
- Albania, Andorra, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia, Bulgaria, Croatia, Czech Republic, Denmark, Estonia, Finland, France, Georgia, Gibraltar, Greece, Iceland, Kazakhstan, Kosovo, Kyrgyzstan, Latvia, Lithuania, Luxembourg, Moldova, Montenegro, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Russia, Serbia, Slovakia, Slovenia, Spain, Sweden, San Marino, Tajikistan, Turkmenistan, Ukraine, Uzbekistan, and Vatican City
- Germany, Liechtenstein, and Switzerland

With the exception of the following types of cards:

- Non-reloadable prepaid Mastercard Cards in the BIN range of 539366 to 539585.
- Both consumer and corporate prepaid Cards that the Issuer does not permit to be used to enter into recurring payment arrangements, and single-use-only Virtual Accounts.
- Non-reloadable prepaid Cards, single-use-only Virtual Accounts, and those Debit Mastercard Cards or Maestro Cards that are not required to be enabled for e-commerce.
- Non-reloadable prepaid Cards, prepaid Cards that the Issuer does not permit to be used to enter into recurring payment arrangements, and single-use-only Virtual Accounts.
- Maestro Cards issued under a BIN assigned for Germany, Liechtenstein, or Switzerland are also excluded.



221
# Card-Not-Present Transactions

# 5.7.2 Acquirer Requirements

An Issuer must be able to send, receive, and process ABU data and must accurately maintain its entire Card portfolio in ABU, subject to the above-listed exceptions.

With respect to newly assigned ICAs and BINs, an Issuer is allowed six months from the date of assignment to come into compliance with the ABU requirements.

All of the types of Account changes defined in the Mastercard Automatic Billing Updater Reference Guide must be submitted to ABU.

An Issuer must not provide ABU support for Cards issued under an ICA or BIN that has not been assigned to it.

An Issuer must participate in the Mastercard Automatic Billing Updater program by completing ABU Customer Form 806 available on Mastercard Connect®.

To support the account validation process, an Issuer must report new Accounts and provide a one-time upload plus 6 months of historic data changes up to a maximum of 40 months data to the Issuer Account Change Database.

An Issuer is permitted to use an alternative continuity service, provided that it has an equivalent level of functionality and supports all Merchants globally.

# 5.7.2 Acquirer Requirements

An Acquirer must comply with the requirements set out in this section, with regard to Merchants located in the following countries:

Albania, Andorra, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Georgia, Germany, Gibraltar, Greece, Hungary, Iceland, Ireland, Italy, Kazakhstan, Kosovo, Kyrgyzstan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Moldova, Montenegro, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Russia, San Marino, Serbia, Slovakia, Spain, Sweden, Switzerland, Tajikistan, Turkmenistan, Ukraine, United Kingdom, Uzbekistan, and Vatican City.

That process the following Transaction types: Recurring payment and Credential-on-file Transactions.

An Acquirer must:

1. Be technically able to send, receive, and process ABU data, and must ensure that the acquiring host processing system used by the Acquirer incorporates ABU functionality.
2. Participate in the ABU program by completing ABU Customer Form 806 available on Mastercard Connect®.
3. Register each Merchant that participates in the ABU program.
4. Submit Account number queries to ABU on behalf of each registered Merchant before authorization. The Acquirer must then take appropriate action based on any response codes received from ABU.



222
# Card-Not-Present Transactions

# 5.8 Authentication Requirements

5. Submit account inquiry updates on behalf of each enrolled Merchant no less than once every 180 days.

It is strongly recommended that an Acquirer query the ABU database for brand flips to/from another scheme on behalf of registered Merchants located in the United Kingdom or Ireland.

An Acquirer has the option to submit brand flips to/from another scheme to the ABU program on behalf of registered Merchants.

An Acquirer is permitted to use an alternative continuity service, provided that it has an equivalent level of functionality and supports all Issuers and Merchants globally.

An Acquirer in the United Kingdom must additionally participate in the Account validation service and take appropriate action to inform Merchants of the response code received from the ABU program to support Account validation as outlined in the Mastercard ABU Reference Guide.

# EEA, UK and Gibraltar

In the EEA, UK and Gibraltar, the Rule on this subject is modified to replace references to the Automatic Billing Updater with references to the corresponding tool of the registered switch of the Customer’s choice.

# 5.8 Authentication Requirements

The Rules in this section apply with regard to Remote Electronic Transactions and to the Merchants that carry out such Transactions.

"PSD2 RTS" means the 2nd Payment Services Directive (Directive [EU] 2015/2366 of 25 November 2015) Regulatory Technical Standards on Strong Customer Authentication ("SCA").

"SCA Country, SCA Countries" means the countries, islands and territories that have adopted legislation requiring Strong Customer Authentication (e.g., legislation transposing the PSD2 RTS, or similar legislation).

These countries are Austria, Belgium, Bulgaria, Croatia, Czech Republic, Cyprus, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, San Marino, Slovakia, Slovenia, Spain, Sweden, United Kingdom, Ceuta, Melilla, Azores, Madeira, Aland Islands, Jan Mayen, French Guiana, Guadeloupe, Martinique, Réunion, Saint Martin (French Part), and Mayotte.

# 5.8.1 Acquirer Requirements

# EMV 3DS and Identity Check

An Acquirer must ensure that its online Merchants support Cardholder authentication using EMV 3-D Secure version 2 (EMV 3DS) and comply with the Mastercard Identity Check Program, including display of the Identity Check brand.

An Acquirer must ensure, for itself and for its Service Providers (e.g., 3-D Secure Service Providers) the full implementation of EMV 3DS 2.2. In addition, it must ensure that its e-commerce Merchants and Service Providers (e.g., 3DS Service Providers) use the EMV 3DS 2.2.



223
# Card-Not-Present Transactions

# 5.8.2 Issuer Requirements

authentication to Merchant app redirection (also called 3DS Requestor App URL). An Acquirer may implement alternative technical authentication solutions that provide equivalent authentication features and performance.

A Merchant that already supports EMV 3DS version 2.1 must continue to support this format to ensure interoperability with Issuers that do not yet support EMV 3DS version 2.2 (for example, those outside of Europe).

In the EEA, Gibraltar, UK, Andorra, Monaco, San Marino, Switzerland, and Vatican City, an Acquirer and its online Merchants may implement alternative technical authentication solutions that are compliant with the Mastercard Identity Check Key Performance Indicators, which are published in the Mastercard Identity Check Program Guide.

# 5.9 Merchant-initiated Transactions

The following Rules apply for Intracountry and Cross-border Transactions within and between SCA Countries.

A Merchant-initiated Transaction (MIT) may represent a single payment or multiple payments (e.g., installment payments, travel bookings, purchases at marketplaces) or a recurring payment arrangement (e.g., utility bills, streaming services).

To set up each individual MIT mandate, SCA is required, in addition to an agreement between the Merchant and the Cardholder specifying the reason for the payment and the payment amount (or an estimate when the precise amount is not known).

In addition to the Rules set out below, a Merchant with Transactions processed by an Acquirer located in an SCA Country that performs a MIT on a Card issued under a Maestro BIN assigned for Belgium must be registered in the Debit Online Low Risk Merchant Program.

An Acquirer is only allowed to process an MIT when:

- An MIT agreement has been established where the Merchant initiates a Transaction in which the Cardholder (1) is not actively triggering the payment and (2) at the time of Transaction initiation, is not interacting with a Merchant app or website, or
- The Transaction is triggered by the Merchant, as the Transaction could not have been triggered by the Cardholder during checkout, because:


# Card-Not-Present Transactions

# 5.9 Merchant-initiated Transactions

The MIT exclusion must not be used to bypass the SCA requirements for Transactions for which Card data has been registered on file with the Merchant and the Cardholder triggers the payment (a Credential-on-File CIT).

An Acquirer must identify the MIT by populating the authorization message (either an authorization request or account status inquiry) with the appropriate value in the field specified by the registered switch of its choice. An Acquirer must use an account status inquiry when the MIT agreement has been established for a zero amount.

Setting up an MIT requires an authorization request or an account status inquiry, the Trace ID of which must be provided by the Acquirer in all subsequent related authorizations. Further processing of an MIT, including the Trace ID, must reflect the recurring payments and/or credential-on-file processing flags and rules.

If the initial authorization occurred before 14 September 2020 and its Trace ID is not available (for example, because it was not stored), then the Trace ID must be populated with a default value as specified by the registered switch of the Customer’s choice.

Issuers must be able to process the Trace ID, for example to validate if SCA took place to set up the MIT.

The requirement to reference the initial Authorization’s Trace ID does not apply to reversals, which must continue to include the Trace ID of the authorization to be reversed.

In the case of Transactions in the travel/hospitality sector that are coded as MIT, the Trace ID must be populated with a default value which is different from that which is used in other sectors, when necessary to indicate that proof of authentication is not available, owing to the involvement of a third party sales agent.

If an Acquirer is not able to properly code a Transaction as MIT, the Acquirer, is allowed to code the Transaction as MOTO, provided that SCA was performed as required by the applicable legislation.

An Acquirer is only allowed to submit an authorization for an MIT without proof of authentication - either coded as MOTO or with MIT indicator - if the Merchant indicates to the Acquirer that the Transaction was initiated on the basis of an MIT agreement.

When an authorization is flagged as a Merchant Initiated Transaction without proof of authentication, the Acquirer must ensure that the Transaction meets the requirements set out in applicable legislation.

An Acquirer must identify the specific MIT type, or in the case of a CIT occurring in an e-commerce environment that will be followed by one or more MITs, the specific CIT type in each authorization message in the field specified by the registered switch of its choice.

Travel/hospitality businesses are those identified with following MCCs:

|Airlines & Air Carriers|MCCs 3000 through 3350 and 4511|
|---|---|
|Lodging|MCCs 3501 through 3999 and 7011|



225
# Card-Not-Present Transactions

# Latin America and the Caribbean Region

|Car Rentals|MCCs 3351 through 3500 and 7512|
|---|---|
|Cruise Lines|MCC 4411|
|Travel Agencies|MCC 4722|
|Passenger Railways and Railroads-Freight|MCC 4112 and 4011|
|Vacation Rentals|MCC 6513|
|Bus Lines|MCC 4131|
|Transportation, including Ferries|MCC 4111|
|Taxi Cabs and Limousines|MCC 4121|
|Transportation Services - Not elsewhere classified|MCC 4789|
|Campgrounds and Trailer Parks|MCC 7033|
|Motor Home and Recreational Vehicle Rentals|MCC 7519|
|Tourist Attractions and Exhibits|MCC 7991|
|Aquariums, Dolphinariums, Zoos and Seaquariums|MCC 7998|
|Insurance Sales, Underwriting and Premiums|MCC 6300|
|Direct Marketing - Insurance Sales|MCC 5960|
|Government Services|MCC 9399|
|Parking Lots & Garages|MCC 7523|

# Latin America and the Caribbean Region

The following modifications to the Rules apply in the Latin America and the Caribbean Region. Refer to Appendix A for the Latin America and the Caribbean Region geographic listing.

# 5.1 Electronic Commerce Transactions

# 5.1.1 Acquirer and Merchant Requirements

In Brazil, the Rule on this subject is modified as follows: Merchant websites must not display the Mastercard Acceptance Mark accompanied by the “débito” identifier.

# 5.1.2 Issuer Requirements

In Brazil, the Rule on this subject is modified as follows:



226
# Card-Not-Present Transactions

# 5.1.4 Debit Small-Ticket Digital Transaction Program: Brazil Only

An Issuer in Brazil must enable all Maestro Account ranges (including prepaid Accounts) to perform e-commerce Transactions. The use of Mastercard® Identity Check authentication is highly recommended.

The Debit Small-Ticket Digital Transaction Program (the “Program”) allows a Maestro Account issued in Brazil to conduct e-commerce Transactions at a Merchant located in Brazil. The following Transaction eligibility requirements apply:

- The Transaction is conducted with a Maestro Account (including prepaid Accounts) issued in Brazil;
- The Transaction occurs at a qualifying Merchant located in Brazil, as identified in DE 43, subfield 6 (Card Acceptor Country Code) of the Authorization Request/0100 or Financial Transaction Request/0200 message and the Merchant Country Name field on the Mastercard Analytics Portal. A qualifying Merchant under the Program is defined as one that maintains monthly combined Mastercard and Maestro fraud Transaction volume that does not exceed 40 basis points;
- Transactions must be identified with all required Transaction data;
- At least sixty percent (60%) of the Transactions must involve Maestro Accounts tokenized via the Mastercard Digital Enablement Service for use in Credential-on-File Transactions occurring at the Merchant’s website or digital application (in Authorization Request/0100 and Financial Transaction Request/0200 messages, DE 48, subelement 26 [Wallet Program Data], subfield 1 [Wallet ID] contains a value of 327 [Merchant tokenization program]);
- For Transaction amounts up to BRL 300, the Issuer must use its standard authorization parameters when deciding whether to approve or decline a Transaction. For Transaction amounts equal to or exceeding BRL 300, the Issuer may implement appropriate risk-based authorization parameters at its discretion;
- New Merchants have a six-month grace period from the start date of the Merchant’s participation in the Program to become compliant with all technical requirements and two more months to be 100% compliant with all additional Program requirements.
- Current participating Merchants have two months to become fully compliant with the new program requirements;
- The Merchant must enable Debit Mastercard and Maestro acceptance, and its Debit Mastercard Transactions must be properly submitted for dual message authorization processing;
- Each Transaction must be identified as either an original Digital Secure Remote Payment Transaction or subsequent Digital Secure Remote Payment Transaction, or involve the sharing of Identity Check Insights; and
- At least sixty percent (60%) of non-recurring Credential-on-File Transactions must involve the sharing of Identity Check Insights.

The Standards set forth in the Chargeback Guide apply to Transactions conducted within the Program. The Acquirer retains fraud-related chargeback liability with respect to any Maestro e-commerce Transaction completed without Issuer authentication of the Cardholder pursuant to this Program.


# Card-Not-Present Transactions

# 5.7 Use of Automatic Billing Updater

The Acquirer must ensure that e-commerce Transactions submitted by a Merchant participating in the Program are fully compliant with all applicable Transaction data requirements. Failure to comply with such requirements, including but not limited to the provision of valid, accurate and complete Merchant or Sponsored Merchant name, Merchant or Sponsored Merchant ID, and MCC information, will result in the Merchant not being accepted into the Program and its Transactions being blocked from the Program.

# 5.7 Use of Automatic Billing Updater

An Issuer in the Latin America and the Caribbean Region must comply with the ABU requirements set forth in this chapter, with the exceptions stated below. In the Latin America and the Caribbean Region, excluding Puerto Rico and the Virgin Islands, U.S., an Issuer using a third-party service for the purpose of communicating Account change information to Account-on-file and recurring payment Transaction Merchants is not required to participate in ABU, provided that such third-party service supports and is accessible to all Merchants regardless of Merchant location. An Issuer in Puerto Rico or the Virgin Islands, U.S. is not required to participate in ABU with respect to any prepaid Card Programs the Issuer may have. An Acquirer in the Latin America and the Caribbean Region must comply with the ABU requirements set forth in this chapter.

# Middle East/Africa Region

The following modifications to the Rules apply in the Middle East/Africa Region. Refer to Appendix A for the Middle East/Africa Region geographic listing.

# 5.1 Electronic Commerce Transactions

In Bahrain, Egypt, Ghana, Iraq, Kenya, Kuwait, Lebanon, Morocco, Oman, Pakistan, Qatar, Saudi Arabia, South Africa, and the United Arab Emirates and effective 1 January 2024 in Nigeria, the Rule on this subject is modified as follows. An Issuer of Accounts in Bahrain, Egypt, Ghana, Iraq, Kenya, Kuwait, Lebanon, Nigeria, Oman, Pakistan, Qatar, Saudi Arabia and the United Arab Emirates that does not meet the Minimum Average Approval Rate (available on Data Integrity Online) for Cross-border Transactions for a covered consumer product type in such country may be assessed for noncompliance and/or incentivized for improved performance as described in the Data Integrity Monitoring Program manual. In Nigeria, this requirement applies to Domestic Transactions only. An Issuer of Accounts in Morocco that does not meet the Minimum Average Approval Rate (available on Data Integrity Online) for Cross-border Card-not-present Transactions for a covered consumer product type in such country may be assessed for noncompliance and/or incentivized for improved performance as described in the Data Integrity Monitoring Program manual.



228
# Card-Not-Present Transactions

# 5.1.1 Acquirer and Merchant Requirements

In Nigeria, the Rule on this subject is modified as follows. Each Acquirer and each Merchant must request Cardholder authentication using EMV 3DS and comply with the requirements set forth in the Identity Check authentication program.

In Qatar, the Rule on this subject is modified as follows. Each Acquirer and each Merchant must request Cardholder authentication using EMV 3DS and comply with the requirements set forth in the Identity Check authentication program.

# 5.1.2 Issuer Requirements

In Nigeria, the Rule on this subject is modified as follows. An Issuer must support EMV 3DS and respond to a Cardholder authentication request using a solution that is compliant with the Identity Check authentication program requirements.

In Qatar, the Rule on this subject is modified as follows. An Issuer must support EMV 3DS and respond to a Cardholder authentication request using a solution that is compliant with the Identity Check authentication program requirements.

# 5.7 Use of Automatic Billing Updater

Each Issuer and Acquirer in the Middle East/Africa Region must comply with the ABU requirements set forth in this chapter.

# United States Region

The following modifications to the Rules apply in the United States (U.S.) Region. Refer to Appendix A for the U.S. Region geographic listing.

# 5.7 Use of Automatic Billing Updater

An Issuer in the United States Region must comply with the ABU requirements set forth in this chapter. An Issuer is not required to comply with the ABU requirements with respect to prepaid Card programs the Issuer may have.

# 5.10 Mastercard Micropayment Solution

The aggregation of separately authorized Cardholder purchases conducted in a Card-not-present environment into a single aggregated Transaction must only occur pursuant to the Mastercard Micropayment Solution, as set forth in this section. The Mastercard Micropayment Solution provides for the aggregation of multiple individual Cardholder-initiated purchases from a single Merchant into a single Transaction clearing record.



229
# Card-Not-Present Transactions

# Additional U.S. Region and U.S. Territory Rules

Before a Merchant may conduct Card-not-present purchase aggregation Transactions, the Merchant must be registered in the Mastercard Micropayment Solution. To propose a Merchant for registration:

- The Acquirer must submit the completed Mastercard Micropayment Solution registration form to micropayments@mastercard.com;
- The Acquirer must provide all information and material required by Mastercard in connection with the proposed registration; and
- The Acquirer and the Merchant must each satisfy all participation requirements described in the Mastercard Micropayment Solution guidelines.

The Mastercard Micropayment Solution guidelines and registration form are available in the Forms Library on Mastercard Connect®.

Mastercard, in its sole discretion, may approve or reject any application for the registration of a Merchant in the Mastercard Micropayment Solution.

For contactless aggregated transit Transaction requirements, refer to Rule 4.5.

# Additional U.S. Region and U.S. Territory Rules

The following modifications to the Rules apply in the United States Region and in American Samoa, Guam, Northern Mariana Islands, Puerto Rico, and the U.S. Virgin Islands (herein, "the U.S. Territories"). These Rules apply in addition to any that apply within the Asia/Pacific Region, with respect to Customers located in American Samoa, Guam, and Northern Mariana Islands; the Latin America and the Caribbean Region, with respect to Customers located in Puerto Rico and the U.S. Virgin Islands; and the United States Region, with respect to U.S. Region Customers.

# 5.1 Electronic Commerce Transactions

# 5.1.1 Acquirer and Merchant Requirements

In addition, with respect to Maestro e-commerce Transactions: In the U.S. Region and U.S. Territories, the Rule on this subject is modified as follows.

1. The Merchant may support EMV 3D Secure (2.0). When supported, the following requirements apply:
2. 1. For the EMV 3D Secure 2.0 specification, the Merchant must support both browser and in-app Transactions.

The Acquirer must technically support the data fields and values described in the "Electronic Commerce Transactions" section of Appendix C for Non-Mastercard BIN Maestro CNP debit card Transactions occurring at a Merchant that chooses to route to the Single Message System. Each resulting Non-Mastercard BIN Maestro CNP debit card


# Card-Not-Present Transactions

# 5.1.2 Issuer Requirements

Transaction (which can be for any amount) must be properly identified in the Financial Transaction Request/0200 message.

8. The Acquirer may submit a Non-Mastercard BIN Maestro CNP debit card Transaction to the Single Message System as an e-commerce Transaction when the e-commerce Merchant is located in the U.S. Region or a U.S. Territory.

9. The Acquirer retains fraud-related chargeback liability with respect to any Non-Mastercard BIN Maestro CNP debit card Transaction.

The following applies with respect to Non-Mastercard BIN Maestro CNP debit card Transactions routed for processing by means of the Single Message System:

An Issuer must be able to receive and respond to a Financial Transaction Request/0200 message when presented by an Acquirer and initiated at an e-commerce Merchant located in the U.S. Region or a U.S. Territory.
