## 📘 Day 9 – Python Dictionaries & Nesting

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
