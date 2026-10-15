---
name: repo-start
description: Repo kurz kennenlernen und lokal gegen Remote abgleichen – bei Abweichung gewinnt der Online-Stand (mit Sicherung). Nutzen bei "mach dich mit meinem repo bekannt", "schau mal auf git", "check ob lokal mit git übereinstimmt", Start einer Session in einem Projekt.
---

# repo-start

1. **Account/Remote:** `gh auth status` + `git remote -v`: passt der aktive GitHub-Account zum Owner? Sonst melden, bevor irgendwas gepusht wird.
2. **Abgleich:** `git fetch`, dann `git status -sb` und `git log --oneline -5 HEAD..@{u}` / `@{u}..HEAD`.
   - Lokal nur hinter Remote → `git pull --ff-only`.
   - Lokal hat eigene/uncommittete Änderungen und weicht ab → **zuerst sichern** (`git branch backup/local-<datum>` bzw. `git stash -u`), dann auf den Remote-Stand bringen. Online gewinnt, aber nichts geht verloren. Force/Reset nur so, nie ohne Sicherung.
   - Kein lokaler Klon → klonen.
3. **Kennenlernen** (max. 8 Zeilen): was ist das, Stack, Start-/Test-/Deploy-Befehle (aus README/AGENTS.md), Teststatus (kurz laufen lassen), auffällige Stolperfallen. Suche über `explorer`, nicht alles selbst lesen.
4. Fehlt eine `AGENTS.md`: anbieten, `project-init` laufen zu lassen.
