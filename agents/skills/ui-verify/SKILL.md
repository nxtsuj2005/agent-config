---
name: ui-verify
description: Startet die App und prüft UI-Änderungen visuell und funktional in der Browser-Preview (Desktop + Mobile, Konsole, Klick-Flows). Nutzen vor "fertig" bei UI-Änderungen oder wenn du sagst "zeig mal", "check im browser", "geht das?".
---

# ui-verify

## Ablauf
1. **Wie startet die App?** Reihenfolge: `t3.json`-Scripts → `package.json`-Scripts (`dev`) → `AGENTS.md`/README → `docker compose`. Erst prüfen, ob schon was läuft (`curl -sf localhost:<port>`), statt doppelt zu starten.
2. **Starten** im Hintergrund und warten, bis die App erreichbar ist (Port pollen, max. ~60 s). Bei Fehlern das Log lesen und die Root Cause fixen.
3. **Prüfen** mit den T3-Preview-Tools (`preview_open`, `preview_snapshot`, `preview_click`/`preview_type`, `preview_evaluate`, `preview_resize`):
   - die geänderten Seiten und Flows wirklich durchklicken, nicht nur laden
   - Konsolen- und Netzwerkfehler (`preview_evaluate`, z. B. Fehler-Listener, fehlgeschlagene Requests)
   - Desktop ~1440px und Mobile 360px (Galaxy Fold): Overflow, abgeschnittene Texte, Touch-Targets
   - Loading-, Empty- und Error-States, falls betroffen
4. **Ohne T3-Preview-Tools** (z. B. CLI auf einem Server): HTTP-Status und HTML per `curl` prüfen und klar sagen, dass der visuelle Check fehlt.
5. **Output:** max. 6 Zeilen ✅/❌ mit `seite – befund`, dazu ein Screenshot, wenn möglich. ❌ wenn möglich gleich fixen und erneut prüfen.
6. Einen selbst gestarteten Dev-Server danach stoppen, außer du willst ihn offen haben.
