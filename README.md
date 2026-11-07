# kkc-agent-skills

Öffentliche Agent Skills und Claude-Plugins der Kai Kramer Consulting GmbH.
Dieses Repo ist ein Claude-Plugin-Marketplace (Name `kkc`) und enthält nur gebaute Releases.
Entwickelt wird woanders; Issues zu den Plugins sind hier willkommen.

## Plugins

| Plugin | Zweck |
|---|---|
| `erechnung` | Prüft E-Rechnungen (XRechnung, ZUGFeRD) gegen EN 16931 und gibt ein Verdict mit Bericht |

## Installation

Claude Code:

    /plugin marketplace add krambox/kkc-agent-skills
    /plugin install erechnung@kkc

Claude.ai (Team/Enterprise): das Repo in der Org-Verwaltung als Plugin-Marketplace hinzufügen.

Jedes Release hat ein Tag `<plugin>-vX.Y.Z`. Wer eine feste Version will, pinnt auf dieses Tag.

## Lizenz

Apache-2.0, siehe `LICENSE`. Mitgelieferte Abhängigkeiten tragen ihre Lizenzen und den NOTICE
im jeweiligen Skill-Ordner.
