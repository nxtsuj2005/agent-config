---
name: agent-audit
description: Prüft kritisch die Arbeit eines anderen Agents (Codex, GPT, früherer Thread, Subagent) – was wurde wirklich gemacht, was ist kaputt/gefakt, was ginge besser. Nutzen bei "check was codex gemacht hat", "review die arbeit", "stimmt das?", wenn du fremden Agent-Output/Reviews pastest oder vor dem Weiterbauen auf fremder Arbeit.
---

# agent-audit

Grundhaltung: **Behauptungen sind Hypothesen.** Du vertraust fremden Agents weniger, also prüfen statt glauben.

## Ablauf
1. **Scope:** Commits/Branch/Diff (`git log`, `git diff <base>...`), gepastete Behauptungen, betroffene Features.
2. **Claims gegen die Realität:** Jede Behauptung („Tests grün“, „Feature X fertig“, „Bug gefixt“) selbst prüfen: Tests laufen lassen, Code lesen, bei UI `ui-verify`.
3. **Typische Agent-Sünden suchen:**
   - Stubs, TODOs, Fake-Daten oder hartcodierte Werte statt echter Logik
   - geskippte oder abgeschwächte Tests, gemockter Erfolg
   - verschluckte Errors (`except: pass`, leere catch)
   - Scope Creep, unnötige Abhängigkeiten
   - Security (Secrets, Injection, Auth)
   - Inkonsistenz zu AGENTS.md und Projektkonventionen
4. Bei großen Diffs den `reviewer`-Subagent mit frischem Kontext parallel nutzen.

## Output (kurz)
- **Verdict:** ✅ passt / ⚠️ Fixes nötig / ❌ neu machen, mit 1 Zeile Begründung
- **Findings:** max. 8, nach Schwere, je `pfad:zeile` – Problem – Fix
- **Besser wäre:** max. 3 Bullets
- Angebot: „soll ich fixen?“
