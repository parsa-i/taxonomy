# Card-Present Transactions

# 4.1 Chip Transactions at Hybrid Terminals

A Customer must comply with the Standards set forth in the M/Chip Requirements for Contact and Contactless manual, as modified from time to time, when deploying Hybrid Terminals and processing Chip Transactions. For information about chip-related incentive interchange rates, see the applicable regional Interchange Manual.

A Chip Transaction must occur at a Hybrid Terminal and be authorized by the Issuer or the chip, resulting in the generation of a unique Transaction Certificate (TC). The Acquirer must send the EMV chip data in DE 55 (Integrated Circuit Card [ICC] System-Related Data) of the Authorization Request/0100 or Financial Transaction Request/0200 message and in DE 55 of the First Presentment/1240 message. A value of 2 or 6 must also be present in position 1 of the three-digit service code in DE 35 (Track 2 Data) of the Authorization Request/0100 or Financial Transaction/0200 message.

As used in this Rule, the following terms have the meanings described:

- “PIN-capable Hybrid POS Terminal” means a Hybrid POS Terminal that is capable at a minimum of performing offline PIN verification when a PIN-preferring Chip Card is presented. It may also be capable of online PIN verification and if attended, must support the signature CVM option (signature collection is not required).
- “PIN-preferring Chip Card” means a Chip Card that has been personalized so that the offline PIN CVM option appears in the Card’s CVM list with a higher priority than the signature option, indicating that PIN CVM is preferred to signature CVM at any POS Terminal that supports PIN.

A chip/PIN Transaction is a Chip Transaction that is processed at a PIN-capable Hybrid POS Terminal with a PIN-preferring Chip Card and completed with offline or online PIN as the CVM. The Cardholder may retain control of the Card while a chip/PIN Transaction is performed.

A non–face-to-face Chip Transaction processed using a Cardholder-controlled remote device is permitted if the Acquirer has received an Application Authentication Cryptogram (AAC) and the Issuer’s approval of the Merchant’s authorization request.

For information about counterfeit and lost/stolen/never-received-issue chip liability shifts, see the Chargeback Guide.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," “Europe Region” and “United States Region” sections at the end of this chapter.

# 4.2 Offline Transactions Performed on Board Planes, Trains, and Ships

A Customer may process a Chip Transaction that takes place at the offline-only Hybrid POS Terminal of a Merchant with no fixed location (for example, aboard a plane, train or ship), if all the following conditions are satisfied:


# Card-Present Transactions

# 4.3 No-CVM Magnetic Stripe and Contact Chip Maestro POS Transactions—Europe Region Only

1. The Hybrid POS Terminal has no online capability and does not perform fallback procedures from chip to magnetic stripe.
2. The Hybrid POS Terminal prompted for PIN as the CVM and the EMV chip provided offline verification of the PIN entered by the Cardholder (or CDCVM was successfully performed on the device).
3. The Hybrid POS Terminal recommended Transaction approval. If the Hybrid POS Terminal recommends against Transaction approval based on its own risk parameters, the Transaction must not proceed.
4. If a Mastercard Card was presented, the Card declined the offline authorization request. The Acquirer processes such declined Transactions at the risk of receiving authorization-related chargebacks. If a Maestro Card was presented, the Merchant processed the Transaction offline as a Merchant-approved Maestro POS Transaction.
5. The Merchant is identified with one of the following MCCs:
1. MCC 4111 (Transportation—Suburban and Local Commuter Passenger, including Ferries)
2. MCC 4112 (Passenger Railways)
3. MCC 4411 (Cruise Lines)
4. MCCs 3000 through 3350 and 4511 (Air Carriers, Airlines)
5. MCC 5811 (Caterers)

NOTE: Duty-free purchases are not covered by this Rule.
6. If applicable, the Acquirer provides in the First Presentment/1240 message:
1. The value of F (Offline Chip) in DE 22 (Point of Service Entry Mode), subfield 7 (Card Data Input Mode).
2. The Application Authentication Cryptogram (AAC) in DE 55.

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.

# 4.3 No-CVM Magnetic Stripe and Contact Chip Maestro POS Transactions—Europe Region Only

NOTE: A Rule on this subject appears in the “Europe Region” section at the end of this chapter.


# 4.4 Contactless Transactions at POS Terminals

When a Contactless Transaction is conducted at a POS Terminal in an amount that does not exceed the applicable Contactless Transaction CVM limit amount, as defined by Merchant location in Appendix E:

- The Transaction must be completed without Cardholder verification (“No CVM” as the CVM); and
- The provision of a Transaction receipt to the Cardholder is at the Merchant’s option. The Merchant must provide a receipt at the Cardholder’s request.

As an exception to the above, a CVM must be obtained for any purchase with cash back or quasi-cash Transaction completed by means of contactless payment functionality.

As an exception to the above, a contactless-only POS Terminal identified as a CAT 1, CAT 2, or CAT 3 device and using MCC 8398 (Organizations, Charitable and Social Service) offering a Transaction equal to or less than USD 15 (or local currency equivalent) may be deployed without the capability to provide a Transaction receipt at the time the Transaction is conducted or at a later date. The inability to provide a receipt must be clearly displayed on the CAT device prior to the Transaction being completed.

There is no maximum Transaction amount for a Contactless Transaction conducted at a POS Terminal.

For CVM requirements, see Rules 3.4, 3.5, and 3.7. For Contactless Transaction identification requirements, see Appendix C.

NOTE: Modifications to this Rule appear in the “Europe Region” and “Latin America and the Caribbean Region” sections at the end of this chapter. Refer to “CVC 3 Verification” in the “Latin America and the Caribbean Region” section for a related Rule.

# 4.5 Contactless Transit Transactions

Mastercard Contactless transit Transactions are permitted only in connection with specific MCCs and can be pre-funded, real-time authorized, or aggregated.

A Merchant offering Mastercard Contactless transit Transactions that utilizes Contactless-only turnstile or at the point of entry acceptance for transportation are not obligated to accept a tap with a non-reloadable prepaid Account provided that other means to make a purchase are located in close proximity to the Contactless-only turnstile or point of entry acceptance device.

# 4.5.1 Mastercard Contactless Transit Aggregated Transactions

A Mastercard Contactless transit aggregated Transaction occurs when the transit Merchant's Acquirer generates a First Presentment/1240 message combining one or more contactless taps performed with one Mastercard Account at one transit Merchant. A "tap" means the Cardholder's tap of the Card or Contactless Payment Device on the contactless reader of the


# Card-Present Transactions

# 4.5.2 Maestro Contactless Transit Aggregated Transactions

POS Terminal with each ride taken. An Acquirer submitting an authorization request to start a
Contactless transit aggregated Transaction, either deferred or in real-time, must confirm the
Issuer’s authorization response was approved, in order to submit the First Presentment/1240
message to clear the aggregated transit fare. As an exception to the foregoing Standard, the
Acquirer may submit a First Presentment/1240 message to claim transit debt, up to a specified
limit in the country for deferred authorizations that were declined and unrecoverable, pursuant
to the transit First Ride Risk (FRR) framework. For more information about transit FRR claim
Transactions, refer to Rule 5.6.1.

In order for the transit Merchant to receive chargeback protection, all of the following must
occur:

1. The Merchant must send a properly identified Authorization Request/0100 message (which
can be for any amount).
2. The Issuer must approve the Transaction.
3. The combined amount of the taps must be equal to or less than the applicable Contactless
transit aggregated CVM limit amount as described in Appendix E.
4. The maximum time period from the first tap until the First Presentment/1240 message is
generated must be 14 calendar days or less.

Upon the Cardholder's request, the Merchant must provide a list of the taps (the date and fare
for each ride taken) that were combined into a First Presentment/1240 message.

Refer to Rule 4.5.1 in the United States Region section at the end of this chapter for the
contactless transit aggregated Transaction procedures applicable to all Transactions occurring
at U.S. Region transit Merchant locations, effective 15 August 2022.

For Mastercard Contactless transit aggregated Transaction identification requirements, see
Appendix C.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region," "Europe Region," and "United
States Region" sections at the end of this chapter.

# 4.5.2 Maestro Contactless Transit Aggregated Transactions

A Maestro Contactless transit aggregated Transaction occurs when the Acquirer generates a
Financial Transaction Request/0200 message for an estimated or maximum amount in
connection with the use of one Maestro Account at one transit Merchant. A Maestro
Contactless transit aggregated Transaction must be processed as follows:

1. The Merchant sends a Financial Transaction Request/0200 message with a value of 06 in
DE 48, subelement 64, subfield 1 (Transit Transaction Type Indicator) for an estimated or
maximum amount not to exceed the applicable Contactless transit aggregated Transaction
CVM limit amount.
2. The Issuer must approve the Transaction.
3. The Cardholder may make subsequent taps for additional rides; these taps will not be sent
to the Issuer for authorization. The combined amount of the taps must be equal to or less
than the applicable Contactless transit aggregated Transaction CVM limit amount as
described in Appendix E.


# Card-Present Transactions

# 4.6 Contactless Transactions at ATM Terminals

4. When the limit is reached or within three calendar days, the Merchant totals the value of all taps and generates an Acquirer Reversal Advice/0420 to reverse any unused funds. The Merchant must inform the Cardholder that the amount held from the available funds in the Account may be greater than the cost of a single fare, and the Merchant must inform the Cardholder of the amount of time that the Merchant requires to reverse all unused funds. This information may be provided on the Merchant’s Website, included in call center scripts, and/or displayed within the transit Merchant's system. The Merchant must also provide specific tap information to the Cardholder upon request. For Maestro Contactless transit aggregated Transaction identification requirements, refer to Appendix C.

NOTE: Variations to this Rule appear in the "Europe Region," "Latin America and the Caribbean Region," and "United States Region" sections at the end of this chapter.

# 4.6 Contactless Transactions at ATM Terminals

A Contactless Transaction conducted at an ATM Terminal must always use online PIN as the CVM. There is no maximum Transaction amount for a Contactless Transaction occurring at an ATM Terminal.

# 4.7 Contactless-only Acceptance

When approved by Mastercard (either on a country-by-country or case-by-case basis), an Acquirer may sponsor Merchants that deploy POS Terminals or MPOS Terminals that utilize only contactless payment functionality. In such event, the Acquirer must ensure that, should any of its Merchants approved by Mastercard to deploy POS Terminals or MPOS Terminals that utilize only contactless payment functionality subsequently deploy POS Terminals or MPOS Terminals with contact payment functionality, such POS Terminals and MPOS Terminals accept and properly process Transactions.

Mastercard has approved the following for contactless-only acceptance:

1. Merchants that deploy unattended POS Terminals that are identified as Cardholder-activated Terminals (CATs), including but not limited to vending machines, parking meters, and fare collection devices.
2. Subject to Corporation approval on a case-by-case basis, Merchants operating mass events, festivals, and sports arenas located in Hungary, Poland, Romania, and the United Kingdom under the following MCCs:
1. MCC 7941—Athletic Fields, Commercial Sports, Professional Sports Clubs, Sports Promoters
2. MCC 7929—Bands, Orchestras, and Miscellaneous Entertainers not elsewhere classified


