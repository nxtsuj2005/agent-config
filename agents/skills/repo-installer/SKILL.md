---
name: repo-installer
description: Macht ein Projekt per One-Liner installier- und updatebar – interaktives Shell-Menü (Proxmox-LXC oder Linux), update-Kommando, immer neuester Stand von GitHub, Hardware-Selbstcheck. Nutzen bei "quickinstall", "setupscript", "install datei", "als lxc hochladen", "updater", "auf jedem rechner draufschmeißen".
---

# repo-installer

## Liefern
1. **`install.sh`** (bash, `set -euo pipefail`, idempotent):
   - Menü wie bei den Proxmox-Community-Skripten (`whiptail`, Fallback `read`): CT-ID, Hostname, IP/DHCP + Gateway, Storage, Cores/RAM/Disk, Port. Defaults vorbelegt, alles überschreibbar.
   - Nicht-interaktiv per Flags/Env (`--yes`, `CT_ID=… IP=…`).
   - Passwörter/Tokens: generieren oder abfragen, am Ende **einmal anzeigen** und root-only speichern (`/root/<app>.credentials`, chmod 600). Nie ins Repo.
   - Fehlschläge laut melden, klare Statusmeldungen, Exit-Codes.
2. **`update`-Kommando** im Ziel (`/usr/local/bin/update` oder `<app>-update`): zieht den aktuellen Stand von GitHub, sichert Daten vorher, migriert, startet den Service neu, Health-Check, Rollback-Hinweis bei Fehler. Daten-Verzeichnis bleibt unangetastet.
3. **Raw-Einstieg:** README-One-Liner `bash -c "$(curl -fsSL https://raw.githubusercontent.com/<user>/<repo>/main/install.sh)"`, damit immer der neueste Stand läuft.
4. **Hardware-Selbstcheck** (Desktop-Apps/Dashboards): Kerne, RAM, Akku ja/nein, Auflösung erkennen und Config/Layout automatisch anpassen, nicht nur auf dem eigenen Gerät perfekt.
5. systemd-Service, Autostart, Logs (`journalctl -u <app>`), kleine Doku „wie updaten“ in 3 Zeilen.

## Prüfen
- Syntax: `bash -n`, `shellcheck` falls da. Wenn möglich in frischem Container/VM testen, sonst Dry-Run.
- Auf Prod/Server nur mit Zugang aus `access-setup` und nach Snapshot/Backup.
- Vor dem Veröffentlichen `ship` (Privatsphäre-Check, Noreply-Mail, keine Secrets).
