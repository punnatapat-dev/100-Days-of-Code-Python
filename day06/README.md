## 📘 Day 6 – Python Functions & Karel 🤖

## 🔧 Functions (Funktionen)

### Konzept
- Funktionen fassen mehrere Anweisungen unter einem Namen zusammen
- Reduzieren Code-Wiederholungen
- Erhöhen Lesbarkeit und Wartbarkeit des Programms

### Syntax
```python
def my_function():
    do_something()
```

### Wichtige Punkte
- Verwendung des Schlüsselworts `def`
- Klammern `()` sind erforderlich
- Code innerhalb der Funktion muss eingerückt sein
- Funktionen werden erst beim Aufruf ausgeführt

---

## ⚠️ Indentation (Einrückung – sehr wichtig in Python)

- Python verwendet Einrückung statt geschweifter Klammern `{ }`
- Eingerückter Code gehört zu einem Block (Funktion, Schleife, Bedingung)
- Falsche Einrückung führt zu Syntax- oder Logikfehlern

### Standard
- 4 Leerzeichen pro Einrückung
- Empfohlener Stil: Spaces statt Tabs (PEP 8)

---

## 🔁 while-Schleife

### Konzept
- Verwendung, wenn die Anzahl der Wiederholungen nicht bekannt ist
- Der Code wird ausgeführt, solange eine Bedingung `True` ist

### Syntax
```python
while condition:
    do_something()
```

### Beispiel
```python
while not at_goal():
    move()
```

### Achtung
- Gefahr von Endlosschleifen (infinite loops)
- Die Bedingung muss sich irgendwann zu `False` ändern

---

## 🧠 for-Schleife vs. while-Schleife

| for-Schleife | while-Schleife |
|-------------|---------------|
| Anzahl der Durchläufe bekannt | Anzahl unbekannt |
| Nutzung mit `list` oder `range()` | Nutzung mit Bedingungen |
| Sicherer | Flexibler, aber fehleranfälliger |

---

## 🔀 Bedingte Anweisungen (if / elif / else)

- Dienen der Entscheidungsfindung im Programm
- Reagieren dynamisch auf unterschiedliche Situationen zur Laufzeit

### Logik-Beispiel
- Wenn eine Wand vor dem Roboter ist → springen
- Wenn keine Wand vorhanden ist → vorwärts gehen
- Wenn kein Weg frei ist → Richtung ändern

---

## 🔍 Verwendete Conditions (Reeborg’s World)

- `front_is_clear()`
- `wall_in_front()`
- `right_is_clear()`
- `wall_on_right()`
- `at_goal()`

### Logik-Tipp
- `not` kehrt den Wahrheitswert einer Bedingung um
- Code liest sich wie ein englischer Satz: `while not at_goal`

---

## 🤖 Mini-Projekte – Robot-Challenges

### 🟢 Hurdle 1
- Verwendung der `for`-Schleife
- Feste Anzahl von Hindernissen

### 🟢 Hurdle 2
- Verwendung von `while not at_goal`
- Zufällige Zielposition

### 🟢 Hurdle 3
- Zufällige Wandplatzierung
- Entscheidungslogik mit `if`

### 🟢 Hurdle 4
- Unterschiedliche Wandhöhen
- Verschachtelte `while`-Schleifen
- Anpassung der `jump()`-Funktion

---

## 🧭 Final Project – Maze Solver

### Algorithmus: Right-Hand-Rule
Der Roboter folgt konsequent der rechten Wand, um den Ausgang aus dem Labyrinth zu finden.

### Entscheidungsreihenfolge
1. Ist rechts frei → nach rechts drehen und vorwärts gehen
2. Ist vorne frei → geradeaus gehen
3. Andernfalls → nach links drehen

### Verwendete Konzepte
- Funktionen
- while-Schleifen
- if / elif / else
- Bedingungen
- Debugging und Edge Cases

---

## 🧠 Didaktischer Hintergrund

Die Aufgaben basieren auf dem Konzept von **Karel the Robot**,  
einem klassischen Lernmodell zur Vermittlung von Programmierlogik.  
Die Umsetzung erfolgt mit **Reeborg’s World**, einer Python-basierten Lernumgebung.

🔗 Reeborg’s World: https://reeborg.ca  
🔗 Karel the Robot (Wikipedia):  
https://en.wikipedia.org/wiki/Karel_(programming_language)

---


