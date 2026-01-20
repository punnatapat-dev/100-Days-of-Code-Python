## 📘 Day 2 – Python Basics

---

## 🧩 Grundlagen

### 🧩 Thema: Python Basics – Datentypen und Rechenoperationen

In diesem Abschnitt werden grundlegende Python-Konzepte vorgestellt und anhand
einfacher Beispiele erklärt. Dazu gehören Datentypen, Type Checking,
Type Conversion sowie mathematische Operatoren.

---

## 📝 Inhalte & Beispiele

- 📝 **String – Subskription**  
  `print("Hello"[0])`

- 📝 **String – Textverkettung**  
  `print("123" + "345")`

- 🔢 **Integer – ganze Zahlen**  
  `print(123 + 345)`

- 🔢 **Large Integer**  
  `print(123_456_789)`

- 🔣 **Float – Gleitkommazahl**  
  `print(3.14159)`

- ✅ **Boolean – Wahrheitswerte**  
  `print(True)`  
  `print(False)`

- ❌ **TypeError (falscher Datentyp)**  
  `len(123)`

- ✅ **Kein TypeError**  
  `len("Hello")`

- 🔍 **Type Checking**  
  `type("abc")` → `str`  
  `type(123)` → `int`  
  `type(3.14)` → `float`  
  `type(True)` → `bool`

- 🔄 **Type Conversion**  
  `str()` · `int()` · `float()` · `bool()`

- 👤 **Benutzereingabe & String-Länge**  
  `name_of_the_user = input("Enter your name")`  
  `len(name_of_the_user)`

- ➕➖✖️➗ **Mathematische Operatoren**  
  `+  -  *  /  //  **`

- 📐 **Rechenreihenfolge (PEMDAS)**  
  `print(3 * (3 + 3) / 3 - 3)` → Ergebnis: `3`

- 🔢 **Number Manipulation**  
  `int(7.98421)` → Flooring  
  `round(7.98421)` → Runden  
  `round(5.4321, 3)` → Dezimalstellen

- 🧵 **f-Strings (formatierte Ausgabe)**  
  `f"Points: {points}, Height: {height} m, Active: {is_active}"`

---

## 🍕 Mini Project – Pizza Cost Calculator

### 📌 Projektbeschreibung
Ein kleines Python-Projekt zur Berechnung des Pizza-Preises pro Person.
Das Projekt kombiniert Benutzereingaben, Datentypen, mathematische Berechnungen
und formatierte Ausgaben.

### ▶️ Live Demo
https://replit.com/@punnatapat-dev/Pizza-Kostenrechner?v=1

### 🛠️ How to Run (Local)
`python main.py`
