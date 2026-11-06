# Findings einordnen

Nur laden, wenn ein konkretes Finding unklar ist. Der Normalfall braucht diese
Datei nicht.

## Verdict

| Verdict | Bedeutung |
|---|---|
| `conformant` | XRechnung oder Factur-X/ZUGFeRD EN 16931 (Extended zählt mit), keine Engine-Fehler |
| `nonconformant` | Format erkannt, aber mindestens ein Finding in `errors` |
| `not_erechnung` | Keine E-Rechnung im Sinne des B2B-Mandats: Bild-PDF, fremdes XML, Profil Minimum/Basic |
| `tool_error` | Keine Prüfung: Java fehlt, Datei unlesbar, XML zu groß, interner Fehler |

Das Verdict beantwortet die Eignung für das deutsche B2B-Mandat, nicht reine
EN-16931-Konformität. Es wird nie aus Findings nachgerechnet oder überstimmt.

## Die drei Buckets

**Nur `errors` machen das Verdict `nonconformant`.** `warnings` und `notices`
ändern nichts. Verdict `conformant` mit zwölf Hinweisen ist kein
Widerspruch.

| Bucket | Herkunft | Wirkung |
|---|---|---|
| `errors` | fatale Schematron-Regel, Schemafehler, PDF/A-Verstoß | `nonconformant` |
| `warnings` | Regel mit Severity „warning“ | keine |
| `notices` | Zusatzprüfung, oft Regeln eines anderen Profils | keine |

## Check sections

`summary.sections` hat immer fünf Einträge: `schema`, `schematron`, `pdfa`,
`embedded_xml`, `metadata_embedding`. `applicable: false` heißt, der Check passt
nicht zur Eingabe (bei reinem XML z. B. `pdfa`). `status` ist der schlimmste
Schweregrad im Bereich: `ok`, `error`, `warning`, `notice`.

PDF/A und XML sind getrennte Urteile. Ein PDF kann `pdfa: error` haben und
trotzdem fehlerfreies XML enthalten. Beide Teilergebnisse nennen.

## Engines

- **mustang** läuft immer (Factur-X/ZUGFeRD-Schematron, Schema, PDF/A über das
  eingebettete veraPDF). veraPDF ist keine eigene Engine.
- **kosit** läuft nur, wenn das Profil (BT-24) XRechnung ist. KoSIT-Regeln
  werden nicht auf reine Factur-X-EN16931-Rechnungen angewandt.

Ein `BR-DE-*`-Hinweis auf einer Factur-X-EN16931-Rechnung heißt nur: Das
Dokument ist keine XRechnung. Erst `summary.profile` lesen, dann bewerten:

| `profile` | Dokument ist | `BR-DE-*` bedeutet |
|---|---|---|
| `urn:cen.eu:en16931:2017` | Factur-X/ZUGFeRD EN 16931 | nur: keine XRechnung |
| `urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0` | XRechnung 3.0 | echte Mängel |
| `…:factur-x.eu:1p0:basic` / `…:minimum` | reduziertes Profil | Verdict `not_erechnung` |

## Häufigster Fall: gar keine E-Rechnung

Ein gewöhnliches PDF ohne eingebettete Rechnungsdaten ergibt `not_erechnung`.
Das ist keine defekte E-Rechnung, sondern keine. Dem Nutzer genau so sagen.

## Finding-IDs und wo sie herkommen

| Präfix | Regelwerk | In `fehlercodes.md`? |
|---|---|---|
| `BR-…`, `BR-CO-…`, `BR-CL-…` | EN 16931 | ja |
| `BR-DE-…` | XRechnung-CIUS (KoSIT) | ja |
| `PEPPOL-EN16931-R…` | Peppol BIS Billing, von KoSIT übernommen | ja |
| `FX-SCH-…` | Factur-X/ZUGFeRD-Schematron, Codelisten | nein |
| `MUSTANG_<typ>` | Mustang-Diagnose ohne Regelkennung | nein |

Für die letzten beiden gibt es keine Tabelle. Die `message` wörtlich
wiedergeben. Details zu PDF/A-Verstößen (veraPDF-Klauseln) stehen nur im
Mustang-Prüfbericht, Feld `mustang-pruefbericht` in der JSON-Datei unter
`artifacts.json`.

## Rechenprüfung

Summen werden auf zwei Wegen geprüft, mit unterschiedlicher Wirkung:

| Finding | Was geprüft wird | Wirkung |
|---|---|---|
| `BR-CO-*` in `errors` | normative Summenregeln der EN 16931: Kopfsummen passen zueinander und zu den Positionssummen | `nonconformant` |
| `MUSTANG_10` in `warnings` | Mustangs eigene Nachrechnung aus den Positionen („Arithmetical issue: Payable total in XML is …, but calculated total is …“) | keine |

`MUSTANG_10` ändert das Verdict nicht, wird aber immer im Chat genannt, mit
beiden Beträgen aus der `message`. Typisch sind Rundungsdifferenzen von wenigen
Cent aus der Positionsberechnung. Als Hinweis an den Rechnungssteller
formulieren, nicht als Mangel. Nicht wegdiskutieren, nicht selbst
korrigieren.
