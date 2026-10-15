---
name: ship
description: Änderungen vor dem Push absichern – bis zu 4 Agents suchen Fehler im Diff, Fixes, Tests, Privatsphäre-Check, dann Commit + Push. Nutzen bei "raus damit", "push das", "hau das ins github", "check die commits auf fehler", "fehlersuche für den letzten push".
---

# ship

"Raus damit" / "push" heißt: absichern, committen, pushen auf dem aktuellen Branch. Keine PRs, keine Force-Pushs.

## Ablauf
1. **Stand:** `git status -sb`, `git fetch`, ungepushte Commits + Dirty-Files auflisten. Weicht der Remote ab (hinter/divergiert): stoppen und kurz melden, nicht blind mergen.
2. **Umfang:** Diff = ungepushte Commits + uncommittete Änderungen.
   - Winzig (Typo, Copy, <~30 Zeilen): selbst gegenlesen, weiter bei Schritt 4.
   - Sonst bis zu **4 Agents** (Skill `swarm`), je ein Bereich, nur lesen + berichten: Logik/Engine, Frontend/Mobile-Edge-Cases, Tests/Randfälle, Sicherheit/Secrets.
   - Modell: Sonnet. Opus nur bei Kundenprojekt, Geld, Auth, Migrationen, Deploy.
3. **Fixen:** Findings nach Schwere abarbeiten, Fixes in disjunkten Dateien parallel möglich. Kein Finding still ignorieren, unsichere als „unsicher“ melden.
4. **Prüfen:** Tests/Lint/Typecheck laufen lassen. Rot → fixen, nicht pushen.
5. **Privatsphäre (vor jedem Push, bei erstem Push eines Repos Pflicht):**
   - `git log -5 --format='%an <%ae>'`: Autor-Mail muss die GitHub-Noreply sein, kein echter Name/keine private Mail.
   - Keine Secrets/Tokens/`.env`/Keys/interne IPs-Passwörter im Diff oder getrackt (`git ls-files | grep -iE '\.env|key|token|secret|\.bak'`).
   - Repo privat oder öffentlich? Beim ersten Push kurz bestätigen lassen, wenn öffentlich.
   - Passender GitHub-Account aktiv (`gh auth status` vs. Owner im Remote)?
6. **Committen:** kleine atomare Conventional Commits, nur eigene Dateien stagen. Dann `git push`, danach `git status -sb` zur Kontrolle.

## Output (max. 6 Zeilen)
✅/⚠️ Pushed (n Commits) · gefundene + gefixte Bugs (Zahl, 1 Zeile je wichtigem) · offen/unsicher · Testergebnis.
