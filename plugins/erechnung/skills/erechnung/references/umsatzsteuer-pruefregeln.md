# Umsatzsteuerliche Plausibilitätsregeln für Rechnungen und E-Rechnungen

Stand: 22. September 2026. Im TAXLaw-Korpus-Release `20260910T100457Z`
recherchiert und gegen die verlinkten amtlichen Primärquellen abgeglichen. Dieses
Dokument ist ein **unverbindlicher technischer Prüfrahmen**. Es ist keine Steuer-
oder Rechtsberatung, ersetzt keine Prüfung des Geschäftsvorfalls und darf weder
eine Zahlungs- noch eine Buchungsfreigabe erzeugen.

## Ergebnislogik

Die steuerliche Plausibilitätsprüfung ist ein eigener Block neben dem
Verdict der technischen Prüfung:

- `D` – **deterministisch aus der Datei prüfbar**: Feld vorhanden, Wert formal
  plausibel, Rechenbeziehung oder ausdrücklich erklärte Steuerkategorie konsistent.
- `K` – **nur mit Kontext prüfbar**: als `warning` oder `not_checked` ausgeben, bis
  z. B. Leistungsart, Ansässigkeit, Unternehmereigenschaft oder Warenbewegung
  bestätigt ist.
- `X` – **nicht aus der Rechnung beweisbar**: externe oder betriebliche Prüfung
  nötig; nie als Fehler der Datei ausgeben.

Nur ein sicher anwendbares `D`-Kriterium darf `error` werden. Ein `K`-Befund darf
höchstens `warning`, ein `X`-Befund nur `notice/not_checked` sein. Die Ausgabe muss
Regel-ID, Befund, Fundstelle, Voraussetzung und Quelle nennen. Ohne bestätigten
Sachverhalt lautet das Ergebnis „steuerlich nicht abschließend prüfbar“, nicht
„steuerlich ungültig“.

## 1. Allgemeine Rechnungsangaben

