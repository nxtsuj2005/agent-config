---
name: autopilot
description: Arbeitet einen Backlog autonom ab – alles, was ohne dich geht, wird gebaut (kleine Commits, verifiziert); alles, was du liefern musst, landet gesammelt in fragen.md. Nutzen bei "autopilot", "bau alles was ohne mich geht", "mach weiter bis nix mehr offen ist", "über nacht", "fix alles was du kannst".
---

# autopilot

## Setup
1. **Backlog** bilden aus dein Liste bzw. `TODO.md`, `fragen.md`, Issues, offenen Punkten im Thread. Priorisieren (Blocker und Bugs zuerst), als Checkliste in `TODO.md` oder der bestehenden Liste führen.
2. Falls verfügbar `/goal` nutzen, damit der Agent dranbleibt.

## Loop (pro Item)
- **Allein machbar?** → bauen, verifizieren (proportional: Tests/Lint, UI via `ui-verify`), **kleiner Commit**, abhaken.
- **Braucht dich** (Keys, Zugänge, Geschäftsentscheidungen, Vor-Ort-Tests, Geld, Prod) → in `fragen.md` eintragen: konkrete Frage + was du schon weißt + Vorschlag (A/B). Dann **weiter mit dem nächsten Item**, nicht warten.
- Nach 2 gescheiterten Ansätzen: Item als blockiert markieren, Notiz dazu, weiter.

## Subagents
- Unabhängige Items parallel: **max. 3**. `explorer` (Haiku) für Suche, Sonnet für Implementierung, Opus nur für subtile Logik.
- Überlappen Items in denselben Dateien → nacheinander bzw. `isolation: worktree`.

## Niemals im Autopilot
Prod-Deploys, Echtgeld/Live-Trading umschalten, Daten löschen, Force-Push, Secrets anfassen → alles nach `fragen.md`.

## Limits
Ist das Usage-Limit nah: aktuellen Stand committen, `handoff` schreiben, sauber stoppen.

## Abschluss (max. 8 Zeilen)
✅ erledigt (Anzahl + wichtigste Commits) · ⛔ blockiert · ❓ `fragen.md` (Anzahl Fragen) · Push-Status.