# 4.8 Mastercard Consumer-Presented QR Transactions at POS Terminals

Card-Present Transactions

# c. MCC 5811—Caterers

# d. MCC 7922—Theatrical Producers (except Motion Pictures), Ticket Agencies

# e. MCC 7999—Recreational Services—not elsewhere classified

1. Merchants located in Hungary, Poland and Romania that use MCC 5994—News Dealers and Newsstands.
2. Merchants located in Hungary that use MCC 5462—Bakeries or MCC 5441—Candy, Nut, Confectionery Stores.
3. Merchants that use MCC 8398—Organizations, Charitable and Social Service.

Unattended POS Terminals that utilize only contactless payment functionality are not required to provide a Transaction receipt at the time the Transaction is conducted; however, the Merchant must have a means by which to provide a receipt to the Cardholder upon request. If such means involves the storage, transmission, or processing of Card data, then it must comply with the Payment Card Industry Data Security Standard (PCI DSS). The manner in which to request a receipt must be clearly displayed at the Merchant location.

As an exception to the above, a contactless-only POS Terminal identified as a CAT 1, CAT 2, or CAT 3 device and using MCC 8398 (Organizations, Charitable and Social Service) offering a Transaction equal to or less than USD 15 (or local currency equivalent) may be deployed without the capability to provide a Transaction receipt at the time the Transaction is conducted or at a later date. The inability to provide a receipt must be clearly displayed on the CAT device prior to the Transaction being completed.

For requirements related to the identification of Contactless-only Transactions occurring at an unattended POS Terminal, see Appendix C. For CAT identification requirements, see Appendix D.

# 4.8 Mastercard Consumer-Presented QR Transactions at POS Terminals

A Mastercard Consumer-Presented QR Transaction is effected through a Cardholder-presented QR Code and by the Merchant capture of the QR Code containing the Transaction Data required to initiate a Transaction. For each Mastercard Consumer-Presented QR Transaction:

- There is no maximum Transaction amount.
- The Transaction must be authorized online by the Issuer.
- The Acquirer must send a properly identified Authorization Request/0100 message or Financial Transaction Request /0200 message.
- The Transaction must be completed with CDCVM. CDCVM is the only valid CVM for Mastercard Consumer-Presented QR Transactions.

For more information about Mastercard Consumer-Presented QR Transactions, refer to the Mastercard Cloud-Based Payments (MCBP) documentation and the M/Chip Requirements for Contact and Contactless manual.


# Card-Present Transactions

# 4.9 Purchase with Cash Back Transactions

Purchase with cash back is an optional service that a Merchant may offer, subject to applicable law or regulation and with the prior approval of its Acquirer, at the Point of Interaction (POI) in a Card-present, face-to-face Transaction environment only. The following requirements apply to purchase with cash back Transactions:

1. A purchase with cash back Transaction is a Transaction arising from the use of a Debit Mastercard (but not any other type of Mastercard) or Maestro Card or Access Device.
2. In a purchase with cash back Transaction, cash may only be provided in combination with a purchase. An Issuer must not approve only the cash back portion of a Transaction containing both a purchase amount and a cash back amount. The cash back service must not be offered in combination with a Manual Cash Disbursement Transaction or the sale of a quasi–cash instrument. Contactless CVM limits do not apply to purchase with cash back Transactions, meaning that such Transactions always require a CVM.
3. In authorization and clearing messages, each purchase with cash back Transaction must contain:
1. The value of 09 (purchase with cash back) in DE 3 (Processing Code), subfield 1 (Cardholder Transaction Type).
2. The total Transaction amount (inclusive of the purchase and cash back amounts) in DE 4 (Amount, Transaction).
3. The cash back amount in DE 54 (Amounts, Additional). The purchase amount, cash back amount, and total Transaction amount must all be in the same currency.

The following requirements apply to Acquirers and Merchants:

1. An education program must be established for the staff of any Merchant that chooses to offer purchase with cash back Transactions, including but not limited to POS Terminal operators.
2. An offer of purchase with cash back that is promoted at the POI must be available to all Cardholders of each Card type for which the service is supported. The Merchant may prompt the Cardholder to use this service.
3. Acquirers or Merchants may establish a minimum and/or maximum cash back amount for the purchase with cash back Transaction, provided that:
1. Any minimum or maximum amount is applied uniformly to all Cardholders.
2. Any minimum amount is not greater than the minimum amount established for any other payment means accepted at the Merchant location.
3. Any maximum amount is not less than the maximum amounts established for any other payment means at the Merchant location.
4. For Debit Mastercard purchase with cash back Transactions, a maximum cash back amount must be established that does not exceed USD 100 or the local currency equivalent, or as applicable in the Merchant's country.
5. For Maestro signature-verified and cross-border purchase with cash back Transactions, a maximum cash back amount must be established that does not exceed USD 100 or


# Card-Present Transactions

# 4.10 Transactions at Unattended POS Terminals

The local currency equivalent. Maestro signature-verified purchase with cash back Transactions may be conducted in signature waiver countries only.

4. The Acquirer must obtain online authorization approval for the full Transaction amount; support for authorization of the purchase amount only is optional.

The following requirements apply to Issuers:

1. An Issuer must properly personalize each Debit Mastercard and Maestro Card and Access Device (including prepaid issuance) to support the purchase with cash back Transaction type. Support is required for both Domestic and Cross-border Transactions, and on both the contact and contactless interfaces of a Dual Interface Card.
2. The Issuer's authorization host must support the purchase with cash back Transaction data fields and values.
3. The Issuer must make an individual authorization decision for each purchase with cash back Transaction. An Issuer that chooses not to offer the cash back service to particular Cardholders must be capable of providing a value of 87 (Purchase Amount Only, No Cash Back Allowed) in DE 39 (Response Code) of the authorization request response message for an Account in good standing and having a sufficient balance, if the POS Terminal indicates support for purchase-amount-only approvals.

NOTE: Variations to this Rule appear in the "Asia/Pacific Region," "Canada Region," "Europe Region," "Latin America and the Caribbean Region," "Middle East/Africa Region," and "United States Region" sections at the end of this chapter.

# 4.10 Transactions at Unattended POS Terminals

A POS Transaction occurring at an unattended POS Terminal is a non-face-to-face Transaction, since no Merchant representative is present at the time of the Transaction. Examples of unattended POS Terminals include ticket dispensing machines, vending machines, automated fuel dispensers, toll booths, and parking meters.

A Mastercard POS Transaction that occurs at an unattended POS Terminal must be identified as a Cardholder-Activated Terminal (CAT) Transaction, as described in Appendix D.

Transaction messages used at unattended POS Terminals must communicate to the Cardholder, at a minimum, the following:

- Invalid Transaction
- Unable to Route
- Invalid PIN—re-enter (if PIN entry is supported)
- Capture Card (if Card retention is supported)

NOTE: Modifications to this Rule appear in the “Europe Region” section at the end of this chapter.


# Card-Present Transactions

# 4.10.1 Automated Fuel Dispenser Transactions

An automated fuel dispenser Transaction is identified with MCC 5542 (Automated Fuel Dispenser) and a CAT level indicator of CAT 1 or CAT 2 (for Card-present Transactions), CAT 6 (for e-commerce Transactions), or CAT 7 (for transponder Transactions), as described in Appendix D.

NOTE: Modifications to this Rule appear in the "Asia/Pacific Region" (pertaining to Malaysia), "Europe Region," and "United States Region" sections at the end of this chapter.

# Authorization Before Fueling

Each automated fuel dispenser Transaction for which authorization is requested prior to the dispensing of fuel is properly processed as follows:

1. The Acquirer’s initial authorization request (0100 or 0200) message (dual message Authorization Request/0100 or single message Financial Transaction Request/0200) to the Issuer must be identified as a preauthorization and reflect one of the following:
1. A maximum fuel dispense amount as determined by the Merchant or Acquirer;
2. A specific amount selected by the Cardholder; or
3. In the U.S. Region only, the amount of USD 1.
2. If the preauthorization request contains the partial approval support indicator, and the Issuer provides a partial approval response, then the final Transaction amount must not exceed the partial approval amount provided in DE 6 (Amount, Cardholder Billing), unless the preauthorization request amount was USD 1.
3. After the fuel is dispensed, the Acquirer must send an advice message (dual message Authorization Advice/0120 or single message Acquirer Reversal Advice/0420) containing the final Transaction amount (in DE 4 [Amount, Transaction] of the 0120 message or in DE 95 [Replacement Amounts] of the 0420 message) to the Issuer. The advice message must be sent no later than 60 minutes (in the Europe Region, 20 minutes) after the original preauthorization request.
4. If fuel is not dispensed or the Cardholder otherwise cancels the Transaction then within 60 minutes of authorization approval (in the Europe Region, 20 minutes), the Acquirer must send either an advice message (Authorization Advice/0120 with a value of zero in DE 4 or Acquirer Reversal Advice/0420 with a value of zero in DE 95) or a full reversal (dual message Reversal Request/0400 with a value of zero in DE 95).
5. Within 60 minutes of receiving the advice message, the Issuer must release any hold that the Issuer placed on the Cardholder's available funds or credit in excess of the Transaction amount specified in DE 4 (Amount, Transaction). If the Issuer displays pending automated fuel dispenser Transaction information in Cardholder-facing applications, the information must be based on the advice message Transaction amount.
6. The Acquirer must send a First Presentment/1240 or Financial Transaction Advice/0220 message with the final Transaction amount in DE 4 (Amount, Transaction).

As a best practice, the Merchant should inform the Cardholder in advance of any estimated amount for which authorization will be requested (for example, on a screen display or sticker at).


# 4.10.2 Electric Vehicle Charging Transactions

The Terminal and obtain the Cardholder’s consent to the amount before initiating the authorization request.

NOTE: A modification to the foregoing paragraph applies in the EEA and appears in the "Europe Region" section at the end of this chapter.

# Authorization After Fueling

A Merchant that instead chooses to initiate the Transaction authorization request after the fuel is dispensed does so at the risk of a possible decline or partial approval. Such authorizations are properly identified as final authorizations. Refer to the Authorization Manual or Customer Interface Specification for more information about advice message requirements for automated fuel dispenser Transactions.

# 4.10.2 Electric Vehicle Charging Transactions

A Transaction occurring at an unattended POS Terminal for the purchase of electric vehicle charging services is identified with MCC 5552 (Electric Vehicle Charging) and a CAT level indicator of CAT 1 or CAT 2 (for Card-present Transactions) or CAT 6 (for e-commerce Transactions) as described in Appendix D. Alternatively, if the primary business of the Merchant is temporary parking services, then MCC 7523 (Automobile Parking Lots and Garages) may be used.

Contactless-only acceptance is permitted (refer to Rules 4.7 and 7.3.2). A contactless-only Terminal supporting a maximum vehicle charging amount that does not exceed the applicable contactless CVM limit is properly identified as CAT 2. The Transaction may be authorized either prior to or after the vehicle charging, as follows.

# Authorization Before Charging

Each electric vehicle charging Transaction for which authorization is requested before vehicle charging begins is properly processed as follows:

