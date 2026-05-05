---
title: Atomic Presence — Datenschutzerklärung
layout: simple
showDate: false
showReadingTime: false
---

**Zuletzt aktualisiert: 15.04.2026**

---

## 1. Überblick

Atomic Presence, entwickelt von QQder339, ist ein Anti-Deepfake-Werkzeug, das kryptografische Hash-Ketten, digitale Signaturen und Audio-Wasserzeichen einsetzt, damit Nutzer:innen die Integrität ihrer Aufnahmen selbst überprüfen können.

**Kurz gesagt: Wir erfassen, speichern oder übertragen KEINE Ihrer personenbezogenen Daten an externe Server. Alle kryptografischen Operationen und Verifikationen werden auf dem Gerät durchgeführt.**

## 2. Daten, die wir NICHT erfassen

Diese App erfasst keine:

- Personenbezogene Daten (Name, E-Mail, Telefonnummer)
- Standortdaten
- Gerätekennungen
- Nutzungsanalyse- oder Tracking-Daten

## 3. Lokal gespeicherte Daten

Die folgenden Daten werden ausschließlich auf Ihrem Gerät gespeichert und niemals nach außen übertragen:

- **Audio-/Videodateien**: Alle aufgenommenen Inhalte werden im lokalen Speicher Ihres Geräts abgelegt
- **Hash-Ketten-Aufzeichnungen**: SHA-256-Hash-Sequenzen und zugehörige Verifikationsdaten
- **Digitale Signaturen**: Signaturdaten, erzeugt durch den auf dem Gerät laufenden Curve25519-Algorithmus
- **Verifikationsberichte**: Integritätsberichte und Metadaten-Aufzeichnungen
- **Anonymisierte Gerätekennung**: Jede `.evidence.json` enthält ein 16-stelliges Hex-Präfix von `SHA-256(identifierForVendor)`, das ausschließlich dazu dient, während der Verifikation Aufnahmen desselben Geräts zu korrelieren. Diese Kennung lebt nur innerhalb von Beweisdateien auf Ihrem Gerät, wird niemals an einen Server übertragen und kann nicht in die ursprünglichen Geräteinformationen zurückgerechnet werden

## 4. Kryptografische Funktionen (vollständig offline)

Alle Kernfunktionen werden auf dem Gerät ohne Netzwerkverbindung abgeschlossen:

- **Hash-Ketten-Erzeugung**: SHA-256-Hash-Sequenzen in Echtzeit; jegliche Berechnung läuft lokal
- **Digitale Signatur**: Verwendet den Curve25519-Algorithmus, um Aufnahmen auf dem Gerät zu signieren
- **Audio-Wasserzeichen**: Bettet FSK-Signale in Aufnahmen ein; jegliche Signalverarbeitung läuft auf dem Gerät
- **Verifikation**: Integritätsprüfung wird lokal berechnet

## 5. Wichtiger Hinweis

Die von dieser App verarbeiteten Inhalte (Audio, Video) können sensible Informationen enthalten. Die gesamte Verarbeitung findet auf Ihrem Gerät statt, und **wir können und werden niemals auf Ihre aufgenommenen Inhalte zugreifen**.

## 6. Drittanbieterdienste

Diese App verwendet **KEINE** Analyse- oder Werbe-Frameworks von Drittanbietern (Kein Google Analytics, kein Facebook SDK, keine Werbung).

## 7. Netzwerkzugriff

Diese App benötigt für sämtliche Funktionen **keine Netzwerkverbindung**. Der einzige Netzwerkzugriff ist:

- **Externe Links**: Öffnet den Browser beim Antippen entsprechender Links

## 8. Kontakt

📧 **qqder339@gmail.com**  
Betreff: Atomic Presence Datenschutzanfrage
