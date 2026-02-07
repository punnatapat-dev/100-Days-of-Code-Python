## 📘 Day 9 – Python Dictionaries & Nesting

---

🎯 **Was ist ein Python Dictionary?**
- Speichert Daten im Format **Key : Value**
- Vergleichbar mit einem Wörterbuch im Alltag  
  - Key = Begriff  
  - Value = Erklärung  

Beispiel:
`programming_dictionary = { "Bug": "An error in a program that prevents it from running as expected.", "Function": "A piece of code that you can easily call over and over again." }`

🔍 **Zugriff auf Daten (Retrieve)**
- Zugriff erfolgt über den **Key**, nicht über einen Index (anders als bei Listen)

Beispiel:
`print(programming_dictionary["Bug"])`

⚠️ Der Key muss **korrekt geschrieben** sein und den **richtigen Datentyp** haben (z. B. String)

➕ **Neue Einträge hinzufügen**
`programming_dictionary["Loop"] = "The action of doing something over and over again."`

✏️ **Einträge ändern**
- Bestehenden Key verwenden und neuen Value zuweisen

`programming_dictionary["Bug"] = "A moth in your computer."`

🧹 **Leeres Dictionary / Dictionary zurücksetzen**
- Leeres Dictionary erstellen:
`empty_dict = {}`

- Dictionary vollständig leeren:
`programming_dictionary = {}`

➡️ Nützlich zum Zurücksetzen von Spielen oder Benutzerdaten

🔁 **Über ein Dictionary iterieren**
- Eine `for`-Schleife gibt **zuerst immer den Key** zurück

Beispiel:
`for key in programming_dictionary: print(key) print(programming_dictionary[key])`

🛠️ **Silent Auction Projekt**
- Verwendung eines Dictionaries zur Speicherung von **Bieternamen und Geboten**
- Mehrere Benutzereingaben verarbeiten
- Vergleich der Gebote zur Ermittlung des Gewinners
- Praxisnahe Übung zur Anwendung von Dictionaries

---

## 🎯Nesting: Lists & Dictionaries

📦 **Was ist Nesting?**
- Nesting bedeutet, dass eine **Liste oder ein Dictionary**  
  als Wert in einer anderen Liste oder einem anderen Dictionary gespeichert wird
- Ermöglicht die strukturierte Speicherung **komplexerer Daten**

📘 **Dictionary mit List als Value**

`travel_log = { "France": ["Paris", "Lille", "Dijon"], "Germany": ["Berlin", "Hamburg", "Stuttgart"] }`

Zugriff auf Daten:

`print(travel_log["France"][1])` → `Lille`

📗 **Liste in Liste (2D-Liste)**

`nested_list = ["A", "B", ["C", "D"]]`

Zugriff auf Daten:

`print(nested_list[2][1])` → `D`

📙 **Dictionary in Dictionary**

`travel_log = { "France": { "num_times_visited": 8, "cities_visited": ["Paris", "Lille", "Dijon"] }, "Germany": { "num_times_visited": 5, "cities_visited": ["Berlin", "Hamburg", "Stuttgart"] } }`

Zugriff auf mehrstufige Daten:

`print(travel_log["Germany"]["cities_visited"][2])` → `Stuttgart`

🧠 **Wichtige Denkweise**
- Zugriff auf ein **Dictionary** → über den **Key**
- Zugriff auf eine **Liste** → über den **Index**
- Schrittweise denken: **von außen nach innen**
- Auf korrekte Schreibweise der Keys achten (vermeidet `KeyError`)

---

## 📘 Day 9 – Blind (Silent) Auction Projekt

🎯 **Projektziele**
- Anwendung von **Python Dictionary**, **Loops** und **Functions** in einem realen Projekt
- Erstellung eines **Blind Auction** Programms mit geheimen Geboten
- Ermittlung des Gewinners anhand des **höchsten Gebots**

🧠 **Grundidee der Blind Auction**
- Jeder Benutzer gibt **Name + Gebot** ein
- Vorherige Gebote sind für andere Benutzer **nicht sichtbar**
- Nachdem alle Gebote abgegeben wurden, gibt das Programm den **Gewinner** bekannt

🗂️ **Datenstruktur**
- Verwendung eines Dictionaries zur Speicherung der Gebote

Beispiel:
`bids = { "Alice": 12, "Bob": 3, "Charlie": 1 }`

- **Key** → Name des Bieters  
- **Value** → Gebotener Preis  

🔁 **Programmablauf (Flow)**
- Anzeige des Programm-Logos
- Eingabe des Bieternamens
- Eingabe des Gebots
- Speicherung der Daten im Dictionary
- Abfrage, ob es weitere Bieter gibt
- Bei **Ja** → Bildschirm leeren → neue Eingabe
- Bei **Nein** → Gewinner berechnen → Ergebnis anzeigen

🧹 **Bildschirm leeren**
- Erzeugung vieler leerer Zeilen, um vorherige Gebote zu verbergen

`print("\n" * 100)`

➡️ Verhindert, dass der nächste Bieter frühere Gebote sehen kann

🧩 **Funktion zur Gewinnerermittlung**
- Iteration über das Dictionary
- Vergleich aller Gebote
- Speicherung des höchsten Gebots und des Gewinnernamens

Grundidee:
`highest_bid = 0`  
`winner = ""`

🛠️ **Verwendete Werkzeuge**
- `input()` → Benutzereingaben erfassen
- `while`-Loop → mehrere Bieter ermöglichen
- `dictionary` → Speicherung der Gebote
- `function` → Trennung der Logik zur Gewinnerermittlung