1. The Merchant must inform the Cardholder of any estimated amount for which authorization will be requested (for example, on a screen display or sticker at the Terminal) and must obtain the Cardholder’s consent to the amount before initiating the authorization request. The estimated amount may be the Terminal’s maximum dispense amount or a specific amount requested by the Cardholder.
2. The Acquirer’s initial authorization request (0100 or 0200) message to the Issuer must be identified as a preauthorization. If the preauthorization request contains the partial approval support indicator, and the Issuer provides a partial approval response, then the final Transaction amount must not exceed the partial approval amount provided in DE 6 (Amount, Cardholder Billing).
3. If the Transaction is finalized for an amount that:
1. Exceeds the authorized amount, then the Acquirer must send an additional (incremental) authorization request for the unauthorized amount (refer to section 2.9);


# Card-Present Transactions

# 4.11 PIN-based Debit Transactions—United States Region Only

b. Is less than the authorized amount, then within 24 hours of finalization, the Acquirer must either send a partial reversal for the excess authorized amount, or submit the Transaction clearing record.

4. In the case of a Transaction cancelled by the Cardholder, then within 24 hours, the Acquirer must send a full reversal request.

# Authorization After Charging

If the Merchant initiates authorization after the vehicle charging is completed, then the Acquirer’s authorization request must be identified as a final authorization.

# 4.11 PIN-based Debit Transactions—United States Region Only

NOTE: A Rule on this subject appears in the “United States Region” section at the end of this chapter.

# 4.12 PIN-less Single Message Transactions—United States Region Only

NOTE: A Rule on this subject appears in the “United States Region” section at the end of this chapter.

# 4.13 Merchant-approved Maestro POS Transactions

This Rule applies to all Merchant-approved Maestro POS Transactions whether processed via the Mastercard® Single Message System or the Mastercard® Dual Message System. Refer to Chapter 3 of the M/Chip Requirements for Contact and Contactless for more detailed information on processing Merchant-approved Maestro POS Transactions that are Chip Transactions.

An Acquirer may elect to accept Merchant-approved Maestro POS Transactions from a Merchant that accepts Maestro Cards. A Merchant-approved Maestro POS Transaction may occur only when the POS Terminal cannot receive an online authorization for a Transaction because of technical difficulties between the Acquirer and the Interchange System or the Interchange System and the Issuer, or other temporary technical problems. Each Acquirer must forward all stored Transactions by means of electronic store-and-forward as soon as the technical problem has been resolved.

The Issuer must treat all Merchant-approved Maestro POS Transactions received by means of the Mastercard® Single Message System as financial request messages. If the Issuer is unavailable to authorize or decline a Merchant-approved Maestro POS Transaction at the time of presentment, the Interchange System indicates this, and returns the Transaction to the Acquirer. These returned Transactions may be submitted by the Acquirer to the Interchange System every 30 minutes, until a response is received from, or on behalf of the Issuer.


Transaction Processing Rules • 11 June 2024 139
# Card-Present Transactions

# 4.14 Mastercard Manual Cash Disbursement Transactions

Merchant-approved Maestro POS Transactions settle only upon authorization by the Issuer. The Acquirer bears all responsibility for a Merchant-approved Maestro POS Transaction that is declined by the Issuer.

If a Merchant-approved POS Transaction is declined by the Issuer for insufficient funds, or because the Transaction exceeds withdrawal limits, the Acquirer may resubmit the Transaction once every 24 hours for a period ending 13 calendar days after the Transaction date. If the Issuer accepts the Transaction on submission or resubmission, the Issuer’s liability is the same as for an online Transaction.

An Issuer is not required to assist an Acquirer in any attempt to collect on a systemically rejected Merchant-approved POS Transaction. The Issuer must make reasonable efforts to collect the Transaction amount, but in doing so, assumes no liability.

NOTE: A variation to this rule appears in the “Europe Region” section at the end of this chapter.

# 4.14 Mastercard Manual Cash Disbursement Transactions

A cash disbursement may be provided to a Mastercard Cardholder by a Customer at its offices and through its authorized agents. For purposes of this Rule, an authorized agent is a financial institution authorized to provide cash disbursement services on behalf of a Customer pursuant to written agreement with the Customer.

The Customer and each of its authorized cash disbursement agents must comply with the requirements set forth in “Mastercard Manual Cash Disbursement Acceptance Procedures” in Chapter 3.

A cash disbursement to a Maestro or Cirrus Cardholder is performed at a Bank Branch Terminal. Refer to Chapter 7 for Bank Branch Terminal requirements.

NOTE: An addition to this Rule appears in the “United States Region” section at the end of this chapter.

# 4.14.1 Non-discrimination Regarding Cash Disbursement Services

Each Customer and each of its authorized cash disbursement agents must comply with the following requirements at each office at which any cash disbursement services are afforded:

1. Not discriminate against or discourage the use of Cards in favor of any card or device bearing or otherwise issued or used in connection with another acceptance brand; and
2. Provide cash disbursement services to all Cardholders on the same terms and regardless of the Issuer.

# 4.14.2 Maximum Cash Disbursement Amounts

A Customer and each of its authorized cash disbursement agents may limit the amount of cash provided to any one Cardholder in one day at any individual office. Such limit may not be less than USD 5,000 per Cardholder in one day and uniformly must be applied to all Cardholders.



140
# Card-Present Transactions

# 4.14.3 Discount or Service Charges

If compliance with this Rule would cause hardship to one or more (but not all) of such individual offices that are required or permitted to provide cash disbursement services, the Customer may establish a maximum cash disbursement amount of less than USD 5,000 per person in one day at each such office, provided that the maximum cash disbursement amount:

1. Is not less than USD 1,000;
2. Is not less than the maximum cash disbursement amount established for any other acceptance brand at the office; and
3. Applies only at those offices where the Customer can, if requested by Mastercard, demonstrate that a higher maximum would create a hardship.

NOTE: Variations to this Rule appear in the “Europe Region” and “United States Region” sections at the end of this chapter.

# 4.14.3 Discount or Service Charges

The Customer and each of its authorized cash disbursement agents must disburse all cash disbursements at par without any discount and without any service or other charge to the Cardholder, except as may be imposed to comply with applicable law. Any charge imposed to comply with applicable law must be charged to and paid by the Cardholder separately and must not be included in the total amount of the cash disbursement.

NOTE: A modification to this Rule appears in the “United States Region” section at the end of this chapter.

# 4.14.4 Mastercard Acceptance Mark Must Be Displayed

A Customer and each of its authorized cash disbursement agents must display the Mastercard Acceptance Mark as required by the Standards at each location where the Customer or any such agent provides cash disbursements to Mastercard Cardholders.

# 4.15 Encashment of Mastercard Travelers Cheques

Each Mastercard Customer must encash Mastercard® Travelers Cheques issued in any currency when presented for payment at any of its locations, provided:

1. Such encashment is permitted by law; and
2. The Customer has the ability (including a foreign exchange capability, with respect to a currency other than U.S. currency Mastercard Travelers Cheques presented for encashment) to encash such cheques as a result of the business it normally conducts at a location. If the encashing Customer encashes any other brand of travelers cheques at a location, the Customer may impose terms and conditions for the encashment of Mastercard Travelers Cheques that it uses to encash other brands of travelers cheques.



141
# Card-Present Transactions

# 4.16 ATM Transactions

The following Rules relate to ATM Transaction processing.

# 4.16.1 “Chained” Transactions

An Acquirer that deploys ATM Terminals that do not retain the Card internally until all Transactions requested by the Cardholder are completed must require the Cardholder to re-enter the PIN for every additional financial Transaction performed. This requirement applies to card swipe readers, card dip readers, and similar devices where a card is not held within the device, and is removed prior to Transaction completion.

# 4.16.2 ATM Transaction Branding

If a Customer that does not have a Mastercard License acquires an ATM transaction initiated by a Mastercard Card that does not display the Maestro and/or Cirrus Marks and sends it through the Mastercard® ATM Network, that transaction is deemed to be an ATM Transaction and all Rules regarding ATM Transactions will apply.

# 4.17 ATM Access Fees

An ATM Access Fee may be charged by an Acquirer only in connection with a cash withdrawal Transaction or a Shared Deposit Transaction that is initiated at the Acquirer’s ATM Terminal with a Card. The ATM Access Fee is added to the amount of the Transaction transmitted to the Issuer. For purposes of this Rule, a Transaction is any Transaction routed through the Mastercard® ATM Network. Nothing contained in this Rule affects the right of an Issuer to determine what fees, if any, to charge its Cardholders.

# 4.17.1 ATM Access Fees - Domestic Transactions

A Cardholder may not be assessed or be required to pay an ATM Access Fee or other fee types imposed, or advised of, at an ATM, in connection with a Domestic Transaction.

NOTE: Variations to this Rule appear in the "Asia/Pacific Region" (pertaining to Australia), "Canada Region," "Europe Region," "Latin America and the Caribbean Region," and "United States Region" sections at the end of this chapter.



142
# Card-Present Transactions

# 4.17.2 ATM Access Fees - Cross-border Transactions

Unless prohibited by local law or regulations, an Acquirer, upon complying with the ATM Access Fee notification requirements, may assess an ATM Access Fee on a Cross-border Transaction, so long as the Acquirer applies the ATM Access Fee in a consistent and nondiscriminatory manner.

# 4.17.3 ATM Access Fee Requirements

An Acquirer that applies or plans to apply an ATM Access Fee to Domestic Transactions, Cross-border Transactions, or both must comply with all of the following requirements.

# Transaction Field Specifications for ATM Access Fees

At the time of each Transaction on which an ATM Access Fee is imposed, the Acquirer of such Transaction must transmit, in the field specified by the applicable technical specifications manual then in effect, the amount of the ATM Access Fee separately from the amount of the cash disbursed in connection with such Transaction.

# Non-discrimination Regarding ATM Access Fees

An Acquirer must not charge an ATM Access Fee in connection with a Transaction that is greater than the amount of any ATM Access Fee charged by that Acquirer in connection with the transactions of any other network accepted at that ATM Terminal.

# Notification of ATM Access Fee

An Acquirer that wishes to charge an ATM Access Fee must notify its Sponsoring Principal, in writing, of its intent to do so prior to the planned first imposition of such ATM Access Fee by the Acquirer. The Principal must update the Location Administration Tool (LAT) regarding its or its Affiliates’ imposition of ATM Access Fees.

# Cancellation of Transaction

Any Acquirer that plans to charge an ATM Access Fee must notify the Cardholder with a screen display that states the ATM Access Fee policy and provides the Cardholder with an option to cancel the requested Transaction.

# Sponsor Approval of Proposed Signage, Screen Display, and Receipt

An Affiliate that plans to charge an ATM Access Fee to a Transaction must submit proposed ATM Terminal signage, screen display, and receipt “copy” that meets the requirements of the Rules to its Sponsor in writing for approval prior to use, unless such Acquirer employs the model form provided in Appendix F. The Sponsor has the right to determine the acceptability of any new or changes to previously approved signage, screen display, and receipt copy. In cases of conflict between the Acquirer and its Sponsor, Mastercard has the sole right to determine the acceptability of any and all signage, screen display, and receipt copy.



