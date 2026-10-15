---
name: spec-writer
description: Macht aus einer lockeren Stichpunkt-/Wunschliste eine strukturierte Task-Spec für Agents (Scope, nicht ändern, Agent-Aufteilung, Tests, Abschlussbericht). Nutzen bei "mach daraus einen prompt", "schreib mir die spec", "für codex/chatgpt aufbereiten", großen Mehrpunkt-Aufträgen.
---

# spec-writer

Input: unsortierte Wünsche des Users (Semikolon-Listen, Sprachnotiz-Stil). Output: **eine** Spec, max. ~1 Seite, als Codeblock zum Weiterreichen.

## Struktur
1. **Ziel** (1–2 Sätze)
2. **Unverändert lassen** (Design, APIs, Engine, Daten – was der User nicht angefasst haben will; „keine stillen Verhaltensänderungen ohne Test“)
3. **Nicht Teil dieses Tasks** (explizit, gegen Scope Creep und Refactoring)
4. **Aufgaben** gruppiert nach Bereich/Rolle (Spieler-Handy, Host, Tisch, Backend …), je 1–3 Zeilen, jede mit Fertig-Kriterium
5. **Agent-Aufteilung** (Skill `swarm`): ein Agent pro Bereich, disjunkte Dateien, Modell je Schwere, max. 4
6. **Tests/Verify**: welche Tests, `ui-verify` bei UI, Geräte aus `ui-polish`
7. **Abschlussbericht**: Umgesetzt · Neue APIs · Tests · Bewusst nicht umgesetzt · Sinnvolle nächste Schritte

## Regeln
- Nur übernehmen, was der User gesagt hat. Annahmen als „Annahme:“ markieren, Unklares als max. 3 gebündelte Fragen vorab.
- Bei bestehenden Features: Absicht vs. Bug trennen („ist Absicht, nicht fixen“).
- Am Ende fragen: „so losschicken?“ – nicht selbst loslaufen.
