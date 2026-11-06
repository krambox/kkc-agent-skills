---
name: erechnung
description: Prüft deutsche E-Rechnungen (XRechnung, ZUGFeRD/Factur-X; PDF oder XML) vollständig lokal mit der gebündelten eRechnung-CLI (Mustang, bei XRechnung zusätzlich KoSIT), ohne Netz und ohne Validierungsdienst. Liefert ein Verdict (conformant, nonconformant, not_erechnung, tool_error) zur Eignung für das B2B-Mandat und einen deutschen Prüfbericht mit Schema, Schematron, PDF/A und Rechenprüfung. Auf ausdrückliche Bitte ergänzt der Skill eine unverbindliche, dokumentbasierte Umsatzsteuer-Plausibilitätsprüfung zu Pflichtangaben, Reverse Charge und innergemeinschaftlichen Fällen. Nutze ihn bei „E-Rechnung prüfen“, „ist das eine gültige XRechnung“, „ZUGFeRD validieren“, „erfüllt das die E-Rechnungspflicht“, „offline prüfen“ oder „Reverse Charge prüfen“. Nicht für Peppol-Zustellung, Erstellen von Rechnungen, Steuer-/Rechtsberatung oder eine definitive Aussage zu Vorsteuerabzug und Steuerschuld.
license: Apache-2.0
metadata:
  author: kai-kramer-consulting
  domain: accounting
---

# E-Rechnung prüfen

Prüft eine E-Rechnung mit der eRechnung-CLI, die als `scripts/erechnung.jar`
im Skill-Paket liegt. Die Rechnung verlässt die Ausführungsumgebung nicht.

## Laufzeit

Python 3.9+ und Java 11+. Das Skript nutzt nur die Standardbibliothek.

Fehlt Java 11+, versucht das Skript einmal
`apt-get install openjdk-17-jre-headless`. Scheitert das, endet der Lauf mit
Verdict `tool_error`, `summary.error` (Grund) und `summary.hint`
(Handlungshinweis). Dann hat keine Prüfung stattgefunden.

## Auslöser und Abgrenzung

| Greift | Greift nicht |
|---|---|
| „Ist diese ZUGFeRD-Rechnung in Ordnung?“ | „Ist diese Rechnung steuerlich absetzbar?“ |
| „XRechnung prüfen / validieren“ | „Schick die Rechnung über Peppol“ |
| „Erfüllt das PDF die E-Rechnungspflicht?“ | „Buche die Rechnung in sevDesk“ |
| Gegenprobe zu einem anderen Validator | „Erstelle mir eine E-Rechnung“ |
| „Prüfe Pflichtangaben/Reverse Charge unverbindlich“ | „Ist diese Rechnung steuerlich voll abzugsfähig?“ |

## Ablauf

### 1. Datei lokal lesbar machen

Rechnung und Skill müssen in derselben Ausführungsumgebung liegen. Chat-Uploads
und lokale Pfade brauchen keinen weiteren Schritt.

### 2. Prüfen

```bash
python3 scripts/erechnung.py validate [--out "<ausgabeverzeichnis>"] "<rechnung>" ["<rechnung>" …]
```

Unter Windows `python` oder `py -3` statt `python3`. Ohne `--out` entsteht
ein temporärer Ordner. Mehrere Rechnungen immer in **einem** Aufruf übergeben,
nicht einzeln: Java startet dann nur einmal.

stdout ist bei einer Rechnung ein JSON-Objekt:

```json
{
  "verdict": "conformant",
  "version": "0.5.1",
  "summary": { "format": "xrechnung", "profile": "…", "sections": {…}, "errors": [], "warnings": [], "notices": [] },
  "artifacts": { "report": "…-pruefbericht.md", "json": "…-erechnung.json", "xml": "…-erechnung.xml" }
}
```

- `verdict` ist das Verdict. Nur dieses Feld entscheidet.
- `version` ist die Version des Skill-Pakets (= CLI-Version).
- `summary` ist die Summary der CLI: Kopf, fünf Check sections und die
  Findings in den Buckets `errors`, `warnings`, `notices`.
- `artifacts.report` ist der deutsche Prüfbericht. `artifacts.json` ist das
  volle CLI-JSON mit Mustang-Prüfbericht. `artifacts.xml` ist das
  E-Rechnung-XML (fehlt, wenn keines gefunden wurde).

Bei mehreren Rechnungen ist stdout JSON Lines: eine Zeile mit diesem Objekt je
Rechnung, in Eingabereihenfolge. Eine Rechnung, die nicht geprüft werden kann,
bekommt `tool_error`; die übrigen werden trotzdem geprüft. Gleiche Dateinamen
bekommen eigene Artefakte (`…-2-pruefbericht.md`).