143
# Card-Present Transactions

# ATM Terminal Signage

An Acquirer that plans to charge an ATM Access Fee may optionally display signage that is clearly visible to Cardholders on or near all Terminals at which ATM Access Fees apply. The minimum requirement for ATM Access Fee signage text is wording that clearly states:

1. The identity of the ATM owner and of the Principal;
2. That the Transaction will be subject to an ATM Access Fee that will be deducted from the Cardholder's Account in addition to any Issuer fees;
3. The amount of, calculation method of, or Corporation-approved generic signage regarding the ATM Access Fee;
4. That the ATM Access Fee is assessed by the Acquirer instead of the Issuer;
5. That the ATM Access Fee is assessed on Cross-border Transactions only or Domestic Transactions only, if applicable.

The minimum requirements for ATM Terminal signage (physical characteristics) are as follows:

1. The signage must bear the heading "Fee Notice";
2. The size of the signage must be a minimum of four inches in height by four inches in width;
3. The text must be clearly visible to all; a minimum of 14-point type is recommended;
4. The heading must be clearly visible to all; a minimum of 18-point type is recommended.

Refer to Appendix F for a model of ATM Terminal signage relating to ATM Access Fee application.

# ATM Terminal Screen Display

An Acquirer that plans to charge an ATM Access Fee must present a screen display message that is clearly visible to Cardholders on all ATM Terminals at which ATM Access Fees apply. If the Cardholder is given the option of choosing a preferred language in which to conduct the Transaction, the screen display message concerning ATM Access Fees must be presented to the Cardholder in that chosen language.

If an Acquirer displays the Mastercard-approved generic ATM Access Fee signage, the Acquirer must include the amount or calculation method of the ATM Access Fee as part of the ATM Terminal screen display.

Refer to Appendix F for a model of an ATM Terminal screen display relating to ATM Access Fee application.

# ATM Transaction Receipts

Any Acquirer that charges an ATM Access Fee must make available to the Cardholder on the Transaction receipt the ATM Access Fee information required by this Rule, in addition to any other information the Acquirer elects to or is required to provide.

The minimum requirements for the Transaction receipt are:

1. A statement of the amount disbursed to the Cardholder;


# Card-Present Transactions

# 4.18 Merchandise Transactions at ATM Terminals

2. A statement of the ATM Access Fee amount with language clearly indicating it is a fee imposed by the Acquirer;

3. A separate statement of the combined amount of the ATM Access Fee and the disbursed amount, with language clearly indicating that this amount will be deducted from the Cardholder’s Account.

Refer to Appendix F for a model of ATM Transaction receipt text relating to ATM Access Fee application.

# 4.18 Merchandise Transactions at ATM Terminals

An ATM Terminal may dispense any merchandise, service, or other thing of value within a Mastercard-approved merchandise category, other than any merchandise, service, or other thing of value which:

1. Is illegal or would tend to offend the public morality or sensibility, disparage Mastercard, or otherwise compromise the good will or name of Mastercard;
2. Mastercard has notified Acquirers must not be dispensed by an ATM Terminal; or
3. Could be used to obtain products or services at a location other than an ATM Terminal which, if dispensed at an ATM Terminal, would be prohibited pursuant to this Rule.

Promptly upon written direction from Mastercard, an Acquirer must cease dispensing at all its ATM Terminals any merchandise, service, or other thing of value which Mastercard has directed is not permitted.

# 4.18.1 Approved Merchandise Categories

|Merchandise Category|Explanation|
|---|---|
|Event Tickets|Admission tickets to scheduled events that upon presentation of such tickets will admit the bearer to such scheduled events in lieu of other forms of admission tickets.|
|Transportation Tickets and Passes|Tickets or passes to board and ride scheduled transportation conveyances in lieu of other forms of transportation tickets.|
|Telecommunications Cards and Services|Prepaid telephone cards that entitle the holder to a specified amount of prepaid time or prepaid wireless telephone time that is credited to a subscriber’s prepaid telephone account.|


# Card-Present Transactions

# 4.18.2 Screen Display Requirement for Merchandise Categories

|Merchandise Category|Explanation|
|---|---|
|Retail Mall Gift Certificates|Gift certificates to be sold at ATM Terminals located in retail shopping malls and redeemable for merchandise at stores located in the mall where dispensed. Customers must receive prior written approval from the Corporation for each specific mall implementation.|
|Charitable Donation Vouchers|Pre-valued donation vouchers that are dispensed as receipts for donations resulting from an authorized Transaction at a participating ATM. Customers must receive prior written approval from the Corporation for each specific charitable entity.|

NOTE: An addition to this Rule appears in the “Europe Region” and the “United States Region” sections at the end of this chapter.

# 4.18.2 Screen Display Requirement for Merchandise Categories

The Acquirer must disclose to the Cardholder via the video monitor screen prior to the initiation of any Merchandise Transaction the following:

1. Full identification of the price and quantity of the Merchandise;
2. Any additional shipping or handling charges (for mailed purchases only);
3. Policy on refunds or returns; and
4. Provision for recourse concerning Cardholder complaints or questions.

# 4.19 Shared Deposits—United States Region Only

NOTE: Rules on this subject appear in the “United States Region” section at the end of this chapter.


# Card-Present Transactions

# Variations and Additions by Region

The remainder of this chapter provides modifications to the Standards set out in this chapter. The modifications are organized by region or country and by applicable subject title.

# Asia/Pacific Region

The following modifications to the Rules apply in the Asia/Pacific Region or in a particular Region country or countries. Refer to Appendix A for the Asia/Pacific Region geographic listing.

# 4.1 Chip Transactions at Hybrid Terminals

For China Domestic Transactions, the Rule on this subject is modified as follows. A Chip Transaction must occur at a Hybrid Terminal and be authorized by the Issuer or the chip, resulting in the generation of a unique Transaction Certificate (TC). The Acquirer must send the PBoC chip data for each Chip Transaction in DE 55 (Integrated Circuit Card [ICC] System-Related Data) of the Preauthorization Request/0100 or Financial Transaction Request/0200 message. For each Chip Transaction, a value of 2 or 6 must also be present in position 1 of the three-digit service code in DE 35 (Track 2 Data) of the Preauthorization Request/0100 or Financial Transaction Request/0200 message.

# 4.5 Contactless Transit Transactions

# 4.5.1 Mastercard Contactless Transit Aggregated Transactions

Effective 3 April 2024 for India Domestic Transactions, the Rule on this subject is modified as follows. In order for the transit Merchant to receive chargeback protection, all of the following must occur:

1. The Merchant must send a properly identified Authorization Request/0100 message (which can be for any amount).
2. The Issuer must approve the Transaction.
3. The combined amount of the taps must be equal to or less than the applicable Contactless transit aggregated CVM limit amount as described in Appendix E.
4. The maximum time period from the first tap until the First Presentment/1240 message is generated must be four calendar days or less.

# 4.9 Purchase with Cash Back Transactions

In the Asia/Pacific Region, the Rule on this subject is modified as follows: Asia/Pacific Region Issuers are not required to support the purchase with cash back Transaction type.


# Card-Present Transactions

# 4.10 Transactions at Unattended POS Terminals

In Australia, the Rule on this subject is modified as follows: For a Debit Mastercard purchase with cash back Transaction, a maximum cash back amount must be established that does not exceed AUD 500.

In India, the Rule on this subject is modified as follows: A Merchant located in India that has received prior approval from its Acquirer may offer a purchase with cash back Transaction with or without an accompanying purchase to a Cardholder presenting a Debit Mastercard or Maestro Card issued in India. The maximum daily cash back amount per Card must be in accordance with applicable law including circulars published by the Reserve Bank of India.

# 4.10 Transactions at Unattended POS Terminals

# 4.10.1 Automated Fuel Dispenser Transactions

In Malaysia, the following Rule applies: A Malaysia Acquirer must present Mastercard automated fuel dispenser Transactions (MCC 5542) to Malaysia Issuers within two business days of the Transaction date. Within one business day of the presentment date of an automated fuel dispenser Transaction (MCC 5542), a Malaysia Issuer must post the Transaction to the Cardholder’s Account and release any hold amount exceeding the Transaction amount from the Cardholder’s Account.

# 4.17 ATM Access Fees

# 4.17.1 ATM Access Fees—Domestic Transactions

The Rule on this subject, as it applies to Domestic Transactions occurring in Australia, is replaced with the following: Subject to complying with the ATM Access Fee notification requirements, an Acquirer in Australia may assess an ATM Access Fee on a Debit Mastercard, Maestro, or Cirrus Transaction initiated with a Card that was issued in Australia provided the Acquirer applies the ATM Access Fee in a consistent and nondiscriminatory manner. For the purpose of this Rule, “ATM Access Fee” means a fee charged by an Acquirer in Australia in connection with a financial or non-financial transaction initiated at that Acquirer’s ATM Terminal with a Card issued in Australia, which fee is added to the amount of the Transaction transmitted to the Issuer.



148
# Card-Present Transactions

# Canada Region

Canada Region

The following modifications to the Rules apply in the Canada Region. Refer to Appendix A for the Canada Region geographic listing.

# 4.9 Purchase with Cash Back Transactions

In the Canada Region, the Rule on this subject is modified as follows. An Issuer must technically support and properly personalize each Debit Mastercard and prepaid Mastercard Card and Access Device to support the purchase with cash back Transaction type. Support is required for both Domestic and Cross-border Transactions, and on both the contact and contactless interfaces of a Dual Interface Card. An Acquirer must technically support the purchase with cash back Transaction for Debit Mastercard and prepaid Mastercard Cards. A Merchant located in the Canada Region may, at its option, support purchase with cash back Transactions as set forth in this chapter, with the following variations:

1. The Merchant may offer purchase with cash back to Debit Mastercard and prepaid Mastercard Cardholders.
2. Purchase with cash back is available only for chip/PIN Transactions.
3. The maximum cash back amount of the purchase with cash back Transaction is CAD 100. Acquirers or Merchants may establish a lower maximum cash back amount, provided that:
1. Any such maximum amount is applied uniformly; and
2. Any maximum amount is not lower than the maximum amount established for any other payment means on which purchase with cash back is offered at the Merchant location.

# 4.10 Transactions at Unattended POS Terminals

# 4.10.1 Automated Fuel Dispenser Transactions

In the Canada Region, if an Issuer approves an online authorization request for an automated fuel dispenser (MCC 5542) Transaction, then within 60 minutes of the time that the authorization request message is sent, the Acquirer must send an authorization advice message advising the Issuer of the Transaction amount. If, after approving the authorization request, the Issuer places a hold on Cardholder funds in excess of CAD 1, then, within 60 minutes of receiving the Acquirer’s authorization advice message, the Issuer must release any hold amount that exceeds the Transaction amount.

# 4.17 ATM Access Fees

# 4.17.1 ATM Access Fees—Domestic Transactions

In the Canada Region, the Rule on this subject is replaced with the following:


# Card-Present Transactions

# Europe Region