| Regel-ID | Klasse | Prüfkriterium | Technische Auswertung | Quelle |
|---|---:|---|---|---|
| `DE-VAT-INV-001` | D | Vollständiger Name und vollständige Anschrift von Leistendem und Empfänger | Beide Parteien müssen identifizierbar sein. Inhaltliche Existenz/Richtigkeit bleibt `X`. | [§ 14 Abs. 4 Nr. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 31 Abs. 2 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__31.html) |
| `DE-VAT-INV-002` | D | Steuernummer **oder** USt-IdNr. des Leistenden | Mindestens eine der Alternativen muss vorhanden sein; bei Gutschrift ist die Kennung des leistenden Unternehmers maßgeblich. | [§ 14 Abs. 4 Nr. 2 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [UStAE 14.5](https://ao.bundesfinanzministerium.de/usth/2024/A-Umsatzsteuergesetz/IV-Steuer-und-Vorsteuer/Paragraf-14/ae-14-5.html) |
| `DE-VAT-INV-003` | D | Ausstellungsdatum | Muss vorhanden und ein gültiges Kalenderdatum sein. | [§ 14 Abs. 4 Nr. 3 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html) |
| `DE-VAT-INV-004` | D/X | Fortlaufende, einmalig vergebene Rechnungsnummer | Vorhandensein/Format `D`; Einmaligkeit über die Buchführung hinweg `X`. Ausnahmen siehe Kleinbetrag/Fahrausweis/Kleinunternehmer. | [§ 14 Abs. 4 Nr. 4 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [BMF 15.10.2025, UStAE 14.5 Abs. 14](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.html) |
| `DE-VAT-INV-005` | D/K | Menge und handelsübliche Art der Gegenstände bzw. Umfang und Art der Leistung | Leere oder rein generische Angabe ist ein Befund; ob die Beschreibung fachlich eindeutig ist, bleibt regelmäßig `K`. | [§ 14 Abs. 4 Nr. 5 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [UStAE 14.5](https://ao.bundesfinanzministerium.de/usth/2024/A-Umsatzsteuergesetz/IV-Steuer-und-Vorsteuer/Paragraf-14/ae-14-5.html) |
| `DE-VAT-INV-006` | D | Liefer-/Leistungszeitpunkt | Datum oder Kalendermonat genügt. Bei abweichendem vereinnahmtem (Teil-)Entgelt gelten die Anzahlungsregeln. | [§ 14 Abs. 4 Nr. 6 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 31 Abs. 4 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__31.html) |
| `DE-VAT-INV-007` | D | Entgelt nach Steuersätzen und Steuerbefreiungen; vereinbarte Minderungen | Summen und Gruppierungen müssen vollständig und rechnerisch konsistent sein. Nicht aus der Rechnung erkennbare Vereinbarungen bleiben `X`. | [§ 14 Abs. 4 Nr. 7 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html) |
| `DE-VAT-INV-008` | D/K | Steuersatz und Steuerbetrag **oder** Hinweis auf Steuerbefreiung | Formale Konsistenz `D`; ob Satz/Befreiung materiell richtig ist, `K`. Ein umgangssprachlicher Hinweis auf den Befreiungsgrund genügt; die Paragrafennennung ist nicht zwingend. | [§ 14 Abs. 4 Nr. 8 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [UStAE 14.5 Abs. 20](https://ao.bundesfinanzministerium.de/usth/2024/A-Umsatzsteuergesetz/IV-Steuer-und-Vorsteuer/Paragraf-14/ae-14-5.html) |
| `DE-VAT-INV-009` | D | Mehrere Steuersätze | Ein zusammengefasster Steuerbetrag ist bei maschineller Ermittlung zulässig, wenn jeder Position ihr Steuersatz zugeordnet ist. | [§ 32 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__32.html) |
| `DE-VAT-INV-010` | K | Rechnungsausstellung binnen sechs Monaten | Nur prüfen, wenn Leistung, Ausstellungsdatum und die Rechnungspflicht sicher bestimmt sind. Sonderfrist für innergemeinschaftliche Fälle siehe unten. | [§ 14 Abs. 2 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html) |
| `DE-VAT-INV-011` | X | Echtheit, Unversehrtheit, verlässlicher Prüfpfad | Benötigt Bestellung, Vertrag, Lieferschein, Zahlung oder interne Kontrollen; ein Dateicheck beweist dies nicht. | [§ 14 Abs. 3 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [BMF 15.10.2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.html) |
| `DE-VAT-INV-012` | K | Unrichtiger/unberechtigter Steuerausweis | Offen ausgewiesene Umsatzsteuer bei Reverse Charge, Steuerbefreiung oder fehlender Berechtigung als hohes Risiko melden; die materielle Steuerschuld nicht aus der Datei entscheiden. | [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html) |

Bei sonstigen Rechnungen dürfen sich die Pflichtangaben unter den Voraussetzungen
des § 31 Abs. 1 UStDV aus mehreren eindeutig bezeichneten Dokumenten ergeben. Bei
einer E-Rechnung müssen dagegen sämtliche umsatzsteuerlichen Pflichtangaben im
strukturierten Teil stehen; ein bloßer Verweis auf eine unstrukturierte Anlage oder
auf einen externen Link genügt nicht. Ergänzende Detailangaben dürfen in einer
eingebetteten Anlage stehen.

## 2. Vereinfachte Rechnungen

| Regel-ID | Klasse | Anwendungsfall und Mindestinhalt | Abgrenzung | Quelle |
|---|---:|---|---|---|
| `DE-VAT-SMALL-001` | D/K | Gesamtbetrag höchstens 250 EUR: Leistender mit Anschrift, Ausstellungsdatum, Art/Menge bzw. Umfang/Art, Bruttobetrag und Steuersatz oder Befreiungshinweis | Kein Empfänger, keine Rechnungsnummer und keine Steuer-ID zwingend. Nicht auf Umsätze nach §§ 3c, 6a oder 13b UStG anwenden. | [§ 33 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__33.html) |
| `DE-VAT-TICKET-001` | D/K | Personenfahrausweis: Beförderer mit Anschrift, Datum, Bruttobetrag; Steuersatz nur, soweit nicht der ermäßigte Satz nach § 12 Abs. 2 Nr. 10 UStG gilt; ggf. Luftverkehrshinweis | Bei grenzüberschreitender Personen-/internationaler Eisenbahnbeförderung ist zusätzlich eine Bescheinigung über Inlandsanteil und dessen Steuersatz erforderlich. | [§ 34 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__34.html) |
| `DE-VAT-KU-001` | D/K | Rechnung eines Kleinunternehmers: Parteien, Steuer-/USt-/KU-IdNr., Datum, Leistung, Gesamtentgelt und Hinweis auf die Steuerbefreiung nach § 19 UStG; ggf. „Gutschrift“ | Ob § 19 UStG tatsächlich anwendbar ist, bleibt `K/X`; kein gesonderter Steuerbetrag. | [§ 34a UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__34a.html) |

Diese drei Rechnungsarten können immer als sonstige Rechnung ausgestellt werden;
die Pflicht zur E-Rechnung greift für sie nicht. Eine freiwillige E-Rechnung bleibt
möglich.

## 3. Gutschrift, Korrektur, Anzahlungs- und Endrechnung

| Regel-ID | Klasse | Prüfkriterium | Technische Auswertung | Quelle |
|---|---:|---|---|---|
| `DE-VAT-SB-001` | D/K | Abrechnung wird vom Leistungsempfänger erstellt | Die Rechnung muss „Gutschrift“ oder eine anerkannte amtssprachliche Entsprechung wie „Self-billing“ enthalten. Vorherige Vereinbarung und fehlender Widerspruch sind `X`. | [§ 14 Abs. 2 und Abs. 4 Nr. 10 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [UStAE 14.3 und 14.5 Abs. 24](https://ao.bundesfinanzministerium.de/usth/2024/A-Umsatzsteuergesetz/IV-Steuer-und-Vorsteuer/Paragraf-14/inhalt.html) |
| `DE-VAT-SB-002` | D | Storno-/Korrekturbeleg des Leistenden | Nicht allein wegen eines negativen Betrags „Gutschrift“ verlangen: Die umgangssprachliche Korrekturgutschrift ist keine Gutschrift im Sinn des § 14 UStG. | [UStAE 14.3 Abs. 2](https://ao.bundesfinanzministerium.de/usth/2024/A-Umsatzsteuergesetz/IV-Steuer-und-Vorsteuer/Paragraf-14/inhalt.html) |
| `DE-VAT-CORR-001` | D/K | Berichtigung fehlender/unrichtiger Angaben | Korrekturdokument muss spezifisch und eindeutig auf die Ursprungsrechnung verweisen und die Form-/Inhaltsanforderungen erfüllen; eine neue Rechnungsnummer ist nicht erforderlich. Wirksamkeit/Urheberschaft bleibt `K/X`. | [§ 31 Abs. 5 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__31.html), [UStAE 14.11](https://ao.bundesfinanzministerium.de/usth/2024/A-Umsatzsteuergesetz/IV-Steuer-und-Vorsteuer/Paragraf-14/inhalt.html) |
| `DE-VAT-ADV-001` | D/K | Rechnung vor Leistung für vereinnahmtes (Teil-)Entgelt | Pflichtangaben gelten sinngemäß; der Vereinnahmungszeitpunkt ist anzugeben, wenn bekannt und nicht identisch mit dem Ausstellungsdatum. Ob/ wann gezahlt wurde, ist `X`. | [§ 14 Abs. 5 i. V. m. Abs. 4 Nr. 6 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html) |
| `DE-VAT-FINAL-001` | D/K | Endrechnung nach Anzahlungsrechnungen | Vereinnahmte Teilentgelte und darauf entfallende Steuerbeträge müssen abgesetzt werden; Gesamtbeträge dürfen zusammengefasst sein. Prüfen nur, wenn Anzahlungen im Dokument/Anhang oder als Kontext vorliegen. | [§ 14 Abs. 5 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [UStAE 14.8](https://ao.bundesfinanzministerium.de/usth/2022/A-Umsatzsteuergesetz/IV-Steuer-und-Vorsteuer/Paragraf-14/ae-14-8.html) |
| `DE-VAT-ADJ-001` | K | Nachträgliche Minderung der Bemessungsgrundlage | Rabatt, Skonto oder Rückgängigmachung erfordert nicht automatisch eine Rechnungsberichtigung; Änderung von Leistungsumfang/-inhalt grundsätzlich schon. Nicht allein aus negativem Beleg ableiten. | [BMF 15.10.2025, Rn. 51a/51b](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile) |

## 4. Reverse Charge nach § 13b UStG

Die Anwendbarkeit hängt oft von Tatsachen ab, die nicht in der Rechnung stehen:
Ansässigkeit und beteiligte Betriebsstätte, Unternehmereigenschaft und Bezugssphäre,
Art der Leistung/Gegenstände, Bescheinigungen bei Bau- oder Reinigungsleistungen,
Wiederverkäufereigenschaft sowie die Zusammenfassung zu einem wirtschaftlichen
Vorgang. Deshalb zunächst den Sachverhalt klassifizieren und erst danach harte
Dokumentregeln anwenden.

| Regel-ID | Klasse | Prüfkriterium | Technische Auswertung | Quelle |
|---|---:|---|---|---|
| `DE-VAT-RC-001` | K | Umsatz fällt unter § 13b Abs. 1 oder Abs. 2, Empfänger schuldet nach Abs. 5 die Steuer | Mögliche Fälle als Kontextfrage ausgeben, nicht allein aus Produkttext/Steuercode entscheiden. | [§ 13b UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html) |
| `DE-VAT-RC-002` | D | Reverse Charge wurde sicher bestätigt/erklärt | „Steuerschuldnerschaft des Leistungsempfängers“ oder die amtssprachliche Entsprechung nach Art. 226 Nr. 11a MwStSystRL (z. B. „Reverse charge“) muss vorhanden sein; deutsche Umsatzsteuer darf nicht gesondert ausgewiesen sein. Fehlt der Hinweis, entfällt die Steuerschuld des Empfängers dadurch nicht. | [§ 14a Abs. 5 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [UStAE 14a.1 Abs. 6](https://mcp.kkc.ai/steuerrecht/references/h_ustae_a14a_p1?lines=1-100) |
| `DE-VAT-RC-003` | K | § 13b Abs. 2 Nr. 10 oder 11 (bestimmte Elektronik bzw. Anlage-4-Gegenstände) | 5.000-EUR-Grenze bezieht sich auf die Summe der Entgelte eines wirtschaftlichen Vorgangs; spätere Minderungen bleiben unberücksichtigt. Einzelrechnung kann den Gesamtvorgang nicht sicher beweisen. | [§ 13b Abs. 2 Nr. 10–11 UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html) |
| `DE-VAT-RC-004` | K | Deutscher Inlandsumsatz mit inländischem Leistenden und Empfänger | Besteht E-Rechnungspflicht, obwohl der Empfänger die Steuer schuldet; Übergangs- und Kleinbetragsregeln gesondert prüfen. | [BMF 15.10.2025, UStAE 14.1 Abs. 4](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.html) |

Die Fallgruppen des § 13b Abs. 2 umfassen insbesondere Leistungen ausländischer
Unternehmer, sicherungsübereignete Gegenstände, grunderwerbsteuerbare Umsätze,
Bauleistungen, bestimmte Gas-/Elektrizitätslieferungen, Emissionsberechtigungen,
Anlage-3-Gegenstände, Gebäudereinigung, bestimmtes Gold, bestimmte Elektronik ab
5.000 EUR, Anlage-4-Gegenstände ab 5.000 EUR und bestimmte
Telekommunikationsleistungen. Die jeweiligen Empfängervoraussetzungen aus Abs. 5
sind zwingend separat zu klären.

## 5. Innergemeinschaftliche Warenumsätze und EU-B2B-Dienstleistungen

| Regel-ID | Klasse | Prüfkriterium | Technische Auswertung | Quelle |
|---|---:|---|---|---|
| `DE-VAT-IGL-001` | K/X | Innergemeinschaftliche Lieferung | Warenbewegung in einen anderen Mitgliedstaat, Erwerberstatus, Erwerbsbesteuerung, Verwendung einer gültigen ausländischen USt-IdNr. und Nachweise sind nicht allein durch die Rechnung bewiesen. | [§ 6a UStG](https://www.gesetze-im-internet.de/ustg_1980/__6a.html) |
| `DE-VAT-IGL-002` | D | Innergemeinschaftliche Lieferung ist bestätigt | USt-IdNr. von Leistendem und Empfänger, Hinweis auf Steuerbefreiung, kein deutscher Steuerbetrag; Rechnung bis zum 15. Tag des Folgemonats. USt-IdNr.-Ausnahme für neue Fahrzeuge/Fahrzeuglieferer nach §§ 1b, 2a beachten. | [§ 14a Abs. 3 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [§ 14 Abs. 4 Nr. 8 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html) |
| `DE-VAT-IGL-004` | K/D | Innergemeinschaftliche Lieferung eines neuen Fahrzeugs | Wenn der Sachverhalt bestätigt ist, müssen zusätzlich die Merkmale nach § 1b Abs. 2 und 3 UStG enthalten sein; Fahrzeugstatus selbst ist Kontext. | [§ 14a Abs. 4 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [§ 1b UStG](https://www.gesetze-im-internet.de/ustg_1980/__1b.html) |
| `DE-VAT-IGL-003` | K | Innergemeinschaftlicher Erwerb in Deutschland | Grenzüberschreitende Warenbewegung und Erwerberstatus sind Kontext. Aus einer ausländischen Lieferantenrechnung allein folgt kein abschließendes Urteil. | [§ 1a UStG](https://www.gesetze-im-internet.de/ustg_1980/__1a.html) |
| `DE-VAT-EUSVC-001` | K | Sonstige B2B-Leistung: Ort nach § 3a Abs. 2 beim Empfänger | Unternehmerbezug und Ausnahmen nach § 3a Abs. 3–8 müssen fachlich geklärt werden; USt-IdNr. ist nur ein Indiz. | [§ 3a UStG](https://www.gesetze-im-internet.de/ustg_1980/__3a.html) |
| `DE-VAT-EUSVC-002` | D | Deutscher Leistender, Empfänger in anderem EU-Staat und Art.-196-/§-3a-Abs.-2-Fall bestätigt | Beide USt-IdNrn., Reverse-Charge-Hinweis in zulässiger Amtssprache, kein deutscher Steuerbetrag; Rechnung bis zum 15. Tag des Folgemonats. | [§ 14a Abs. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [Art. 196 und Art. 226 Nr. 11a MwStSystRL](https://eur-lex.europa.eu/eli/dir/2006/112/2025-03-20/eng) |
| `DE-VAT-EUSVC-003` | K | EU-Leistender, deutscher unternehmerischer Empfänger | Grundsätzlich Empfänger-Steuerschuld nach § 13b Abs. 1; Rechnungsrecht kann sich nach dem Sitzstaat des Leistenden richten. Ausländische Umsatzsteuer als hohes Plausibilitätsrisiko, nicht automatisch als deutscher Formfehler melden. | [§ 13b Abs. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html), [§ 14 Abs. 7 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [Art. 196 MwStSystRL](https://eur-lex.europa.eu/eli/dir/2006/112/2025-03-20/eng) |
| `DE-VAT-TRI-001` | K/D | Innergemeinschaftliches Dreiecksgeschäft ist bestätigt | Beide USt-IdNrn., Hinweis auf Dreiecksgeschäft **und** Steuerschuld des letzten Abnehmers, kein gesonderter Steuerbetrag. | [§ 14a Abs. 7 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [UStAE 25b.1 Abs. 8](https://ao.bundesfinanzministerium.de/usth/2023/A-Umsatzsteuergesetz/VI-Sonderregelungen/Paragraf-25b/ae-25b-1.html) |
| `DE-VAT-VATID-001` | D/X | USt-IdNr. vorhanden | Syntax/Länderkürzel `D`; Gültigkeit und Zuordnung zu Name/Anschrift zum Leistungszeitpunkt `X` über BZSt/VIES bestätigen und Nachweis speichern. Ein VIES-Ausfall ist kein Negativnachweis. | [§ 18e UStG](https://www.gesetze-im-internet.de/ustg_1980/__18e.html), [EU-Kommission: VIES](https://ec.europa.eu/taxation_customs/vies?locale=de), [MwStSystRL Art. 215](https://eur-lex.europa.eu/eli/dir/2006/112/2025-03-20/eng) |

## 6. E-Rechnung im deutschen B2B-Inlandsverkehr

### Geltungsbereich und Zeitachse

Die Pflicht betrifft grundsätzlich Leistungen eines inländischen Unternehmers an
einen anderen inländischen Unternehmer für dessen Unternehmen. „Inländisch“ kann
auch über eine am Umsatz beteiligte Betriebsstätte bestimmt werden. Keine allgemeine
Pflicht folgt allein daraus, dass eine deutsche Anschrift oder USt-IdNr. im Dokument
steht. Ist mindestens eine beteiligte Partei nicht im Inland ansässig, besteht nach
der Verwaltungsauffassung grundsätzlich keine Pflicht. Die Umsatzart allein
entscheidet das aber nicht; Mischumsätze, Optionsfälle und beteiligte inländische
Betriebsstätten müssen gesondert beurteilt werden.

| Leistungszeit | Grundregel für die Ausstellung im Pflichtbereich | Quelle |
|---|---|---|
| ab 1.1.2025 bis 31.12.2026 | E-Rechnung ist die Grundregel; über § 27 Abs. 38 Nr. 1 UStG sind Papier oder mit Empfängerzustimmung andere elektronische Formate übergangsweise zulässig. | [§ 27 Abs. 38 Nr. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html) |
| 1.1.2027 bis 31.12.2027 | Übergang nur, wenn Vorjahres-Gesamtumsatz des Ausstellers höchstens 800.000 EUR beträgt; daneben bleibt nicht EN-16931-konformes EDI mit Zustimmung bis Ende 2027 erlaubt. | [§ 27 Abs. 38 Nr. 2–3 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html) |
| ab 1.1.2028 | Keine allgemeine Übergangsregel mehr; im Pflichtbereich muss das Format § 14 Abs. 1 Satz 6 UStG erfüllen. | [§ 14 Abs. 1–2 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 27 Abs. 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html) |

Kleinbetragsrechnungen, Fahrausweise und Rechnungen von Kleinunternehmern können
unabhängig davon stets als sonstige Rechnung übermittelt werden. Die
Empfangsbereitschaft für E-Rechnungen gilt seit 1. Januar 2025 ohne entsprechende
Aussteller-Übergangsfrist auch für inländische Unternehmer einschließlich
Kleinunternehmern; eine E-Mail-Adresse kann technisch genügen.

### Technische Plausibilitätsregeln

| Regel-ID | Klasse | Prüfkriterium | Technische Auswertung | Quelle |
|---|---:|---|---|---|
| `DE-VAT-EINV-001` | D | E-Rechnungsformat | Strukturierte Rechnung muss EN 16931 entsprechen oder vereinbarungsgemäß eine richtige, vollständige, verlustfreie Extraktion in ein EN-16931-konformes/interoperables Format ermöglichen. Reines PDF ist eine sonstige Rechnung. | [§ 14 Abs. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [BMF 15.10.2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.html) |
| `DE-VAT-EINV-002` | D | Formatfehler vs. Geschäftsregelfehler | Syntax-/Formatfehler können dazu führen, dass nur eine sonstige elektronische Rechnung vorliegt. Ein Geschäftsregelfehler ist separat zu bewerten; nur die Verletzung einer umsatzsteuerlichen Pflichtangabe macht die Rechnung insoweit nicht ordnungsmäßig. | [BMF 15.10.2025, Rn. 6a, 6b, 35a](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile) |
| `DE-VAT-EINV-003` | D | Zulässige deutsche Formate | XRechnung sowie ZUGFeRD ab 2.0.1 außer `MINIMUM` und `BASIC-WL` werden vom BMF als Beispiele für EN-16931-basierte Formate genannt. Andere EN-16931-Formate sind nicht ausgeschlossen. | [BMF 15.10.2025, UStAE 14.1 Abs. 12–14](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile) |
| `DE-VAT-EINV-004` | D | Hybridrechnung | Bei Abweichungen ist der strukturierte Datenteil führend. Widersprüche zwischen XML und Sichtteil melden; steuerliche Prüfung auf XML stützen. | [BMF 15.10.2025, UStAE 14.4 Abs. 3](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile) |
| `DE-VAT-EINV-005` | K | Pflicht zur E-Rechnung | Erst nach Bestätigung von Leistungsdatum, B2B-Unternehmensbezug, beiderseitiger Ansässigkeit/Betriebsstättenbeteiligung, Umsatzart und Ausnahme/Übergang anwenden. Ein nicht strukturiertes Format vor 2028 ist nicht ohne diese Fakten fehlerhaft. | [§§ 14, 27 Abs. 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/) |
| `DE-VAT-EINV-006` | D/K | PDF/A | PDF/A ist keine eigenständige Pflichtangabe nach §§ 14, 14a UStG. PDF/A-Befund als technisches Teilurteil ausgeben und nicht allein daraus „umsatzsteuerlich unwirksam“ folgern. | [§ 14 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [BMF 15.10.2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.html) |

## 7. Aufbewahrung und Grenzen der Dateiprüfung

| Regel-ID | Klasse | Prüfkriterium | Bewertung | Quelle |
|---|---:|---|---|---|
| `DE-VAT-ARCH-001` | X | Aufbewahrung | Ein- und Ausgangsrechnungen grundsätzlich acht Jahre ab Schluss des Ausstellungsjahres; bei E-Rechnung mindestens strukturierten Teil unversehrt in ursprünglicher Form und maschinell auswertbar aufbewahren. Nicht durch Prüfung einer Einzeldatei belegbar. | [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html), [BMF 15.10.2025, Rn. 60](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile) |
| `DE-VAT-LIMIT-001` | X | Tatsächliche Leistung und Leistungsempfänger | Vertrag, Leistung, Warenbewegung, Zahlungsfluss, wirtschaftlicher Vorgang, Empfängerstatus und Leistungsort sind nicht durch ein formal valides XML bewiesen. | [§§ 3a, 6a, 13b UStG](https://www.gesetze-im-internet.de/ustg_1980/) |
| `DE-VAT-LIMIT-002` | K/X | Richtiger Steuersatz oder Befreiung | Waren-/Leistungsklassifikation, Verwendungszweck, Option und zeitlicher Rechtsstand sind Kontext; Validator darf nur Rechen- und Erklärungskonsistenz zusagen. | [§§ 4, 9, 12 UStG](https://www.gesetze-im-internet.de/ustg_1980/) |
| `DE-VAT-LIMIT-003` | X | Vorsteuerabzug | Eine formal ordnungsmäßige Rechnung ist nicht alleiniger Beweis des Vorsteuerabzugs. Keine Aussage „vorsteuerabzugsberechtigt“ erzeugen. | [§ 15 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html) |

## 8. Minimaler Ablauf für den Skill

1. Technische Validierung unverändert ausführen (Format/Syntax, EN 16931 bzw.
   Profil, Rechenregeln, PDF/A als getrenntes Teilurteil).
2. Explizit erklärte Rechnungsart, Steuerkategorien, Länder, Datumswerte, Parteien,
   USt-IdNrn., Beträge und Hinweise extrahieren.
3. Nur `D`-Regeln anwenden, deren Tatbestand aus Datei oder Nutzerkontext feststeht.
4. Für `K`-Regeln die fehlenden Tatsachen nennen; keine Transaktionsart erraten.
5. `X`-Prüfungen als externe Checkliste ausgeben. USt-IdNr.-Abfrage nur auf
   ausdrückliche Nutzerbitte bzw. mit geeignetem Online-Zugang; Zeitpunkt und
   Ergebnis protokollieren.
6. Schlussformel: „Unverbindliche technische Plausibilitätsprüfung; keine Steuer-
   oder Rechtsberatung und keine Zahlungs-/Buchungsfreigabe.“

## Quellen und Rechtsstand

Primärquellen:

- TAXLaw-Abrufbasis (amtliche Inhalte, Release `20260910T100457Z`):
  [§ 14 UStG](https://mcp.kkc.ai/steuerrecht/references/n_de_ustg_p14),
  [§ 14a UStG](https://mcp.kkc.ai/steuerrecht/references/n_de_ustg_p14a),
  [§ 13b UStG](https://mcp.kkc.ai/steuerrecht/references/n_de_ustg_p13b),
  [§ 14b UStG](https://mcp.kkc.ai/steuerrecht/references/n_de_ustg_p14b),
  [§ 15 UStG](https://mcp.kkc.ai/steuerrecht/references/n_de_ustg_p15),
  [§ 27 UStG](https://mcp.kkc.ai/steuerrecht/references/n_de_ustg_p27),
  [§ 3a UStG](https://mcp.kkc.ai/steuerrecht/references/n_de_ustg_p3a),
  [§ 6a UStG](https://mcp.kkc.ai/steuerrecht/references/n_de_ustg_p6a),
  [§ 31 UStDV](https://mcp.kkc.ai/steuerrecht/references/n_de_ustdv_p31),
  [§ 33 UStDV](https://mcp.kkc.ai/steuerrecht/references/n_de_ustdv_p33),
  [§ 34a UStDV](https://mcp.kkc.ai/steuerrecht/references/n_de_ustdv_p34a),
  [UStAE 13b.14](https://mcp.kkc.ai/steuerrecht/references/h_ustae_a13b_p14) und
  [BMF-Schreiben vom 15.10.2025](https://mcp.kkc.ai/steuerrecht/references/v_bmf_20251015_iiic2s7287a00019007243).
- [UStG – aktuelle Gesamtausgabe](https://www.gesetze-im-internet.de/ustg_1980/),
  insbesondere §§ 1a, 3a, 4, 6a, 12, 13b, 14, 14a, 14b, 14c, 15, 18e und 27.
- [UStDV – aktuelle Gesamtausgabe](https://www.gesetze-im-internet.de/ustdv_1980/),
  insbesondere §§ 31 bis 34a.
- [BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.html).
- [BMF: Umsatzsteuer-Anwendungserlass, laufend konsolidierte Fassung](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/Umsatzsteuer-Anwendungserlass-aktuell.pdf?__blob=publicationFile).
- [BMF-FAQ zur E-Rechnung, Stand März 2026](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) nur als ergänzende amtliche Erläuterung; Gesetz und BMF-Schreiben gehen vor.
- [MwStSystRL 2006/112/EG, konsolidierte Fassung 20.03.2025](https://eur-lex.europa.eu/eli/dir/2006/112/2025-03-20/eng), insbesondere Art. 44, 196, 215 und 226.
- [EU-Kommission: VIES](https://ec.europa.eu/taxation_customs/vies?locale=de).

Rechtsstände sind zeitabhängig. Vor Anwendung sind Leistungsdatum und zu diesem
Zeitpunkt geltende Fassung zu bestimmen. Die E-Rechnungsregeln des BMF-Schreibens
vom 15. Oktober 2025 gelten für nach dem 31. Dezember 2024 ausgeführte Umsätze;
für frühere Umsätze ist der damalige Rechtsstand zu verwenden. Übergangsregeln des
§ 27 Abs. 38 UStG enden spätestens am 31. Dezember 2027. Normen, BMF-Schreiben,
UStAE und EU-Recht vor einer produktiven Regeländerung erneut prüfen.
