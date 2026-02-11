## 📘 Day 14 – Higher or Lower Game

🎯 **Projektziel**
Ein **Higher-or-Lower**-Spiel erstellen, bei dem der Spieler zwei Instagram-Accounts vergleicht und rät, wer **mehr Follower** hat.

Das Spiel läuft so lange weiter, wie der Spieler richtig rät.  
Sobald der Spieler falsch liegt, wird der **Endstand (Score)** angezeigt.

---

## 🧠 Zentrale Programmierfähigkeit
Dieses Projekt trainiert eine entscheidende Fähigkeit:

**Ein großes Problem in kleinere, lösbare Teilaufgaben zu zerlegen.**

Das eigentliche Lernziel ist nicht nur Code zu schreiben –  
sondern eine Lösung **zu analysieren, zu strukturieren und Schritt für Schritt aufzubauen.**

---

## 🧩 Problemzerlegung (Schritt-für-Schritt-Planung)

Vor dem Programmieren wurde das Projekt in Aufgaben aufgeteilt:

- ASCII Art anzeigen (Logo und VS-Symbol)
- Zwei zufällige Accounts aus `game_data` erzeugen
- Account-Daten lesbar formatieren
- Benutzereingabe abfragen (A oder B)
- Follower-Zahlen auslesen
- Follower-Zahlen vergleichen
- Prüfen, ob die Antwort korrekt ist
- Score zählen und aktualisieren
- Spiel wiederholen, solange die Antwort korrekt ist
- Das vorherige B wird im nächsten Durchlauf zu A
- Bildschirm zwischen Runden leeren
- Spiel beenden, wenn der Spieler falsch rät

---

## 🏗 Projektstruktur

Das Projekt besteht aus:
- `main.py`
- `art.py`
- `game_data.py`

**art.py** enthält:
- `logo` (ASCII Art)
- `vs` (ASCII Art)

**game_data.py** enthält:
- `data` → Liste von Dictionaries

Jedes Dictionary enthält:
- `name`
- `follower_count`
- `description`
- `country`

---

## 🛠 Wichtige Funktionen

### 1️⃣ `format_data(account)`
Formatiert Account-Informationen für die Ausgabe.

`def format_data(account):`  
`    name = account["name"]`  
`    description = account["description"]`  
`    country = account["country"]`  
`    return f"{name}, a {description}, from {country}"`

---

### 2️⃣ `check_answer(guess, a_followers, b_followers)`
Prüft, ob der Spieler richtig geraten hat.

`def check_answer(guess, a_followers, b_followers):`  
`    if a_followers > b_followers:`  
`        return guess == "a"`  
`    else:`  
`        return guess == "b"`

---

## 🔁 Game-Loop-Logik

Das Spiel läuft in einer `while`-Schleife:

- `game_should_continue = True`

`while game_should_continue:`

Wenn die Antwort richtig ist:
- Score erhöhen
- B → A verschieben
- Neues B generieren
- Spiel fortsetzen

Beispiel:
- `account_a = account_b`
- `account_b = random.choice(data)`

Wenn die Antwort falsch ist:
- Endstand anzeigen
- Flag auf `False` setzen
- Schleife beenden

---

## ⚠ Wichtiger Logik-Detailpunkt
A und B dürfen **nie identisch** sein:

`while account_a == account_b:`  
`    account_b = random.choice(data)`

---

## 🧹 Bildschirm zwischen Runden leeren
`print("\n" * 20)`  
`print(logo)`

---

## 📊 Lernergebnisse
Nach diesem Projekt verstehst du:
- wie man `random.choice()` nutzt
- wie man mit einer **Liste von Dictionaries** arbeitet
- wie man wiederverwendbare Funktionen schreibt
- wie man Boolean-Werte (`True/False`) zurückgibt
- wie man Game-Loops sauber strukturiert
- wie man Flags zur Ablaufsteuerung nutzt
- wie man Score zählt und erhöht
- wie man State zwischen Runden verwaltet

---

## 📅 Lernstrategie (Sehr wichtig)

Wenn du Schwierigkeiten hattest und die Lösung anschauen musstest:
Das ist normal. Das bedeutet: **Du lernst.**

Folge diesem Prozess:

### 🧠 Schritt 1 – Lösung verstehen
Nicht nur Code lesen, sondern fragen:
- Warum gibt die Funktion `True/False` zurück?
- Warum muss B zu A werden?
- Warum nutzen wir eine `while`-Schleife?
- Warum funktioniert `return guess == "a"`?

Falls nötig: recherchieren oder Lektionen erneut ansehen.

### ✍ Schritt 2 – Aus dem Kopf neu schreiben
Lösung schließen, Datei löschen, neu bauen – ohne Hilfe.

Wenn du es neu bauen kannst → du verstehst es.  
Wenn nicht → erneut überprüfen und wiederholen.

### 📆 Schritt 3 – Wiederholung einplanen
In den Kalender eintragen:

**Redo Day 14 – Higher Lower Game (No Help)**  
→ 7 Tage später

Das nutzt **Spaced Repetition** und stärkt das Langzeitgedächtnis.

🔁 Erweiterter Wiederholungsplan:
- nach 1 Woche
- nach 1 Monat
- nach 3 Monaten

---

## 🚀 Abschlussreflexion
Dieses Projekt ging nicht um das Spiel.

Es ging darum, **wie ein Programmierer zu denken**:
- Probleme zerlegen
- das kleinste Teilproblem zuerst lösen
- Schritt für Schritt aufbauen
- häufig testen
- in Funktionen strukturieren
- Loops und Logik sauber verwenden

So arbeiten echte Entwickler.