Subject to complying with the ATM Access Fee notification requirements of the Rules, an Acquirer in the Canada Region may assess an ATM Access Fee on a Transaction initiated with a Card that was issued in the Canada Region provided the Acquirer applies the ATM Access Fee in a consistent and nondiscriminatory manner.

# Europe Region

The following modifications to the Rules apply in the Europe Region or in a particular Region country or countries. Refer to Appendix A for the Europe Region, Non-Single European Payments Area (Non-SEPA) and Single European Payments Area (SEPA) geographic listing.

# 4.1 Chip Transactions at Hybrid Terminals

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. EMV chip data must be provided in the field specified by the registered switch of the Customer's choice for authorization and clearing messages.

# 4.2 Offline Transactions Performed on Board Planes, Trains, and Ships

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. Decline of the authorization by the EMV chip must be indicated in the field and with the value specified by the registered switch of the Customer's choice.

# 4.3 No-CVM Magnetic Stripe and Contact Chip Maestro POS Transactions

In the Europe Region, magnetic stripe and Contact Chip Maestro POS Transactions may be completed without CVM in the acceptance environments listed in this Rule, up to the maximum Transaction amount set out below.

|Acceptance Environment|Maximum Transaction Amount|
|---|---|
|Tollways (MCC 4784)|EUR 100 (or local currency equivalent)|
|Parking Lots and Garages (MCC 7523)|EUR 50 (or local currency equivalent)|
|Transit Vending Machines (MCCs 4111, 4112 and 4131)|EUR 25 (or local currency equivalent)|

Maestro Contactless Transactions may also be completed in these environments in accordance with the Standards applicable to Maestro Contactless Transactions. The following Rules apply to Magnetic Stripe and Contact Chip Maestro POS Transactions:

1. The Merchant must obtain authorization online from the Issuer or offline from the chip. Magnetic stripe Transactions may also be authorized according to the Merchant-approved Transaction Rules, at POS Terminals that are not located in the EEA, UK or Gibraltar. At POS


# 4.4 Contactless Transactions at POS Terminals

1. Terminals located in the EEA, UK and Gibraltar, magnetic stripe Transactions must not be completed.
2. The Acquirer bears the liability for fraud on magnetic stripe and Contact Chip Maestro POS Transactions completed without CVM.
3. The Transactions must be identified with one of the above-listed MCCs.
4. Transactions at vending machines and transit vending machines must be identified as unattended Transactions.
5. A POS Terminal at which no-CVM Maestro POS Transactions are performed may have a PIN pad.
6. An Issuer of Chip Cards must be able to authorize no-CVM Maestro POS Transactions even when the chip data in the authorization message indicates “Cardholder verification was not successful.”
7. In the tollways environment, the Merchant may at its option maintain a negative file in the POS Terminal, provided this is done in a PCI-compliant manner.
8. An Issuer in the Netherlands is not required to technically support no-CVM Maestro POS Transactions at transit vending machines. Transit vending machines that support no-CVM Maestro POS Transactions must not be deployed in the Netherlands.

In the Europe Region, the Rule on this subject is modified as follows. Merchants that operate tollways (MCC 4784) and parking lots and garages (MCC 7523) may configure their POS Terminals to perform Maestro Contactless Transactions that exceed the applicable CVM limit without a CVM. An Issuer must not systematically decline such Maestro Contactless Transactions when completed without a CVM. The Acquirer is liable for a fraudulent Maestro Contactless Transaction that exceeds the CVM Limit and is completed without a CVM.

If a Maestro Card that also bears a domestic debit brand mark is used in a Contactless Transaction and the domestic debit brand does not support contactless payment functionality, the Transaction must be identified in all Transaction messages as a Maestro Contactless Transaction and all Rules regarding such Transactions apply to the Transaction. If processed by means of the Interchange System, the Maestro Contactless Transaction is identified by the following values, which indicate that an EMV Mode Contactless Transaction has occurred:

1. In authorization:
1. DE 22 (POS entry mode), subfield 1 (POS Terminal PAN Entry Mode) must contain the value of 7, and
2. DE 61 (POS Data), subfield 11 (POS Card Data Terminal Input Capability) must contain the value of 3.
2. In clearing:
1. DE 22 (POS entry mode), subfield 1 (Terminal Data: Card Data Input Capability) must contain the value of M, and


# Card-Present Transactions

# 4.5 Contactless Transit Aggregated Transactions

b. DE 22 (POS data), subfield 7 (Card Data: Input Mode) must contain the value of M. If the Transaction is processed via a means other than the Interchange System (including bilateral and on-us processing), the Acquirer must ensure that corresponding data elements contain values that enable Issuers to clearly identify the transaction as a Maestro Contactless Transaction.

# 4.5 Contactless Transit Aggregated Transactions

# 4.5.1 Mastercard Contactless Transit Aggregated Transactions

In the EEA, UK or Gibraltar, the Rule on this subject is modified as follows. A clearing message must be identified as specified by the registered switch of the Customer's choice.

# 4.5.2 Maestro Contactless Transit Aggregated Transactions

In the Europe Region, the Rule on this subject is replaced with the following. A Maestro Contactless transit aggregated Transaction occurs when the Acquirer generates an Authorization Request/0100 message for an estimated amount in connection with the use of one Maestro Account at one transit Merchant. Maestro Contactless transit aggregated Transactions must be processed as follows.

1. The Merchant sends an Authorization Request/0100 message with a value of 06 in DE 48, subelement 64, subfield 1 (Transit Transaction Type Indicator) for an estimated amount not to exceed the applicable Contactless transit Transaction CVM limit amount.
2. The Merchant must obtain Issuer approval of the Transaction.
3. The Cardholder may make subsequent taps for additional rides; these taps will not be sent to the Issuer for authorization. The combined amount of the taps must be equal to or less than the Contactless transit aggregated Transaction CVM limit amount as described in Appendix E.
4. When the limit is reached or within three calendar days, the Merchant totals the value of all taps and generates a Reversal Request/0400 or Authorization Advice/0120 message to reverse any unused funds.

The Merchant must inform the Cardholder that the amount held from the available funds in the Account may be greater than the cost of a single fare, and the Merchant must inform the Cardholder of the amount of time that the Merchant takes to reverse all unused funds. This information may be provided on the Merchant's Website, included in call center scripts, and/or displayed within the transit Merchant's system. The Merchant must also provide specific tap information to the Cardholder upon request.

For Contactless transit aggregated Transaction identification requirements, refer to Appendix C. In the EEA, UK or Gibraltar, the Rule on this subject is modified as follows. Maestro Contactless transit aggregated Transactions must be identified as specified by the registered switch of the Customer's choice.


# Card-Present Transactions

# 4.9 Purchase with Cash Back Transactions

Authorization, reversal and advice messages must be identified as specified by the registered switch of the Customer's choice.

# 4.9 Purchase with Cash Back Transactions

In the Europe Region, the following additional Rules apply to all types of Mastercard and Maestro Transactions, unless otherwise specified.

# Acquirer and Merchant Requirements

A Merchant must offer purchase with cash back Transactions on all Europe Region-issued Debit Mastercard and Maestro Cards if the Merchant offers this transaction type on any other debit brand.

A Merchant located in the United Kingdom is permitted to offer a cash back Transaction without an accompanying purchase, upon presentation of a Debit Mastercard Card. All other Standards applicable to purchase with cash back Transactions must be respected. The maximum cash back amount is GBP 100.

An Acquirer in Montenegro, Romania, or Serbia must technically support purchase with cash back Transactions in its host system and on the attended POS Terminals of its Merchants.

An Acquirer in Armenia, Belarus, Georgia, Kazakhstan, Kyrgyzstan, Russia, Tajikistan, Turkmenistan, Ukraine, and Uzbekistan that supports purchase with cash back Transactions must technically support purchase-only approval in its host system and at all participating POS Terminals.

In Albania, Austria, Bulgaria, Cyprus, Czech Republic, Hungary, Kosovo, Montenegro, North Macedonia, Poland, Romania, Serbia, Slovakia, and Slovenia, an Acquirer must itself support in its host systems and must ensure that new POS Terminals (and effective 23 July 2023, all POS Terminals) deployed which support purchase with cash back Transactions on the contact interface, also support purchase with cash back Transactions on the contactless interface, for both Domestic and Cross-border Transactions.

In Moldova, the following purchase with cash back Transaction requirements apply:

- an Acquirer that supports purchase with cash back Transactions must technically support purchase-only approval in its host and at all participating POS Terminals;
- POI currency conversion must not be offered on a purchase with cash back Transaction; and
- a Merchant in Moldova that supports purchase with cash back Transactions must show the cash back amount separately on the Transaction receipt.

# Maximum Cash Back Amount

The maximum cash back amount of a purchase with cash back Transaction is set out in the following table.

Maximum Cash Back Amount
GBP 100


# Card-Present Transactions

# 4.9 Purchase with Cash Back Transactions

|Country|Maximum Cash Back Amount|
|---|---|
|Armenia|AMD 30,000|
|Austria|EUR 200 (no maximum on Intracountry Maestro Transactions completed with PIN or CDCVM)|
|Belarus|BYN 100|
|Georgia|GEL 150|
|Germany|EUR 200|
|Kazakhstan|KZT 50,000|
|Kyrgyzstan|KGS 5,000|
|Moldova|MDL 1,000|
|Poland|PLN 1,000|
|Russia|RUB 5,000|
|Switzerland|CHF 300|
|Tajikistan|TJS 500|
|Turkmenistan|TKM 400|
|Ukraine|UAH 6,000|
|Uzbekistan|UZS 500,000|
|All other Europe Region countries|EUR 100 or the local currency equivalent|

Except as specified elsewhere in this Rule, an Acquirer or Merchant may establish a lower maximum cash back amount, provided that:

- Any such maximum amount is applied uniformly; and
- Any maximum amount is not lower than the maximum amount established for any other payment means on which purchase with cash back is offered at the Merchant location.

# CVM Requirements

The following CVMs must be supported by Issuers and Acquirers for purchase with cash back Transactions:

- Online PIN and offline PIN must be supported for Contact Chip Transactions; and
- Online PIN and CDCVM must be supported for Contactless Transactions.

As an exception to this Rule:


# Card-Present Transactions

# 4.9 Purchase with Cash Back Transactions

• Only online PIN is supported for Contact Chip Transactions and Contactless Transactions on Cards issued under a BIN assigned for Russia; and

• Only online PIN is supported for Contact Chip Transactions on Cards issued under a BIN assigned for Ukraine or Switzerland.

# Mastercard Cards, excluding Debit Mastercard Cards

A Merchant located in the Europe Region may, at its option, support purchase with cash back Transactions on Mastercard Cards.

If supported, the following requirements apply to purchase with cash back Transactions on Mastercard Cards:

1. Purchase with cash back on Mastercard Cards is not available for paper-based, key-entered, or magnetic stripe Transactions. It is available for all other types of Mastercard Transactions.
2. If a Merchant provides purchase with cash back only upon presentation of particular Cards, then the Merchant must not promote the service at the POI location or prompt the Cardholder to use purchase with cash back.

# Intracountry Transactions

The following Rules apply to Intracountry Transactions under all brands in the country mentioned.

