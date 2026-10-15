---
name: handoff
description: Schreibt einen Copy-Paste-Übergabe-Prompt, damit ein neuer Thread, Codex oder ein anderer Agent nahtlos weitermacht. Nutzen bei "handoff", "übergabe", "ich compacte", "limit ist gleich voll", "mach nen prompt für codex/neuen chat", oder proaktiv, wenn eine Session sehr lang wird.
---

# handoff

## Vorher
1. Arbeitsstand sichern: Uncommittetes als kleine Commits (WIP-Commit auf dem Feature-Branch ist ok), damit der Nachfolger den echten Stand sieht.
2. Laufende Hintergrundprozesse notieren (Dev-Server, Ports) oder stoppen.

## Prompt (ein einziger ```-Block, self-contained)
Der Nachfolger kennt **nichts** außer AGENTS.md. Deshalb rein:
- **Ziel:** 1–2 Sätze, was am Ende stehen soll
- **Ort:** Repo-Pfad, Branch/Worktree, relevante URLs/Ports
- **Erledigt:** Bullets mit Commit-Hashes
- **Offen:** nächste Schritte in Reihenfolge, der erste ganz konkret
- **Entscheidungen:** was entschieden wurde und warum, damit nichts neu diskutiert wird
- **Sackgassen:** was probiert wurde und nicht ging (spart dem Nachfolger Tokens)
- **Dateien:** `pfad:zeile` der Hotspots
- **Verify:** exakte Befehle, um den Stand zu prüfen
- **Offene Fragen an dich**

Ziel ist Codex: das Gleiche, aber explizit sagen, dass es die Arbeit von Claude fortsetzt und erst kurz den Stand prüfen soll.
In T3 geht alternativ ein neuer Thread mit `@<thread-titel>`-Referenz; der Prompt bleibt trotzdem die sichere Variante.

Zusätzlich als `.handoff/<YYYYMMDD-HHMM>-<slug>.md` im Repo speichern (`.handoff/` in `.git/info/exclude`).

## Compact-Safe-Check
Wenn du fragst „kann ich compacten?“: ja nur, wenn alles committet ist, kein Subagent oder Hintergrundjob noch läuft und der Handoff steht. Antwort in 1 Zeile.
