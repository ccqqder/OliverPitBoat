---
title: Atomic Presence Support
layout: simple
summary: Support und Kontakt für Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---


---

## FAQ

**F: Der QR-Code im Video ist unscharf und kann bei der Überprüfung nicht eingelesen werden?**  
A: Sorgen Sie während der Aufnahme für ausreichende Bildschirmhelligkeit und halten Sie die Kamera 30–50 cm vom Bildschirm entfernt. Der QR-Code aktualisiert sich einmal pro Sekunde — die Kamera muss klar fokussieren können. Wenn das Problem weiter besteht, versuchen Sie eine niedrigere Aufnahmeauflösung.

**F: Die Audio-Wasserzeichen-Verifikation schlägt fehl?**  
A: Die Wasserzeichen-Verifikation kann fehlschlagen, wenn: das Audio stark komprimiert wurde (z. B. weitergeleitet über WhatsApp), das Audio abgeschnitten wurde oder zu starke Hintergrundgeräusche vorhanden waren. Nehmen Sie in einer ruhigen Umgebung auf und verwenden Sie für die Verifikation die Originalaudiodatei.

**F: Die digitale Signatur ist auf einem neuen Gerät ungültig?**  
A: Der Signaturschlüssel jedes Geräts wird im iOS-Keychain gespeichert; ein neues Gerät erzeugt einen anderen Schlüssel. Sie müssen den öffentlichen Schlüssel NICHT manuell exportieren — jede von der App geschriebene `.evidence.json` enthält bereits den öffentlichen Schlüssel, der für die Signatur dieser Aufnahme verwendet wurde, sodass jede Person mit der Beweisdatei die Verifikation unabhängig vom Gerät durchführen kann.

**F: Die App ist während der Aufnahme abgestürzt — ist die Datei noch da?**  
A: Wenn die App unerwartet abstürzt, können Teilaufnahmen im Documents-Verzeichnis verbleiben. Öffnen Sie die App erneut, tippen Sie oben im Hauptbildschirm auf den Button **VERIFIZIEREN** und prüfen Sie die drei Tabs (Stufe 1 / Stufe 2 / Stufe 3) auf wiederherstellbare Dateien.

**F: Die Hash-Ketten-Verifikation zeigt „Integrität gebrochen", obwohl ich die Aufnahme nicht bearbeitet habe?**  
A: Mögliche Ursachen: Die App wurde während der Aufnahme vom System unterbrochen, niedriger Akkustand oder ein Schreibfehler durch unzureichenden Speicher. Stellen Sie vor der Aufnahme ausreichend Akku und Speicherplatz sicher.

---

## Fehlersuche

1. **Stellen Sie ausreichend Speicherplatz sicher** (empfohlen mindestens 2 GB frei)
2. **Halten Sie den Bildschirm während der Aufnahme aktiv**, um Systemunterbrechungen zu vermeiden
3. **App erzwingen-beenden und neu starten**
4. **iOS-Version prüfen** ≥ 17.0
5. Wenn ein bestimmtes Szenario regelmäßig Probleme verursacht, machen Sie einen Screenshot der Fehlermeldung und schreiben Sie uns

---

## Support kontaktieren

📧 **qqder339@gmail.com**  
Betreff: `[Atomic Presence] Problembeschreibung`

Bitte angeben: Gerätemodell, iOS-Version, App-Version, Aufnahmemodus (Video/Audio), Schritte zur Reproduktion.

> Diese App erfasst keine Nutzerdaten. Alle kryptografischen Operationen laufen vollständig auf dem Gerät. Wir haben keinen Zugriff auf Ihre Aufnahmen.