1. For Intracountry Transactions in Poland, an Issuer in Poland must not apply a cash back limit lower than PLN 1,000. An Acquirer in Poland that supports purchase with cash back must not apply a cash back limit lower than PLN 1,000. A Merchant in Poland that offers purchase with cash back must not apply a cash back limit lower than PLN 1,000.
2. An Issuer in Russia must not apply a cash back limit lower than RUB 5,000. A Merchant located in Russia that provides purchase with cash back service must be duly signed up by its Acquirer as a bank payment agent in accordance with the local legislation.
3. Intracountry Transactions in Ukraine must be processed in UAH only; POI currency conversion must not be offered.
4. In Switzerland the purchase amount, cash back amount, and Transaction amount must all be in the same currency. The cash back amount must not be lower than CHF 10. An Issuer must decline the Transaction if the cash back amount exceeds CHF 300. The purchase amount of a purchase with cash back Transaction must not be lower than CHF 20.
5. An Issuer in Armenia, Belarus, Georgia, Kazakhstan, Kyrgyzstan, Russia, Tajikistan, Turkmenistan, Ukraine, and Uzbekistan must not apply a cash back limit lower than those specified in the above table of maximum cash back amounts.
6. Intracountry Transactions in Moldova must be processed in MDL only.

# Issuer Requirements

The following requirements apply to Issuers:

1. An Issuer in the Europe Region must technically support purchase with cash back Transactions on Debit Mastercard and Maestro Cards. The Issuer must make individual


# Card-Present Transactions

# 4.9 Purchase with Cash Back Transactions

Authorization decisions and must not automatically decline authorization of purchase with cash back Transactions on these Cards.

An Issuer must technically support purchase with cash back Transactions on Mastercard Cards issued under a BIN or BIN range assigned for the following countries:

|Country|Requirement|Effective date|
|---|---|---|
|Russia|Technical support in host systems|In effect|
|Ukraine|Technical support in host systems|In effect|
|Armenia, Belarus, Georgia, Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan|Technical support in host systems|16 July 2021|
|Newly issued and reissued Cards and MDES tokens must have the PWCB flag| |1 January 2023|
| |All Cards and MDES Tokens in circulation must have the PWCB flag|1 December 2025|
|Italy|Technical support for PWCB Transactions on Prepaid Cards and Tokens in the Issuer's host system|1 July 2021|
| |Newly issued and reissued Prepaid Cards and Tokens must have the PWCB flag| |
|Moldova|Technical support in host systems|1 December 2022|
| |Newly issued and reissued Cards and MDES tokens must have the PWCB flag|1 April 2023|
| |All Cards and MDES tokens in circulation must have the PWCB flag|1 January 2025|

Details of Technical Support Requirements for Issuers

In addition, an Issuer must technically support purchase with cash back Transactions, including in the Issuer authorization host system and with respect to purchase-amount-only approvals as


# Card-Present Transactions

# 4.10 Transactions at Unattended POS Terminals

set forth in global Rule 4.9, on Mastercard Cards issued under a BIN or BIN range assigned for the following countries:

|Country|Mandate applies to Mastercard Cards issued or reissued on or after|With the exception of the following types of Cards|
|---|---|---|
|Germany|1 January 2017|Prepaid Mastercard Cards|
|Romania|1 September 2017|No exceptions|
|Russia, Ukraine|1 January 2020|No exceptions|
|Armenia, Belarus, Georgia, Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan|1 January 2023|No exceptions|
|Moldova|1 April 2023|No exceptions|

1. An Issuer that intends to support purchase with cash back Transactions for its Mastercard Cardholders must properly personalize the chip on its Mastercard Cards.

2. An Issuer that supports partial approval may use partial approval to authorize only the purchase amount. Partial approval must not be used to authorize only the cash back amount.

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A purchase with cash back Transaction must be identified in authorization and clearing messages as specified by the registered switch of the Customer's choice. The Transaction amount and cash back amount must be identified in the fields and with the values specified by the registered switch of the Customer's choice.

# 4.10 Transactions at Unattended POS Terminals

In SCA Countries, the Rule on this subject is modified as follows. A CAT Level 2 Terminal supporting contact Transactions that does not operate in a transport or parking environment (MCCs 4111, 4112, 4131, 4784, 4789, and 7523) must:

- Be upgraded to have dual capability by the addition of an offline PIN-capable PIN pad, or
- Be upgraded to become a CAT Level 1 Terminal by the addition of an online PIN-capable PIN pad, or
- Have contact chip functionality removed, resulting in contactless-only acceptance, or
- Be removed from deployment.

A CAT Level 3 Terminal supporting contact Transactions that does not operate in a transport or parking environment (MCCs 4784 and 7523) must:

- Be upgraded with the addition of an offline PIN-capable PIN pad, or
- Have contact chip functionality removed, resulting in contactless-only acceptance, or
- Be removed from deployment.


# Card-Present Transactions

# 4.10.1 Automated Fuel Dispenser Transactions

A CAT Level 4 Terminal supporting contact Transactions must:

- Be upgraded with the addition of an offline PIN-capable PIN pad, or
- Have contact chip functionality removed, resulting in contactless-only acceptance, or
- Be removed from deployment.

CAT Transactions must be identified in authorization and clearing messages as specified by the registered switch of the Customer’s choice.

References in Appendix D to Acquirer MIP X-Code processing are replaced by references to corresponding authorization services of the registered switch of the Issuer’s choice.

# 4.10.1 Automated Fuel Dispenser Transactions

In the Europe Region, the Rule on this subject is modified as follows. Support for partial amount preauthorization is mandatory for Issuers and Acquirers of Maestro Cards if the Customer supports partial amount preauthorization for any other debit brand. Support of partial amount preauthorization is also required for all Mastercard Account ranges if the Customer supports partial amount preauthorization for Maestro or any other debit brand.

For more information on Maestro petrol Transaction preauthorizations, refer to “Maestro Preauthorized Transaction Processing” in Chapter 7 of the Authorization Manual and “Maestro Pre-authorized Transactions” in Chapter 5 of the Customer Interface Specification manual.

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. A Merchant must inform the Cardholder of any estimated amount for which authorization will be requested and obtain the Cardholder’s consent to the amount before initiating the authorization request. As an example, a Merchant may comply with this information requirement by allowing the Cardholder to select the preauthorization amount at the Terminal or via a clearly readable sticker or other notice placed at the Point-of-Interaction (POI). The Cardholder may express consent to the amount by continuing with the Transaction.

The preauthorization request amount, advice request amount, and partial approval support indicator must be provided in authorization messages, and the final Transaction amount must be provided in clearing messages, in the fields and with the values specified by the registered switch of the Customer’s choice.

# 4.13 Merchant-approved Maestro POS Transactions

In the EEA, UK and Gibraltar, the Rule on this subject is modified as follows. References to the Interchange System are replaced with references to the registered switch of the Customer’s choice.

In Belgium, the Rule on this subject is modified as follows. For Domestic Transactions in Belgium, the Acquirer may resubmit the Transaction once every 24 hours for a period ending 30 calendar days after the Transaction date, if a Merchant-approved Maestro POS Transaction is declined by the Issuer for insufficient funds, or because the Transaction exceeds withdrawal limits.


# 4.14 Mastercard Manual Cash Disbursement Transactions

# 4.14.2 Maximum Cash Disbursement Amounts

In the Europe Region, the Rule on this subject is modified as follows. The maximum cash disbursement amounts of USD 5,000 and USD 1,000 are replaced by EUR 5,000 and EUR 1,000, respectively.

# 4.17 ATM Access Fees

# 4.17.1 ATM Access Fees - Domestic Transactions

The Acquirer does not receive a Service fee in connection with an intra-European or inter-European Transaction on which an ATM Access Fee has been charged. In the Europe Region, the Rule on this subject, as it applies to Domestic Transactions in the countries listed below, is replaced with the following:

- All countries and territories in the European Economic Area, excluding Poland
- United Kingdom
- Uzbekistan

Subject to complying with the ATM Access Fee notification requirements of the Rules, an Acquirer may assess an ATM Access Fee on a Domestic Transaction, provided the Acquirer applies the ATM Access Fee in a consistent and nondiscriminatory manner. For example, the amount of the ATM Access Fee must not be greater than that charged on other brands or networks (whether card scheme or other access device or app-based payment method). The ATM Access Fee may vary according to the Card or payment application (whether access device or app-based payment method) category (credit, debit, prepaid, commercial), on condition that corresponding cash withdrawal transactions on other brands and payment applications at that ATM Terminal attract an equal or higher ATM Access Fee. The ATM Access Fee must be properly populated in Transaction messages.

"ATM Access Fee" means a fee charged by an Acquirer in connection with a financial ATM Transaction and added to the Transaction amount that is transmitted to the Issuer. An Acquirer must not assess an ATM Access Fee on a non-financial (anything other than cash withdrawal) Transaction.

# 4.18 Merchandise Transactions at ATM Terminals

# 4.18.1 Approved Merchandise Categories

In the Europe Region, the Rule on this subject is modified as follows.


# Card-Present Transactions

# Latin America and the Caribbean Region

|Merchandise Category|Explanation|
|---|---|
|Mobile Phone Top Up|The purchase of a specified amount of prepaid wireless telephone time, to be credited to the mobile SIM card associated with the subscriber’s prepaid telephone account. The Transaction is identified with MCC 4814.|
|Bill Payment|Payment via the ATM of utility, telephone or other bills. The Transaction may be identified with MCC 4900 or MCC 6050.|

# Latin America and the Caribbean Region

The following modifications to the Rules apply in the Latin America and the Caribbean Region. Refer to Appendix A for the Latin America and the Caribbean Region geographic listing.

# 4.4 Contactless Transactions at POS Terminals

In the Latin America and the Caribbean Region, the Rule on this subject, as it applies in Brazil, is modified as follows. If the Cardholder selects the “debit” option when using a Mastercard Card issued in Brazil to initiate a Contactless Transaction at a Merchant located in Brazil, Mastercard® Single Message System processing requirements and the chargeback procedures in Chapter 4 of the Chargeback Guide will apply. The resulting Transaction is referred to as a Maestro Magnetic Stripe Mode Contactless Transaction.

# 4.5 Contactless Transit Aggregated Transactions

# 4.5.2 Maestro Contactless Transit Aggregated Transactions

In the Latin America and the Caribbean Region, the Rule on this subject is modified as follows. In Mexico, when the limit is reached or within two calendar days, the Merchant totals the value of all taps and generates an Acquirer Reversal Advice/0420 message to reverse any unused funds. Specific Maestro Contactless transit aggregated Transaction CVM limits apply in the Bolivarian Republic of Venezuela, Colombia, and Mexico.

# 4.9 Purchase with Cash Back Transactions

In Argentina, the Rule on this subject is modified as follows with respect to Domestic Transactions: For purchase with cash back Transactions with or without an accompanying purchase, a Merchant may accept Maestro Cards, Debit Mastercard, and Prepaid Mastercard Cards. The following requirements apply to purchase with cash back Transactions:


# Card-Present Transactions

# 4.9 Purchase with Cash Back Transactions

