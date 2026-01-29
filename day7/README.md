# 📘 Day 7 – Hangman Projekt

Dieses Projekt ist die Umsetzung des Spiels **Hangman** mit **Python**.  
Der Spieler muss ein Wort erraten, indem er Buchstaben einzeln eingibt.

- Falsche Vermutung → Ein Leben geht verloren und die Hangman-Zeichnung wird erweitert  
- Richtige Vermutung → Der Buchstabe wird im Wort ergänzt, kein Leben geht verloren  
- Ziel ist es, **das Wort vollständig zu erraten, bevor alle Leben aufgebraucht sind**

---

## 🧠 Wiederholte Konzepte / Lerninhalte
- `for`-Schleifen und `while`-Schleifen
- `if / else`
- Listen (Lists) und Strings
- Funktion `range()`
- Verwendung von Modulen
- Kombination mehrerer Python-Konzepte in einem Projekt

---

## 🎯 Ziel des Projekts
- Ein funktionsfähiges Hangman-Spiel erstellen
- Logisches Denken (Logic) trainieren
- Strukturiertes Programmieren anhand eines echten Projekts üben

---

## 📌 Logik des Hangman-Spiels 
Bevor mit dem Programmieren begonnen wird, muss das Spielprinzip von Hangman klar verstanden werden.  
Zur Planung der Programmlogik wird ein Flowchart verwendet.

Ablauf des Spiels:
1. Spielstart → Zufälliges Wort auswählen
2. Anzeige von Unterstrichen `_` entsprechend der Wortlänge
3. Der Spieler rät einen Buchstaben
   - Richtiger Buchstabe → Buchstabe wird im Wort ergänzt
   - Falscher Buchstabe → Ein Leben geht verloren und die Hangman-Zeichnung wird erweitert
4. Überprüfung des Spielendes
   - Alle Buchstaben erraten → Gewinn
   - Keine Leben mehr → Verlust

---

## 🧩 Step 1 – Grundlagen des Spiels
Das Projekt ist in insgesamt **5 Schritte (Steps)** unterteilt.

### Aufgaben
- Ein Wort zufällig aus `word_list` auswählen und in `chosen_word` speichern
- Buchstabeneingabe vom Benutzer mit `input()` und Umwandlung in Kleinbuchstaben
- Mit einer `for`-Schleife jeden Buchstaben des Wortes überprüfen
  - Gleich → `"Right"`
  - Ungleich → `"Wrong"`

**Ziel von Step 1**
- Zufällige Wortauswahl verstehen
- Benutzereingaben verarbeiten
- Verwendung von `for`-Schleifen mit Strings
- Buchstaben einzeln vergleichen

---

## 🧩 Step 2 – Wortanzeige zum Erraten
**Ziel:**  
Das Lösungswort nicht direkt anzeigen, sondern als `_ _ _` darstellen.

### Aufgaben
- Einen Platzhalter mit `_` entsprechend der Wortlänge erstellen
- Die Variable `display` verwenden
- Mit einer `for`-Schleife das Wort durchlaufen
  - Wenn der Buchstabe `guess` entspricht → Buchstabe anzeigen
  - Sonst → `_` anzeigen

---

## 🧩 Step 3 – Wiederholbares Spielen & Gewinnen
**Ziel:**  
Das Spiel soll mehrere Versuche erlauben und richtige Buchstaben speichern.

### Aufgaben
- Verwendung von `while not game_over`
- Eine Liste `correct_letters` erstellen, um richtige Buchstaben zu speichern
- `display` nach jedem Versuch aktualisieren
- Wenn keine `_` mehr vorhanden sind → Spieler gewinnt

---

## 🧩 Step 4 – Leben & Hangman-Zeichnung
**Ziel:**  
Ein echtes Verlust-Szenario im Spiel umsetzen.

### Aufgaben
- Variable `lives = 6` erstellen
- Bei falscher Vermutung → `lives -= 1`
- Wenn `lives == 0` → Spiel endet (Verlust)
- Anzeige der Hangman-Zeichnung mit `stages[lives]` (ASCII Art)

---

## 🧩 Step 5 – Projekt abschließen (Final)
**Ziel:**  
Das Spiel vervollständigen, benutzerfreundlicher gestalten und Module nutzen.

### Aufgaben
- Import der benötigten Module
  - `hangman_words` → `word_list`
  - `hangman_art` → `stages`, `logo`
- Anzeige des Logos beim Spielstart
- Falls ein Buchstabe erneut geraten wird → Hinweis anzeigen (kein Lebensverlust)
- Bei falschem Buchstaben → Hinweis anzeigen, dass ein Leben verloren wurde
- Anzeige der verbleibenden Leben (`lives / 6`)
- Bei Spielverlust → Anzeige des richtigen Wortes (`chosen_word`)

---
