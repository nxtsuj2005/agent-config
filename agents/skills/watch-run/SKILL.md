---
name: watch-run
description: Langer Beobachtungs-/Messlauf (Netzwerk, Router, Server) sauber starten, überwachen und wieder beenden – Intervall-Logger, Auswertung, Aufräumen. Nutzen bei "mitschreiben", "loggen bis morgen", "dauertest", "schau ob es ausfälle gibt".
---

# watch-run

1. **Plan (3 Zeilen):** was wird gemessen, Intervall, wo liegt das Log, wie lange, welcher Rechner (Laptop: Akku/Sleep beachten, am Kabel lassen).
2. **Start** als eigener Prozess mit Pidfile (`setsid nohup … & echo $! > pidfile`), Log mit Rotation, Zeitstempel. Nie `pkill -f`.
3. **Mehr Messpunkte** anbieten (zusätzliche Ziele/Geräte), aber erst nach OK.
4. **Auswerten:** Ausfälle als Zeitleiste (von–bis), Ursache-Hypothesen mit Prozent, auffällige Geräte (häufige Reconnects). Messwerte nie erfinden, Lücken im Log benennen.
5. **Ende:** Auf Ansage („schalt das Logging ab“) per Pidfile stoppen, bestätigen, Log-Pfad nennen, Zugänge/Jobs aufräumen (`access-setup`).