1. The Acquirer must obtain online authorization approval for the entire Transaction amount; partial approval is not permitted.
2. A surcharge must not be applied to the Transaction by the Merchant or the Acquirer.
3. Installment billing of the Transaction must not be offered to the Cardholder.
4. All Transactions must be authenticated using the highest priority CVM supported by both the Card and the POS Terminal.
5. When cash is provided with an accompanying purchase, the total Transaction amount in DE 4 (Amount, Transaction) must be greater than the cash back amount in DE 54 (Additional Amounts), subfield 5 (Amount).
6. When cash is provided without an accompanying purchase, the total Transaction amount in DE 4 (Amount, Transaction) must be equal to the cash back amount in DE 54 (Additional Amounts), subfield 5 (Amount).
7. Acquirers must not offer purchase with cash back Transactions with or without an accompanying purchase to Cards issued outside the country.
8. Purchase with cash back Transactions with or without an accompanying purchase are not available for Mastercard® credit card products.

In Brazil, the Rule on this subject is modified as follows with respect to Domestic Transactions. A Merchant may offer the purchase with cash back service on the following Card types:

- For purchase with cash back Transactions with an accompanying purchase, a Merchant may accept Maestro Cards, Mastercard débito, Debit Mastercard and prepaid Mastercard Cards enabled for Mastercard Single Message System processing.
- For purchase with cash back Transactions without an accompanying purchase, a Merchant may accept Maestro Cards, Mastercard débito, Debit Mastercard and prepaid Mastercard Cards enabled for either Mastercard Dual Message System or Mastercard Single Message System processing.
- Issuers and Acquirers must not support Purchase with Cash Back Transactions for the following Card types:
- MBF Mastercard® Refeição (Meal)®Alimentação (Food)
- MBM Mastercard
- MLE Mastercard® Agro (available only in Brazil)®Pedágio Prepaid Card
- MLF Mastercard

The following requirements apply to purchase with cash back Transactions:

1. The Acquirer must obtain online authorization approval for the entire Transaction amount. Partial approval is not permitted.
2. A surcharge must not be applied to the Transaction by the Merchant or the Acquirer.
3. Installment billing of the Transaction must not be offered to the Cardholder.
4. All Transactions must be PIN-verified.
5. When cash is provided with an accompanying purchase, the total Transaction amount in DE 4 (Amount, Transaction) must be greater than the cash back amount in DE 54 (Additional Amounts), subfield 5 (Amount).



161
# Card-Present Transactions

# 4.17 ATM Access Fees

6. When cash is provided without an accompanying purchase, the total Transaction amount in DE 4 (Amount, Transaction) must be equal to the cash back amount in DE 54 (Additional Amounts), subfield 5 (Amount).

In Colombia and Venezuela, the Rule on this subject is modified as follows. Colombia and Venezuela Issuers are not required to support the purchase with cash back Transaction type.

In Uruguay, the Rule on this subject is modified as follows with respect to Domestic Transactions: For purchase with cash back Transactions with an accompanying purchase, a Merchant may accept Maestro Cards, Debit Mastercard, and Prepaid Mastercard Cards.

The following requirements apply to purchase with cash back Transactions:

1. The Acquirer must obtain online authorization approval for the entire Transaction amount; partial approval is not permitted.
2. A surcharge must not be applied to the Transaction by the Merchant or the Acquirer.
3. Installment billing of the Transaction must not be offered to the Cardholder.
4. All Transactions must be authenticated using the highest priority CVM supported by both the Card and the POS Terminal.
5. For Mastercard purchase with cash back Transactions, a maximum cash back amount of USD 60 or local currency equivalent applies.
6. When cash is provided with an accompanying purchase, the total Transaction amount in DE 4 (Amount, Transaction) must be greater than the cash back amount in DE 54 (Additional Amounts), subfield 5 (Amount).
7. Acquirers must not offer purchase with cash back Transactions to Cards issued outside the country.
8. Purchase with cash back Transactions are not available for Mastercard® credit card products.

# 4.17 ATM Access Fees

# 4.17.1 ATM Access Fees—Domestic Transactions

In the Latin America and the Caribbean Region, the Rule on this subject, as it applies to Domestic Transactions occurring in the countries listed below, is replaced with the following: Subject to complying with the ATM Access Fee notification requirements, the Acquirer may assess an ATM Access Fee on a Domestic Transaction provided the Acquirer applies the ATM Access Fee in a consistent and nondiscriminatory manner.

For the purposes of this Rule, “ATM Access Fee” means a fee charged by an Acquirer in connection with any financial Transaction initiated at that Acquirer’s ATM with a Card and added to the amount of the Transaction transmitted to the Issuer.

Argentina
Brazil


162
# Card-Present Transactions

# Middle East/Africa Region

Chile

Colombia

Ecuador

Mexico

Panama

Peru

Puerto Rico

Venezuela

# Middle East/Africa Region

The following modifications to the Rules apply in the Middle East/Africa Region. Refer to Appendix A for the Middle East/Africa Region geographic listing.

# 4.9 Purchase with Cash Back Transactions

In Kenya, the Rule on this subject is modified as follows:

A Merchant located in Kenya that has received prior approval from its Acquirer may offer a purchase with cash back Transaction with or without an accompanying purchase to any Cardholder presenting a Mastercard Card, Prepaid Mastercard Card, Debit Mastercard Card, or Maestro Card issued in Kenya.

For purchase with cash back Transactions, a maximum cash back amount must be established that does not exceed KES 100,000.

PIN verification must be obtained for each purchase with cash back Transaction without an accompanying purchase.

In South Africa, the Rule on this subject is modified as follows:

A Merchant located in South Africa that has received prior approval from its Acquirer may offer a purchase with cash back Transaction with or without an accompanying purchase to any Cardholder presenting a Mastercard, Debit Mastercard, or Maestro Card issued in South Africa.

PIN verification must be obtained for each purchase with cash back Transaction without an accompanying purchase.

# United States Region

The following modifications to the Rules apply in the United States (U.S.) Region. Refer to Appendix A for the U.S. Region geographic listing.

# 4.1 Chip Transactions at Hybrid Terminals

The Rule on this subject is modified as follows:



163
# Card-Present Transactions

# 4.5 Contactless Transit Transactions

- “PIN-capable Hybrid POS Terminal” means a Hybrid POS Terminal capable of performing both online and offline PIN verification when a PIN-preferring Chip Card is presented, and which, if attended, also supports the signature CVM. Signature collection is optional.
- “PIN-preferring Chip Card” means a Chip Card that has been personalized so that a PIN CVM option (online PIN or offline PIN) appears in the Card’s CVM list with a higher priority than the signature CVM, indicating that a PIN CVM is preferred to the signature CVM at any POS Terminal that supports the same PIN CVM option.

Technical fallback occurs when a Chip Card is presented at a Hybrid Terminal but due to the failure of Chip Transaction processing, the Transaction is completed using the magnetic stripe or manual key entry of the PAN. The ratio of technical fallback Transactions to all Transactions completed at Hybrid Terminals at a particular Merchant location or at an ATM Terminal for a calendar month must not exceed five percent of all Chip Card Transactions at that Merchant location or ATM Terminal. An Acquirer with a Merchant that has exceeded the Standard set forth in the preceding sentence may be subject to noncompliance assessments.

# 4.5 Contactless Transit Transactions

# 4.5.1 Mastercard Contactless Transit Aggregated Transactions

In the U.S. Region, effective 15 August 2022, the Rule on this subject is replaced with the following. A contactless transit aggregated Transaction occurs when one or more contactless taps performed with one Mastercard or Maestro Account at one U.S. Region transit Merchant during a 24-hour period (the “tap aggregation period”) are combined into a total Transaction amount and subsequently submitted for authorization on a deferred basis. A “tap” means the Cardholder’s tap of the Card or Contactless Payment Device on the contactless reader of the POS Terminal with each ride taken.

The following requirements apply.

# Account Verification Required

Upon the first use of a Mastercard or Maestro Account at the transit Merchant on a given day (the “initial tap”), the Merchant starts the 24-hour aggregation period. The initial tap must be processed as follows:

- The Merchant sends an Account status inquiry (ASI) Authorization Request/0100 or Financial Transaction Request/0200 message, either deferred or in real-time. An ASI request contains a value of 8 (Account Status Inquiry Service [ASI]) in DE 61, subfield 7 (POS Transaction Status) and a Transaction amount of zero.
- If the Issuer approves or does not decline the ASI request, then the Merchant may proceed with tap aggregation as specified in this Rule.
- If the Issuer declines the ASI request, then the Merchant must not proceed with tap aggregation. The Merchant may submit a transit debt recovery Transaction for the amount of a single ride (if taken).


# Card-Present Transactions

# 4.5.2 Maestro Contactless Transit Aggregated Transactions

# Aggregation Procedures

The following requirements apply for each tap aggregation period:

1. Following successful account verification as described above, the Merchant or its Acquirer maintains a record of each subsequent tap that occurs within the 24-hour aggregation period.
2. At the end of the aggregation period, the Merchant uses the last tap to initiate an Authorization Request/0100 or Financial Transaction Request/0200 message for the combined total amount of taps (rides taken) during the aggregation period. The total aggregated amount must not exceed the applicable contactless Transaction CVM limit amount (USD 100).
3. The Merchant must receive Issuer authorization for the Transaction. If the Issuer declines, the Merchant may submit a transit debt recovery Transaction. If the transit debt recovery Transaction is declined, the Merchant must not perform tap aggregation involving the Account until debt recovery on the Account is successfully completed and the Issuer approves a new Account verification request.
4. Upon the Cardholder’s request, the Merchant must provide a list of the taps that were aggregated (the date, time [if available], and fare for each ride taken).

Multiple aggregation cycles may occur in the same 24-hour period, at the Merchant’s discretion. As described in the “Contactless Transactions” section of Appendix C, Transaction messages for the combined total amount of aggregated taps occurring in an aggregation period must contain:

- A value of 05 (Other) in DE 48, subelement 64, subfield 1 (Transit Transaction Type) of Authorization Request/0100 and Financial Transaction Request/0200 messages and in PDS 0210, subfield 1 (Transit Transaction Type) of First Presentment/1240 messages; and
- A value of 1 (Deferred authorization) in DE 61, subfield 7 of the Authorization Request/0100 or Financial Transaction Request/0200 message.

# 4.5.2 Maestro Contactless Transit Aggregated Transactions

In the U.S. Region, effective 15 August 2022, the Rule on this subject is replaced with U.S. Region Rule 4.5.1.

# 4.9 Purchase with Cash Back Transactions

In the U.S. Region, the Rule on this subject is modified as follows.

A Merchant located in the United States that has received prior approval from its Acquirer may offer a Cardholder a cash back Transaction with or without an accompanying purchase when a Debit Mastercard (including prepaid) Card is presented. A maximum cash back amount must be established in an amount that does not exceed USD 200 per Transaction.

A Merchant may charge a fee on the cash back portion of a Transaction. The fee charged by the Merchant must be:

1. The same or less than the fee charged for a cash back transaction for all other payment networks.


# Card-Present Transactions

# 4.10 Transactions at Unattended POS Terminals

