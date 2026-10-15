---
name: swarm
description: Große Aufgabe auf mehrere Subagents verteilen – pro Teilaufgabe ein Agent mit passendem Modell, max. 4 parallel, disjunkte Dateien. Nutzen bei "setz pro aufgabe einen agenten", "mehrere agents", "parallel", "schick ein paar agents drauf".
---

# swarm

## Planen
1. Auftrag in Teilaufgaben zerlegen. Jede Teilaufgabe bekommt **eigene Dateien/Verzeichnisse**. Überschneidet sich was: nacheinander oder eigener Worktree.
2. **Anzahl:** höchstens 4 (sagt der User eine andere Zahl, gilt die). Lieber weniger, wenn die Aufgaben klein sind.
3. **Modell pro Aufgabe** (beim Aufruf `model` setzen):
   - Haiku: gezielte Suche, Umbenennen, Tests laufen lassen, Logs zusammenfassen
   - Sonnet: Implementierung, Review, große Suche mit viel Kontext
   - Opus: nur subtile Logik oder kritisch (Kundenprojekt, Geld, Auth, Migration)

4. **Provider mischen:** Teilaufgaben, die unabhängig sind (Review, Bug-Hunt, Tests, abgegrenztes Modul), gehen per `delegate_task` an Codex (`providerInstanceId: codex`, `model: gpt-6.1-sol`), den Rest macht Claude. So verteilen sich die Limits und es läuft parallel. Läuft die Session selbst in Codex, umgekehrt an Claude. Zählt zu den max. 4.

## Brief je Agent (kurz, self-contained)
Ziel · Dateien, die er anfassen darf · Dateien, die er **nicht** anfassen darf · Fertig-Kriterium · Bericht in max. 10 Zeilen (geändert, offen, unsicher).
Agents machen **keine** schreibenden git-Befehle.

## Danach (Hauptagent)
- Ergebnisse kritisch lesen (Behauptungen prüfen, nicht glauben), Konflikte lösen.
- Tests/Lint laufen lassen, dann pro Bereich ein kleiner Commit.
- Bericht an den User als Tabelle: Agent · Aufgabe · Modell · Ergebnis (max. 8 Zeilen).
