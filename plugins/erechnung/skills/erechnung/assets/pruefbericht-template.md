# Prüfbericht-Layout

Das ist die Form, die `scripts/erechnung.py validate` als
`<datei>-pruefbericht.md` erzeugt. Hier nachschlagen, wenn der Bericht von Hand
ergänzt oder in ein anderes Format übertragen wird.

## Pflichtbestandteile

Jeder Prüfbericht enthält, in dieser Reihenfolge:

1. **Kopf**: Datei, Format, Profil (BT-24), Generation, Anhang, Engines,
   Validator-Versionen, **Skill-Paket-Version**, Dauer. Versionen sind nicht
   optional: Sie machen das Verdict reproduzierbar und zeigen, ob das
   hochgeladene Skill-Paket veraltet ist.
2. **Verdict**: `conformant`, `nonconformant`, `not_erechnung` oder
   `tool_error`, wörtlich aus dem JSON, mit deutscher Einordnung. Bei
   `tool_error` zusätzlich Grund und Handlungshinweis.
3. **Prüfbereiche**: die fünf Check sections mit Status oder „nicht anwendbar“.
4. **Findings**, in der Reihenfolge Fehler → Warnungen → Hinweise. Jedes mit
   ID, Engine, Check section, wörtlicher Meldung und Fundstelle.
5. **Abgrenzung**: technische Prüfung, keine steuerliche, rechtliche oder
   buchhalterische Freigabe.

Leere Buckets und fehlende Kopffelder fallen weg. Nicht mit Platzhaltern
auffüllen.

## Vorlage

```markdown
# E-Rechnungs-Prüfbericht

- **Datei:** `<dateiname>`
- **Format:** <xrechnung|facturx_en16931|…>
- **Profil (BT-24):** `<profil-urn>`
- **Generation:** <generation>
- **Anhang:** `<factur-x.xml>`
- **Engines:** mustang[, kosit]
- **Validator:** mustang <version>[, kosit <version>]
- **Skill-Paket:** eRechnung <version>
- **Dauer:** <n> ms

## Verdict: **<verdict>** – <deutsche Einordnung>

## Prüfbereiche

| Check section | Status |
|---|---|
| schema | ok |
| schematron | warning |
| pdfa | nicht anwendbar |
| embedded_xml | nicht anwendbar |
| metadata_embedding | nicht anwendbar |

## Fehler (<n>)

- **<ID>** _<engine>, <section>_ — <Meldung wörtlich>
  - Fundstelle: `<location>`

## Warnungen (<n>)

## Hinweise (<n>)

---

*Technische Prüfung (Mustang, bei XRechnung zusätzlich KoSIT). Keine
steuerliche, rechtliche oder buchhalterische Freigabe und keine
Zahlungsfreigabe.*
```

## Was nicht hineingehört

- Korrekturvorschläge. Der Bericht ist Befund, nicht Beratung. Vorschläge
  gehören in die Chat-Antwort und werden dort als Vorschlag gekennzeichnet.
- Umformulierte Meldungen. Die `message` bleibt wörtlich, erklärt wird daneben.
- Rechnungsinhalte, die kein Finding verlangt (Beträge, IBANs, Namen).

## Chat-Zusammenfassung

Zwei bis vier Sätze neben dem Bericht, nicht statt seiner:

> Verdict **conformant**: XRechnung 3.0, geprüft mit Mustang und KoSIT
> (Skill-Paket 0.5.1). Keine Fehler, zwei Hinweise aus dem XRechnung-Regelwerk
> zu optionalen Feldern. Handlungsbedarf: keiner.