b. Disclosed to the Cardholder before completion of the Transaction.

c. Detailed in DE 54 (Amounts, Additional) of the First Presentment/1240 message.

d. Detailed in DE 28 (Amount, Transaction Fee) of the Authorization Request/0100 message or Financial Transaction Request/0200.

e. Included in the total Transaction amount transmitted in DE 4 (Amount, Transaction) of authorization and clearing messages.

# 4.10 Transactions at Unattended POS Terminals

# 4.10.1 Automated Fuel Dispenser Transactions

In the U.S. Region, the Rule on this subject is modified as follows. An automated fuel dispenser Merchant identified by the Corporation to be an Excessive Chargeback Merchant (ECM) must use the Mastercard Address Verification Service (AVS) to verify the Cardholder’s ZIP code before completing a Cardholder-Activated Terminal (CAT) Level 2 Transaction. For information about ECM criteria, refer to section 8.3, “Excessive Chargeback Program,” of the Security Rules and Procedures. For information about ECM requirements to use AVS, refer to United States Region section, section 5.11.4, "Additional Cardholder Identification" of the Mastercard Rules manual.

# 4.11 PIN-based Debit Transactions

In the U.S. Region, a Customer may choose to acquire Transactions effected with Debit Mastercard Cards where PIN is used as the Cardholder verification method (CVM).

# 4.12 PIN-less Single Message Transactions

In the U.S. Region, a PIN-less Single Message Transaction is a Transaction where the Cardholder is not required to be verified by PIN or other CVM if all of the following conditions exist:

- The Card is issued in the U.S. Region; and
- The Card has an IIN/BIN that begins with a four; and
- The Transaction is initiated by means of a POS Terminal located in the U.S. Region; and
- The Transaction amount is equal to or less than USD 100; and
- The Transaction is a magnetic stripe Transaction, Contact Chip Transaction, or Contactless Transaction; and
- The Transaction type cannot be performed at an unattended POS Terminal; and
- DE 18 (Merchant Type) does not contain any of the following Merchant category code (MCC) values:


# Card-Present Transactions

# 4.14 Mastercard Manual Cash Disbursement Transactions

- MCC 6540 (Funding Transactions)
- MCC 7800 (Government Owned Lottery [U.S. Region Only])
- MCC 7801 (Internet Gambling [U.S. Region Only])
- MCC 7802 (Government Licensed Horse/Dog Racing [U.S. Region Only])
- MCC 7995 (Gambling Transactions)
- MCC 9405 (Intra-Government Purchases: Government Only)

If all of the conditions are met, a Corporation-assigned indicator will be populated in DE 48, subelement 81 of the Financial Transaction Request/0200 message, indicating that the Transaction qualifies for processing as a PIN-less Single Message Transaction.

For Transactions qualifying as PIN-less Single Message Transactions:

1. No CVM is required.
2. An Acquirer must be able to route a PIN-less Single Message Transaction to the Issuer for approval.
3. An Acquirer must only route a PIN-less Single Message Transaction when the final purchase Transaction amount is certain at the time of authorization.
4. An Issuer may not charge back a PIN-less Single Message Transaction for reason of fraud.

# 4.14 Mastercard Manual Cash Disbursement Transactions

In the U.S. Region, the Rule on this subject is modified as follows: Subject to compliance with the Standards, each Customer within the United States Region must provide cash disbursement services to all Cardholders at all of the Customer’s offices where teller services are provided.

# 4.14.2 Maximum Cash Disbursement Amounts

In the U.S. Region, the Rule on this subject is replaced with the following: A Customer and each of its authorized cash disbursement agents may limit the amount of cash provided to any one Cardholder in one day at any individual office. Any such limit must be uniformly applied to all Cardholders of the same Card type. With respect to prepaid Cards, the limit must not be less than USD 5,000 per Cardholder in one day. With respect to all other Card types, the limit must not be less than USD 1,000 per Cardholder in one day.

# 4.14.3 Discount or Service Charges

In the U.S. Region, the Rule on this subject is replaced with the following: With respect to the acceptance of prepaid Cards, the Customer and each of its authorized cash disbursement agents must disburse all cash disbursements at par without any discount and without any service or other charge to the Cardholder, except as may be imposed to comply with applicable law. Any charge imposed to comply with applicable law must be charged to and paid by the Cardholder separately and must not be included in the total amount of the cash disbursement.

With respect to the acceptance of any type of Mastercard Card other than a prepaid Card, a Customer or its authorized cash disbursement agent may charge a fee for performance of the



167
# Card-Present Transactions

# 4.17 ATM Access Fees

cash disbursement service (herein, a “Manual Cash Disbursement Access Fee”). Any Manual Cash Disbursement Access Fee charged must be:

1. Not greater than the fee established for any other payment network.
2. Disclosed to the Cardholder before a Transaction authorization request is submitted. At the time of disclosure, the Cardholder must be afforded the opportunity to opt out of completing the Transaction.
3. Disclosed on the Transaction receipt.
4. Detailed in DE 28 (Amount, Transaction Fee) of the Authorization Request/0100 or Financial Transaction Request/0200 message.
5. Detailed in DE 54 (Amounts, Additional) of the First Presentment/1240 message.
6. Included in the total Transaction amount transmitted in DE 4 (Amount, Transaction) of authorization and clearing messages.

# 4.17 ATM Access Fees

# 4.17.1 ATM Access Fees—Domestic Transactions

In the U.S. Region, the Rule on this subject is replaced with the following: In all states and territories of the United States and in the District of Columbia, upon complying with the ATM Access Fee notification requirements of the Rules, an Acquirer may assess an ATM Access Fee on a Domestic Transaction.

# 4.18 Merchandise Transactions at ATM Terminals

# 4.18.1 Approved Merchandise Categories

In the U.S. Region, the Rule on this subject is modified to add postage stamps issued by the U.S. Postal Service as an approved merchandise category.

# 4.19 Shared Deposits

In the U.S. Region, an Acquirer may choose to participate in the Shared Deposit service; provided, if the Acquirer deploys ATM Terminals that participate in any other shared deposit service, those ATM Terminals must participate in the Shared Deposit service. An Acquirer may make only its ATM Terminals available for participation in the Shared Deposit service. An Acquirer that, as an Issuer, elects to take part in the Shared Deposit service must designate its BINs/IINs and ATM Terminals that participate in any other shared deposit service for participation in the Shared Deposit service.

# 4.19.1 Non-discrimination Regarding Shared Deposits

An Acquirer may impose a dollar limit on Shared Deposits accepted at an ATM Terminal provided that the limit imposed on Cardholders is the same or more favorable than the limits imposed on cardholders of other networks. This Rule does not limit the application of other non-discrimination provisions contained in the Standards.



168
# Card-Present Transactions

# 4.19.2 Terminal Signs and Notices

An Acquirer must display a notice regarding funds availability in accordance with section 229.18(c) of Regulation CC, 12 C.F.R. § 229.18(c) on each ATM Terminal that participates in the Shared Deposit service.

# 4.19.3 Maximum Shared Deposit Amount

The maximum Shared Deposit Transaction amount must be limited to USD 99,999.99.

# 4.19.4 Deposit Verification

An Acquirer must process its Shared Deposits as follows.

1. The Acquirer must complete an examination of each Shared Deposit no later than one business day after the date of the Transaction;
2. Such examination must be conducted under dual control standards either by two employees of the Acquirer or by one or more employees of the Acquirer with a surveillance camera monitoring the examination;
3. The examination must consist of the following:
1. The deposit must be verified to ensure that the dollar amount of the deposit keyed by the Cardholder at the ATM Terminal matches the deposit contents; the deposit envelope is not empty; and the deposit envelope does not contain only non-negotiable items;
2. The Acquirer must identify any irregularities that would make an item in the deposit envelope non-negotiable, such as:
- The deposited currency is counterfeit;
- The deposited currency, check or money order is in a denomination other than U.S. Region currency;
- The item is drawn on or payable by an institution located outside the U.S. Region;
- The item has a passbook attached;
- The item is a photocopy;
- The item is a certificate of deposit or banker’s acceptance;
- The item is a non-negotiable writing;
- The item is a returned or cancelled check or draft;
- A date is not present on the item;
- The item is postdated;
- The item is dated more than six months prior to the date of the deposit;
- The payee field has not been completed;
- Either the written or numeric amount does not appear on the item;
- The written amount does not match the numeric amount on the item;
- The amount on the item appears altered;
- The item includes restrictive wording;
- The item is missing an endorsement;
- The item, which requires a signature, is unsigned.


# Card-Present Transactions

# 4.19.5 ATM Terminal Clearing and Deposit Processing

The Acquirer must submit an adjustment within one business day of the deposit verification date if a discrepancy exists between the deposit amount and the amount keyed into the ATM Terminal.

An Acquirer that accepts Shared Deposits must clear its ATM Terminals at least once each business day. By the end of the business day following the day on which an ATM Terminal was cleared, the Acquirer must forward for collection all Shared Deposits cleared from that Terminal in the same manner it would forward its own Cardholders' deposits.

# 4.19.6 Shared Deposits in Excess of USD 10,000

If an Acquirer receives a Shared Deposit or series of related Shared Deposits made to a single Account on one business day containing currency in excess of USD 10,000, the Acquirer must notify the Issuer of this fact by telephone, facsimile, or any other means permitted by the Corporation within two business days of the date of deposit. The Acquirer must record the occurrence as well as the act of reporting the occurrence and must include the name of the Issuer’s employee that received notification.

The notification must include the following:

1. Cardholder number;
2. Amount of currency;
3. Amount of currency in bills of denomination of USD 10,000 or higher;
4. ATM Terminal location;
5. Date and time of deposit.

If the Acquirer fails to provide notification of such cash deposits and the Issuer is assessed penalties or fines as a result of the Acquirer’s failure, the Acquirer must indemnify the Issuer for such penalties and fines.

# 4.19.7 Notice of Return

If an item sent by an Acquirer to the payor bank of the item for presentment is returned to the Acquirer for any reason or the Acquirer receives notice of nonpayment of the item for any reason from the payor bank, the Acquirer must notify the Issuer of the receipt of such return or notice, and must initiate return of the returned item to the Issuer no later than one business day following the receipt of the returned item or the notice of nonpayment, whichever is received first. Such notice to the Issuer must include the reason for nonpayment as set forth on the returned item or notice of nonpayment received.

# 4.19.8 Liability for Shared Deposits

The maximum damages that an Acquirer may face for its failure to comply with these Shared Deposit Rules is the amount of loss incurred by the Issuer with respect to a particular Shared Deposit, not to exceed the amount of the Shared Deposit. In addition, an Acquirer will not be liable to an Issuer for any amount of the Shared Deposit that the Issuer could have recovered from the Cardholder. An Issuer must claim that:


# Card-Present Transactions

# 4.19.8 Liability for Shared Deposits

1. Its Cardholder would not accept the adjustment of an improper Shared Deposit;
2. It could not debit the Cardholder when the Issuer received notice of the improper deposit;
3. It could have debited the Cardholder if the Acquirer had complied with these Shared Deposit Rules.

In all events, the Issuer must first attempt to collect from its Cardholder.