Exit: `0` conformant, `1` nonconformant, `2` not_erechnung, `3` tool_error.
Bei mehreren Rechnungen der höchste Wert; das Verdict je Zeile entscheidet.
Meldungen auf stderr (etwa „Picked up JAVA_TOOL_OPTIONS“) sind kein Ergebnis.

### 3. Im Chat zusammenfassen

Zwei bis vier Sätze: Verdict, was den Ausschlag gibt, was der Nutzer tun müsste,
Version des Skill-Pakets. Fehler einzeln nennen, Warnungen und Hinweise
gebündelt („6 Hinweise, alle XRechnung-spezifisch“). Den Prüfbericht nicht
nacherzählen.

Den Prüfbericht mit dem Datei-Mechanismus des Hosts liefern, sonst den
absoluten Pfad nennen. Layout: `assets/pruefbericht-template.md`.

### 4. Optional: Umsatzsteuerliche Plausibilität

Nur auf ausdrückliche Bitte und erst nach der technischen Prüfung. Dann
`references/umsatzsteuer-pruefregeln.md` laden und das E-Rechnung-XML unter
`artifacts.xml` lesen.

Das Ergebnis als getrennten Block ausgeben: `plausibel`, `auffällig` oder
`nicht aus dem Dokument prüfbar`. Reverse Charge, Leistungsort, Warenbewegung,
Unternehmereigenschaft, USt-IdNr.-Gültigkeit und materiell richtigen Steuersatz
nicht aus Feldern erraten. Fehlenden Kontext konkret nennen. Abschluss immer:
„Unverbindliche technische Plausibilitätsprüfung; keine Steuer- oder
Rechtsberatung und keine Zahlungs-/Buchungsfreigabe."

## Qualitäts-Gates

Diese Regeln gelten ohne Ausnahme:

- **Kein Verdict ohne Lauf.** Ohne JSON von `erechnung.py validate` wird kein
  Ergebnis behauptet.
- **`tool_error` heißt: nicht geprüft.** Grund und `hint` nennen. Nie als
  „ungültig“ oder „konform“ ausgeben.
- **Nur `errors` kippen das Verdict.** `warnings` und `notices` nicht. Eine
  Rechnung kann `conformant` sein und ein Dutzend Hinweise haben. Hinweise
  nicht als Mängel verkaufen.
- **`MUSTANG_10` immer nennen.** Mustangs eigene Nachrechnung meldet
  Betragsdifferenzen nur als Warnung. Beide Beträge im Chat nennen, als
  Hinweis an den Rechnungssteller, ohne das Verdict umzudeuten.
- **PDF/A und XML sind getrennte Urteile.** Bei PDFs beide Check sections
  nennen.
- **IDs und Meldungen wörtlich übernehmen.** Keine Bedeutungen erfinden.
- **Keine Rechnungsdaten erfinden.** Korrekturvorschläge als Vorschlag
  kennzeichnen.
- **Keine Steuer- oder Rechtsberatung.** Die optionale Prüfung bewertet nur
  dokumentbasierte Plausibilität.
- **Sparsam mit sensiblen Inhalten.** Beträge, IBANs und Namen im Chat nur,
  soweit die Erklärung sie braucht.

## Referenzen, nur bei Bedarf laden

| Datei | Wann |
|---|---|
| `references/befund-interpretation.md` | Finding unklar; Profil-Frage; Check section oder Verdict einordnen |
| `references/fehlercodes.md` | Ein `BR-*`, `BR-DE-*`, `BR-CO-*`, `BR-CL-*` oder `PEPPOL-*` braucht BT/BG-Zuordnung |
| `references/umsatzsteuer-pruefregeln.md` | Nutzer fragt ausdrücklich nach Pflichtangaben, Umsatzsteuer, Reverse Charge, innergemeinschaftlicher Lieferung/Leistung oder E-Rechnungspflicht |

`references/fehlercodes.md` ist groß. Gezielt suchen, nicht am Stück lesen:

```bash
grep -n 'BR-DE-15' references/fehlercodes.md
```

`FX-SCH-*`, `MUSTANG_*` und veraPDF-Klauseln stehen dort **nicht**. Sie werden
so wiedergegeben, wie die Engine sie liefert.

## Grenzen

- Keine Peppol-Zustellung, keine Signaturprüfung.
- Keine Aussage zur fachlichen oder steuerlichen Richtigkeit: Leistungszeitraum,
  Leistungsort, Warenbewegung, Steuersatz und Vorsteuerabzug brauchen
  Sachverhalt und Nachweise.
- Kein Reparieren und kein Erzeugen von Rechnungen.
- Ein anderer Validator kann anders urteilen (andere Regelstände). Beide
  Ergebnisse nebeneinanderstellen, Validator-Versionen und Profil nennen.
