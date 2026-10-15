---
name: access-setup
description: Zugänge für Agents sicher einrichten (Proxmox-/GitHub-Token, Fritzbox, UniFi, SSH) – exakt nötige Rechte nennen, Secret per Terminal-Kommando übergeben statt in den Chat, erst lesen dann ändern. Nutzen bei "gib dir zugang", "api key", "token", "passwort hinterlegen", "kannst du auf X zugreifen".
---

# access-setup

## Ablauf
1. **Rechte vorab nennen** (nicht erst auf Nachfrage): Wo erzeugt man den Zugang (Menüpfad), und welche **minimalen Rechte** braucht er. Beispiele: GitHub-Token nur die nötigen Repo-Scopes; Proxmox-Token mit Rolle/Pfad für die konkrete CT/VM (Privilege Separation beachten); Fritzbox/UniFi eigener Benutzer.
2. **Übergabe ohne Chat:** Ein copy-paste-fertiges Kommando, das das Secret versteckt einliest und root-/user-only ablegt, z. B.
   `read -rs T && (umask 077; printf '%s' "$T" > ~/.<name>_token); unset T`
   Dazu sagen, **wo** die Datei liegt und dass ich sie von dort lese. Nie das Secret wiederholen, nie committen, nie loggen.
3. **Erst lesen:** Mit Read-only-Abfragen anfangen (Status, Logs, Geräteliste). Änderungen (Kanal wechseln, Funk abschalten, Container anlegen/löschen, Sleep/Config am Laptop) erst nach OK, außer der User hat die konkrete Änderung schon beauftragt. Vorher Snapshot/Backup bei Prod.
4. **Aufräumen:** Am Ende anbieten, Token zu löschen/zu rotieren und temporäre Logger/Jobs zu stoppen.
5. Gepastetes Secret im Chat: nicht wiederholen, in Secret-Store legen, Rotation empfehlen.
