---
name: design-demo
description: Baut klickbare, animierte Demo-Varianten (eine HTML, lokal im Browser geöffnet), damit der User sich für eine Design-Richtung entscheiden kann. Nur bei großen Redesigns, offener Design-Identität oder auf Wunsch ("zeig mir Varianten", "ich hab mein Design noch nicht gefunden"). Bei kleinen UI-Änderungen direkt umsetzen und mit ui-verify prüfen.
---

# design-demo

Ziel: du **siehst** die Richtungen, bevor gebaut wird. Keine Beschreibungen, keine ASCII-Mockups.

**Wann:** nur bei großen Redesigns, wenn die Design-Identität offen ist, oder auf Wunsch. Bei Tweaks, Bugfixes und Feedback-Listen: direkt umsetzen (`ui-polish` + `ui-verify`).

## Ablauf
1. **Kontext (kurz):** bestehendes Design checken (DESIGN.md, Tailwind-Config, CSS-Variablen, Fonts, Komponenten). Echte Inhalte des Projekts nutzen (Texte, Daten, Logos), kein Lorem Ipsum.
2. **Varianten:** 2–3 klar unterschiedliche Richtungen (außer du willst nur eine). Jede Variante hat eine eigene Idee, nicht 3× dasselbe in anderen Farben. Falls installiert, `frontend-design` / `impeccable` / `emil-design-eng` für Taste nutzen.
3. **Bauen** in `.design-demos/<slug>/` im Projekt (vorher `echo .design-demos/ >> .git/info/exclude`, damit nichts committet wird):
   - Self-contained HTML/CSS/JS, kein Build-Step. CDNs (Tailwind Play CDN, Google Fonts, Icons) sind für Demos ok.
   - `index.html` mit Umschalter A/B/C (je 1 Zeile Idee) und einem Toggle Desktop ↔ Mobile (360px, Galaxy Fold).
   - **Klickbar:** Navigation, Hover-, Active- und Focus-States, die wichtigsten Flows (Formular, Modal, Tabs, Filter …) mit Fake-Daten.
   - **Animiert:** Enter-Transitions, Micro-Interactions, Loading- und Empty-States. Lebendig, aber nicht drüber; `prefers-reduced-motion` respektieren.
4. **Zeigen:** Eine einzige `index.html` (alle Varianten per Tab/Taste 1–4 umschaltbar), per `xdg-open` direkt im Browser auf dem Rechner öffnen. Bei Bedarf zusätzlich Preview/Server (`python3 -m http.server`).
5. **Selbstcheck vor dem Zeigen:** Screenshot/Snapshot in Desktop- und Mobile-Breite prüfen. Kaputtes Layout, Overflow oder Konsolenfehler erst fixen.
6. **Präsentieren (kurz):** `A – …`, `B – …`, `C – …`, dann „welche? oder mix?“. Danach stoppen und auf die Wahl warten.
7. **Nach der Wahl:** im echten Code umsetzen (kleine Commits), dann den Demo-Server stoppen und `.design-demos/<slug>` löschen.
