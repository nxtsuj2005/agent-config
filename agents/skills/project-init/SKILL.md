---
name: project-init
description: Richtet ein Repo agent-ready ein – schlanke AGENTS.md (für Claude + Codex), t3.json mit Worktree-Setup und Dev/Test-Scripts, optional DESIGN.md. Nutzen bei "init das projekt", neuen Repos oder Repos ohne AGENTS.md.
---

# project-init

## 1. Analysieren
Stack, Paketmanager, Befehle (run/test/lint/typecheck/build/deploy), gitignorte Config-Dateien (`.env*`, lokale DBs) und Stolperfallen herausfinden. Für die Suche den `explorer`-Subagent nutzen. Was sich nicht ableiten lässt (Deploy-Weg, No-Gos), einmal gebündelt bei dir erfragen (max. 5 Fragen).

## 2. AGENTS.md (eine Quelle für Claude + Codex)
- Claude liest `AGENTS.md` nativ, **solange keine `CLAUDE.md` existiert**. Deshalb nur AGENTS.md.
- Gibt es eine `CLAUDE.md`: nach Rückfrage in die AGENTS.md mergen (`git mv` bzw. zusammenführen) und `CLAUDE.md` löschen. Claude-only-Kram gehört nach `.claude/rules/*.md`.
- Vorlage: `templates/AGENTS.md`. **Max. ~80 Zeilen.** Nur, was der Agent nicht selbst aus dem Code lesen kann: exakte Befehle, Konventionen, Stolperfallen, Deploy. Keine Verzeichnis-Tour, keine Style-Regeln, die der Linter schon erzwingt, nichts aus der README kopieren. Nicht mit `/init` generieren.

## 3. t3.json + Worktree-Setup
- Vorlage: `templates/t3.json`, Schema: https://t3.codes/schema/t3.json (Icons: play|test|lint|configure|build|debug).
- `scripts/worktree-setup.sh` aus `templates/worktree-setup.sh` übernehmen und an den Stack anpassen. Das Script kopiert gitignorte Configs aus dem Haupt-Worktree und installiert die Dependencies. Danach `chmod +x`.
- Dev-Script mit `previewUrl` (richtiger Port!) und Test-Script mit `icon: test`.
- `defaultThreadEnvMode: "worktree"` nur nach Rückfrage. Empfohlen für prod-nahe Repos und parallele Threads.

## 4. Optional: DESIGN.md (UI-Projekte)
Fragen, ob gewünscht. Wenn ja, `impeccable init` nutzen (falls installiert) oder eine passende Vorlage aus VoltAgent/awesome-design-md mit den echten Projektfarben und -fonts anpassen.

## 5. Abschluss
Kleine Commits: `docs: add AGENTS.md`, `chore: add t3.json + worktree setup`. Das Worktree-Script einmal testen (`git worktree add /tmp/wt-test && cd … && ../scripts/worktree-setup.sh`, danach wieder aufräumen).
