# Fehlercodes aus offiziellen Schematron-Quellen

## Inhalt

- [Herkunft und Grenzen](#herkunft-und-grenzen)
- [Regelkatalog](#regelkatalog)
- [Ableitung](#ableitung)

## Herkunft und Grenzen

Diese Tabelle wurde mechanisch aus folgenden offiziellen, versionierten Primärquellen erzeugt:

- EN16931 Validation Artefacts `validation-1.3.15`, Commit `bf3a7d8d7137bec0c90f35d0fad42e30128fa2fd` (EUPL-1.2): CII- und UBL-Schematron.
- KoSIT XRechnung Schematron `v2.5.0` für XRechnung 3.0.2, Release-Artefakt `xrechnung-3.0.2-schematron-2.5.0.zip`, SHA-256 `a0f3d82737759bee8591c298ff24983a8f1c667f85e45a34863c75a242bc6f43` (Apache-2.0): ausgelieferte CII- und UBL-Schematrons einschließlich der von KoSIT integrierten Peppol-Regeln.
- OpenPeppol BIS Billing `v3.0.20`, Commit `261c458474e27d58a25be629cccac28883171c92` (Apache-2.0): offizielle Syntaxstruktur für zusätzliche Regel-zu-BT/BG-Referenzen. KoSIT v2.5.0 deklariert genau diese BIS-Version als Build-Eingang.

Quellen:

- https://github.com/ConnectingEurope/eInvoicing-EN16931/tree/validation-1.3.15
- https://github.com/itplr-kosit/xrechnung-schematron/releases/tag/v2.5.0
- https://github.com/OpenPEPPOL/peppol-bis-invoice-3/tree/v3.0.20

`MUSTANG_*`-Kennungen und veraPDF-/PDF-A-Regeln stehen nicht in diesen Schematrons. Sie sind Implementierungs- beziehungsweise PDF/A-Diagnosen und müssen anhand der im Validatorbericht genannten Mustang-Version sowie ISO-Klausel/veraPDF-Regel ausgewertet werden.

Eine `assert`-Regel meldet einen Verstoß, wenn ihre XPath-Testbedingung im angegebenen Dokumentkontext **falsch** ist. Die Spalte Bedeutung übernimmt den normativen Meldungstext aus dem Schematron; BT/BG-Bezüge werden ausschließlich aus diesem Text extrahiert. Sie sind leer, wenn die offizielle Meldung keinen BT/BG-Bezug nennt.

## Regelkatalog

| Code | Regelwerk | Severity | BT/BG | Bedeutung |
|---|---|---|---|---|
| `BR-01` | EN16931 | fatal | `BT-24` | An Invoice shall have a Specification identifier (BT-24). |
| `BR-02` | EN16931 | fatal | `BT-1` | An Invoice shall have an Invoice number (BT-1). |
| `BR-03` | EN16931 | fatal | `BT-2` | An Invoice shall have an Invoice issue date (BT-2). |
| `BR-04` | EN16931 | fatal | `BT-3` | An Invoice shall have an Invoice type code (BT-3). |
| `BR-05` | EN16931 | fatal | `BT-5` | An Invoice shall have an Invoice currency code (BT-5). |
| `BR-06` | EN16931 | fatal | `BT-27` | An Invoice shall contain the Seller name (BT-27). |
| `BR-07` | EN16931 | fatal | `BT-44` | An Invoice shall contain the Buyer name (BT-44). |
| `BR-08` | EN16931 | fatal | `BG-5` | CII: An Invoice shall contain the Seller postal address (BG-5).<br>UBL: An Invoice shall contain the Seller postal address. |
| `BR-09` | EN16931 | fatal | `BG-5`, `BT-40` | The Seller postal address (BG-5) shall contain a Seller country code (BT-40). |
| `BR-10` | EN16931 | fatal | `BG-8` | An Invoice shall contain the Buyer postal address (BG-8). |
| `BR-11` | EN16931 | fatal | `BT-55` | The Buyer postal address shall contain a Buyer country code (BT-55). |
| `BR-12` | EN16931 | fatal | `BT-106` | An Invoice shall have the Sum of Invoice line net amount (BT-106). |
| `BR-13` | EN16931 | fatal | `BT-109` | An Invoice shall have the Invoice total amount without VAT (BT-109). |
| `BR-14` | EN16931 | fatal | `BT-112` | An Invoice shall have the Invoice total amount with VAT (BT-112). |
| `BR-15` | EN16931 | fatal | `BT-115` | An Invoice shall have the Amount due for payment (BT-115). |
| `BR-16` | EN16931 | fatal | `BG-25` | CII: An Invoice shall have at least one Invoice line (BG-25).<br>UBL: An Invoice shall have at least one Invoice line (BG-25) |
| `BR-17` | EN16931 | fatal | `BG-4`, `BG-10`, `BT-59` | CII: The Payee name (BT-59) shall be provided in the Invoice, if the Payee (BG-10) is different from the Seller (BG-4).<br>UBL: The Payee name (BT-59) shall be provided in the Invoice, if the Payee (BG-10) is different from the Seller (BG-4) |
| `BR-18` | EN16931 | fatal | `BG-4`, `BG-11`, `BT-62` | CII: The Seller tax representative name (BT-62) shall be provided in the Invoice, if the Seller (BG-4) has a Seller tax representative party (BG-11).<br>UBL: The Seller tax representative name (BT-62) shall be provided in the Invoice, if the Seller (BG-4) has a Seller tax representative party (BG-11) |
| `BR-19` | EN16931 | fatal | `BG-4`, `BG-11`, `BG-12` | The Seller tax representative postal address (BG-12) shall be provided in the Invoice, if the Seller (BG-4) has a Seller tax representative party (BG-11). |
| `BR-20` | EN16931 | fatal | `BG-4`, `BG-11`, `BG-12`, `BT-69` | The Seller tax representative postal address (BG-12) shall contain a Tax representative country code (BT-69), if the Seller (BG-4) has a Seller tax representative party (BG-11). |
| `BR-21` | EN16931 | fatal | `BG-25`, `BT-126` | Each Invoice line (BG-25) shall have an Invoice line identifier (BT-126). |
| `BR-22` | EN16931 | fatal | `BG-25`, `BT-129` | Each Invoice line (BG-25) shall have an Invoiced quantity (BT-129). |
| `BR-23` | EN16931 | fatal | `BG-25`, `BT-130` | An Invoice line (BG-25) shall have an Invoiced quantity unit of measure code (BT-130). |
| `BR-24` | EN16931 | fatal | `BG-25`, `BT-131` | Each Invoice line (BG-25) shall have an Invoice line net amount (BT-131). |
| `BR-25` | EN16931 | fatal | `BG-25`, `BT-153` | Each Invoice line (BG-25) shall contain the Item name (BT-153). |
| `BR-26` | EN16931 | fatal | `BG-25`, `BT-146` | Each Invoice line (BG-25) shall contain the Item net price (BT-146). |
| `BR-27` | EN16931 | fatal | `BT-146` | The Item net price (BT-146) shall NOT be negative. |
| `BR-28` | EN16931 | fatal | `BT-148` | The Item gross price (BT-148) shall NOT be negative. |
| `BR-29` | EN16931 | fatal | `BT-73`, `BT-74` | If both Invoicing period start date (BT-73) and Invoicing period end date (BT-74) are given then the Invoicing period end date (BT-74) shall be later or equal to the Invoicing period start date (BT-73). |
| `BR-30` | EN16931 | fatal | `BT-134`, `BT-135` | If both Invoice line period start date (BT-134) and Invoice line period end date (BT-135) are given then the Invoice line period end date (BT-135) shall be later or equal to the Invoice line period start date (BT-134). |
| `BR-31` | EN16931 | fatal | `BG-20`, `BT-92`, `BT-99` | Each Document level allowance (BG-20) shall have a Document level allowance amount (BT-92). |
| `BR-32` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-102` | Each Document level allowance (BG-20) shall have a Document level allowance VAT category code (BT-95). |
| `BR-33` | EN16931 | fatal | `BG-20`, `BT-97`, `BT-98`, `BT-104`, `BT-105` | Each Document level allowance (BG-20) shall have a Document level allowance reason (BT-97) or a Document level allowance reason code (BT-98). |
| `BR-36` | EN16931 | fatal | `BG-21`, `BT-92`, `BT-99` | Each Document level charge (BG-21) shall have a Document level charge amount (BT-99). |
| `BR-37` | EN16931 | fatal | `BG-21`, `BT-95`, `BT-102` | Each Document level charge (BG-21) shall have a Document level charge VAT category code (BT-102). |
| `BR-38` | EN16931 | fatal | `BG-21`, `BT-97`, `BT-98`, `BT-104`, `BT-105` | Each Document level charge (BG-21) shall have a Document level charge reason (BT-104) or a Document level charge reason code (BT-105). |
| `BR-41` | EN16931 | fatal | `BG-27`, `BT-136`, `BT-141` | Each Invoice line allowance (BG-27) shall have an Invoice line allowance amount (BT-136). |
| `BR-42` | EN16931 | fatal | `BG-27`, `BT-139`, `BT-140`, `BT-144`, `BT-145` | Each Invoice line allowance (BG-27) shall have an Invoice line allowance reason (BT-139) or an Invoice line allowance reason code (BT-140). |
| `BR-43` | EN16931 | fatal | `BG-28`, `BT-136`, `BT-141` | Each Invoice line charge (BG-28) shall have an Invoice line charge amount (BT-141). |
| `BR-44` | EN16931 | fatal | `BG-28`, `BT-139`, `BT-140`, `BT-144`, `BT-145` | CII: Each Invoice line charge (BG-28) shall have an Invoice line charge reason (BT-144) or an Invoice line charge reason code (BT-145).<br>UBL: Each Invoice line charge shall have an Invoice line charge reason or an invoice line allowance reason code. |
| `BR-45` | EN16931 | fatal | `BG-23`, `BT-116` | Each VAT breakdown (BG-23) shall have a VAT category taxable amount (BT-116). |
| `BR-46` | EN16931 | fatal | `BG-23`, `BT-117` | Each VAT breakdown (BG-23) shall have a VAT category tax amount (BT-117). |
| `BR-47` | EN16931 | fatal | `BG-23`, `BT-118` | Each VAT breakdown (BG-23) shall be defined through a VAT category code (BT-118). |
| `BR-48` | EN16931 | fatal | `BG-23`, `BT-119` | Each VAT breakdown (BG-23) shall have a VAT category rate (BT-119), except if the Invoice is not subject to VAT. |
| `BR-49` | EN16931 | fatal | `BG-16`, `BT-81` | A Payment instruction (BG-16) shall specify the Payment means type code (BT-81). |
| `BR-50` | EN16931 | fatal | `BG-16`, `BG-17`, `BT-84` | CII: A Payment account identifier (BT-84) shall be present if Credit transfer (BG-16) information is provided in the Invoice.<br>UBL: A Payment account identifier (BT-84) shall be present if Credit transfer (BG-17) information is provided in the Invoice. |
| `BR-51` | EN16931 | CII: fatal<br>UBL: warning | `BT-87`, `BT-97` | CII: In accordance with card payments security standards an invoice should never include a full card primary account number (BT-97). At the moment PCI Security Standards Council has defined that the first 6 digits and last 4 digits are the maximum number of digits to be shown.<br>UBL: In accordance with card payments security standards an invoice should never include a full card primary account number (BT-87). At the moment PCI Security Standards Council has defined that the first 6 digits and last 4 digits are the maximum number of digits to be shown. |
| `BR-52` | EN16931 | fatal | `BG-24`, `BT-18`, `BT-122` | Each Additional supporting document (BG-24) shall contain a Supporting document reference (BT-122). |
| `BR-53` | EN16931 | fatal | `BT-6`, `BT-110`, `BT-111` | If the VAT accounting currency code (BT-6) is present, then the Invoice total VAT amount in accounting currency (BT-111) shall be provided. |
| `BR-54` | EN16931 | fatal | `BG-32`, `BT-160`, `BT-161` | Each Item attribute (BG-32) shall contain an Item attribute name (BT-160) and an Item attribute value (BT-161). |
| `BR-55` | EN16931 | fatal | `BG-3`, `BT-25` | Each Preceding Invoice reference (BG-3) shall contain a Preceding Invoice reference (BT-25). |
| `BR-56` | EN16931 | fatal | `BG-11`, `BT-63` | Each Seller tax representative party (BG-11) shall have a Seller tax representative VAT identifier (BT-63). |
| `BR-57` | EN16931 | fatal | `BG-15`, `BT-80` | Each Deliver to address (BG-15) shall contain a Deliver to country code (BT-80). |
| `BR-61` | EN16931 | fatal | `BT-81`, `BT-84` | If the Payment means type code (BT-81) means SEPA credit transfer, Local credit transfer or Non-SEPA international credit transfer, the Payment account identifier (BT-84) shall be present. |
| `BR-62` | EN16931 | fatal | `BT-34` | The Seller electronic address (BT-34) shall have a Scheme identifier. |
| `BR-63` | EN16931 | fatal | `BT-49` | The Buyer electronic address (BT-49) shall have a Scheme identifier. |
| `BR-64` | EN16931 | fatal | `BT-157` | The Item standard identifier (BT-157) shall have a Scheme identifier. |
| `BR-65` | EN16931 | fatal | `BT-158` | The Item classification identifier (BT-158) shall have a Scheme identifier. |
| `BR-AE-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | CII: An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Reverse charge" shall contain in the VAT breakdown (BG-23) exactly one VAT category code (BT-118) equal with "VAT reverse charge".<br>UBL: An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Reverse charge" shall contain in the VAT Breakdown (BG-23) exactly one VAT category code (BT-118) equal with "VAT reverse charge". |
| `BR-AE-02` | EN16931 | fatal | `BG-25`, `BT-31`, `BT-32`, `BT-47`, `BT-48`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Reverse charge" shall contain the Seller VAT Identifier (BT-31), the Seller Tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48) and/or the Buyer legal registration identifier (BT-47). |
| `BR-AE-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-47`, `BT-48`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Reverse charge" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48) and/or the Buyer legal registration identifier (BT-47). |
| `BR-AE-04` | EN16931 | fatal | `BG-21`, `BT-31`, `BT-32`, `BT-47`, `BT-48`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Reverse charge" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48) and/or the Buyer legal registration identifier (BT-47). |
| `BR-AE-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Reverse charge" the Invoiced item VAT rate (BT-152) shall be 0 (zero). |
| `BR-AE-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96`, `BT-103` | In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Reverse charge" the Document level allowance VAT rate (BT-96) shall be 0 (zero). |
| `BR-AE-07` | EN16931 | fatal | `BG-21`, `BT-96`, `BT-102`, `BT-103` | In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Reverse charge" the Document level charge VAT rate (BT-103) shall be 0 (zero). |
| `BR-AE-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-99`, `BT-102`, `BT-116`, `BT-118`, `BT-131`, `BT-151` | In a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Reverse charge" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amounts (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Reverse charge". |
| `BR-AE-09` | EN16931 | fatal | `BG-23`, `BT-117`, `BT-118` | The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Reverse charge" shall be 0 (zero). |
| `BR-AE-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Reverse charge" shall have a VAT exemption reason code (BT-121), meaning "Reverse charge" or the VAT exemption reason text (BT-120) "Reverse charge" (or the equivalent standard text in another language).<br>UBL: A VAT breakdown (BG-23) with VAT Category code (BT-118) "Reverse charge" shall have a VAT exemption reason code (BT-121), meaning "Reverse charge" or the VAT exemption reason text (BT-120) "Reverse charge" (or the equivalent standard text in another language). |
| `BR-AF-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "IGIC" shall contain in the VAT breakdown (BG-23) at least one VAT category code (BT-118) equal with "IGIC". |
| `BR-AF-02` | EN16931 | fatal | `BG-25`, `BT-31`, `BT-32`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "IGIC" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-AF-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "IGIC" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-AF-04` | EN16931 | fatal | `BG-21`, `BT-31`, `BT-32`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "IGIC" shall contain the Seller VAT Identifier (BT-31), the Seller Tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-AF-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | CII: In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "IGIC" the invoiced item VAT rate (BT-152) shall be greater than 0 (zero).<br>UBL: In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "IGIC" the invoiced item VAT rate (BT-152) shall be 0 (zero) or greater than zero. |
| `BR-AF-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96` | In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "IGIC" the Document level allowance VAT rate (BT-96) shall be 0 (zero) or greater than zero. |
| `BR-AF-07` | EN16931 | fatal | `BG-21`, `BT-102`, `BT-103` | In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "IGIC" the Document level charge VAT rate (BT-103) shall be 0 (zero) or greater than zero. |
| `BR-AF-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-96`, `BT-99`, `BT-102`, `BT-103`, `BT-116`, `BT-118`, `BT-119`, `BT-131`, `BT-151`, `BT-152` | For each different value of VAT category rate (BT-119) where the VAT category code (BT-118) is "IGIC", the VAT category taxable amount (BT-116) in a VAT breakdown (BG-23) shall equal the sum of Invoice line net amounts (BT-131) plus the sum of document level charge amounts (BT-99) minus the sum of document level allowance amounts (BT-92) where the VAT category code (BT-151, BT-102, BT-95) is "IGIC" and the VAT rate (BT-152, BT-103, BT-96) equals the VAT category rate (BT-119). |
| `BR-AF-09` | EN16931 | fatal | `BG-23`, `BT-116`, `BT-117`, `BT-118`, `BT-119` | The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where VAT category code (BT-118) is "IGIC" shall equal the VAT category taxable amount (BT-116) multiplied by the VAT category rate (BT-119). |
| `BR-AF-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with VAT Category code (BT-118) "IGIC" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120).<br>UBL: A VAT breakdown (BG-23) with VAT Category code (BT-118) "IGIC" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120). |
| `BR-AG-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "IPSI" shall contain in the VAT breakdown (BG-23) at least one VAT category code (BT-118) equal with "IPSI". |
| `BR-AG-02` | EN16931 | fatal | `BG-25`, `BT-31`, `BT-32`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "IPSI" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-AG-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "IPSI" shall contain the Seller VAT Identifier (BT-31), the Seller Tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-AG-04` | EN16931 | fatal | `BG-21`, `BT-31`, `BT-32`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "IPSI" shall contain the Seller VAT Identifier (BT-31), the Seller Tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-AG-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "IPSI" the Invoiced item VAT rate (BT-152) shall be 0 (zero) or greater than zero. |
| `BR-AG-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96` | In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "IPSI" the Document level allowance VAT rate (BT-96) shall be 0 (zero) or greater than zero. |
| `BR-AG-07` | EN16931 | fatal | `BG-21`, `BT-102`, `BT-103` | In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "IPSI" the Document level charge VAT rate (BT-103) shall be 0 (zero) or greater than zero. |
| `BR-AG-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-96`, `BT-99`, `BT-102`, `BT-103`, `BT-116`, `BT-118`, `BT-119`, `BT-131`, `BT-151`, `BT-152` | For each different value of VAT category rate (BT-119) where the VAT category code (BT-118) is "IPSI", the VAT category taxable amount (BT-116) in a VAT breakdown (BG-23) shall equal the sum of Invoice line net amounts (BT-131) plus the sum of document level charge amounts (BT-99) minus the sum of document level allowance amounts (BT-92) where the VAT category code (BT-151, BT-102, BT-95) is "IPSI" and the VAT rate (BT-152, BT-103, BT-96) equals the VAT category rate (BT-119). |
| `BR-AG-09` | EN16931 | fatal | `BG-23`, `BT-116`, `BT-117`, `BT-118`, `BT-119` | The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where VAT category code (BT-118) is "IPSI" shall equal the VAT category taxable amount (BT-116) multiplied by the VAT category rate (BT-119). |
| `BR-AG-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with VAT Category code (BT-118) "IPSI" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120).<br>UBL: A VAT breakdown (BG-23) with VAT Category code (BT-118) "IPSI" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120). |
| `BR-B-01` | EN16931 | fatal | `BT-95`, `BT-102`, `BT-151` | An Invoice where the VAT category code (BT-151, BT-95 or BT-102) is “Split payment” shall be a domestic Italian invoice. |
| `BR-B-02` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-25`, `BT-95`, `BT-102`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is “Split payment" shall not contain an invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is “Standard rated”. |
| `BR-CL-01` | EN16931 | fatal | `BT-3` | The document type code MUST be coded by the invoice and credit note related code lists of UNTDID 1001. |
| `BR-CL-03` | EN16931 | fatal | `BT-92`, `BT-93`, `BT-99`, `BT-100`, `BT-106`, `BT-107`, `BT-108`, `BT-109`, `BT-110`, `BT-111`, `BT-112`, `BT-113`, `BT-114`, `BT-115`, `BT-116`, `BT-131`, `BT-136`, `BT-137`, `BT-141`, `BT-142`, `BT-146`, `BT-148` | currencyID MUST be coded using ISO code list 4217 alpha-3 |
| `BR-CL-04` | EN16931 | fatal | `BT-5` | Invoice currency code MUST be coded using ISO code list 4217 alpha-3 |
| `BR-CL-05` | EN16931 | fatal | `BT-6` | Tax currency code MUST be coded using ISO code list 4217 alpha-3 |
| `BR-CL-06` | EN16931 | fatal | `BT-8` | CII: Value added tax point date code MUST be coded using a restriction of UNTDID 2475.<br>UBL: Value added tax point date code MUST be coded using a restriction of UNTDID 2005. |
| `BR-CL-07` | EN16931 | fatal |  | Object identifier identification scheme identifier MUST be coded using a restriction of UNTDID 1153. |
| `BR-CL-08` | EN16931 | fatal | `BT-22` | CII: Subject Code MUST be coded using a restriction of UNTDID 4451.<br>UBL: Invoiced note subject code shall be coded using UNCL4451 |
| `BR-CL-10` | EN16931 | fatal |  | Any identifier identification scheme identifier MUST be coded using one of the ISO 6523 ICD list. |
| `BR-CL-11` | EN16931 | fatal | `BT-30`, `BT-47`, `BT-61` | Any registration identifier identification scheme identifier MUST be coded using one of the ISO 6523 ICD list. |
| `BR-CL-13` | EN16931 | fatal |  | Item classification identifier identification scheme identifier MUST be coded using one of the UNTDID 7143 list. |
| `BR-CL-14` | EN16931 | fatal | `BT-40`, `BT-55`, `BT-69`, `BT-80` | Country codes in an invoice MUST be coded using ISO code list 3166-1 |
| `BR-CL-15` | EN16931 | fatal | `BT-159` | Country codes in an invoice MUST be coded using ISO code list 3166-1 |
| `BR-CL-16` | EN16931 | fatal | `BT-81` | CII: Payment means in an invoice MUST be coded using UNTDID 4461 code list<br>UBL: Payment means in an invoice MUST be coded using UNCL4461 code list |
| `BR-CL-17` | EN16931 | fatal | `BT-95`, `BT-102`, `BT-118` | CII: Invoice tax categories MUST be coded using UNCL 5305 code list<br>UBL: Invoice tax categories MUST be coded using UNCL5305 code list |
| `BR-CL-18` | EN16931 | fatal | `BT-151` | CII: Invoice tax categories MUST be coded using UNCL 5305 code list<br>UBL: Invoice tax categories MUST be coded using UNCL5305 code list |
| `BR-CL-19` | EN16931 | fatal | `BT-98`, `BT-105`, `BT-140`, `BT-145` | Coded allowance reasons MUST belong to the UNCL 5189 code list |
| `BR-CL-20` | EN16931 | fatal | `BT-98`, `BT-105`, `BT-140`, `BT-145` | Coded charge reasons MUST belong to the UNCL 7161 code list |
| `BR-CL-21` | EN16931 | fatal | `BT-157` | Item standard identifier scheme identifier MUST belong to the ISO 6523 ICD code list |
| `BR-CL-22` | EN16931 | fatal | `BT-121` | Tax exemption reason code identifier scheme identifier MUST belong to the CEF VATEX code list |
| `BR-CL-23` | EN16931 | fatal | `BT-129`, `BT-149` | Unit code MUST be coded according to the UN/ECE Recommendation 20 with Rec 21 extension |
| `BR-CL-24` | EN16931 | fatal |  | For Mime code in attribute use MIMEMediaType. |
| `BR-CL-25` | EN16931 | fatal | `BT-34`, `BT-49` | Endpoint identifier scheme identifier MUST belong to the CEF EAS code list |
| `BR-CL-26` | EN16931 | fatal |  | Delivery location identifier scheme identifier MUST belong to the ISO 6523 ICD code list |
| `BR-CO-03` | EN16931 | fatal | `BT-7`, `BT-8` | Value added tax point date (BT-7) and Value added tax point date code (BT-8) are mutually exclusive. |
| `BR-CO-04` | EN16931 | fatal | `BG-25`, `BT-151` | Each Invoice line (BG-25) shall be categorized with an Invoiced item VAT category code (BT-151). |
| `BR-CO-05` | EN16931 | fatal | `BT-97`, `BT-98`, `BT-104`, `BT-105` | Document level allowance reason code (BT-98) and Document level allowance reason (BT-97) shall indicate the same type of allowance. |
| `BR-CO-06` | EN16931 | fatal | `BT-97`, `BT-98`, `BT-104`, `BT-105` | Document level charge reason code (BT-105) and Document level charge reason (BT-104) shall indicate the same type of charge. |
| `BR-CO-07` | EN16931 | fatal | `BT-139`, `BT-140`, `BT-144`, `BT-145` | Invoice line allowance reason code (BT-140) and Invoice line allowance reason (BT-139) shall indicate the same type of allowance reason. |
| `BR-CO-08` | EN16931 | fatal | `BT-139`, `BT-140`, `BT-144`, `BT-145` | Invoice line charge reason code (BT-145) and Invoice line charge reason (BT-144) shall indicate the same type of charge reason. |
| `BR-CO-09` | EN16931 | fatal | `BT-31`, `BT-32`, `BT-48`, `BT-63` | The Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48) shall have a prefix in accordance with ISO code ISO 3166-1 alpha-2 by which the country of issue may be identified. Nevertheless, Greece may use the prefix ‘EL’. |
| `BR-CO-10` | EN16931 | fatal | `BT-106`, `BT-131` | Sum of Invoice line net amount (BT-106) = Σ Invoice line net amount (BT-131). |
| `BR-CO-11` | EN16931 | fatal | `BT-92`, `BT-107` | Sum of allowances on document level (BT-107) = Σ Document level allowance amount (BT-92). |
| `BR-CO-12` | EN16931 | fatal | `BT-99`, `BT-108` | Sum of charges on document level (BT-108) = Σ Document level charge amount (BT-99). |
| `BR-CO-13` | EN16931 | fatal | `BT-107`, `BT-108`, `BT-109`, `BT-131` | Invoice total amount without VAT (BT-109) = Σ Invoice line net amount (BT-131) - Sum of allowances on document level (BT-107) + Sum of charges on document level (BT-108). |
| `BR-CO-14` | EN16931 | fatal | `BT-110`, `BT-111`, `BT-117` | Invoice total VAT amount (BT-110) = Σ VAT category tax amount (BT-117). |
| `BR-CO-15` | EN16931 | fatal | `BT-109`, `BT-110`, `BT-112` | Invoice total amount with VAT (BT-112) = Invoice total amount without VAT (BT-109) + Invoice total VAT amount (BT-110). |
| `BR-CO-16` | EN16931 | fatal | `BT-112`, `BT-113`, `BT-114`, `BT-115` | Amount due for payment (BT-115) = Invoice total amount with VAT (BT-112) -Paid amount (BT-113) +Rounding amount (BT-114). |
| `BR-CO-17` | EN16931 | fatal | `BT-116`, `BT-117`, `BT-119` | VAT category tax amount (BT-117) = VAT category taxable amount (BT-116) x (VAT category rate (BT-119) / 100), rounded to two decimals. |
| `BR-CO-18` | EN16931 | fatal | `BG-23` | An Invoice shall at least have one VAT breakdown group (BG-23). |
| `BR-CO-19` | EN16931 | fatal | `BG-14`, `BT-73`, `BT-74` | If Invoicing period (BG-14) is used, the Invoicing period start date (BT-73) or the Invoicing period end date (BT-74) shall be filled, or both. |
| `BR-CO-20` | EN16931 | fatal | `BG-26`, `BT-134`, `BT-135` | If Invoice line period (BG-26) is used, the Invoice line period start date (BT-134) or the Invoice line period end date (BT-135) shall be filled, or both. |
| `BR-CO-21` | EN16931 | fatal | `BG-20`, `BT-97`, `BT-98`, `BT-104`, `BT-105` | Each Document level allowance (BG-20) shall contain a Document level allowance reason (BT-97) or a Document level allowance reason code (BT-98), or both. |
| `BR-CO-22` | EN16931 | fatal | `BG-21`, `BT-97`, `BT-98`, `BT-104`, `BT-105` | Each Document level charge (BG-21) shall contain a Document level charge reason (BT-104) or a Document level charge reason code (BT-105), or both. |
| `BR-CO-23` | EN16931 | fatal | `BG-27`, `BG-28`, `BT-139`, `BT-140` | Each Invoice line allowance (BG-27) shall contain an Invoice line allowance reason (BT-139) or an Invoice line allowance reason code (BT-140), or both. |
| `BR-CO-24` | EN16931 | fatal | `BG-27`, `BG-28`, `BT-144`, `BT-145` | Each Invoice line charge (BG-28) shall contain an Invoice line charge reason (BT-144) or an Invoice line charge reason code (BT-145), or both. |
| `BR-CO-25` | EN16931 | fatal | `BT-9`, `BT-20`, `BT-115` | In case the Amount due for payment (BT-115) is positive, either the Payment due date (BT-9) or the Payment terms (BT-20) shall be present. |
| `BR-CO-26` | EN16931 | fatal | `BT-29`, `BT-30`, `BT-31`, `BT-32`, `BT-90` | In order for the buyer to automatically identify a supplier, the Seller identifier (BT-29), the Seller legal registration identifier (BT-30) and/or the Seller VAT identifier (BT-31) shall be present. |
| `BR-CO-27` | EN16931 | fatal | `BT-84` | Either the IBAN or a Proprietary ID (BT-84) shall be used. |
| `BR-DEC-01` | EN16931 | fatal | `BT-92`, `BT-99` | The allowed maximum number of decimals for the Document level allowance amount (BT-92) is 2. |
| `BR-DEC-02` | EN16931 | fatal | `BT-93`, `BT-100` | The allowed maximum number of decimals for the Document level allowance base amount (BT-93) is 2. |
| `BR-DEC-05` | EN16931 | fatal | `BT-92`, `BT-99` | The allowed maximum number of decimals for the Document level charge amount (BT-99) is 2. |
| `BR-DEC-06` | EN16931 | fatal | `BT-93`, `BT-100` | The allowed maximum number of decimals for the Document level charge base amount (BT-100) is 2. |
| `BR-DEC-09` | EN16931 | fatal | `BT-106` | The allowed maximum number of decimals for the Sum of Invoice line net amount (BT-106) is 2. |
| `BR-DEC-10` | EN16931 | fatal | `BT-107` | The allowed maximum number of decimals for the Sum of allowanced on document level (BT-107) is 2. |
| `BR-DEC-11` | EN16931 | fatal | `BT-108` | The allowed maximum number of decimals for the Sum of charges on document level (BT-108) is 2. |
| `BR-DEC-12` | EN16931 | fatal | `BT-109` | The allowed maximum number of decimals for the Invoice total amount without VAT (BT-109) is 2. |
| `BR-DEC-13` | EN16931 | fatal | `BT-110`, `BT-111` | The allowed maximum number of decimals for the Invoice total VAT amount (BT-110) is 2. |
| `BR-DEC-14` | EN16931 | fatal | `BT-112` | The allowed maximum number of decimals for the Invoice total amount with VAT (BT-112) is 2. |
| `BR-DEC-15` | EN16931 | fatal | `BT-110`, `BT-111` | The allowed maximum number of decimals for the Invoice total VAT amount in accounting currency (BT-111) is 2. |
| `BR-DEC-16` | EN16931 | fatal | `BT-113` | The allowed maximum number of decimals for the Paid amount (BT-113) is 2. |
| `BR-DEC-17` | EN16931 | fatal | `BT-114` | The allowed maximum number of decimals for the Rounding amount (BT-114) is 2. |
| `BR-DEC-18` | EN16931 | fatal | `BT-115` | The allowed maximum number of decimals for the Amount due for payment (BT-115) is 2. |
| `BR-DEC-19` | EN16931 | fatal | `BT-116` | The allowed maximum number of decimals for the VAT category taxable amount (BT-116) is 2. |
| `BR-DEC-20` | EN16931 | fatal | `BT-117` | The allowed maximum number of decimals for the VAT category tax amount (BT-117) is 2. |
| `BR-DEC-23` | EN16931 | fatal | `BT-131` | The allowed maximum number of decimals for the Invoice line net amount (BT-131) is 2. |
| `BR-DEC-24` | EN16931 | fatal | `BT-136`, `BT-141` | The allowed maximum number of decimals for the Invoice line allowance amount (BT-136) is 2. |
| `BR-DEC-25` | EN16931 | fatal | `BT-137`, `BT-142` | The allowed maximum number of decimals for the Invoice line allowance base amount (BT-137) is 2. |
| `BR-DEC-27` | EN16931 | fatal | `BT-136`, `BT-141` | The allowed maximum number of decimals for the Invoice line charge amount (BT-141) is 2. |
| `BR-DEC-28` | EN16931 | fatal | `BT-137`, `BT-142` | The allowed maximum number of decimals for the Invoice line charge base amount (BT-142) is 2. |
| `BR-E-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Exempt from VAT" shall contain exactly one VAT breakdown (BG-23) with the VAT category code (BT-118) equal to "Exempt from VAT". |
| `BR-E-02` | EN16931 | fatal | `BG-25`, `BT-31`, `BT-32`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Exempt from VAT" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-E-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Exempt from VAT" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-E-04` | EN16931 | fatal | `BG-21`, `BT-31`, `BT-32`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Exempt from VAT" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-E-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Exempt from VAT", the Invoiced item VAT rate (BT-152) shall be 0 (zero). |
| `BR-E-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96`, `BT-103` | In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Exempt from VAT", the Document level allowance VAT rate (BT-96) shall be 0 (zero). |
| `BR-E-07` | EN16931 | fatal | `BG-21`, `BT-96`, `BT-102`, `BT-103` | In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Exempt from VAT", the Document level charge VAT rate (BT-103) shall be 0 (zero). |
| `BR-E-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-99`, `BT-102`, `BT-116`, `BT-118`, `BT-131`, `BT-151` | In a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Exempt from VAT" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amounts (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Exempt from VAT". |
| `BR-E-09` | EN16931 | fatal | `BG-23`, `BT-117`, `BT-118` | The VAT category tax amount (BT-117) In a VAT breakdown (BG-23) where the VAT category code (BT-118) equals "Exempt from VAT" shall equal 0 (zero). |
| `BR-E-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Exempt from VAT" shall have a VAT exemption reason code (BT-121) or a VAT exemption reason text (BT-120).<br>UBL: A VAT breakdown (BG-23) with VAT Category code (BT-118) "Exempt from VAT" shall have a VAT exemption reason code (BT-121) or a VAT exemption reason text (BT-120). |
| `BR-G-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Export outside the EU" shall contain in the VAT breakdown (BG-23) exactly one VAT category code (BT-118) equal with "Export outside the EU". |
| `BR-G-02` | EN16931 | fatal | `BG-25`, `BT-31`, `BT-32`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Export outside the EU" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63). |
| `BR-G-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Export outside the EU" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63). |
| `BR-G-04` | EN16931 | fatal | `BG-21`, `BT-31`, `BT-32`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Export outside the EU" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63). |
| `BR-G-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Export outside the EU" the Invoiced item VAT rate (BT-152) shall be 0 (zero). |
| `BR-G-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96`, `BT-103` | In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Export outside the EU" the Document level allowance VAT rate (BT-96) shall be 0 (zero). |
| `BR-G-07` | EN16931 | fatal | `BG-21`, `BT-96`, `BT-102`, `BT-103` | In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Export outside the EU" the Document level charge VAT rate (BT-103) shall be 0 (zero). |
| `BR-G-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-99`, `BT-102`, `BT-116`, `BT-118`, `BT-131`, `BT-151` | In a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Export outside the EU" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amounts (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Export outside the EU". |
| `BR-G-09` | EN16931 | fatal | `BG-23`, `BT-117`, `BT-118` | The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Export outside the EU" shall be 0 (zero). |
| `BR-G-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with the VAT Category code (BT-118) "Export outside the EU" shall have a VAT exemption reason code (BT-121), meaning "Export outside the EU" or the VAT exemption reason text (BT-120) "Export outside the EU" (or the equivalent standard text in another language).<br>UBL: A VAT breakdown (BG-23) with the VAT Category code (BT-118) "Export outside the EU" shall have a VAT exemption reason code (BT-121), meaning "Export outside the EU" or the VAT exemption reason text (BT-120) "Export outside the EU" (or the equivalent standard text in another language). |
| `BR-IC-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Intra-community supply" shall contain in the VAT breakdown (BG-23) exactly one VAT category code (BT-118) equal with "Intra-community supply". |
| `BR-IC-02` | EN16931 | fatal | `BG-25`, `BT-31`, `BT-32`, `BT-48`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Intra-community supply" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48). |
| `BR-IC-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-48`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Intra-community supply" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48). |
| `BR-IC-04` | EN16931 | fatal | `BG-21`, `BT-31`, `BT-32`, `BT-48`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Intra-community supply" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48). |
| `BR-IC-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Intracommunity supply" the Invoiced item VAT rate (BT-152) shall be 0 (zero). |
| `BR-IC-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96`, `BT-103` | In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Intra-community supply" the Document level allowance VAT rate (BT-96) shall be 0 (zero). |
| `BR-IC-07` | EN16931 | fatal | `BG-21`, `BT-96`, `BT-102`, `BT-103` | In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Intra-community supply" the Document level charge VAT rate (BT-103) shall be 0 (zero). |
| `BR-IC-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-99`, `BT-102`, `BT-116`, `BT-118`, `BT-131`, `BT-151` | In a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amounts (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Intra-community supply". |
| `BR-IC-09` | EN16931 | fatal | `BG-23`, `BT-117`, `BT-118` | The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" shall be 0 (zero). |
| `BR-IC-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with the VAT Category code (BT-118) "Intra-community supply" shall have a VAT exemption reason code (BT-121), meaning "Intra-community supply" or the VAT exemption reason text (BT-120) "Intra-community supply" (or the equivalent standard text in another language).<br>UBL: A VAT breakdown (BG-23) with the VAT Category code (BT-118) "Intra-community supply" shall have a VAT exemption reason code (BT-121), meaning "Intra-community supply" or the VAT exemption reason text (BT-120) "Intra-community supply" (or the equivalent standard text in another language). |
| `BR-IC-11` | EN16931 | fatal | `BG-14`, `BG-23`, `BT-72`, `BT-118` | In an Invoice with a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" the Actual delivery date (BT-72) or the Invoicing period (BG-14) shall not be blank. |
| `BR-IC-12` | EN16931 | fatal | `BG-23`, `BT-80`, `BT-118` | In an Invoice with a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" the Deliver to country code (BT-80) shall not be blank. |
| `BR-O-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Not subject to VAT" shall contain exactly one VAT breakdown group (BG-23) with the VAT category code (BT-118) equal to "Not subject to VAT". |
| `BR-O-02` | EN16931 | fatal | `BG-25`, `BT-31`, `BT-32`, `BT-48`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Not subject to VAT" shall not contain the Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) or the Buyer VAT identifier (BT-48). |
| `BR-O-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-48`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Not subject to VAT" shall not contain the Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) or the Buyer VAT identifier (BT-48). |
| `BR-O-04` | EN16931 | fatal | `BG-21`, `BT-31`, `BT-32`, `BT-48`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Not subject to VAT" shall not contain the Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) or the Buyer VAT identifier (BT-48). |
| `BR-O-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | An Invoice line (BG-25) where the VAT category code (BT-151) is "Not subject to VAT" shall not contain an Invoiced item VAT rate (BT-152). |
| `BR-O-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96`, `BT-103` | A Document level allowance (BG-20) where VAT category code (BT-95) is "Not subject to VAT" shall not contain a Document level allowance VAT rate (BT-96). |
| `BR-O-07` | EN16931 | fatal | `BG-21`, `BT-96`, `BT-102`, `BT-103` | A Document level charge (BG-21) where the VAT category code (BT-102) is "Not subject to VAT" shall not contain a Document level charge VAT rate (BT-103). |
| `BR-O-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-99`, `BT-102`, `BT-116`, `BT-118`, `BT-131`, `BT-151` | In a VAT breakdown (BG-23) where the VAT category code (BT-118) is " Not subject to VAT" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amounts (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Not subject to VAT". |
| `BR-O-09` | EN16931 | fatal | `BG-23`, `BT-117`, `BT-118` | The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Not subject to VAT" shall be 0 (zero). |
| `BR-O-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with VAT Category code (BT-118) " Not subject to VAT" shall have a VAT exemption reason code (BT-121), meaning " Not subject to VAT" or a VAT exemption reason text (BT-120) " Not subject to VAT" (or the equivalent standard text in another language).<br>UBL: A VAT breakdown (BG-23) with VAT Category code (BT-118) " Not subject to VAT" shall have a VAT exemption reason code (BT-121), meaning " Not subject to VAT" or a VAT exemption reason text (BT-120) " Not subject to VAT" (or the equivalent standard text in another language). |
| `BR-O-11` | EN16931 | fatal | `BG-23`, `BT-118` | An Invoice that contains a VAT breakdown group (BG-23) with a VAT category code (BT-118) "Not subject to VAT" shall not contain other VAT breakdown groups (BG-23). |
| `BR-O-12` | EN16931 | fatal | `BG-23`, `BG-25`, `BT-118`, `BT-151` | An Invoice that contains a VAT breakdown group (BG-23) with a VAT category code (BT-118) "Not subject to VAT" shall not contain an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is not "Not subject to VAT". |
| `BR-O-13` | EN16931 | fatal | `BG-20`, `BG-23`, `BT-95`, `BT-102`, `BT-118` | An Invoice that contains a VAT breakdown group (BG-23) with a VAT category code (BT-118) "Not subject to VAT" shall not contain Document level allowances (BG-20) where Document level allowance VAT category code (BT-95) is not "Not subject to VAT". |
| `BR-O-14` | EN16931 | fatal | `BG-21`, `BG-23`, `BT-95`, `BT-102`, `BT-118` | An Invoice that contains a VAT breakdown group (BG-23) with a VAT category code (BT-118) "Not subject to VAT" shall not contain Document level charges (BG-21) where Document level charge VAT category code (BT-102) is not "Not subject to VAT". |
| `BR-S-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Standard rated" shall contain in the VAT breakdown (BG-23) at least one VAT category code (BT-118) equal with "Standard rated". |
| `BR-S-02` | EN16931 | fatal | `BG-25`, `BT-31`, `BT-32`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Standard rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-S-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Standard rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-S-04` | EN16931 | fatal | `BG-21`, `BT-31`, `BT-32`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Standard rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-S-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Standard rated" the Invoiced item VAT rate (BT-152) shall be greater than zero. |
| `BR-S-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96`, `BT-103` | In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Standard rated" the Document level allowance VAT rate (BT-96) shall be greater than zero. |
| `BR-S-07` | EN16931 | fatal | `BG-21`, `BT-96`, `BT-102`, `BT-103` | In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Standard rated" the Document level charge VAT rate (BT-103) shall be greater than zero. |
| `BR-S-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-96`, `BT-99`, `BT-102`, `BT-103`, `BT-116`, `BT-118`, `BT-119`, `BT-131`, `BT-151`, `BT-152` | For each different value of VAT category rate (BT-119) where the VAT category code (BT-118) is "Standard rated", the VAT category taxable amount (BT-116) in a VAT breakdown (BG-23) shall equal the sum of Invoice line net amounts (BT-131) plus the sum of document level charge amounts (BT-99) minus the sum of document level allowance amounts (BT-92) where the VAT category code (BT-151, BT-102, BT-95) is "Standard rated" and the VAT rate (BT-152, BT-103, BT-96) equals the VAT category rate (BT-119). |
| `BR-S-09` | EN16931 | fatal | `BG-23`, `BT-116`, `BT-117`, `BT-118`, `BT-119` | The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where VAT category code (BT-118) is "Standard rated" shall equal the VAT category taxable amount (BT-116) multiplied by the VAT category rate (BT-119). |
| `BR-S-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Standard rate" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120).<br>UBL: A VAT breakdown (BG-23) with VAT Category code (BT-118) "Standard rate" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120). |
| `BR-Z-01` | EN16931 | fatal | `BG-20`, `BG-21`, `BG-23`, `BG-25`, `BT-95`, `BT-102`, `BT-118`, `BT-151` | An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Zero rated" shall contain in the VAT breakdown (BG-23) exactly one VAT category code (BT-118) equal with "Zero rated". |
| `BR-Z-02` | EN16931 | fatal | `BT-31`, `BT-32`, `BT-63`, `BT-151` | An Invoice that contains an Invoice line where the Invoiced item VAT category code (BT-151) is "Zero rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-Z-03` | EN16931 | fatal | `BG-20`, `BT-31`, `BT-32`, `BT-63`, `BT-95` | An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Zero rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-Z-04` | EN16931 | fatal | `BT-31`, `BT-32`, `BT-63`, `BT-102` | An Invoice that contains a Document level charge where the Document level charge VAT category code (BT-102) is "Zero rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63). |
| `BR-Z-05` | EN16931 | fatal | `BG-25`, `BT-151`, `BT-152` | In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Zero rated" the Invoiced item VAT rate (BT-152) shall be 0 (zero). |
| `BR-Z-06` | EN16931 | fatal | `BG-20`, `BT-95`, `BT-96`, `BT-103` | In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Zero rated" the Document level allowance VAT rate (BT-96) shall be 0 (zero). |
| `BR-Z-07` | EN16931 | fatal | `BG-21`, `BT-96`, `BT-102`, `BT-103` | In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Zero rated" the Document level charge VAT rate (BT-103) shall be 0 (zero). |
| `BR-Z-08` | EN16931 | fatal | `BG-23`, `BT-92`, `BT-95`, `BT-99`, `BT-102`, `BT-116`, `BT-118`, `BT-131`, `BT-151` | In a VAT breakdown (BG-23) where VAT category code (BT-118) is "Zero rated" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amount (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Zero rated". |
| `BR-Z-09` | EN16931 | fatal | `BG-23`, `BT-117`, `BT-118` | The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where VAT category code (BT-118) is "Zero rated" shall equal 0 (zero). |
| `BR-Z-10` | EN16931 | fatal | `BG-23`, `BT-118`, `BT-120`, `BT-121` | CII: A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Zero rated" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120).<br>UBL: A VAT breakdown (BG-23) with VAT Category code (BT-118) "Zero rated" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120). |
| `CII-DT-001` | EN16931 | fatal |  | schemeName should not be present |
| `CII-DT-002` | EN16931 | fatal |  | schemeAgencyName should not be present |
| `CII-DT-003` | EN16931 | fatal |  | schemeDataURI should not be present |
| `CII-DT-004` | EN16931 | fatal |  | schemeURI should not be present |
| `CII-DT-005` | EN16931 | fatal |  | schemeID should not be present |
| `CII-DT-006` | EN16931 | fatal |  | schemeAgencyID should not be present |
| `CII-DT-007` | EN16931 | fatal |  | schemeVersionID should not be present |
| `CII-DT-008` | EN16931 | fatal |  | name should not be present |
| `CII-DT-009` | EN16931 | fatal |  | listURI should not be present |
| `CII-DT-010` | EN16931 | fatal |  | listID should not be present |
| `CII-DT-011` | EN16931 | fatal |  | listAgencyID should not be present |
| `CII-DT-012` | EN16931 | fatal |  | listVersionID should not be present |
| `CII-DT-013` | EN16931 | fatal |  | languageID should not be present |
| `CII-DT-014` | EN16931 | fatal |  | languageLocaleID should not be present |
| `CII-DT-015` | EN16931 | fatal |  | URIID should not be present |
| `CII-DT-016` | EN16931 | fatal |  | StatusCode should not be present |
| `CII-DT-017` | EN16931 | fatal |  | CopyIndicator should not be present |
| `CII-DT-018` | EN16931 | fatal |  | TypeCode should not be present |
| `CII-DT-019` | EN16931 | fatal |  | GlobalID should not be present |
| `CII-DT-020` | EN16931 | fatal |  | RevisionID should not be present |
| `CII-DT-021` | EN16931 | fatal |  | Name should not be present |
| `CII-DT-022` | EN16931 | fatal |  | AttachmentBinaryObject should not be present |
| `CII-DT-023` | EN16931 | fatal |  | Information should not be present |
| `CII-DT-024` | EN16931 | fatal |  | ReferenceTypeCode should not be present |
| `CII-DT-025` | EN16931 | fatal |  | SectionName should not be present |
| `CII-DT-026` | EN16931 | fatal |  | PreviousRevisionID should not be present |
| `CII-DT-027` | EN16931 | fatal |  | FormattedIssueDateTime should not be present |
| `CII-DT-028` | EN16931 | fatal |  | EffectiveSpecifiedPeriod should not be present |
| `CII-DT-029` | EN16931 | fatal |  | IssuerTradeParty should not be present |
| `CII-DT-030` | EN16931 | fatal |  | AttachedSpecifiedBinaryFile should not be present |
| `CII-DT-031` | EN16931 | fatal |  | currencyID should not be present |
| `CII-DT-032` | EN16931 | fatal |  | currencyCodeListVersionID should not be present |
| `CII-DT-033` | EN16931 | fatal |  | unitCode should not be present |
| `CII-DT-034` | EN16931 | fatal |  | unitCodeListID should not be present |
| `CII-DT-035` | EN16931 | fatal |  | unitCodeListAgencyID should not be present |
| `CII-DT-036` | EN16931 | fatal |  | unitCodeListAgencyName should not be present |
| `CII-DT-037` | EN16931 | fatal |  | TypeCode shall be 'VAT' |
| `CII-DT-038` | EN16931 | warning |  | CalculatedRate should not be present |
| `CII-DT-039` | EN16931 | warning |  | CalculationSequenceNumeric should not be present |
| `CII-DT-040` | EN16931 | warning |  | BasisQuantity should not be present |
| `CII-DT-041` | EN16931 | warning |  | BasisAmount should not be present |
| `CII-DT-042` | EN16931 | warning |  | UnitBasisAmount should not be present |
| `CII-DT-043` | EN16931 | warning |  | LineTotalBasisAmount should not be present |
| `CII-DT-044` | EN16931 | warning |  | AllowanceChargeBasisAmount should not be present |
| `CII-DT-045` | EN16931 | warning |  | @listID should not be present |
| `CII-DT-046` | EN16931 | warning |  | @listAgencyID should not be present |
| `CII-DT-047` | EN16931 | warning |  | @listVersionID should not be present |
| `CII-DT-048` | EN16931 | warning |  | @listURI should not be present |
| `CII-DT-049` | EN16931 | warning |  | CurrencyCode should not be present |
| `CII-DT-050` | EN16931 | warning |  | Jurisdiction should not be present |
| `CII-DT-051` | EN16931 | warning |  | CustomsDutyIndicator should not be present |
| `CII-DT-052` | EN16931 | warning |  | ExemptionReasonCode should not be present |
| `CII-DT-053` | EN16931 | warning |  | TaxBasisAllowanceRate should not be present |
| `CII-DT-054` | EN16931 | warning |  | TaxPointDate should not be present |
| `CII-DT-055` | EN16931 | warning |  | Type should not be present |
| `CII-DT-056` | EN16931 | warning |  | InformationAmount should not be present |
| `CII-DT-057` | EN16931 | warning |  | CategoryName should not be present |
| `CII-DT-058` | EN16931 | warning |  | DueDateTypeCode should not be present |
| `CII-DT-059` | EN16931 | warning |  | @format should not be present |
| `CII-DT-060` | EN16931 | warning |  | SpecifiedTradeAccountingAccount should not be present |
| `CII-DT-061` | EN16931 | warning |  | ServiceSupplyTradeCountry should not be present |
| `CII-DT-062` | EN16931 | warning |  | BuyerRepayableTaxSpecifiedTradeAccountingAccount should not be present |
| `CII-DT-063` | EN16931 | warning |  | SellerPayableTaxSpecifiedTradeAccountingAccount should not be present |
| `CII-DT-064` | EN16931 | warning |  | SellerRefundableTaxSpecifiedTradeAccountingAccount should not be present |
| `CII-DT-065` | EN16931 | warning |  | BuyerDeductibleTaxSpecifiedTradeAccountingAccount should not be present |
| `CII-DT-066` | EN16931 | warning |  | BuyerNonDeductibleTaxSpecifiedTradeAccountingAccount should not be present |
| `CII-DT-067` | EN16931 | warning |  | PlaceApplicableTradeLocation should not be present |
| `CII-DT-068` | EN16931 | fatal |  | DateTime shall not be used. |
| `CII-DT-069` | EN16931 | fatal |  | DurationMeasure shall not be used. |
| `CII-DT-070` | EN16931 | fatal |  | InclusiveIndicator shall not be used. |
| `CII-DT-071` | EN16931 | fatal |  | Description shall not be used. |
| `CII-DT-072` | EN16931 | fatal |  | DateTime shall not be used. |
| `CII-DT-073` | EN16931 | fatal |  | CompleteDateTime shall not be used. |
| `CII-DT-074` | EN16931 | fatal |  | OpenIndicator shall not be used. |
| `CII-DT-075` | EN16931 | fatal |  | SeasonCode shall not be used. |
| `CII-DT-076` | EN16931 | fatal |  | ID shall not be used. |
| `CII-DT-077` | EN16931 | fatal |  | Name shall not be used. |
| `CII-DT-078` | EN16931 | fatal |  | SequenceNumeric shall not be used. |
| `CII-DT-079` | EN16931 | fatal |  | StartDateFlexibilityCode shall not be used. |
| `CII-DT-080` | EN16931 | fatal |  | ContinuousIndicator shall not be used. |
| `CII-DT-081` | EN16931 | fatal |  | PurposeCode shall not be used. |
| `CII-DT-082` | EN16931 | fatal |  | ID shall not be used. |
| `CII-DT-083` | EN16931 | fatal |  | PostOfficeBox shall not be used. |
| `CII-DT-084` | EN16931 | fatal |  | BuildingName shall not be used. |
| `CII-DT-086` | EN16931 | fatal |  | LineFour shall not be used. |
| `CII-DT-087` | EN16931 | fatal |  | LineFive shall not be used. |
| `CII-DT-088` | EN16931 | fatal |  | StreetName shall not be used. |
| `CII-DT-089` | EN16931 | fatal |  | CitySubDivisionName shall not be used. |
| `CII-DT-090` | EN16931 | fatal |  | CountryName shall not be used. |
| `CII-DT-091` | EN16931 | fatal |  | CountrySubDivisionID shall not be used. |
| `CII-DT-092` | EN16931 | fatal |  | AttentionOf shall not be used. |
| `CII-DT-093` | EN16931 | fatal |  | CareOf shall not be used. |
| `CII-DT-094` | EN16931 | fatal |  | BuildingNumber shall not be used. |
| `CII-DT-095` | EN16931 | fatal |  | DepartmentName shall not be used. |
| `CII-DT-096` | EN16931 | fatal |  | AdditionalStreetName shall not be used. |
| `CII-DT-097` | EN16931 | fatal |  | Date time string with format attribute 102 shall be YYYYMMDD. |
| `CII-DT-098` | EN16931 | warning |  | ExemptionReason should not be present |
| `CII-DT-101` | EN16931 | fatal |  | schemeName should not be present |
| `CII-DT-102` | EN16931 | fatal |  | schemeAgencyName should not be present |
| `CII-DT-103` | EN16931 | fatal |  | schemeDataURI should not be present |
| `CII-DT-104` | EN16931 | fatal |  | schemeURI should not be present |
| `CII-SR-001` | EN16931 | warning |  | SpecifiedTransactionID should not be present |
| `CII-SR-002` | EN16931 | warning |  | TestIndicator should not be present |
| `CII-SR-003` | EN16931 | warning |  | BusinessProcessSpecifiedDocumentContextParameter should exist maximum once |
| `CII-SR-006` | EN16931 | warning |  | BIMSpecifiedDocumentContextParameter should not be present |
| `CII-SR-007` | EN16931 | warning |  | ScenarioSpecifiedDocumentContextParameter should not be present |
| `CII-SR-008` | EN16931 | warning |  | ApplicationSpecifiedDocumentContextParameter should not be present |
| `CII-SR-009` | EN16931 | fatal |  | GuidelineSpecifiedDocumentContextParameter must exist exactly once |
| `CII-SR-010` | EN16931 | fatal |  | ID must exist exactly once |
| `CII-SR-011` | EN16931 | warning |  | SubsetSpecifiedDocumentContextParameter should not be present |
| `CII-SR-012` | EN16931 | warning |  | MessageStandardSpecifiedDocumentContextParameter should not be present |
| `CII-SR-013` | EN16931 | warning |  | Name should not be present |
| `CII-SR-014` | EN16931 | fatal |  | TypeCode must exist exactly once |
| `CII-SR-015` | EN16931 | warning |  | DateTime should not be present |
| `CII-SR-016` | EN16931 | warning |  | CopyIndicator should not be present |
| `CII-SR-017` | EN16931 | warning |  | Purpose should not be present |
| `CII-SR-018` | EN16931 | warning |  | ControlRequirementIndicator should not be present |
| `CII-SR-019` | EN16931 | warning |  | LanguageID should not be present |
| `CII-SR-020` | EN16931 | warning |  | PurposeCode should not be present |
| `CII-SR-021` | EN16931 | warning |  | RevisionDateTime should not be present |
| `CII-SR-022` | EN16931 | warning |  | VersionID should not be present |
| `CII-SR-023` | EN16931 | warning |  | GlobalID should not be present |
| `CII-SR-024` | EN16931 | warning |  | RevisionID should not be present |
| `CII-SR-025` | EN16931 | warning |  | PreviousRevisionID should not be present |
| `CII-SR-026` | EN16931 | warning |  | CategoryCode should not be present |
| `CII-SR-027` | EN16931 | warning |  | Subject should not be present |
| `CII-SR-028` | EN16931 | warning |  | ContentCode should not be present |
| `CII-SR-030` | EN16931 | warning |  | Content should exist maximum once |
| `CII-SR-032` | EN16931 | warning |  | ID should not be present |
| `CII-SR-033` | EN16931 | warning |  | EffectiveSpecifiedPeriod should not be present |
| `CII-SR-034` | EN16931 | warning |  | IssuerTradeParty should not be present |
| `CII-SR-035` | EN16931 | warning |  | DescriptionCode should not be present |
| `CII-SR-036` | EN16931 | warning |  | ParentLineID should not be present |
| `CII-SR-037` | EN16931 | warning |  | LineStatusCode should not be present |
| `CII-SR-038` | EN16931 | warning |  | LineStatusReasonCode should not be present |
| `CII-SR-039` | EN16931 | warning |  | IncludedNote should exist maximum once |
| `CII-SR-04` | EN16931 | warning |  | [CII-SR-004] - Value should not be present |
| `CII-SR-040` | EN16931 | warning |  | Content should exist maximum once |
| `CII-SR-041` | EN16931 | warning |  | SubjectCode should not be present |
| `CII-SR-042` | EN16931 | warning |  | ID should not be present |
| `CII-SR-043` | EN16931 | warning |  | CategoryCode should not be present |
| `CII-SR-044` | EN16931 | warning |  | Subject should not be present |
| `CII-SR-045` | EN16931 | warning |  | ID should not be present |
| `CII-SR-046` | EN16931 | fatal |  | schemeID must be present if GlobalID is present |
| `CII-SR-048` | EN16931 | warning |  | ManufacturerAssignedID should not be present |
| `CII-SR-049` | EN16931 | warning |  | TradeName should not be present |
| `CII-SR-05` | EN16931 | warning |  | [CII-SR-005] - SpecifiedDocumentVersion should not be present |
| `CII-SR-050` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-051` | EN16931 | warning |  | NetWeightMeasure should not be present |
| `CII-SR-052` | EN16931 | warning |  | GrossWeightMeasure should not be present |
| `CII-SR-053` | EN16931 | warning |  | ProductGroupID should not be present |
| `CII-SR-054` | EN16931 | warning |  | EndItemTypeCode should not be present |
| `CII-SR-055` | EN16931 | warning |  | EndItemName should not be present |
| `CII-SR-056` | EN16931 | warning |  | AreaDensityMeasure should not be present |
| `CII-SR-057` | EN16931 | warning |  | UseDescription should not be present |
| `CII-SR-058` | EN16931 | warning |  | BrandName should not be present |
| `CII-SR-059` | EN16931 | warning |  | SubBrandName should not be present |
| `CII-SR-060` | EN16931 | warning |  | DrainedNetWeightMeasure should not be present |
| `CII-SR-061` | EN16931 | warning |  | VariableMeasureIndicator should not be present |
| `CII-SR-062` | EN16931 | warning |  | ColourCode should not be present |
| `CII-SR-063` | EN16931 | warning |  | ColourDescription should not be present |
| `CII-SR-064` | EN16931 | warning |  | Designation should not be present |
| `CII-SR-065` | EN16931 | warning |  | FormattedCancellationAnnouncedLaunchDateTime should not be present |
| `CII-SR-066` | EN16931 | warning |  | FormattedLatestProductDataChangeDateTime should not be present |
| `CII-SR-067` | EN16931 | warning |  | ID should not be present |
| `CII-SR-068` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-069` | EN16931 | fatal |  | Description should exist maximum once. |
| `CII-SR-070` | EN16931 | warning |  | ValueMeasure should not be present |
| `CII-SR-071` | EN16931 | warning |  | MeasurementMethodCode should not be present |
| `CII-SR-072` | EN16931 | fatal |  | Value should exist maximum once. |
| `CII-SR-073` | EN16931 | warning |  | ValueCode should not be present |
| `CII-SR-074` | EN16931 | warning |  | ValueDateTime should not be present |
| `CII-SR-075` | EN16931 | warning |  | ValueIndicator should not be present |
| `CII-SR-076` | EN16931 | warning |  | ContentTypeCode should not be present |
| `CII-SR-077` | EN16931 | warning |  | ValueSpecifiedBinaryFile should not be present |
| `CII-SR-078` | EN16931 | warning |  | ApplicableProductCharacteristicCondition should not be present |
| `CII-SR-079` | EN16931 | warning |  | ApplicableReferencedStandard should not be present |
| `CII-SR-080` | EN16931 | warning |  | ApplicableMaterialGoodsCharacteristic should not be present |
| `CII-SR-081` | EN16931 | warning |  | SystemID should not be present |
| `CII-SR-082` | EN16931 | warning |  | SystemName should not be present |
| `CII-SR-083` | EN16931 | warning |  | ClassName should not be present |
| `CII-SR-084` | EN16931 | warning |  | SubClassCode should not be present |
| `CII-SR-085` | EN16931 | warning |  | ClassProductCharacteristic should not be present |
| `CII-SR-086` | EN16931 | warning |  | ApplicableReferencedStandard should not be present |
| `CII-SR-087` | EN16931 | warning |  | IndividualTradeProductInstance should not be present |
| `CII-SR-088` | EN16931 | warning |  | CertificationEvidenceReferenceReferencedDocument should not be present |
| `CII-SR-089` | EN16931 | warning |  | InspectionReferenceReferencedDocument should not be present |
| `CII-SR-090` | EN16931 | fatal |  | ID should exist maximum once. |
| `CII-SR-091` | EN16931 | warning |  | Name should not be present |
| `CII-SR-092` | EN16931 | warning |  | SubordinateTradeCountrySubDivision should not be present |
| `CII-SR-093` | EN16931 | warning |  | LinearSpatialDimension should not be present |
| `CII-SR-094` | EN16931 | warning |  | MinimumLinearSpatialDimension should not be present |
| `CII-SR-095` | EN16931 | warning |  | MaximumLinearSpatialDimension should not be present |
| `CII-SR-096` | EN16931 | warning |  | ManufacturerTradeParty should not be present |
| `CII-SR-097` | EN16931 | warning |  | PresentationSpecifiedBinaryFile should not be present |
| `CII-SR-098` | EN16931 | warning |  | MSDSReferenceReferencedDocument should not be present |
| `CII-SR-099` | EN16931 | warning |  | AdditionalReferenceReferencedDocument should not be present |
| `CII-SR-100` | EN16931 | warning |  | LegalRightsOwnerTradeParty should not be present |
| `CII-SR-101` | EN16931 | warning |  | BrandOwnerTradeParty should not be present |
| `CII-SR-102` | EN16931 | warning |  | IncludedReferencedProduct should not be present |
| `CII-SR-103` | EN16931 | warning |  | InformationNoteshould not be present |
| `CII-SR-104` | EN16931 | warning |  | BuyerReference should not be present |
| `CII-SR-105` | EN16931 | warning |  | BuyerRequisitionerTradeParty should not be present |
| `CII-SR-106` | EN16931 | warning |  | ApplicableTradeDeliveryTerms should not be present |
| `CII-SR-107` | EN16931 | warning |  | SellerOrderReferencedDocument should not be present |
| `CII-SR-108` | EN16931 | warning |  | IssuerAssignedID should not be present |
| `CII-SR-109` | EN16931 | warning |  | QuotationReferencedDocument should not be present |
| `CII-SR-110` | EN16931 | warning |  | ContractReferencedDocument should not be present |
| `CII-SR-111` | EN16931 | warning |  | DemandForecastReferencedDocument should not be present |
| `CII-SR-112` | EN16931 | warning |  | PromotionalDealReferencedDocument should not be present |
| `CII-SR-113` | EN16931 | warning |  | AdditionalReferencedDocument should not be present |
| `CII-SR-114` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-115` | EN16931 | warning |  | MinimumQuantity should not be present |
| `CII-SR-116` | EN16931 | warning |  | MaximumQuantity should not be present |
| `CII-SR-117` | EN16931 | warning |  | ChangeReason should not be present |
| `CII-SR-118` | EN16931 | warning |  | OrderUnitConversionFactorNumeric should not be present |
| `CII-SR-119` | EN16931 | warning |  | Only allowances on price a price should be present |
| `CII-SR-120` | EN16931 | warning |  | ID should not be present |
| `CII-SR-121` | EN16931 | warning |  | SequenceNumeric should not be present |
| `CII-SR-122` | EN16931 | warning |  | CalculationPercent should not be present |
| `CII-SR-123` | EN16931 | warning |  | BasisAmount should not be present |
| `CII-SR-124` | EN16931 | warning |  | BasisQuantity should not be present |
| `CII-SR-125` | EN16931 | warning |  | PrepaidIndicator should not be present |
| `CII-SR-126` | EN16931 | warning |  | UnitBasisAmount should not be present |
| `CII-SR-127` | EN16931 | warning |  | ReasonCode should not be present |
| `CII-SR-128` | EN16931 | warning |  | Reason should not be present |
| `CII-SR-129` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-130` | EN16931 | warning |  | CategoryTradeTax should not be present |
| `CII-SR-131` | EN16931 | warning |  | ActualTradeCurrencyExchange should not be present |
| `CII-SR-132` | EN16931 | warning |  | ValiditySpecifiedPeriod should not be present |
| `CII-SR-133` | EN16931 | warning |  | DeliveryTradeLocation should not be present |
| `CII-SR-134` | EN16931 | warning |  | TradeComparisonReferencePrice should not be present |
| `CII-SR-135` | EN16931 | warning |  | AssociatedReferencedDocument should not be present |
| `CII-SR-136` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-138` | EN16931 | warning |  | MinimumQuantity should not be present |
| `CII-SR-139` | EN16931 | warning |  | MaximumQuantity should not be present |
| `CII-SR-140` | EN16931 | warning |  | ChangeReason should not be present |
| `CII-SR-141` | EN16931 | warning |  | OrderUnitConversionFactorNumeric should not be present |
| `CII-SR-142` | EN16931 | warning |  | AppliedTradeAllowanceCharge should not be present |
| `CII-SR-143` | EN16931 | warning |  | ValiditySpecifiedPeriod should not be present |
| `CII-SR-144` | EN16931 | warning |  | DeliveryTradeLocation should not be present |
| `CII-SR-145` | EN16931 | warning |  | TradeComparisonReferencePrice should not be present |
| `CII-SR-146` | EN16931 | warning |  | AssociatedReferencedDocument should not be present |
| `CII-SR-147` | EN16931 | warning |  | RequisitionerReferencedDocument should not be present |
| `CII-SR-148` | EN16931 | warning |  | ItemSellerTradeParty should not be present |
| `CII-SR-149` | EN16931 | warning |  | ItemBuyerTradeParty should not be present |
| `CII-SR-150` | EN16931 | warning |  | IncludedSpecifiedMarketplace should not be present |
| `CII-SR-151` | EN16931 | warning |  | RequestedQuantity should not be present |
| `CII-SR-152` | EN16931 | warning |  | ReceivedQuantity should not be present |
| `CII-SR-153` | EN16931 | warning |  | ChargeFreeQuantity should not be present |
| `CII-SR-154` | EN16931 | warning |  | PackageQuantity should not be present |
| `CII-SR-155` | EN16931 | warning |  | ProductUnitQuantity should not be present |
| `CII-SR-156` | EN16931 | warning |  | PerPackageUnitQuantity should not be present |
| `CII-SR-157` | EN16931 | warning |  | NetWeightMeasure should not be present |
| `CII-SR-158` | EN16931 | warning |  | GrossWeightMeasure should not be present |
| `CII-SR-159` | EN16931 | warning |  | TheoreticalWeightMeasure should not be present |
| `CII-SR-160` | EN16931 | warning |  | DespatchedQuantity should not be present |
| `CII-SR-161` | EN16931 | warning |  | SpecifiedDeliveryAdjustment should not be present |
| `CII-SR-162` | EN16931 | warning |  | IncludedSupplyChainPackaging should not be present |
| `CII-SR-163` | EN16931 | warning |  | RelatedSupplyChainConsignment should not be present |
| `CII-SR-164` | EN16931 | warning |  | ShipToTradeParty should not be present |
| `CII-SR-165` | EN16931 | warning |  | UltimateShipToTradeParty should not be present |
| `CII-SR-166` | EN16931 | warning |  | ShipFromTradeParty should not be present |
| `CII-SR-167` | EN16931 | warning |  | ActualDespatchSupplyChainEvent should not be present |
| `CII-SR-168` | EN16931 | warning |  | ActualPickUpSupplyChainEvent should not be present |
| `CII-SR-169` | EN16931 | warning |  | RequestedDeliverySupplyChainEvent should not be present |
| `CII-SR-170` | EN16931 | warning |  | ActualDeliverySupplyChainEvent should not be present |
| `CII-SR-171` | EN16931 | warning |  | ActualReceiptSupplyChainEvent should not be present |
| `CII-SR-172` | EN16931 | warning |  | AdditionalReferencedDocument should not be present |
| `CII-SR-173` | EN16931 | warning |  | DespatchAdviceReferencedDocument should not be present |
| `CII-SR-174` | EN16931 | warning |  | ReceivingAdviceReferencedDocument should not be present |
| `CII-SR-175` | EN16931 | warning |  | DeliveryNoteReferencedDocument should not be present |
| `CII-SR-176` | EN16931 | warning |  | ConsumptionReportReferencedDocument should not be present |
| `CII-SR-177` | EN16931 | warning |  | RequestedQuantity should not be present |
| `CII-SR-178` | EN16931 | warning |  | PaymentReference should not be present |
| `CII-SR-179` | EN16931 | warning |  | InvoiceIssuerReference should not be present |
| `CII-SR-180` | EN16931 | warning |  | TotalAdjustmentAmount should not be present |
| `CII-SR-181` | EN16931 | warning |  | DiscountIndicator should not be present |
| `CII-SR-182` | EN16931 | warning |  | CalculatedAmount should not be present |
| `CII-SR-183` | EN16931 | warning |  | IndicatorString should not be present |
| `CII-SR-184` | EN16931 | warning |  | ID should not be present |
| `CII-SR-185` | EN16931 | warning |  | SequenceNumeric should not be present |
| `CII-SR-186` | EN16931 | warning |  | @format should not be present |
| `CII-SR-187` | EN16931 | warning |  | BasisQuantity should not be present |
| `CII-SR-188` | EN16931 | warning |  | PrepaidIndicator should not be present |
| `CII-SR-189` | EN16931 | warning |  | UnitBasisAmount should not be present |
| `CII-SR-190` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-191` | EN16931 | warning |  | CategoryTradeTax should not be present |
| `CII-SR-192` | EN16931 | warning |  | ActualTradeCurrencyExchange should not be present |
| `CII-SR-193` | EN16931 | warning |  | ID should not be present |
| `CII-SR-194` | EN16931 | warning |  | SubtotalCalculatedTradeTax should not be present |
| `CII-SR-195` | EN16931 | warning |  | SpecifiedLogisticsServiceCharge should not be present |
| `CII-SR-196` | EN16931 | warning |  | SpecifiedTradePaymentTerms should not be present |
| `CII-SR-197` | EN16931 | warning |  | ChargeTotalAmount should not be present |
| `CII-SR-198` | EN16931 | warning |  | AllowanceTotalAmount should not be present |
| `CII-SR-199` | EN16931 | warning |  | TaxBasisTotalAmount should not be present |
| `CII-SR-200` | EN16931 | warning |  | TaxTotalAmount should not be present |
| `CII-SR-201` | EN16931 | warning |  | GrandTotalAmount should not be present |
| `CII-SR-202` | EN16931 | warning |  | InformationAmount should not be present |
| `CII-SR-203` | EN16931 | warning |  | TotalAllowanceChargeAmount should not be present |
| `CII-SR-204` | EN16931 | warning |  | TotalRetailValueInformationAmount should not be present |
| `CII-SR-205` | EN16931 | warning |  | GrossLineTotalAmount should not be present |
| `CII-SR-206` | EN16931 | warning |  | NetLineTotalAmount should not be present |
| `CII-SR-207` | EN16931 | warning |  | NetIncludingTaxesLineTotalAmount should not be present |
| `CII-SR-208` | EN16931 | warning |  | ProductWeightLossInformationAmount should not be present |
| `CII-SR-209` | EN16931 | warning |  | SpecifiedFinancialAdjustment should not be present |
| `CII-SR-210` | EN16931 | warning |  | InvoiceReferencedDocument should not be present |
| `CII-SR-212` | EN16931 | warning |  | PayableSpecifiedTradeAccountingAccount should not be present |
| `CII-SR-213` | EN16931 | warning |  | SetTriggerCode should not be present |
| `CII-SR-214` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-215` | EN16931 | warning |  | AmountTypeCode should not be present |
| `CII-SR-216` | EN16931 | warning |  | Name should not be present |
| `CII-SR-217` | EN16931 | warning |  | CostReferenceDimensionPattern should not be present |
| `CII-SR-218` | EN16931 | warning |  | PurchaseSpecifiedTradeAccountingAccount should not be present |
| `CII-SR-219` | EN16931 | warning |  | SalesSpecifiedTradeAccountingAccount should not be present |
| `CII-SR-220` | EN16931 | warning |  | SpecifiedTradeSettlementFinancialCard should not be present |
| `CII-SR-221` | EN16931 | warning |  | IncludedSubordinateTradeLineItem should not be present |
| `CII-SR-222` | EN16931 | warning |  | RoleCode should not be present |
| `CII-SR-223` | EN16931 | warning |  | LegalClassificationCode should not be present |
| `CII-SR-224` | EN16931 | warning |  | Name should not be present |
| `CII-SR-225` | EN16931 | warning |  | PostalTradeAddress should not be present |
| `CII-SR-226` | EN16931 | warning |  | RoleCode should not be present |
| `CII-SR-227` | EN16931 | warning |  | ID should not be present |
| `CII-SR-228` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-229` | EN16931 | warning |  | JobTitle should not be present |
| `CII-SR-230` | EN16931 | warning |  | Responsibility should not be present |
| `CII-SR-231` | EN16931 | warning |  | PersonID should not be present |
| `CII-SR-232` | EN16931 | warning |  | URIID should not be present |
| `CII-SR-233` | EN16931 | warning |  | ChannelCode should not be present |
| `CII-SR-234` | EN16931 | warning |  | DirectTelephoneUniversalCommunication should not be present |
| `CII-SR-235` | EN16931 | warning |  | MobileTelephoneUniversalCommunication should not be present |
| `CII-SR-236` | EN16931 | warning |  | FaxUniversalCommunication should not be present |
| `CII-SR-237` | EN16931 | warning |  | ChannelCode should not be present |
| `CII-SR-238` | EN16931 | warning |  | CompleteNumber should not be present |
| `CII-SR-239` | EN16931 | warning |  | TelexUniversalCommunication should not be present |
| `CII-SR-240` | EN16931 | warning |  | VOIPUniversalCommunication should not be present |
| `CII-SR-241` | EN16931 | warning |  | InstantMessagingUniversalCommunication should not be present |
| `CII-SR-242` | EN16931 | warning |  | SpecifiedNote should not be present |
| `CII-SR-243` | EN16931 | warning |  | SpecifiedContactPerson should not be present |
| `CII-SR-244` | EN16931 | warning |  | ChannelCode should not be present |
| `CII-SR-245` | EN16931 | warning |  | CompleteNumber should not be present |
| `CII-SR-246` | EN16931 | warning |  | AssociatedRegisteredTax should not be present |
| `CII-SR-247` | EN16931 | warning |  | EndPointURIUniversalCommunication should not be present |
| `CII-SR-248` | EN16931 | warning |  | LogoAssociatedSpecifiedBinaryFile should not be present |
| `CII-SR-249` | EN16931 | warning |  | RoleCode should not be present |
| `CII-SR-250` | EN16931 | warning |  | Description should not be present |
| `CII-SR-251` | EN16931 | warning |  | LegalClassificationCode should not be present |
| `CII-SR-252` | EN16931 | warning |  | Name should not be present |
| `CII-SR-254` | EN16931 | warning |  | PostalTradeAddress should not be present |
| `CII-SR-255` | EN16931 | warning |  | AuthorizedLegalRegistration should not be present |
| `CII-SR-256` | EN16931 | warning |  | ID should not be present |
| `CII-SR-257` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-258` | EN16931 | warning |  | JobTitle should not be present |
| `CII-SR-259` | EN16931 | warning |  | Responsibility should not be present |
| `CII-SR-260` | EN16931 | warning |  | PersonID should not be present |
| `CII-SR-261` | EN16931 | warning |  | URIID should not be present |
| `CII-SR-262` | EN16931 | warning |  | ChannelCode should not be present |
| `CII-SR-263` | EN16931 | warning |  | DirectTelephoneUniversalCommunication should not be present |
| `CII-SR-264` | EN16931 | warning |  | MobileTelephoneUniversalCommunication should not be present |
| `CII-SR-265` | EN16931 | warning |  | FaxUniversalCommunication should not be present |
| `CII-SR-266` | EN16931 | warning |  | ChannelCode should not be present |
| `CII-SR-267` | EN16931 | warning |  | CompleteNumber should not be present |
| `CII-SR-268` | EN16931 | warning |  | TelexUniversalCommunication should not be present |
| `CII-SR-269` | EN16931 | warning |  | VOIPUniversalCommunication should not be present |
| `CII-SR-270` | EN16931 | warning |  | InstantMessagingUniversalCommunication should not be present |
| `CII-SR-271` | EN16931 | warning |  | SpecifiedNote should not be present |
| `CII-SR-272` | EN16931 | warning |  | SpecifiedContactPerson should not be present |
| `CII-SR-273` | EN16931 | warning |  | ChannelCode should not be present |
| `CII-SR-274` | EN16931 | warning |  | CompleteNumber should not be present |
| `CII-SR-275` | EN16931 | warning |  | AssociatedRegisteredTax should not be present |
| `CII-SR-276` | EN16931 | warning |  | EndPointURIUniversalCommunication should not be present |
| `CII-SR-277` | EN16931 | warning |  | LogoAssociatedSpecifiedBinaryFile should not be present |
| `CII-SR-278` | EN16931 | warning |  | SalesAgentTradeParty should not be present |
| `CII-SR-279` | EN16931 | warning |  | BuyerRequisitionerTradeParty should not be present |
| `CII-SR-280` | EN16931 | warning |  | BuyerAssignedAccountantTradeParty should not be present |
| `CII-SR-281` | EN16931 | warning |  | SellerAssignedAccountantTradeParty should not be present |
| `CII-SR-282` | EN16931 | warning |  | BuyerTaxRepresentativeTradeParty should not be present |
| `CII-SR-283` | EN16931 | warning |  | GlobalID should not be present |
| `CII-SR-284` | EN16931 | warning |  | RoleCode should not be present |
| `CII-SR-285` | EN16931 | warning |  | Description should not be present |
| `CII-SR-286` | EN16931 | warning |  | SpecifiedLegalOrganization should not be present |
| `CII-SR-287` | EN16931 | warning |  | DefinedTradeContact should not be present |
| `CII-SR-288` | EN16931 | warning |  | URIUniversalCommunication should not be present |
| `CII-SR-289` | EN16931 | warning |  | AssociatedRegisteredTax should not be present |
| `CII-SR-290` | EN16931 | warning |  | EndPointURIUniversalCommunication should not be present |
| `CII-SR-291` | EN16931 | warning |  | LogoAssociatedSpecifiedBinaryFile should not be present |
| `CII-SR-292` | EN16931 | warning |  | ProductEndUserTradeParty should not be present |
| `CII-SR-293` | EN16931 | warning |  | ApplicableTradeDeliveryTerms should not be present |
| `CII-SR-294` | EN16931 | warning |  | LineID should not be present |
| `CII-SR-295` | EN16931 | warning |  | LineID should not be present |
| `CII-SR-296` | EN16931 | warning |  | QuotationReferencedDocument should not be present |
| `CII-SR-297` | EN16931 | warning |  | OrderResponseReferencedDocument should not be present |
| `CII-SR-298` | EN16931 | warning |  | LineID should not be present |
| `CII-SR-299` | EN16931 | warning |  | DemandForecastReferencedDocument should not be present |
| `CII-SR-300` | EN16931 | warning |  | SupplyInstructionReferencedDocument should not be present |
| `CII-SR-301` | EN16931 | warning |  | PromotionalDealReferencedDocument should not be present |
| `CII-SR-302` | EN16931 | warning |  | PriceListReferencedDocument should not be present |
| `CII-SR-303` | EN16931 | warning |  | LineID should not be present |
| `CII-SR-304` | EN16931 | warning |  | RequisitionerReferencedDocument should not be present |
| `CII-SR-305` | EN16931 | warning |  | BuyerAgentTradeParty should not be present |
| `CII-SR-306` | EN16931 | warning |  | PurchaseConditionsReferencedDocument should not be present |
| `CII-SR-307` | EN16931 | warning |  | Description should not be present |
| `CII-SR-308` | EN16931 | warning |  | RelatedSupplyChainConsignment should not be present |
| `CII-SR-309` | EN16931 | warning |  | RoleCode should not be present |
| `CII-SR-310` | EN16931 | warning |  | Description should not be present |
| `CII-SR-311` | EN16931 | warning |  | SpecifiedLegalOrganization should not be present |
| `CII-SR-312` | EN16931 | warning |  | DefinedTradeContact should not be present |
| `CII-SR-313` | EN16931 | warning |  | URIUniversalCommunication should not be present |
| `CII-SR-314` | EN16931 | warning |  | SpecifiedTaxRegistration should not be present |
| `CII-SR-315` | EN16931 | warning |  | EndPointURIUniversalCommunication should not be present |
| `CII-SR-316` | EN16931 | warning |  | LogoAssociatedSpecifiedBinaryFile should not be present |
| `CII-SR-317` | EN16931 | warning |  | UltimateShipToTradeParty should not be present |
| `CII-SR-318` | EN16931 | warning |  | ShipFromTradeParty should not be present |
| `CII-SR-319` | EN16931 | warning |  | ActualDespatchSupplyChainEvent should not be present |
| `CII-SR-320` | EN16931 | warning |  | ActualPickUpSupplyChainEvent should not be present |
| `CII-SR-321` | EN16931 | warning |  | ID should not be present |
| `CII-SR-322` | EN16931 | warning |  | DateTime should not be present |
| `CII-SR-323` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-324` | EN16931 | warning |  | Description should not be present |
| `CII-SR-325` | EN16931 | warning |  | DescriptionBinaryObject should not be present |
| `CII-SR-326` | EN16931 | warning |  | UnitQuantity should not be present |
| `CII-SR-327` | EN16931 | warning |  | LatestOccurrenceDateTime should not be present |
| `CII-SR-328` | EN16931 | warning |  | EarliestOccurrenceDateTime should not be present |
| `CII-SR-329` | EN16931 | warning |  | OccurrenceSpecifiedPeriod should not be present |
| `CII-SR-330` | EN16931 | warning |  | OccurrenceLogisticsLocation should not be present |
| `CII-SR-331` | EN16931 | warning |  | ActualReceiptSupplyChainEvent should not be present |
| `CII-SR-332` | EN16931 | warning |  | AdditionalReferencedDocument should not be present |
| `CII-SR-333` | EN16931 | warning |  | LineID should not be present |
| `CII-SR-334` | EN16931 | warning |  | LineID should not be present |
| `CII-SR-335` | EN16931 | warning |  | DeliveryNoteReferencedDocument should not be present |
| `CII-SR-336` | EN16931 | warning |  | ConsumptionReportReferencedDocument should not be present |
| `CII-SR-337` | EN16931 | warning |  | PreviousDeliverySupplyChainEvent should not be present |
| `CII-SR-338` | EN16931 | warning |  | PackingListReferencedDocument should not be present |
| `CII-SR-339` | EN16931 | warning |  | DuePayableAmount should not be present |
| `CII-SR-340` | EN16931 | warning |  | CreditorReferenceTypeCode should not be present |
| `CII-SR-341` | EN16931 | warning |  | CreditorReferenceType should not be present |
| `CII-SR-342` | EN16931 | warning |  | CreditorReferenceIssuerID should not be present |
| `CII-SR-344` | EN16931 | warning |  | PaymentCurrencyCode should not be present |
| `CII-SR-345` | EN16931 | warning |  | InvoiceIssuerReference should not be present |
| `CII-SR-346` | EN16931 | warning |  | InvoiceDateTime should not be present |
| `CII-SR-347` | EN16931 | warning |  | NextInvoiceDateTime should not be present |
| `CII-SR-348` | EN16931 | warning |  | CreditReasonCode should not be present |
| `CII-SR-349` | EN16931 | warning |  | CreditReason should not be present |
| `CII-SR-350` | EN16931 | warning |  | InvoicerTradeParty should not be present |
| `CII-SR-351` | EN16931 | warning |  | InvoiceeTradeParty should not be present |
| `CII-SR-352` | EN16931 | warning |  | RoleCode should not be present |
| `CII-SR-353` | EN16931 | warning |  | Description should not be present |
| `CII-SR-354` | EN16931 | warning |  | LegalClassificationCode should not be present |
| `CII-SR-355` | EN16931 | warning |  | Name should not be present |
| `CII-SR-356` | EN16931 | warning |  | TradingBusinessName should not be present |
| `CII-SR-357` | EN16931 | warning |  | PostalTradeAddress should not be present |
| `CII-SR-358` | EN16931 | warning |  | AuthorizedLegalRegistration should not be present |
| `CII-SR-359` | EN16931 | warning |  | DefinedTradeContact should not be present |
| `CII-SR-360` | EN16931 | warning |  | PostalTradeAddress should not be present |
| `CII-SR-361` | EN16931 | warning |  | URIUniversalCommunication should not be present |
| `CII-SR-362` | EN16931 | warning |  | SpecifiedTaxRegistration should not be present |
| `CII-SR-363` | EN16931 | warning |  | EndPointURIUniversalCommunication should not be present |
| `CII-SR-364` | EN16931 | warning |  | LogoAssociatedSpecifiedBinaryFile should not be present |
| `CII-SR-365` | EN16931 | warning |  | PayerTradeParty should not be present |
| `CII-SR-366` | EN16931 | warning |  | TaxApplicableTradeCurrencyExchange should not be present |
| `CII-SR-367` | EN16931 | warning |  | InvoiceApplicableTradeCurrencyExchange should not be present |
| `CII-SR-368` | EN16931 | warning |  | PaymentApplicableTradeCurrencyExchange should not be present |
| `CII-SR-369` | EN16931 | warning |  | PaymentChannelCode should not be present |
| `CII-SR-370` | EN16931 | warning |  | GuaranteeMethodCode should not be present |
| `CII-SR-371` | EN16931 | warning |  | PaymentMethodCode should not be present |
| `CII-SR-372` | EN16931 | warning |  | MicrochipIndicator should not be present |
| `CII-SR-373` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-375` | EN16931 | warning |  | ExpiryDate should not be present |
| `CII-SR-376` | EN16931 | warning |  | VerificationNumeric should not be present |
| `CII-SR-377` | EN16931 | warning |  | ValidFromDateTime should not be present |
| `CII-SR-378` | EN16931 | warning |  | CreditLimitAmountshould not be present |
| `CII-SR-379` | EN16931 | warning |  | CreditAvailableAmount should not be present |
| `CII-SR-380` | EN16931 | warning |  | InterestRatePercent should not be present |
| `CII-SR-381` | EN16931 | warning |  | Description should not be present |
| `CII-SR-382` | EN16931 | warning |  | AccountName should not be present |
| `CII-SR-384` | EN16931 | warning |  | ClearingSystemName should not be present |
| `CII-SR-385` | EN16931 | warning |  | Name should not be present |
| `CII-SR-386` | EN16931 | warning |  | LocationFinancialInstitutionAddress should not be present |
| `CII-SR-388` | EN16931 | warning |  | ID should not be present |
| `CII-SR-389` | EN16931 | warning |  | SequenceNumeric should not be present |
| `CII-SR-390` | EN16931 | warning |  | BasisQuantity should not be present |
| `CII-SR-391` | EN16931 | warning |  | PrepaidIndicator should not be present |
| `CII-SR-392` | EN16931 | warning |  | UnitBasisAmount should not be present |
| `CII-SR-393` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-394` | EN16931 | warning |  | ActualTradeCurrencyExchange should not be present |
| `CII-SR-395` | EN16931 | warning |  | SubtotalCalculatedTradeTax should not be present |
| `CII-SR-396` | EN16931 | warning |  | SpecifiedLogisticsServiceCharge should not be present |
| `CII-SR-397` | EN16931 | warning |  | ID should not be present |
| `CII-SR-398` | EN16931 | warning |  | FromEventCode should not be present |
| `CII-SR-399` | EN16931 | warning |  | SettlementPeriodMeasure should not be present |
| `CII-SR-400` | EN16931 | warning |  | DateTime should not be present |
| `CII-SR-401` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-402` | EN16931 | warning |  | InstructionTypeCode should not be present |
| `CII-SR-404` | EN16931 | warning |  | PartialPaymentPercent should not be present |
| `CII-SR-405` | EN16931 | warning |  | PaymentMeansID should not be present |
| `CII-SR-406` | EN16931 | warning |  | PartialPaymentAmount should not be present |
| `CII-SR-407` | EN16931 | warning |  | ApplicableTradePaymentPenaltyTerms should not be present |
| `CII-SR-408` | EN16931 | warning |  | ApplicableTradePaymentDiscountTerms should not be present |
| `CII-SR-409` | EN16931 | warning |  | PayeeTradeParty should not be present |
| `CII-SR-411` | EN16931 | warning |  | InformationAmount should not be present |
| `CII-SR-412` | EN16931 | warning |  | TotalDiscountAmount should not be present |
| `CII-SR-413` | EN16931 | warning |  | TotalAllowanceChargeAmount should not be present |
| `CII-SR-414` | EN16931 | warning |  | RetailValueExcludingTaxInformationAmount should not be present |
| `CII-SR-415` | EN16931 | warning |  | TotalDepositFeeInformationAmount should not be present |
| `CII-SR-416` | EN16931 | warning |  | ProductValueExcludingTobaccoTaxInformationAmount should not be present |
| `CII-SR-417` | EN16931 | warning |  | TotalRetailValueInformationAmount should not be present |
| `CII-SR-418` | EN16931 | warning |  | GrossLineTotalAmount should not be present |
| `CII-SR-419` | EN16931 | warning |  | NetLineTotalAmount should not be present |
| `CII-SR-420` | EN16931 | warning |  | NetIncludingTaxesLineTotalAmount should not be present |
| `CII-SR-421` | EN16931 | warning |  | SpecifiedFinancialAdjustment should not be present |
| `CII-SR-422` | EN16931 | warning |  | LineID should not be present |
| `CII-SR-423` | EN16931 | warning |  | ProFormaInvoiceReferencedDocument should not be present |
| `CII-SR-424` | EN16931 | warning |  | LetterOfCreditReferencedDocument should not be present |
| `CII-SR-425` | EN16931 | warning |  | FactoringAgreementReferencedDocument should not be present |
| `CII-SR-426` | EN16931 | warning |  | FactoringListReferencedDocument should not be present |
| `CII-SR-427` | EN16931 | warning |  | PayableSpecifiedTradeAccountingAccount should not be present |
| `CII-SR-428` | EN16931 | warning |  | SetTriggerCode should not be present |
| `CII-SR-429` | EN16931 | warning |  | TypeCode should not be present |
| `CII-SR-430` | EN16931 | warning |  | AmountTypeCode should not be present |
| `CII-SR-431` | EN16931 | warning |  | Name should not be present |
| `CII-SR-432` | EN16931 | warning |  | CostReferenceDimensionPattern should not be present |
| `CII-SR-433` | EN16931 | warning |  | PurchaseSpecifiedTradeAccountingAccount should not be present |
| `CII-SR-434` | EN16931 | warning |  | SalesSpecifiedTradeAccountingAccount should not be present |
| `CII-SR-435` | EN16931 | warning |  | SpecifiedTradeSettlementFinancialCard should not be present |
| `CII-SR-436` | EN16931 | warning |  | SpecifiedAdvancePayment should not be present |
| `CII-SR-437` | EN16931 | warning |  | UltimatePayeeTradeParty should not be present |
| `CII-SR-438` | EN16931 | warning |  | ValuationBreakdownStatement should not be present |
| `CII-SR-439` | EN16931 | fatal |  | ChargeAmount should exist maximum once |
| `CII-SR-440` | EN16931 | fatal |  | ActualAmount should exist maximum once |
| `CII-SR-441` | EN16931 | fatal |  | ChargeAmount should exist maximum once |
| `CII-SR-442` | EN16931 | warning |  | Reference should not be present |
| `CII-SR-443` | EN16931 | warning |  | ID should not be present |
| `CII-SR-444` | EN16931 | warning |  | ProprietaryID should not be present |
| `CII-SR-445` | EN16931 | warning |  | IncludedTradeTax should not be present |
| `CII-SR-446` | EN16931 | warning |  | IncludedTradeTax should not be present |
| `CII-SR-447` | EN16931 | warning |  | UltimateCustomerOrderReferencedDocument should not be present |
| `CII-SR-448` | EN16931 | warning |  | UltimateCustomerOrderReferencedDocument should not be present |
| `CII-SR-449` | EN16931 | warning |  | Only one delivery to location identifier should be present (either the ID or the Global ID) |
| `CII-SR-450` | EN16931 | warning |  | Only one buyer identifier should be present (either the ID or the Global ID) |
| `CII-SR-451` | EN16931 | warning |  | Only one payee identifier should be present (either the ID or the Global ID) |
| `CII-SR-452` | EN16931 | warning |  | Only one SpecifiedTradePaymentTerms should be present |
| `CII-SR-453` | EN16931 | warning |  | Only one SpecifiedTradePaymentTerms Description should be present |
| `CII-SR-454` | EN16931 | warning |  | Only one ApplicableTradeTax should be present |
| `CII-SR-455` | EN16931 | fatal |  | DefinedTradeContact of SellerTradeParty shall exist maximum once |
| `CII-SR-456` | EN16931 | fatal |  | DefinedTradeContact of BuyerTradeParty shall exist maximum once |
| `CII-SR-457` | EN16931 | warning |  | IssuerAssignedID with TypeCode 50 should exist maximum once |
| `CII-SR-458` | EN16931 | warning |  | IssuerAssignedID with TypeCode 130 should exist maximum once |
| `CII-SR-459` | EN16931 | fatal |  | SellerTradeParty URIUniversalCommunication should exist maximum once |
| `CII-SR-460` | EN16931 | fatal |  | BuyerTradeParty URIUniversalCommunication should exist maximum once |
| `CII-SR-461` | EN16931 | fatal |  | Only one TaxPointDate shall be present |
| `CII-SR-462` | EN16931 | fatal |  | Only one DueDateTypeCode shall be present |
| `CII-SR-463` | EN16931 | fatal | `BG-20`, `BG-21` | Each Specified Trade Allowance Charge (BG-20)(BG-21) shall contain a Charge Indicator. |
| `CII-SR-464` | EN16931 | warning | `BT-86` | Only one BT-86 element is allowed on an invoice. |
| `CII-SR-465` | EN16931 | warning | `BT-41` | Only one BT-41 element is allowed on an invoice. |
| `CII-SR-466` | EN16931 | warning | `BT-56` | Only one BT-56 element is allowed on an invoice. |
| `UBL-CR-001` | EN16931 | warning |  | A UBL invoice should not include extensions |
| `UBL-CR-002` | EN16931 | warning |  | A UBL invoice should not include the UBLVersionID or it should be 2.1 |
| `UBL-CR-003` | EN16931 | warning |  | A UBL invoice should not include the ProfileExecutionID |
| `UBL-CR-004` | EN16931 | warning |  | A UBL invoice should not include the CopyIndicator |
| `UBL-CR-005` | EN16931 | warning |  | A UBL invoice should not include the UUID |
| `UBL-CR-006` | EN16931 | warning |  | A UBL invoice should not include the IssueTime |
| `UBL-CR-007` | EN16931 | warning |  | A UBL invoice should not include the PricingCurrencyCode |
| `UBL-CR-008` | EN16931 | warning |  | A UBL invoice should not include the PaymentCurrencyCode |
| `UBL-CR-009` | EN16931 | warning |  | A UBL invoice should not include the PaymentAlternativeCurrencyCode |
| `UBL-CR-010` | EN16931 | warning |  | A UBL invoice should not include the AccountingCostCode |
| `UBL-CR-011` | EN16931 | warning |  | A UBL invoice should not include the LineCountNumeric |
| `UBL-CR-012` | EN16931 | warning |  | A UBL invoice should not include the InvoicePeriod StartTime |
| `UBL-CR-013` | EN16931 | warning |  | A UBL invoice should not include the InvoicePeriod EndTime |
| `UBL-CR-014` | EN16931 | warning |  | A UBL invoice should not include the InvoicePeriod DurationMeasure |
| `UBL-CR-015` | EN16931 | warning |  | A UBL invoice should not include the InvoicePeriod Description |
| `UBL-CR-016` | EN16931 | warning |  | A UBL invoice should not include the OrderReference CopyIndicator |
| `UBL-CR-017` | EN16931 | warning |  | A UBL invoice should not include the OrderReference UUID |
| `UBL-CR-018` | EN16931 | warning |  | A UBL invoice should not include the OrderReference IssueDate |
| `UBL-CR-019` | EN16931 | warning |  | A UBL invoice should not include the OrderReference IssueTime |
| `UBL-CR-020` | EN16931 | warning |  | A UBL invoice should not include the OrderReference CustomerReference |
| `UBL-CR-021` | EN16931 | warning |  | A UBL invoice should not include the OrderReference OrderTypeCode |
| `UBL-CR-022` | EN16931 | warning |  | A UBL invoice should not include the OrderReference DocumentReference |
| `UBL-CR-023` | EN16931 | warning |  | A UBL invoice should not include the BillingReference CopyIndicator |
| `UBL-CR-024` | EN16931 | warning |  | A UBL invoice should not include the BillingReference UUID |
| `UBL-CR-025` | EN16931 | warning |  | A UBL invoice should not include the BillingReference IssueTime |
| `UBL-CR-026` | EN16931 | warning |  | A UBL invoice should not include the BillingReference DocumentTypeCode |
| `UBL-CR-027` | EN16931 | warning |  | A UBL invoice should not include the BillingReference DocumentType |
| `UBL-CR-028` | EN16931 | warning |  | A UBL invoice should not include the BillingReference Xpath |
| `UBL-CR-029` | EN16931 | warning |  | A UBL invoice should not include the BillingReference LanguageID |
| `UBL-CR-030` | EN16931 | warning |  | A UBL invoice should not include the BillingReference LocaleCode |
| `UBL-CR-031` | EN16931 | warning |  | A UBL invoice should not include the BillingReference VersionID |
| `UBL-CR-032` | EN16931 | warning |  | A UBL invoice should not include the BillingReference DocumentStatusCode |
| `UBL-CR-033` | EN16931 | warning |  | A UBL invoice should not include the BillingReference DocumenDescription |
| `UBL-CR-034` | EN16931 | warning |  | A UBL invoice should not include the BillingReference Attachment |
| `UBL-CR-035` | EN16931 | warning |  | A UBL invoice should not include the BillingReference ValidityPeriod |
| `UBL-CR-036` | EN16931 | warning |  | A UBL invoice should not include the BillingReference IssuerParty |
| `UBL-CR-037` | EN16931 | warning |  | A UBL invoice should not include the BillingReference ResultOfVerification |
| `UBL-CR-038` | EN16931 | warning |  | A UBL invoice should not include the BillingReference SelfBilledInvoiceDocumentReference |
| `UBL-CR-039` | EN16931 | warning |  | A UBL invoice should not include the BillingReference CreditNoteDocumentReference |
| `UBL-CR-040` | EN16931 | warning |  | A UBL invoice should not include the BillingReference SelfBilledCreditNoteDocumentReference |
| `UBL-CR-041` | EN16931 | warning |  | A UBL invoice should not include the BillingReference DebitNoteDocumentReference |
| `UBL-CR-042` | EN16931 | warning |  | A UBL invoice should not include the BillingReference ReminderDocumentReference |
| `UBL-CR-043` | EN16931 | warning |  | A UBL invoice should not include the BillingReference AdditionalDocumentReference |
| `UBL-CR-044` | EN16931 | warning |  | A UBL invoice should not include the BillingReference BillingReferenceLine |
| `UBL-CR-045` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference CopyIndicator |
| `UBL-CR-046` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference UUID |
| `UBL-CR-047` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference IssueDate |
| `UBL-CR-048` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference IssueTime |
| `UBL-CR-049` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference DocumentTypeCode |
| `UBL-CR-050` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference DocumentType |
| `UBL-CR-051` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference Xpath |
| `UBL-CR-052` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference LanguageID |
| `UBL-CR-053` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference LocaleCode |
| `UBL-CR-054` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference VersionID |
| `UBL-CR-055` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference DocumentStatusCode |
| `UBL-CR-056` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference DocumentDescription |
| `UBL-CR-057` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference Attachment |
| `UBL-CR-058` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference ValidityPeriod |
| `UBL-CR-059` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference IssuerParty |
| `UBL-CR-060` | EN16931 | warning |  | A UBL invoice should not include the DespatchDocumentReference ResultOfVerification |
| `UBL-CR-061` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference CopyIndicator |
| `UBL-CR-062` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference UUID |
| `UBL-CR-063` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference IssueDate |
| `UBL-CR-064` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference IssueTime |
| `UBL-CR-065` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference DocumentTypeCode |
| `UBL-CR-066` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference DocumentType |
| `UBL-CR-067` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference Xpath |
| `UBL-CR-068` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference LanguageID |
| `UBL-CR-069` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference LocaleCode |
| `UBL-CR-070` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference VersionID |
| `UBL-CR-071` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference DocumentStatusCode |
| `UBL-CR-072` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference DocumentDescription |
| `UBL-CR-073` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference Attachment |
| `UBL-CR-074` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference ValidityPeriod |
| `UBL-CR-075` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference IssuerParty |
| `UBL-CR-076` | EN16931 | warning |  | A UBL invoice should not include the ReceiptDocumentReference ResultOfVerification |
| `UBL-CR-077` | EN16931 | warning |  | A UBL invoice should not include the StatementDocumentReference |
| `UBL-CR-078` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference CopyIndicator |
| `UBL-CR-079` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference UUID |
| `UBL-CR-080` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference IssueDate |
| `UBL-CR-081` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference IssueTime |
| `UBL-CR-082` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference DocumentTypeCode |
| `UBL-CR-083` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference DocumentType |
| `UBL-CR-084` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference Xpath |
| `UBL-CR-085` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference LanguageID |
| `UBL-CR-086` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference LocaleCode |
| `UBL-CR-087` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference VersionID |
| `UBL-CR-088` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference DocumentStatusCode |
| `UBL-CR-089` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference DocumentDescription |
| `UBL-CR-090` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference Attachment |
| `UBL-CR-091` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference ValidityPeriod |
| `UBL-CR-092` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference IssuerParty |
| `UBL-CR-093` | EN16931 | warning |  | A UBL invoice should not include the OriginatorDocumentReference ResultOfVerification |
| `UBL-CR-094` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference CopyIndicator |
| `UBL-CR-095` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference UUID |
| `UBL-CR-096` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference IssueDate |
| `UBL-CR-097` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference IssueTime |
| `UBL-CR-098` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference DocumentTypeCode |
| `UBL-CR-099` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference DocumentType |
| `UBL-CR-100` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference Xpath |
| `UBL-CR-101` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference LanguageID |
| `UBL-CR-102` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference LocaleCode |
| `UBL-CR-103` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference VersionID |
| `UBL-CR-104` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference DocumentStatusCode |
| `UBL-CR-105` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference DocumentDescription |
| `UBL-CR-106` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference Attachment |
| `UBL-CR-107` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference ValidityPeriod |
| `UBL-CR-108` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference IssuerParty |
| `UBL-CR-109` | EN16931 | warning |  | A UBL invoice should not include the ContractDocumentReference ResultOfVerification |
| `UBL-CR-110` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference CopyIndicator |
| `UBL-CR-111` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference UUID |
| `UBL-CR-112` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference IssueDate |
| `UBL-CR-113` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference IssueTime |
| `UBL-CR-114` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference DocumentType |
| `UBL-CR-115` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Xpath |
| `UBL-CR-116` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference LanguageID |
| `UBL-CR-117` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference LocaleCode |
| `UBL-CR-118` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference VersionID |
| `UBL-CR-119` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference DocumentStatusCode |
| `UBL-CR-121` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External DocumentHash |
| `UBL-CR-122` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External HashAlgorithmMethod |
| `UBL-CR-123` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External ExpiryDate |
| `UBL-CR-124` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External ExpiryTime |
| `UBL-CR-125` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External MimeCode |
| `UBL-CR-126` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External FormatCode |
| `UBL-CR-127` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External EncodingCode |
| `UBL-CR-128` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External CharacterSetCode |
| `UBL-CR-129` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External FileName |
| `UBL-CR-130` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference Attachment External Descriprion |
| `UBL-CR-131` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference ValidityPeriod |
| `UBL-CR-132` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference IssuerParty |
| `UBL-CR-133` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference ResultOfVerification |
| `UBL-CR-134` | EN16931 | warning |  | A UBL invoice should not include the ProjectReference UUID |
| `UBL-CR-135` | EN16931 | warning |  | A UBL invoice should not include the ProjectReference IssueDate |
| `UBL-CR-136` | EN16931 | warning |  | A UBL invoice should not include the ProjectReference WorkPhaseReference |
| `UBL-CR-137` | EN16931 | warning |  | A UBL invoice should not include the Signature |
| `UBL-CR-138` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty CustomerAssignedAccountID |
| `UBL-CR-139` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty AdditionalAccountID |
| `UBL-CR-140` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty DataSendingCapability |
| `UBL-CR-141` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party MarkCareIndicator |
| `UBL-CR-142` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party MarkAttentionIndicator |
| `UBL-CR-143` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party WebsiteURI |
| `UBL-CR-144` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party LogoReferenceID |
| `UBL-CR-145` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party IndustryClassificationCode |
| `UBL-CR-146` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party Language |
| `UBL-CR-147` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress ID |
| `UBL-CR-148` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress AddressTypeCode |
| `UBL-CR-149` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress AddressFormatCode |
| `UBL-CR-150` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress Postbox |
| `UBL-CR-151` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress Floor |
| `UBL-CR-152` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress Room |
| `UBL-CR-153` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress BlockName |
| `UBL-CR-154` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress BuildingName |
| `UBL-CR-155` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress BuildingNumber |
| `UBL-CR-156` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress InhouseMail |
| `UBL-CR-157` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress Department |
| `UBL-CR-158` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress MarkAttention |
| `UBL-CR-159` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress MarkCare |
| `UBL-CR-160` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress PlotIdentification |
| `UBL-CR-161` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress CitySubdivisionName |
| `UBL-CR-162` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress CountrySubentityCode |
| `UBL-CR-163` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress Region |
| `UBL-CR-164` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress District |
| `UBL-CR-165` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress TimezoneOffset |
| `UBL-CR-166` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress Country Name |
| `UBL-CR-167` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PostalAddress LocationCoordinate |
| `UBL-CR-168` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PhysicalLocation |
| `UBL-CR-169` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme RegistrationName |
| `UBL-CR-170` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme TaxLevelCode |
| `UBL-CR-171` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme ExemptionReasonCode |
| `UBL-CR-172` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme ExemptionReason |
| `UBL-CR-173` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme RegistrationAddress |
| `UBL-CR-174` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme TaxScheme Name |
| `UBL-CR-175` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme TaxScheme TaxTypeCode |
| `UBL-CR-176` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme TaxScheme CurrencyCode |
| `UBL-CR-177` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyTaxScheme TaxScheme JurisdictionRegionAddress |
| `UBL-CR-178` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity RegistrationDate |
| `UBL-CR-179` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity RegistrationExpirationDate |
| `UBL-CR-180` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity CompanyLegalFormCode |
| `UBL-CR-181` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity SoleProprietorshipIndicator |
| `UBL-CR-182` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity CompanyLiquidationStatusCode |
| `UBL-CR-183` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity CorporateStockAmount |
| `UBL-CR-184` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity FullyPaidSharesIndicator |
| `UBL-CR-185` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity RegistrationAddress |
| `UBL-CR-186` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity CorporateRegistrationScheme |
| `UBL-CR-187` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity HeadOfficeParty |
| `UBL-CR-188` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PartyLegalEntity ShareholderParty |
| `UBL-CR-189` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party Contact ID |
| `UBL-CR-190` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party Contact Telefax |
| `UBL-CR-191` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party Contact Note |
| `UBL-CR-192` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party Contact OtherCommunication |
| `UBL-CR-193` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party Person |
| `UBL-CR-194` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party AgentParty |
| `UBL-CR-195` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party ServiceProviderParty |
| `UBL-CR-196` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party PowerOfAttorney |
| `UBL-CR-197` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty Party FinancialAccount |
| `UBL-CR-198` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty DespatchContact |
| `UBL-CR-199` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty AccountingContact |
| `UBL-CR-200` | EN16931 | warning |  | A UBL invoice should not include the AccountingSupplierParty SellerContact |
| `UBL-CR-201` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty CustomerAssignedAccountID |
| `UBL-CR-202` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty SupplierAssignedAccountID |
| `UBL-CR-203` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty AdditionalAccountID |
| `UBL-CR-204` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party MarkCareIndicator |
| `UBL-CR-205` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party MarkAttentionIndicator |
| `UBL-CR-206` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party WebsiteURI |
| `UBL-CR-207` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party LogoReferenceID |
| `UBL-CR-208` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party IndustryClassificationCode |
| `UBL-CR-209` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party Language |
| `UBL-CR-210` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress ID |
| `UBL-CR-211` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress AddressTypeCode |
| `UBL-CR-212` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress AddressFormatCode |
| `UBL-CR-213` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress Postbox |
| `UBL-CR-214` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress Floor |
| `UBL-CR-215` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress Room |
| `UBL-CR-216` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress BlockName |
| `UBL-CR-217` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress BuildingName |
| `UBL-CR-218` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress BuildingNumber |
| `UBL-CR-219` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress InhouseMail |
| `UBL-CR-220` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress Department |
| `UBL-CR-221` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress MarkAttention |
| `UBL-CR-222` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress MarkCare |
| `UBL-CR-223` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress PlotIdentification |
| `UBL-CR-224` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress CitySubdivisionName |
| `UBL-CR-225` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress CountrySubentityCode |
| `UBL-CR-226` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress Region |
| `UBL-CR-227` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress District |
| `UBL-CR-228` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress TimezoneOffset |
| `UBL-CR-229` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress Country Name |
| `UBL-CR-230` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PostalAddress LocationCoordinate |
| `UBL-CR-231` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PhysicalLocation |
| `UBL-CR-232` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme RegistrationName |
| `UBL-CR-233` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme TaxLevelCode |
| `UBL-CR-234` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme ExemptionReasonCode |
| `UBL-CR-235` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme ExemptionReason |
| `UBL-CR-236` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme RegistrationAddress |
| `UBL-CR-237` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme TaxScheme Name |
| `UBL-CR-238` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme TaxScheme TaxTypeCode |
| `UBL-CR-239` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme TaxScheme CurrencyCode |
| `UBL-CR-240` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyTaxScheme TaxScheme JurisdictionRegionAddress |
| `UBL-CR-241` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity RegistrationDate |
| `UBL-CR-242` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity RegistrationExpirationDate |
| `UBL-CR-243` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity CompanyLegalFormCode |
| `UBL-CR-244` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity CompanyLegalForm |
| `UBL-CR-245` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity SoleProprietorshipIndicator |
| `UBL-CR-246` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity CompanyLiquidationStatusCode |
| `UBL-CR-247` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity CorporateStockAmount |
| `UBL-CR-248` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity FullyPaidSharesIndicator |
| `UBL-CR-249` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity RegistrationAddress |
| `UBL-CR-250` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity CorporateRegistrationScheme |
| `UBL-CR-251` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity HeadOfficeParty |
| `UBL-CR-252` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PartyLegalEntity ShareholderParty |
| `UBL-CR-253` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party Contact ID |
| `UBL-CR-254` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party Contact Telefax |
| `UBL-CR-255` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party Contact Note |
| `UBL-CR-256` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party Contact OtherCommunication |
| `UBL-CR-257` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party Person |
| `UBL-CR-258` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party AgentParty |
| `UBL-CR-259` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party ServiceProviderParty |
| `UBL-CR-260` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party PowerOfAttorney |
| `UBL-CR-261` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty Party FinancialAccount |
| `UBL-CR-262` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty DeliveryContact |
| `UBL-CR-263` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty AccountingContact |
| `UBL-CR-264` | EN16931 | warning |  | A UBL invoice should not include the AccountingCustomerParty BuyerContact |
| `UBL-CR-265` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty MarkCareIndicator |
| `UBL-CR-266` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty MarkAttentionIndicator |
| `UBL-CR-267` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty WebsiteURI |
| `UBL-CR-268` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty LogoReferenceID |
| `UBL-CR-269` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty EndpointID |
| `UBL-CR-270` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty IndustryClassificationCode |
| `UBL-CR-271` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty Language |
| `UBL-CR-272` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PostalAddress |
| `UBL-CR-273` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PhysicalLocation |
| `UBL-CR-274` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyTaxScheme |
| `UBL-CR-275` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity RegistrationName |
| `UBL-CR-276` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity RegistrationDate |
| `UBL-CR-277` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity RegistrationExpirationDate |
| `UBL-CR-278` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity CompanyLegalFormCode |
| `UBL-CR-279` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity CompanyLegalForm |
| `UBL-CR-280` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity SoleProprietorshipIndicator |
| `UBL-CR-281` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity CompanyLiquidationStatusCode |
| `UBL-CR-282` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity CorporateStockAmount |
| `UBL-CR-283` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity FullyPaidSharesIndicator |
| `UBL-CR-284` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity RegistrationAddress |
| `UBL-CR-285` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity CorporateRegistrationScheme |
| `UBL-CR-286` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity HeadOfficeParty |
| `UBL-CR-287` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PartyLegalEntity ShareholderParty |
| `UBL-CR-288` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty Contact |
| `UBL-CR-289` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty Person |
| `UBL-CR-290` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty AgentParty |
| `UBL-CR-291` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty ServiceProviderParty |
| `UBL-CR-292` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty PowerOfAttorney |
| `UBL-CR-293` | EN16931 | warning |  | A UBL invoice should not include the PayeeParty FinancialAccount |
| `UBL-CR-294` | EN16931 | warning |  | A UBL invoice should not include the BuyerCustomerParty |
| `UBL-CR-295` | EN16931 | warning |  | A UBL invoice should not include the SellerSupplierParty |
| `UBL-CR-296` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty MarkCareIndicator |
| `UBL-CR-297` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty MarkAttentionIndicator |
| `UBL-CR-298` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty WebsiteURI |
| `UBL-CR-299` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty LogoReferenceID |
| `UBL-CR-300` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty EndpointID |
| `UBL-CR-301` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty IndustryClassificationCode |
| `UBL-CR-302` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyIdentification |
| `UBL-CR-303` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty Language |
| `UBL-CR-304` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress ID |
| `UBL-CR-305` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress AddressTypeCode |
| `UBL-CR-306` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress AddressFormatCode |
| `UBL-CR-307` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress Postbox |
| `UBL-CR-308` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress Floor |
| `UBL-CR-309` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress Room |
| `UBL-CR-310` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress BlockName |
| `UBL-CR-311` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress BuildingName |
| `UBL-CR-312` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress BuildingNumber |
| `UBL-CR-313` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress InhouseMail |
| `UBL-CR-314` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress Department |
| `UBL-CR-315` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress MarkAttention |
| `UBL-CR-316` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress MarkCare |
| `UBL-CR-317` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress PlotIdentification |
| `UBL-CR-318` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress CitySubdivisionName |
| `UBL-CR-319` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress CountrySubentityCode |
| `UBL-CR-320` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress Region |
| `UBL-CR-321` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress District |
| `UBL-CR-322` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress TimezoneOffset |
| `UBL-CR-323` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress Country Name |
| `UBL-CR-324` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PostalAddress LocationCoordinate |
| `UBL-CR-325` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PhysicalLocation |
| `UBL-CR-326` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme RegistrationName |
| `UBL-CR-327` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme TaxLevelCode |
| `UBL-CR-328` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme ExemptionReasonCode |
| `UBL-CR-329` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme ExemptionReason |
| `UBL-CR-330` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme RegistrationAddress |
| `UBL-CR-331` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme TaxScheme Name |
| `UBL-CR-332` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme TaxScheme TaxTypeCode |
| `UBL-CR-333` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme TaxScheme CurrencyCode |
| `UBL-CR-334` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyTaxScheme TaxScheme JurisdictionRegionAddress |
| `UBL-CR-335` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PartyLegalEntity |
| `UBL-CR-336` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty Contact |
| `UBL-CR-337` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty Person |
| `UBL-CR-338` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty AgentParty |
| `UBL-CR-339` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty ServiceProviderParty |
| `UBL-CR-340` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty PowerOfAttorney |
| `UBL-CR-341` | EN16931 | warning |  | A UBL invoice should not include the TaxRepresentativeParty FinancialAccount |
| `UBL-CR-342` | EN16931 | warning |  | A UBL invoice should not include the Delivery ID |
| `UBL-CR-343` | EN16931 | warning |  | A UBL invoice should not include the Delivery Quantity |
| `UBL-CR-344` | EN16931 | warning |  | A UBL invoice should not include the Delivery MinimumQuantity |
| `UBL-CR-345` | EN16931 | warning |  | A UBL invoice should not include the Delivery MaximumQuantity |
| `UBL-CR-346` | EN16931 | warning |  | A UBL invoice should not include the Delivery ActualDeliveryTime |
| `UBL-CR-347` | EN16931 | warning |  | A UBL invoice should not include the Delivery LatestDeliveryDate |
| `UBL-CR-348` | EN16931 | warning |  | A UBL invoice should not include the Delivery LatestDeliveryTime |
| `UBL-CR-349` | EN16931 | warning |  | A UBL invoice should not include the Delivery ReleaseID |
| `UBL-CR-350` | EN16931 | warning |  | A UBL invoice should not include the Delivery TrackingID |
| `UBL-CR-351` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Description |
| `UBL-CR-352` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Conditions |
| `UBL-CR-353` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation CountrySubentity |
| `UBL-CR-354` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation CountrySubentityCode |
| `UBL-CR-355` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation LocationTypeCode |
| `UBL-CR-356` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation InformationURI |
| `UBL-CR-357` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Name |
| `UBL-CR-358` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation ValidityPeriod |
| `UBL-CR-359` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address ID |
| `UBL-CR-360` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address AddressTypeCode |
| `UBL-CR-361` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address AddressFormatCode |
| `UBL-CR-362` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address Postbox |
| `UBL-CR-363` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address Floor |
| `UBL-CR-364` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address Room |
| `UBL-CR-365` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address BlockName |
| `UBL-CR-366` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address BuildingName |
| `UBL-CR-367` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address BuildingNumber |
| `UBL-CR-368` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address InhouseMail |
| `UBL-CR-369` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address Department |
| `UBL-CR-370` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address MarkAttention |
| `UBL-CR-371` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address MarkCare |
| `UBL-CR-372` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address PlotIdentification |
| `UBL-CR-373` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address CitySubdivisionName |
| `UBL-CR-374` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address CountrySubentityCode |
| `UBL-CR-375` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address Region |
| `UBL-CR-376` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address District |
| `UBL-CR-377` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address TimezoneOffset |
| `UBL-CR-378` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address Country Name |
| `UBL-CR-379` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation Address LocationCoordinate |
| `UBL-CR-380` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation SubsidiaryLocation |
| `UBL-CR-381` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryLocation LocationCoordinate |
| `UBL-CR-382` | EN16931 | warning |  | A UBL invoice should not include the Delivery AlternativeDeliveryLocation |
| `UBL-CR-383` | EN16931 | warning |  | A UBL invoice should not include the Delivery RequestedDeliveryPeriod |
| `UBL-CR-384` | EN16931 | warning |  | A UBL invoice should not include the Delivery EstimatedDeliveryPeriod |
| `UBL-CR-385` | EN16931 | warning |  | A UBL invoice should not include the Delivery CarrierParty |
| `UBL-CR-386` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty MarkCareIndicator |
| `UBL-CR-387` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty MarkAttentionIndicator |
| `UBL-CR-388` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty WebsiteURI |
| `UBL-CR-389` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty LogoReferenceID |
| `UBL-CR-390` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty EndpointID |
| `UBL-CR-391` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty IndustryClassificationCode |
| `UBL-CR-392` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty PartyIdentification |
| `UBL-CR-393` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty Language |
| `UBL-CR-394` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty PostalAddress |
| `UBL-CR-395` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty PhysicalLocation |
| `UBL-CR-396` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty PartyTaxScheme |
| `UBL-CR-397` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty PartyLegalEntity |
| `UBL-CR-398` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty Contact |
| `UBL-CR-399` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty Person |
| `UBL-CR-400` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty AgentParty |
| `UBL-CR-401` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty ServiceProviderParty |
| `UBL-CR-402` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty PowerOfAttorney |
| `UBL-CR-403` | EN16931 | warning |  | A UBL invoice should not include the DeliveryParty FinancialAccount |
| `UBL-CR-404` | EN16931 | warning |  | A UBL invoice should not include the Delivery NotifyParty |
| `UBL-CR-405` | EN16931 | warning |  | A UBL invoice should not include the Delivery Despatch |
| `UBL-CR-406` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryTerms |
| `UBL-CR-407` | EN16931 | warning |  | A UBL invoice should not include the Delivery MinimumDeliveryUnit |
| `UBL-CR-408` | EN16931 | warning |  | A UBL invoice should not include the Delivery MaximumDeliveryUnit |
| `UBL-CR-409` | EN16931 | warning |  | A UBL invoice should not include the Delivery Shipment |
| `UBL-CR-410` | EN16931 | warning |  | A UBL invoice should not include the DeliveryTerms |
| `UBL-CR-411` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans ID |
| `UBL-CR-412` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentDueDate |
| `UBL-CR-413` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentChannelCode |
| `UBL-CR-414` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans InstructionID |
| `UBL-CR-415` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CardAccount CardTypeCode |
| `UBL-CR-416` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CardAccount ValidityStartDate |
| `UBL-CR-417` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CardAccount ExpiryDate |
| `UBL-CR-418` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CardAccount IssuerID |
| `UBL-CR-419` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CardAccount IssueNumberID |
| `UBL-CR-420` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CardAccount CV2ID |
| `UBL-CR-421` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CardAccount CardChipCode |
| `UBL-CR-422` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CardAccount ChipApplicationID |
| `UBL-CR-424` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount AliasName |
| `UBL-CR-425` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount AccountTypeCode |
| `UBL-CR-426` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount AccountFormatCode |
| `UBL-CR-427` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount CurrencyCode |
| `UBL-CR-428` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount PaymentNote |
| `UBL-CR-429` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount FinancialInstitutionBranch Name |
| `UBL-CR-430` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount FinancialInstitutionBranch FinancialInstitution Name |
| `UBL-CR-431` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount FinancialInstitutionBranch FinancialInstitution Address |
| `UBL-CR-432` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount FinancialInstitutionBranch Address |
| `UBL-CR-433` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PayeeFinancialAccount Country |
| `UBL-CR-434` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans CreditAccount |
| `UBL-CR-435` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate MandateTypeCode |
| `UBL-CR-436` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate MaximumPaymentInstructionsNumeric |
| `UBL-CR-437` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate MaximumPaidAmount |
| `UBL-CR-438` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate SignatureID |
| `UBL-CR-439` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerParty |
| `UBL-CR-440` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerFinancialAccount Name |
| `UBL-CR-441` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerFinancialAccount AliasName |
| `UBL-CR-442` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerFinancialAccount AccountTypeCode |
| `UBL-CR-443` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerFinancialAccount AccountFormatCode |
| `UBL-CR-444` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerFinancialAccount CurrencyCode |
| `UBL-CR-445` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerFinancialAccount PaymentNote |
| `UBL-CR-446` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerFinancialAccount FinancialInstitutionBranch |
| `UBL-CR-447` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PayerFinancialAccount Country |
| `UBL-CR-448` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate ValidityPeriod |
| `UBL-CR-449` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate PaymentReversalPeriod |
| `UBL-CR-450` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans PaymentMandate Clause |
| `UBL-CR-451` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans TradeFinancing |
| `UBL-CR-452` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms ID |
| `UBL-CR-453` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms PaymentMeansID |
| `UBL-CR-454` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms PrepaidPaymentReferenceID |
| `UBL-CR-455` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms ReferenceEventCode |
| `UBL-CR-456` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms SettlementDiscountPercent |
| `UBL-CR-457` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms PenaltySurchargePercent |
| `UBL-CR-458` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms PaymentPercent |
| `UBL-CR-459` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms Amount |
| `UBL-CR-460` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms SettlementDiscountAmount |
| `UBL-CR-461` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms PenaltyAmount |
| `UBL-CR-462` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms PaymentTermsDetailsURI |
| `UBL-CR-463` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms PaymentDueDate |
| `UBL-CR-464` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms InstallmentDueDate |
| `UBL-CR-465` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms InvoicingPartyReference |
| `UBL-CR-466` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms SettlementPeriod |
| `UBL-CR-467` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms PenaltyPeriod |
| `UBL-CR-468` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms ExchangeRate |
| `UBL-CR-469` | EN16931 | warning |  | A UBL invoice should not include the PaymentTerms ValidityPeriod |
| `UBL-CR-470` | EN16931 | warning |  | A UBL invoice should not include the PrepaidPayment |
| `UBL-CR-471` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge ID |
| `UBL-CR-472` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge PrepaidIndicator |
| `UBL-CR-473` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge SequenceNumeric |
| `UBL-CR-474` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge AccountingCostCode |
| `UBL-CR-475` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge AccountingCost |
| `UBL-CR-476` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge PerUnitAmount |
| `UBL-CR-477` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory Name |
| `UBL-CR-478` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory BaseUnitMeasure |
| `UBL-CR-479` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory PerUnitAmount |
| `UBL-CR-480` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory TaxExemptionReasonCode |
| `UBL-CR-481` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory TaxExemptionReason |
| `UBL-CR-482` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory TierRange |
| `UBL-CR-483` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory TierRatePercent |
| `UBL-CR-484` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory TaxScheme Name |
| `UBL-CR-485` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory TaxScheme TaxTypeCode |
| `UBL-CR-486` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory TaxScheme CurrencyCode |
| `UBL-CR-487` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxCategory TaxScheme JurisdictionRegionAddress |
| `UBL-CR-488` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge TaxTotal |
| `UBL-CR-489` | EN16931 | warning |  | A UBL invoice should not include the AllowanceCharge PaymentMeans |
| `UBL-CR-490` | EN16931 | warning |  | A UBL invoice should not include the TaxExchangeRate |
| `UBL-CR-491` | EN16931 | warning |  | A UBL invoice should not include the PricingExchangeRate |
| `UBL-CR-492` | EN16931 | warning |  | A UBL invoice should not include the PaymentExchangeRate |
| `UBL-CR-493` | EN16931 | warning |  | A UBL invoice should not include the PaymentAlternativeExchangeRate |
| `UBL-CR-494` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal RoundingAmount |
| `UBL-CR-495` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxEvidenceIndicator |
| `UBL-CR-496` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxIncludedIndicator |
| `UBL-CR-497` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal CalulationSequenceNumeric |
| `UBL-CR-498` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TransactionCurrencyTaxAmount |
| `UBL-CR-499` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal Percent |
| `UBL-CR-500` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal BaseUnitMeasure |
| `UBL-CR-501` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal PerUnitAmount |
| `UBL-CR-502` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TierRange |
| `UBL-CR-503` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TierRatePercent |
| `UBL-CR-504` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory Name |
| `UBL-CR-505` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory BaseUnitMeasure |
| `UBL-CR-506` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory PerUnitAmount |
| `UBL-CR-507` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory TierRange |
| `UBL-CR-508` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory TierRatePercent |
| `UBL-CR-509` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory TaxScheme Name |
| `UBL-CR-510` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory TaxScheme TaxTypeCode |
| `UBL-CR-511` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory TaxScheme CurrencyCode |
| `UBL-CR-512` | EN16931 | warning |  | A UBL invoice should not include the TaxTotal TaxSubtotal TaxCategory TaxScheme JurisdictionRegionAddress |
| `UBL-CR-513` | EN16931 | warning |  | A UBL invoice should not include the WithholdingTaxTotal |
| `UBL-CR-514` | EN16931 | warning |  | A UBL invoice should not include the LegalMonetaryTotal PayableAlternativeAmount |
| `UBL-CR-515` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine UUID |
| `UBL-CR-516` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine TaxPointDate |
| `UBL-CR-517` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AccountingCostCode |
| `UBL-CR-518` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine PaymentPurposeCode |
| `UBL-CR-519` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine FreeOfChargeIndicator |
| `UBL-CR-520` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine InvoicePeriod StartTime |
| `UBL-CR-521` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine InvoicePeriod EndTime |
| `UBL-CR-522` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine InvoicePeriod DurationMeasure |
| `UBL-CR-523` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine InvoicePeriod DescriptionCode |
| `UBL-CR-524` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine InvoicePeriod Description |
| `UBL-CR-525` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine OrderLineReference SalesOrderLineID |
| `UBL-CR-526` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine OrderLineReference UUID |
| `UBL-CR-527` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine OrderLineReference LineStatusCode |
| `UBL-CR-528` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine OrderLineReference OrderReference |
| `UBL-CR-529` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DespatchLineReference |
| `UBL-CR-530` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine ReceiptLineReference |
| `UBL-CR-531` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine BillingReference |
| `UBL-CR-532` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference CopyIndicator |
| `UBL-CR-533` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference UUID |
| `UBL-CR-534` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference IssueDate |
| `UBL-CR-535` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference IssueTime |
| `UBL-CR-537` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference DocumentType |
| `UBL-CR-538` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference Xpath |
| `UBL-CR-539` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference LanguageID |
| `UBL-CR-540` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference LocaleCode |
| `UBL-CR-541` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference VersionID |
| `UBL-CR-542` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference DocumentStatusCode |
| `UBL-CR-543` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference DocumentDescription |
| `UBL-CR-544` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference Attachment |
| `UBL-CR-545` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference ValidityPeriod |
| `UBL-CR-546` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference IssuerParty |
| `UBL-CR-547` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DocumentReference ResultOfVerification |
| `UBL-CR-548` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine PricingReference |
| `UBL-CR-549` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine OriginatorParty |
| `UBL-CR-550` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Delivery |
| `UBL-CR-551` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine PaymentTerms |
| `UBL-CR-552` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge ID |
| `UBL-CR-553` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge PrepaidIndicator |
| `UBL-CR-554` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge SequenceNumeric |
| `UBL-CR-555` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge AccountingCostCode |
| `UBL-CR-556` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge AccountingCost |
| `UBL-CR-557` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge PerUnitAmount |
| `UBL-CR-558` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge TaxCategory |
| `UBL-CR-559` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge TaxTotal |
| `UBL-CR-560` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine AllowanceCharge PaymentMeans |
| `UBL-CR-561` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine TaxTotal |
| `UBL-CR-562` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine WithholdingTaxTotal |
| `UBL-CR-563` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item PackQuantity |
| `UBL-CR-564` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item PackSizeNumeric |
| `UBL-CR-565` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item CatalogueIndicator |
| `UBL-CR-566` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item HazardousRiskIndicator |
| `UBL-CR-567` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalInformation |
| `UBL-CR-568` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Keyword |
| `UBL-CR-569` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item BrandName |
| `UBL-CR-570` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ModelName |
| `UBL-CR-571` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item BuyersItemIdentification ExtendedID |
| `UBL-CR-572` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item BuyersItemIdentification BarcodeSymbologyID |
| `UBL-CR-573` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item BuyersItemIdentification PhysicalAttribute |
| `UBL-CR-574` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item BuyersItemIdentification MeasurementDimension |
| `UBL-CR-575` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item BuyersItemIdentification IssuerParty |
| `UBL-CR-576` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item SellersItemIdentification ExtendedID |
| `UBL-CR-577` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item SellersItemIdentification BarcodeSymbologyID |
| `UBL-CR-578` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item SellersItemIdentification PhysicalAttribute |
| `UBL-CR-579` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item SellersItemIdentification MeasurementDimension |
| `UBL-CR-580` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item SellersItemIdentification IssuerParty |
| `UBL-CR-581` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ManufacturersItemIdentification |
| `UBL-CR-582` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item StandardItemIdentification ExtendedID |
| `UBL-CR-583` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item StandardItemIdentification BarcodeSymbologyID |
| `UBL-CR-584` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item StandardItemIdentification PhysicalAttribute |
| `UBL-CR-585` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item StandardItemIdentification MeasurementDimension |
| `UBL-CR-586` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item StandardItemIdentification IssuerParty |
| `UBL-CR-587` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item CatalogueItemIdentification |
| `UBL-CR-588` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemIdentification |
| `UBL-CR-589` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item CatalogueDocumentReference |
| `UBL-CR-590` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ItemSpecificationDocumentReference |
| `UBL-CR-591` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item OriginCountry Name |
| `UBL-CR-592` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item CommodityClassification NatureCode |
| `UBL-CR-593` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item CommodityClassification CargoTypeCode |
| `UBL-CR-594` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item CommodityClassification CommodityCode |
| `UBL-CR-595` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item TransactionConditions |
| `UBL-CR-596` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item HazardousItem |
| `UBL-CR-597` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory Name |
| `UBL-CR-598` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory BaseUnitMeasure |
| `UBL-CR-599` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory PerUnitAmount |
| `UBL-CR-600` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory TaxExemptionReasonCode |
| `UBL-CR-601` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory TaxExemptionReason |
| `UBL-CR-602` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory TierRange |
| `UBL-CR-603` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory TierRatePercent |
| `UBL-CR-604` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory TaxScheme Name |
| `UBL-CR-605` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory TaxScheme TaxTypeCode |
| `UBL-CR-606` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory TaxScheme CurrencyCode |
| `UBL-CR-607` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ClassifiedTaxCategory TaxScheme JurisdictionRegionAddress |
| `UBL-CR-608` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty ID |
| `UBL-CR-609` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty NameCode |
| `UBL-CR-610` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty TestMethod |
| `UBL-CR-611` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty ValueQuantity |
| `UBL-CR-612` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty ValueQualifier |
| `UBL-CR-613` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty ImportanceCode |
| `UBL-CR-614` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty ListValue |
| `UBL-CR-615` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty UsabilityPeriod |
| `UBL-CR-616` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty ItemPropertyGroup |
| `UBL-CR-617` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty RangeDimension |
| `UBL-CR-618` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item AdditionalItemProperty ItemPropertyRange |
| `UBL-CR-619` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ManufacturerParty |
| `UBL-CR-620` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item InformationContentProviderParty |
| `UBL-CR-621` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item OriginAddress |
| `UBL-CR-622` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item ItemInstance |
| `UBL-CR-623` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Certificate |
| `UBL-CR-624` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Dimension |
| `UBL-CR-625` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price PriceChangeReason |
| `UBL-CR-626` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price PriceTypeCode |
| `UBL-CR-627` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price PriceType |
| `UBL-CR-628` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price OrderableUnitFactorRate |
| `UBL-CR-629` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price ValidityPeriod |
| `UBL-CR-630` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price PriceList |
| `UBL-CR-632` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge ID |
| `UBL-CR-633` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge AllowanceChargeReasonCode |
| `UBL-CR-634` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge AllowanceChargeReason |
| `UBL-CR-635` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge MultiplierFactorNumeric |
| `UBL-CR-636` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge PrepaidIndicator |
| `UBL-CR-637` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge SequenceNumeric |
| `UBL-CR-638` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge AccountingCostCode |
| `UBL-CR-639` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge AccountingCost |
| `UBL-CR-640` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge PerUnitAmount |
| `UBL-CR-641` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge TaxCategory |
| `UBL-CR-642` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge TaxTotal |
| `UBL-CR-643` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price AllowanceCharge PaymentMeans |
| `UBL-CR-644` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine Item Price PricingExchangeRate |
| `UBL-CR-645` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine DeliveryTerms |
| `UBL-CR-646` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine SubInvoiceLine |
| `UBL-CR-647` | EN16931 | warning |  | A UBL invoice should not include the InvoiceLine ItemPriceExtension |
| `UBL-CR-648` | EN16931 | warning |  | A UBL invoice should not include the CustomizationID scheme identifier |
| `UBL-CR-649` | EN16931 | warning |  | A UBL invoice should not include the ProfileID scheme identifier |
| `UBL-CR-650` | EN16931 | warning |  | A UBL invoice shall not include the Invoice ID scheme identifier |
| `UBL-CR-651` | EN16931 | warning |  | A UBL invoice should not include the SalesOrderID scheme identifier |
| `UBL-CR-652` | EN16931 | warning |  | A UBL invoice should not include the PartyTaxScheme CompanyID scheme identifier |
| `UBL-CR-653` | EN16931 | warning |  | A UBL invoice should not include the PaymentID scheme identifier |
| `UBL-CR-654` | EN16931 | warning |  | A UBL invoice should not include the PayeeFinancialAccount scheme identifier |
| `UBL-CR-655` | EN16931 | warning |  | A UBL invoice shall not include the FinancialInstitutionBranch ID scheme identifier |
| `UBL-CR-656` | EN16931 | warning |  | A UBL invoice should not include the InvoiceTypeCode listID |
| `UBL-CR-657` | EN16931 | warning |  | A UBL invoice should not include the DocumentCurrencyCode listID |
| `UBL-CR-658` | EN16931 | warning |  | A UBL invoice should not include the TaxCurrencyCode listID |
| `UBL-CR-659` | EN16931 | warning |  | A UBL invoice shall not include the AdditionalDocumentReference DocumentTypeCode listID |
| `UBL-CR-660` | EN16931 | warning |  | A UBL invoice should not include the Country Identification code listID |
| `UBL-CR-661` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeansCode listID |
| `UBL-CR-662` | EN16931 | warning |  | A UBL invoice should not include the AllowanceChargeReasonCode listID |
| `UBL-CR-663` | EN16931 | warning |  | A UBL invoice should not include the unitCodeListID |
| `UBL-CR-664` | EN16931 | warning |  | A UBL invoice should not include the FinancialInstitutionBranch FinancialInstitution |
| `UBL-CR-665` | EN16931 | warning |  | A UBL invoice should not include the AdditionalDocumentReference ID schemeID unless the DocumentTypeCode equals '130' |
| `UBL-CR-666` | EN16931 | fatal |  | A UBL invoice shall not include an AdditionalDocumentReference simultaneously referring an Invoice Object Identifier and an Attachment |
| `UBL-CR-667` | EN16931 | warning |  | A UBL invoice should not include a Buyer Item Identification schemeID |
| `UBL-CR-668` | EN16931 | warning |  | A UBL invoice should not include a Sellers Item Identification schemeID |
| `UBL-CR-669` | EN16931 | warning |  | A UBL invoice should not include a Price Allowance Reason Code |
| `UBL-CR-670` | EN16931 | warning |  | A UBL invoice should not include a Price Allowance Reason |
| `UBL-CR-671` | EN16931 | warning |  | A UBL invoice should not include a Price Allowance Multiplier Factor |
| `UBL-CR-672` | EN16931 | warning |  | A UBL credit note should not include the CreditNoteTypeCode listID |
| `UBL-CR-673` | EN16931 | fatal |  | A UBL invoice shall not include an AdditionalDocumentReference simultaneously referring an Invoice Object Identifier and an Document Description |
| `UBL-CR-674` | EN16931 | warning |  | A UBL invoice should not include the PrimaryAccountNumber schemeID |
| `UBL-CR-675` | EN16931 | warning |  | A UBL invoice should not include the NetworkID schemeID |
| `UBL-CR-676` | EN16931 | warning |  | A UBL invoice should not include the PaymentMandate/ID schemeID |
| `UBL-CR-677` | EN16931 | warning |  | A UBL invoice should not include the PayerFinancialAccount/ID schemeID |
| `UBL-CR-678` | EN16931 | warning |  | A UBL invoice should not include the TaxCategory/ID schemeID |
| `UBL-CR-679` | EN16931 | warning |  | A UBL invoice should not include the ClassifiedTaxCategory/ID schemeID |
| `UBL-CR-680` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans/PayerFinancialAccount |
| `UBL-CR-681` | EN16931 | warning |  | A UBL invoice should not include the PaymentMeans InstructionNote |
| `UBL-CR-682` | EN16931 | warning |  | A UBL invoice should not include the Delivery DeliveryAddress |
| `UBL-DT-01` | EN16931 | fatal | `BT-92`, `BT-93`, `BT-99`, `BT-100`, `BT-106`, `BT-107`, `BT-108`, `BT-109`, `BT-110`, `BT-111`, `BT-112`, `BT-113`, `BT-114`, `BT-115`, `BT-116`, `BT-117`, `BT-131`, `BT-136`, `BT-137`, `BT-141`, `BT-142` | Amounts shall be decimal up to two fraction digits |
| `UBL-DT-06` | EN16931 | fatal |  | Binary object elements shall contain the mime code attribute |
| `UBL-DT-07` | EN16931 | fatal |  | Binary object elements shall contain the file name attribute |
| `UBL-DT-08` | EN16931 | warning |  | Scheme name attribute should not be present |
| `UBL-DT-09` | EN16931 | warning |  | Scheme agency name attribute should not be present |
| `UBL-DT-10` | EN16931 | warning |  | Scheme data uri attribute should not be present |
| `UBL-DT-11` | EN16931 | warning |  | Scheme uri attribute should not be present |
| `UBL-DT-12` | EN16931 | warning |  | Format attribute should not be present |
| `UBL-DT-13` | EN16931 | warning |  | Unit code list identifier attribute should not be present |
| `UBL-DT-14` | EN16931 | warning |  | Unit code list agency identifier attribute should not be present |
| `UBL-DT-15` | EN16931 | warning |  | Unit code list agency name attribute should not be present |
| `UBL-DT-16` | EN16931 | warning |  | List agency name attribute should not be present |
| `UBL-DT-17` | EN16931 | warning |  | List name attribute should not be present |
| `UBL-DT-18` | EN16931 | warning |  | Name attribute should not be present |
| `UBL-DT-19` | EN16931 | warning |  | Language identifier attribute should not be present |
| `UBL-DT-20` | EN16931 | warning |  | List uri attribute should not be present |
| `UBL-DT-21` | EN16931 | warning |  | List scheme uri attribute should not be present |
| `UBL-DT-22` | EN16931 | warning |  | Language local identifier attribute should not be present |
| `UBL-DT-23` | EN16931 | warning |  | Uri attribute should not be present |
| `UBL-DT-24` | EN16931 | warning |  | Currency code list version id should not be present |
| `UBL-DT-25` | EN16931 | warning |  | CharacterSetCode attribute should not be present |
| `UBL-DT-26` | EN16931 | warning |  | EncodingCode attribute should not be present |
| `UBL-DT-27` | EN16931 | warning |  | Scheme Agency ID attribute should not be present |
| `UBL-DT-28` | EN16931 | warning |  | List Agency ID attribute should not be present |
| `UBL-SR-01` | EN16931 | fatal |  | Contract identifier shall occur maximum once. |
| `UBL-SR-02` | EN16931 | fatal |  | Receive advice identifier shall occur maximum once |
| `UBL-SR-03` | EN16931 | fatal |  | Despatch advice identifier shall occur maximum once |
| `UBL-SR-04` | EN16931 | fatal |  | Invoice object identifier shall occur maximum once |
| `UBL-SR-05` | EN16931 | fatal |  | Payment terms shall occur maximum once |
| `UBL-SR-06` | EN16931 | fatal |  | Preceding invoice reference shall occur maximum once |
| `UBL-SR-07` | EN16931 | fatal |  | If there is a preceding invoice reference, the preceding invoice number shall be present |
| `UBL-SR-08` | EN16931 | fatal |  | Invoice period shall occur maximum once |
| `UBL-SR-09` | EN16931 | fatal |  | Seller name shall occur maximum once |
| `UBL-SR-10` | EN16931 | fatal |  | Seller trader name shall occur maximum once |
| `UBL-SR-11` | EN16931 | fatal |  | Seller legal registration identifier shall occur maximum once |
| `UBL-SR-12` | EN16931 | fatal |  | Seller VAT identifier shall occur maximum once |
| `UBL-SR-13` | EN16931 | fatal |  | Seller tax registration shall occur maximum once |
| `UBL-SR-14` | EN16931 | fatal |  | Seller additional legal information shall occur maximum once |
| `UBL-SR-15` | EN16931 | fatal |  | Buyer name shall occur maximum once |
| `UBL-SR-16` | EN16931 | fatal |  | Buyer identifier shall occur maximum once |
| `UBL-SR-17` | EN16931 | fatal |  | Buyer legal registration identifier shall occur maximum once |
| `UBL-SR-18` | EN16931 | fatal |  | Buyer VAT identifier shall occur maximum once |
| `UBL-SR-19` | EN16931 | fatal |  | Payee name shall occur maximum once, if the Payee is different from the Seller |
| `UBL-SR-20` | EN16931 | fatal |  | Payee identifier shall occur maximum once, if the Payee is different from the Seller |
| `UBL-SR-21` | EN16931 | fatal |  | Payee legal registration identifier shall occur maximum once, if the Payee is different from the Seller |
| `UBL-SR-22` | EN16931 | fatal |  | Seller tax representative name shall occur maximum once, if the Seller has a tax representative |
| `UBL-SR-23` | EN16931 | fatal |  | Seller tax representative VAT identifier shall occur maximum once, if the Seller has a tax representative |
| `UBL-SR-24` | EN16931 | fatal |  | Deliver to information shall occur maximum once |
| `UBL-SR-25` | EN16931 | fatal |  | Deliver to party name shall occur maximum once |
| `UBL-SR-26` | EN16931 | fatal |  | Payment reference shall occur maximum once |
| `UBL-SR-27` | EN16931 | fatal |  | Payment means text shall occur maximum once |
| `UBL-SR-28` | EN16931 | fatal |  | Mandate reference identifier shall occur maximum once |
| `UBL-SR-29` | EN16931 | fatal |  | Bank creditor reference shall occur maximum once |
| `UBL-SR-30` | EN16931 | fatal |  | Document level allowance reason shall occur maximum once |
| `UBL-SR-31` | EN16931 | fatal |  | Document level charge reason shall occur maximum once |
| `UBL-SR-32` | EN16931 | fatal |  | VAT exemption reason text shall occur maximum once |
| `UBL-SR-33` | EN16931 | fatal |  | Supporting document description shall occur maximum once |
| `UBL-SR-34` | EN16931 | fatal |  | Invoice line note shall occur maximum once |
| `UBL-SR-35` | EN16931 | fatal |  | Referenced purchase order line identifier shall occur maximum once |
| `UBL-SR-36` | EN16931 | fatal |  | Invoice line period shall occur maximum once |
| `UBL-SR-37` | EN16931 | fatal |  | Item price discount shall occur maximum once |
| `UBL-SR-39` | EN16931 | fatal |  | Project reference shall occur maximum once. |
| `UBL-SR-40` | EN16931 | fatal |  | Buyer trade name shall occur maximum once |
| `UBL-SR-42` | EN16931 | fatal |  | Party tax scheme shall occur maximum twice in accounting supplier party |
| `UBL-SR-43` | EN16931 | fatal |  | Scheme identifier shall only be used for invoiced object (document type code with value 130 or 50) |
| `UBL-SR-44` | EN16931 | fatal |  | An Invoice may only have one unique PaymentID, but the PaymentID may be used for multiple PaymentMeans |
| `UBL-SR-45` | EN16931 | fatal |  | Due Date shall occur maximum once |
| `UBL-SR-46` | EN16931 | fatal |  | Payment means text shall occur maximum once |
| `UBL-SR-47` | EN16931 | fatal |  | When there are more than one payment means code, they shall be equal |
| `UBL-SR-48` | EN16931 | fatal |  | Invoice lines shall have one and only one classified tax category. |
| `UBL-SR-49` | EN16931 | fatal |  | Value tax point date shall occur maximum once |
| `UBL-SR-50` | EN16931 | fatal |  | Item description shall occur maximum once |
| `UBL-SR-51` | EN16931 | fatal |  | An address can only have one third line. |
| `UBL-SR-52` | EN16931 | fatal |  | Document reference shall occur maximum once |
| `UBL-SR-53` | EN16931 | fatal |  | CompanyID (VAT Identifier) must be stated when providing the PartyTaxScheme/TaxScheme/ID. |
| `UBL-SR-54` | EN16931 | fatal | `BG-18` | An Invoice shall contain maximum one Payment Card account (BG-18). |
| `UBL-SR-55` | EN16931 | fatal | `BG-19` | An Invoice shall contain maximum one Payment Mandate (BG-19). |
| `PEPPOL-EN16931-R001` | Peppol in XRechnung | fatal | `BT-23` | Business process MUST be provided. |
| `PEPPOL-EN16931-R005` | Peppol in XRechnung | fatal | `BT-6` | VAT accounting currency code MUST be different from invoice currency code when provided. |
| `PEPPOL-EN16931-R008` | Peppol in XRechnung | fatal |  | Document MUST not contain empty elements. |
| `PEPPOL-EN16931-R010` | Peppol in XRechnung | fatal | `BT-49` | Buyer electronic address MUST be provided |
| `PEPPOL-EN16931-R020` | Peppol in XRechnung | fatal | `BT-34` | Seller electronic address MUST be provided |
| `PEPPOL-EN16931-R040` | Peppol in XRechnung | fatal | `BT-92`, `BT-99`, `BT-136`, `BT-141` | Allowance/charge amount must equal base amount * percentage/100 if base amount and percentage exists |
| `PEPPOL-EN16931-R041` | Peppol in XRechnung | fatal | `BT-93`, `BT-100`, `BT-137`, `BT-142` | Allowance/charge base amount MUST be provided when allowance/charge percentage is provided. |
| `PEPPOL-EN16931-R042` | Peppol in XRechnung | fatal | `BT-94`, `BT-101`, `BT-138`, `BT-143` | Allowance/charge percentage MUST be provided when allowance/charge base amount is provided. |
| `PEPPOL-EN16931-R043` | Peppol in XRechnung | fatal |  | Allowance/charge ChargeIndicator value MUST equal 'true' or 'false' |
| `PEPPOL-EN16931-R043-1` | Peppol in XRechnung | fatal |  | Allowance/charge ChargeIndicator value MUST equal 'true' or 'false' |
| `PEPPOL-EN16931-R043-2` | Peppol in XRechnung | fatal |  | Allowance/charge ChargeIndicator value MUST equal 'true' or 'false' |
| `PEPPOL-EN16931-R044` | Peppol in XRechnung | fatal |  | Charge on price level is NOT allowed. Only value 'false' allowed. |
| `PEPPOL-EN16931-R046` | Peppol in XRechnung | fatal | `BT-146` | Item net price MUST equal (Gross price - Allowance amount) when gross price is provided. |
| `PEPPOL-EN16931-R053` | Peppol in XRechnung | fatal | `BG-23` | CII: No more than one tax total amount must be provided where currency id equals document currency code.<br>UBL: Only one tax total with tax subtotals MUST be provided. |
| `PEPPOL-EN16931-R054` | Peppol in XRechnung | fatal | `BT-6` | CII: Only one tax total amount must be provided where currency id equals tax currency code, if tax currency code (BT-6) is provided.<br>UBL: Only one tax total without tax subtotals MUST be provided when tax currency code is provided. |
| `PEPPOL-EN16931-R055` | Peppol in XRechnung | fatal | `BT-6` | Invoice total VAT amount and Invoice total VAT amount in accounting currency MUST have the same operational sign |
| `PEPPOL-EN16931-R061` | Peppol in XRechnung | fatal | `BT-89` | Mandate reference MUST be provided for direct debit. |
| `PEPPOL-EN16931-R101` | Peppol in XRechnung | fatal |  | CII: Element Additional referenced document can only be used for Invoice line object.<br>UBL: Element Document reference can only be used for Invoice line object |
| `PEPPOL-EN16931-R110` | Peppol in XRechnung | fatal | `BT-134` | Start date of line period MUST be within invoice period. |
| `PEPPOL-EN16931-R111` | Peppol in XRechnung | fatal | `BT-135` | End date of line period MUST be within invoice period. |
| `PEPPOL-EN16931-R120` | Peppol in XRechnung | warning | `BT-131` | Invoice line net amount MUST equal (Invoiced quantity * (Item net price/item price base quantity) + Sum of invoice line charge amount - sum of invoice line allowance amount |
| `PEPPOL-EN16931-R121` | Peppol in XRechnung | fatal | `BT-149` | Base quantity MUST be a positive number above zero. |
| `PEPPOL-EN16931-R130` | Peppol in XRechnung | fatal |  | Unit code of price base quantity MUST be same as invoiced quantity. |
| `BR-DE-1` | XRechnung | fatal | `BG-16` | Eine Rechnung (INVOICE) muss Angaben zu "PAYMENT INSTRUCTIONS" (BG-16) enthalten. |
| `BR-DE-10` | XRechnung | fatal | `BG-15`, `BT-77` | Das Element "Deliver to city" (BT-77) muss übermittelt werden, wenn die Gruppe "DELIVER TO ADDRESS" (BG-15) übermittelt wird. |
| `BR-DE-11` | XRechnung | fatal | `BG-15`, `BT-78` | Das Element "Deliver to post code" (BT-78) muss übermittelt werden, wenn die Gruppe "DELIVER TO ADDRESS" (BG-15) übermittelt wird. |
| `BR-DE-14` | XRechnung | fatal | `BT-119` | Das Element "VAT category rate" (BT-119) muss übermittelt werden. |
| `BR-DE-15` | XRechnung | fatal | `BT-10` | Das Element "Buyer reference" (BT-10) muss übermittelt werden. |
| `BR-DE-16` | XRechnung | fatal | `BG-11`, `BT-31`, `BT-32` | Wenn in einer Rechnung die Steuercodes S, Z, E, AE, K, G, L oder M verwendet werden, muss mindestens eines der Elemente "Seller VAT identifier" (BT-31), "Seller tax registration identifier" (BT-32) oder "SELLER TAX REPRESENTATIVE PARTY" (BG-11) übermittelt werden. |
| `BR-DE-17` | XRechnung | warning | `BT-3` | Mit dem Element "Invoice type code" (BT-3) sollen ausschließlich folgende Codes aus der Codeliste UNTDID 1001 übermittelt werden: 326 (Partial invoice), 380 (Commercial invoice), 384 (Corrected invoice), 389 (Self-billed invoice) und 381 (Credit note),875 (Partial construction invoice), 876 (Partial final construction invoice), 877 (Final construction invoice). |
| `BR-DE-18` | XRechnung | fatal | `BT-20`, `BT-115` | CII: Skonto Zeilen in muessen diesem regulärem Ausdruck entsprechen: . Die Informationen zur Gewährung von Skonto müssen wie folgt im Element "Payment terms" (BT-20) übermittelt werden: Anzugeben ist im ersten Segment "SKONTO", im zweiten "TAGE=n", im dritten "PROZENT=n". Prozentzahlen sind ohne Vorzeichen sowie mit Punkt getrennt von zwei Nachkommastellen anzugeben. Liegt dem zu berechnenden Betrag nicht BT-115, "fälliger Betrag" zugrunde, sondern nur ein Teil des fälligen Betrags der Rechnung, ist der Grundwert zur Berechnung von Skonto als viertes Segment "BASISBETRAG=n" gemäß dem semantischen Datentypen Amount anzugeben. Jeder Eintrag beginnt mit einer #, die Segmente sind mit einer # getrennt und eine Zeile schließt mit einer # ab. Am Ende einer vollständigen Skontoangabe muss ein XML-konformer Zeilenumbruch folgen. Alle Angaben zur Gewährung von Skonto müssen in Großbuchstaben gemacht werden. Zusätzliches Whitespace (Leerzeichen, Tabulatoren oder Zeilenumbrüche) ist nicht zulässig. Andere Zeichen oder Texte als in den oberen Vorgaben genannt sind nicht zulässig.<br>UBL: Skonto Zeilen in müssen diesem regulärem Ausdruck entsprechen: . Die Informationen zur Gewährung von Skonto müssen wie folgt im Element "Payment terms" (BT-20) übermittelt werden: Anzugeben ist im ersten Segment "SKONTO", im zweiten "TAGE=n", im dritten "PROZENT=n". Prozentzahlen sind ohne Vorzeichen sowie mit Punkt getrennt von zwei Nachkommastellen anzugeben. Liegt dem zu berechnenden Betrag nicht BT-115, "fälliger Betrag" zugrunde, sondern nur ein Teil des fälligen Betrags der Rechnung, ist der Grundwert zur Berechnung von Skonto als viertes Segment "BASISBETRAG=n" gemäß dem semantischen Datentypen Amount anzugeben. Jeder Eintrag beginnt mit einer #, die Segmente sind mit einer # getrennt und eine Zeile schließt mit einer # ab. Am Ende einer vollständigen Skontoangabe muss ein XML-konformer Zeilenumbruch folgen. Alle Angaben zur Gewährung von Skonto müssen in Großbuchstaben gemacht werden. Zusätzliches Whitespace (Leerzeichen, Tabulatoren oder Zeilenumbrüche) ist nicht zulässig. Andere Zeichen oder Texte als in den oberen Vorgaben genannt sind nicht zulässig. |
| `BR-DE-19` | XRechnung | warning | `BT-81`, `BT-84` | "Payment account identifier" (BT-84) soll eine korrekte IBAN enthalten, wenn in "Payment means type code" (BT-81) mit dem Code 58 SEPA als Zahlungsmittel gefordert wird. |
| `BR-DE-2` | XRechnung | fatal | `BG-6` | Die Gruppe "SELLER CONTACT" (BG-6) muss übermittelt werden. |
| `BR-DE-20` | XRechnung | warning | `BT-81`, `BT-91` | "Debited account identifier" (BT-91) soll eine korrekte IBAN enthalten, wenn in "Payment means type code" (BT-81) mit dem Code 59 SEPA als Zahlungsmittel gefordert wird. |
| `BR-DE-21` | XRechnung | warning | `BT-24` | Das Element "Specification identifier" (BT-24) soll syntaktisch der Kennung des Standards XRechnung entsprechen. |
| `BR-DE-22` | XRechnung | fatal |  | CII: Not all filename attributes of the embeddedDocumentBinaryObject elements are unique<br>UBL: Das "filename"-Attribut aller "EmbeddedDocumentBinaryObject"-Elemente muss eindeutig sein |
| `BR-DE-23-a` | XRechnung | fatal | `BG-17`, `BT-81` | Wenn BT-81 "Payment means type code" einen Schlüssel für Überweisungen enthält (30, 58), muss BG-17 "CREDIT TRANSFER" übermittelt werden. |
| `BR-DE-23-b` | XRechnung | fatal | `BG-18`, `BG-19`, `BT-81` | Wenn BT-81 "Payment means type code" einen Schlüssel für Überweisungen enthält (30, 58), dürfen BG-18 und BG-19 nicht übermittelt werden. |
| `BR-DE-24-a` | XRechnung | fatal | `BG-18`, `BT-81` | Wenn BT-81 "Payment means type code" einen Schlüssel für Kartenzahlungen enthält (48, 54, 55), muss genau BG-18 "PAYMENT CARD INFORMATION" übermittelt werden. |
| `BR-DE-24-b` | XRechnung | fatal | `BG-17`, `BG-19`, `BT-81` | Wenn BT-81 "Payment means type code" einen Schlüssel für Kartenzahlungen enthält (48, 54, 55), dürfen BG-17 und BG-19 nicht übermittelt werden. |
| `BR-DE-25-a` | XRechnung | fatal | `BG-19`, `BT-81` | Wenn BT-81 "Payment means type code" einen Schlüssel für Lastschriften enthält (59), muss genau BG-19 "DIRECT DEBIT" übermittelt werden. |
| `BR-DE-25-b` | XRechnung | fatal | `BG-17`, `BG-18`, `BT-81` | Wenn BT-81 "Payment means type code" einen Schlüssel für Lastschriften enthält (59), dürfen BG-17 und BG-18 nicht übermittelt werden. |
| `BR-DE-26` | XRechnung | warning | `BG-3`, `BT-3` | CII: Wenn im Element Invoice type code (BT-3) der Code 384 (Corrected invoice) übergeben wird, soll PRECEDING INVOICE REFERENCE BG-3 mind. einmal vorhanden sein.<br>UBL: Wenn im Element "Invoice type code" (BT-3) der Code 384 (Corrected invoice) übergeben wird, soll PRECEDING INVOICE REFERENCE BG-3 mind. einmal vorhanden sein. |
| `BR-DE-27` | XRechnung | warning | `BT-42` | In BT-42 sollen mindestens drei Ziffern enthalten sein. |
| `BR-DE-28` | XRechnung | warning | `BT-43` | In BT-43 soll genau ein @-Zeichen enthalten sein, welches nicht von einem Leerzeichen, einem Punkt, aber mindestens zwei Zeichen auf beiden Seiten flankiert werden soll. Ein Punkt sollte nicht am Anfang oder am Ende stehen. |
| `BR-DE-3` | XRechnung | fatal | `BT-37` | Das Element "Seller city" (BT-37) muss übermittelt werden. |
| `BR-DE-30` | XRechnung | fatal | `BG-19`, `BT-90` | Wenn "DIRECT DEBIT" BG-19 vorhanden ist, dann muss "Bank assigned creditor identifier" BT-90 übermittelt werden. |
| `BR-DE-31` | XRechnung | fatal | `BG-19`, `BT-91` | Wenn "DIRECT DEBIT" BG-19 vorhanden ist, dann muss "Debited account identifier" BT-91 übermittelt werden. |
| `BR-DE-4` | XRechnung | fatal | `BT-38` | Das Element "Seller post code" (BT-38) muss übermittelt werden. |
| `BR-DE-5` | XRechnung | fatal | `BT-41` | Das Element "Seller contact point" (BT-41) muss übermittelt werden. |
| `BR-DE-6` | XRechnung | fatal | `BT-42` | Das Element "Seller contact telephone number" (BT-42) muss übermittelt werden. |
| `BR-DE-7` | XRechnung | fatal | `BT-43` | Das Element "Seller contact email address" (BT-43) muss übermittelt werden. |
| `BR-DE-8` | XRechnung | fatal | `BT-52` | Das Element "Buyer city" (BT-52) muss übermittelt werden. |
| `BR-DE-9` | XRechnung | fatal | `BT-53` | Das Element "Buyer post code" (BT-53) muss übermittelt werden. |
| `BR-DE-CVD-01` | XRechnung | fatal | `BT-12` | Das Element "Contract reference" (BT-12) muss übermittelt werden. |
| `BR-DE-CVD-02` | XRechnung | fatal | `BT-17` | Das Element "Tender or lot reference" (BT-17) muss übermittelt werden. |
| `BR-DE-CVD-03` | XRechnung | fatal | `BG-25`, `BT-158`, `BT-160` | In einer Rechnung muss mindestens eine INVOICE LINE (BG-25) enthalten sein, in der der Scheme identifier von "Item classification identifier" (BT-158) den Wert 'CVD' und der "Item attribute name" (BT-160) den Wert 'cva' enthält. |
| `BR-DE-CVD-04` | XRechnung | fatal | `BT-158` | Ein "Item classification identifier" (BT-158) mit dem Scheme identifier 'CVD' muss einen Wert aus der Liste der zulässigen Fahrzeugkategorien enthalten. |
| `BR-DE-CVD-05` | XRechnung | fatal | `BG-32`, `BT-160`, `BT-161` | Wenn innerhalb von ITEM ATTRIBUTES (BG-32) der "Item attribute name" (BT-160) den Wert 'cva' hat, muss der "Item attribute value" (BT-161) einen der zulässigen Werte enthalten. |
| `BR-DE-CVD-06-a` | XRechnung | fatal | `BT-158`, `BT-160` | Wenn der Scheme identifier von "Item classification identifier" (BT-158) mit dem Wert 'CVD' angegeben ist, muss in derselben Rechnungszeile genau ein "Item attribute name" (BT-160) mit dem Wert 'cva' vorhanden sein. |
| `BR-DE-CVD-06-b` | XRechnung | fatal | `BT-158`, `BT-160` | Wenn "Item attribute name" (BT-160) mit dem Wert 'cva' angegeben ist, muss in derselben Rechnungszeile genau ein "Item classification identifier" (BT-158) mit dem Scheme identifier 'CVD' vorhanden sein. |
| `BR-DE-TMP-32` | XRechnung | information | `BG-14`, `BG-26`, `BT-72` | Eine Rechnung sollte zur Angabe des Liefer-/Leistungsdatums entweder BT-72 "Actual delivery date", BG-14 "Invoicing period" oder in jeder Rechnungsposition BG-26 "Invoice line period" enthalten. |
| `BR-DEX-01` | XRechnung | fatal | `BT-125` | Das Element "Attached Document" (BT-125) benutzt einen nicht zulässigen MIME-Code: . Im Falle einer Extension darf zusätzlich zu der Liste der mime codes (definiert in Abschnitt 8.2, "Binary Object") der MIME-Code application/xml genutzt werden. |
| `BR-DEX-02` | XRechnung | warning | `BG-25`, `BT-131` | Der Wert von "Invoice line net amount" (BT-131) einer "INVOICE LINE" (BG-25) oder einer "SUB INVOICE LINE" (BG-DEX-01) soll der Summe der "Invoice line net amount" (BT-131) der direkt darunterliegenden "SUB INVOICE LINE" (BG-DEX-01) entsprechen. |
| `BR-DEX-03` | XRechnung | fatal |  | Eine Sub Invoice Line (BG-DEX-01) muss genau eine "SUB INVOICE LINE VAT INFORMATION" (BG-DEX-06) enthalten. |
| `BR-DEX-04` | XRechnung | fatal |  | Any scheme identifier in MUST be coded using one of the ISO 6523 ICD list. |
| `BR-DEX-05` | XRechnung | fatal |  | Any scheme identifier in MUST be coded using one of the ISO 6523 ICD list. |
| `BR-DEX-06` | XRechnung | fatal |  | Any scheme identifier in MUST be coded using one of the ISO 6523 ICD list. |
| `BR-DEX-07` | XRechnung | fatal |  | Any scheme identifier for an Endpoint Identifier in MUST belong to the CEF EAS code list. |
| `BR-DEX-08` | XRechnung | fatal |  | Any scheme identifier for a Delivery location identifier in MUST be coded using one of the ISO 6523 ICD list. |
| `BR-DEX-09` | XRechnung | fatal | `BT-112`, `BT-113`, `BT-114`, `BT-115` | Amount due for payment (BT-115) = Invoice total amount with VAT (BT-112) - Paid amount (BT-113) + Rounding amount (BT-114) + Σ Third party payment amount (BT-DEX-002). |
| `BR-DEX-10` | XRechnung | fatal |  | Das Element "Third party payment type" BT-DEX-001 muss übermittelt werden, wenn die Gruppe "THIRD PARTY PAYMENT" (BG-DEX-09) übermittelt wird. |
| `BR-DEX-11` | XRechnung | fatal |  | Das Element "Third party payment amount" BT-DEX-002 muss übermittelt werden, wenn die Gruppe "THIRD PARTY PAYMENT" (BG-DEX-09) übermittelt wird. |
| `BR-DEX-12` | XRechnung | fatal |  | Das Element "Third party payment description" BT-DEX-003 muss übermittelt werden, wenn die Gruppe "THIRD PARTY PAYMENT" (BG-DEX-09) übermittelt wird. |
| `BR-DEX-13` | XRechnung | fatal |  | Die maximale Anzahl zulässiger Nachkommastellen für das Element "Third party payment amount" (BT-DEX-002) ist 2. |
| `BR-DEX-14` | XRechnung | fatal | `BT-5` | Die Währungsangabe von "Third party payment amount" BT-DEX-002 muss BT-5 ("Invoice currency code") entsprechen. |
| `BR-DEX-15` | XRechnung | warning |  | This CII file might use the concept of Sub Invoice Lines. However XRechnung does not support this. |
| `BR-TMP-2` | XRechnung | warning | `BT-124` | BT-124 "External document location" muss eine absolute URL mit gültigem Schema enthalten. |
| `BR-TMP-3` | XRechnung | fatal | `BT-149`, `BT-150` | Wenn BT-149 (Item price base quantity) sowohl in GrossPriceProductTradePrice als auch in NetPriceProductTradePrice vorhanden ist, müssen die Werte identisch sein. Wenn BT-150 (unit of measure code) auf dem NetPrice-Pfad vorhanden ist, muss es auch auf dem GrossPrice-Pfad vorhanden und identisch sein. |
| `BR-TMP-CVD-01` | XRechnung | fatal | `BT-158` | Das Bildungsschema für "Item classification identifier" (BT-158) ist aus der Codeliste UNTDID 7143 zu wählen. |

## Ableitung

Die Datei wurde mit `skillbuilder/erechnung/generate_fehlercodes.py` erzeugt. Beispiel:

```bash
python3 skillbuilder/erechnung/generate_fehlercodes.py \
  --en16931-root /path/to/eInvoicing-EN16931 \
  --kosit-release-root /path/to/xrechnung-3.0.2-schematron-2.5.0 \
  --peppol-root /path/to/peppol-bis-invoice-3 \
  --output /path/to/validate-erechnung/references/fehlercodes.md
```

Beim Aktualisieren immer Tags, Commit und Release-Hash gemeinsam ändern und die generierte Datei erneut prüfen. Keine Sekundärquelle für Code-zu-BT-Zuordnungen verwenden.
