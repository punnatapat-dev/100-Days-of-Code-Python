## 📘 Python Basics – Datentypen, Operatoren und Number Manipulation
---
## 🧩 Grundlagen

### 🧩 Thema: Python Basics – Datentypen und Rechenoperationen

In diesem Abschnitt werden grundlegende Python-Konzepte vorgestellt und anhand
einfacher Code-Beispiele erklärt.  
Dazu gehören **primitive Datentypen**, **Type Checking**, **Type Conversion**,
**mathematische Operatoren** sowie **Number Manipulation**.

---

### 📝 Inhalte & Beispiele

```python
# String – Subskription
print("Hello"[0])

# String – Textverkettung
print("123" + "345")

# Integer – ganze Zahlen
print(123 + 345)

# Large Integer
print(123_456_789)

# Float – Gleitkommazahl
print(3.14159)

# Boolean – Wahrheitswerte
print(True)
print(False)

# TypeError (falscher Datentyp)
# len(123)

# Kein TypeError
len("Hello")

# Type Checking
print(type("abc"))    # str
print(type(123))      # int
print(type(3.14))     # float
print(type(True))     # bool

# Type Conversion
str()
int()
float()
bool()

# Benutzer-Eingabe
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_name))

# Mathematische Operatoren
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

# PEMDAS – Rechenreihenfolge
print(3 * (3 + 3) / 3 - 3)  # Ergebnis: 3

# Number Manipulation
print(int(7.98421))
print(round(7.98421))
print(round(5.4321, 3))

score = 20
score += 5
score -= 3
score *= 2
score /= 4

points = 15
height = 1.75
is_active = True

print(f"Points: {points}, Height: {height} m, Active: {is_active}")

# 🍕 Day 2 – Mini Project – Pizza Cost Calculator

## 📌 Projektbeschreibung
Ein kleines Python-Projekt zur Berechnung des Pizza-Preises pro Person.
Das Projekt kombiniert Benutzereingaben, Datentypen, mathematische Berechnungen
und formatierte Ausgaben.

## ▶️ Live Demo
https://replit.com/@punnatapat-dev/Pizza-Kostenrechner?v=1

## 🛠️ How to Run (Local)
```bash
python main.py
