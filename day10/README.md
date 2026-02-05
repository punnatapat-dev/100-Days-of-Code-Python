## 📘 Day 10 – Functions with Outputs

🎯 **Lerninhalte**
- Verständnis der **drei Arten von Funktionen**
  - Einfache Funktionen (ohne Input / Output)
  - Funktionen mit **Input**
  - Funktionen mit **Output** (`return`)
- Verwendung von `return`, um Ergebnisse aus Funktionen zurückzugeben
- Weiterverwendung von Rückgabewerten in späteren Berechnungen
- Reduzierung von Code-Duplikaten  
  (**DRY – Don’t Repeat Yourself**)

⚙️ **Grundidee von Funktionen**
- Funktion = **Maschine**
- **Input → Verarbeitung → Output**
- Output einer Funktion kann Input einer anderen Funktion sein  
  (**Function Chaining**)

🔁 **print vs. return**
- `print` → zeigt Werte **nur auf dem Bildschirm**
- `return` → gibt Werte **an den aufrufenden Code zurück** (weiterverwendbar)

---

## 📘 Multiple Return Statements

🧠 **Zentrale Konzepte**
- Sobald `return` ausgeführt wird, **endet die Funktion sofort**
- Code **nach `return` wird nicht mehr ausgeführt**

🔁 **Multiple Return**
- Eine Funktion kann mehrere `return`-Stellen haben
- Vorteile:
  - Klare Behandlung verschiedener Bedingungen
  - **Early Exit** bei Fehlern oder ungültigen Inputs
  - Effizienterer Code

🔙 **Empty Return (Early Return)**
- `return` ohne Wert beendet die Funktion sofort
- Typische Nutzung:
  - Unvollständige oder falsche Benutzereingaben
  - Schutz vor fehlerhafter Weiterverarbeitung

✅ **Best Practice**
- Statt leerem `return` besser **aussagekräftige Rückgabewerte** verwenden
- Macht Code:
  - lesbarer
  - leichter zu debuggen
  - robuster

---

## 📘 Docstrings in Python

📌 **Was ist ein Docstring?**
- Docstrings sind **offizielle Dokumentationen** für Funktionen oder Module
- Erklären:
  - Zweck der Funktion
  - erwartete Inputs
  - Rückgabewerte

✍️ **Schreibweise**
- Direkt **nach der Funktionsdefinition**
- Mit `""" """`

Beispiel:
`def format_name(f_name, l_name):`
`    """Formats first and last name into title case."""`
`    return f"{f_name.title()} {l_name.title()}"`

📄 **Eigenschaften**
- Mehrzeilig möglich
- Abrufbar wie bei Built-in-Funktionen (z. B. `len()`)
- Empfohlen für sauberen, professionellen Code

⚠️ Hinweis:
- `""" """` **nicht** als Kommentar-Ersatz verwenden
- Für Kommentare mehrere Zeilen markieren und  
  `Ctrl + /` (Windows) oder `Cmd + /` (Mac) nutzen

---

## 📘 Project – Calculator  
*(Functions + Dictionary + Recursion)*

🎯 **Projektziele**
- Entwicklung eines **textbasierten Taschenrechners**
- Ablauf:
  - Zahl eingeben
  - Operator wählen (`+ - * /`)
  - nächste Zahl eingeben
  - Gleichung + Ergebnis anzeigen
- Benutzerentscheidung:
  - `y` → weiterrechnen mit letztem Ergebnis
  - `n` → neue Berechnung starten

🧠 **Verwendete Konzepte**
- Funktionen mit Input & Output (`return`)
- Funktionen als Werte in einem Dictionary speichern
- Auswahl der Funktion über den Operator-Key  
  z. B. `operations["+"]`
- Schleifen für fortlaufende Berechnungen
- **Recursion** (`calculator()` erneut aufrufen) für Neustart
- Verwendung von `float()` für Dezimaldivision
- Ausgabe einer vollständigen Rechnung  
  z. B. `5 * 3 = 15.0`
- Anzeige eines Logos zu Beginn:
  - `from art import logo`
  - `print(logo)`

🔁 **Programmablauf (Flow)**
- `num1` eingeben
- Operatoren anzeigen (Keys von `operations`)
- `operation_symbol` wählen
- `num2` eingeben
- Berechnung:
  - `answer = operations[operation_symbol](num1, num2)`
- Abfrage `y/n`
  - `y` → `num1 = answer`, weiterrechnen
  - `n` → Neustart durch erneuten Funktionsaufruf
