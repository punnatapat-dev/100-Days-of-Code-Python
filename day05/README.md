## 📘 Day 5 –  Beginner – Python Loops 🔐

### 🔁 Loops (for loop)
- Eine **Schleife (Loop)** führt denselben Code mehrmals aus, ohne ihn zu wiederholen.
- Die `for`-Schleife wird sehr häufig verwendet, besonders in Kombination mit **Listen**.

### for loop + List
- Mit `for` werden alle Elemente einer Liste der Reihe nach durchlaufen.
- In jedem Durchlauf wird ein Element in einer temporären Variable gespeichert.

**Beispielidee**
- Durchlaufe eine Liste
- Weise jedem Element eine Variable zu
- Führe den Code für jedes Item aus

### ⚠️ Einrückung (sehr wichtig)
- **Eingerückter Code** gehört zur Schleife → wird jedes Mal ausgeführt
- **Nicht eingerückter Code** gehört nicht zur Schleife → wird nur einmal nach der Schleife ausgeführt

### ⭐ Wichtige Punkte
- Eine `for`-Schleife kann mehrere Anweisungen enthalten
- Sie reduziert Wiederholungen und macht den Code übersichtlicher

---

### 🔢 Arbeiten mit Zahlen & for-Schleifen

#### Python & Zahlen
- Python besitzt eingebaute Funktionen wie `sum()` und `max()`
- Diese Funktionen können mit iterierbaren Objekten wie Listen verwendet werden

#### Konzept: Accumulator
- Eine Variable zum Zwischenspeichern von Werten während der Schleife
- Startet mit einem Anfangswert, z. B. `total = 0`
- Der Wert wird in jedem Durchlauf erhöht

#### `max()` mit einer for-Schleife nachbauen
- Erstelle eine Variable zur Speicherung des größten Werts
- Durchlaufe alle Zahlen mit einer Schleife
- Vergleiche die Werte mit einer `if`-Bedingung
- Aktualisiere den Wert, wenn eine größere Zahl gefunden wird

**Lernziele**
- Kombination von `for`-Schleifen und `if`-Bedingungen
- Verständnis der Funktionsweise von eingebauten Funktionen

---

### 📌 for-Schleifen mit `range()`
- `range()` erzeugt eine Zahlenfolge
- Eine Liste ist dafür nicht zwingend erforderlich

**Beispiele**
- `range(1, 10)` → 1–9  
- `range(1, 11)` → 1–10  
- `range(1, 11, 3)` → 1, 4, 7, 10  


---

## 🧩 Mini Project – Username Generator 👤🔐

📌 **Projektbeschreibung**

Ein kleines textbasiertes Python-Programm zur Übung von **for-Loops**, **Listen**,  
**Zufallsfunktionen** und **String-Verarbeitung**.

Der Benutzer gibt an, wie viele **Adjektive**, **Nomen**, **Symbole** und **Zahlen**  
im Benutzernamen enthalten sein sollen.  
Das Programm erzeugt anschließend einen **zufälligen, einzigartigen Benutzernamen**.

---

### 🛠 Das Projekt verwendet:

- Benutzereingaben (`input`)
- Schleifen (`for loop`)
- Listen (`list`)
- Zufallsfunktionen (`random.choice`, `random.shuffle`)
- String-Verkettung (`+=`)
- Zahlenbereiche mit `range()`

---

▶️ **Live Demo (Replit)**  
[https://replit.com/@punnatapat-dev/Username-Generator](https://replit.com/@punnatapat-dev/Username-Generator)
