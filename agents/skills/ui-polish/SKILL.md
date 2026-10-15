---
name: ui-polish
description: UI-Feinschliff für Web/Handy – Geräte-Fit (kein Scrollen, Fold, iPhone-Safari), Anti-AI-Slop, gleiche Kriterien auf allen Screens, stabiles Layout. Nutzen bei Design-Feedback, "sieht nach AI aus", "handy view", "überlappt", "Fold", "iPhone", "ohne scrollen", "Lobby/Menü angleichen".
---

# ui-polish

Vor dem Anfassen: **Welche Rolle/Ansicht?** (Spieler-Handy, Host, TV/Tisch, Desktop). Unklar → einmal fragen. Dann Taste: `frontend-design` / `impeccable` nutzen, falls da.

## 1. Geräte-Matrix (mit `ui-verify` prüfen, Screenshots)
- Handy hoch ~360×740 und iPhone 16 ~393×852 (Safe Areas, `100dvh` statt `100vh`, Safari-Toolbar)
- **Galaxy Z Fold 8 (nicht Ultra), innen aufgeklappt:** fast quadratisches Display, **hoch und quer ohne Balken** (Größen mit dem User bestätigen)
- Querformat Handy, Desktop/TV ~1440+
- Spiel-/Kernansicht muss **ohne Scrollen** passen. Keine Überlappungen (Badges, Buttons, Texte).
- iOS Safari kennt die Vibration-API nicht → anderes Signal (visuell/Ton), nicht „fixen“.

## 2. Anti-AI-Slop
- Kein Neon-Glow, keine Lila-Blau-Gradients, keine Glas-Karten überall, kein einheitlicher Radius+Schatten auf allem
- Icons aus **einer** Familie, keine Emojis als Icons
- Schrift bewusst wählen (nicht Inter/Roboto/Space Grotesk als Reflex), Palette mit Haltung
- Buttons flach, wenn das Design flach ist; Hierarchie statt gleicher Karten

## 3. Konsistenz
Jede Design-Entscheidung auf **alle** Screens anwenden (Lobby, Menüs, Tisch, Popups, Fehler-/Leerzustände), nicht nur den gerade bearbeiteten.

## 4. Stabilität & Bedienung
- Bedienelemente erscheinen/verschwinden nicht: ausgrauen statt entfernen, damit nichts springt
- Slider mit festen Stufen (z. B. 5er/Blind-Schritte), keine krummen Werte
- Hotkeys für Host/Desktop (Enter = bestätigen, Backspace = ablehnen) wo es oft gebraucht wird
- Animation nur über `transform`/`opacity` (Layout-Animation ist auf schwacher GPU teuer), `prefers-reduced-motion` respektieren

## Output
Max. 6 Zeilen: pro Gerät ✅/❌ + was gefixt. Offene Design-Entscheidungen als A/B.
