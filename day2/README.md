## 📘 Day 2 – Primitive Datentypen in Python

🧩 **Thema:** Grundlegende (primitive) Datentypen in Python  
In diesem Abschnitt werden die wichtigsten Datentypen in Python vorgestellt und anhand
einfacher Code-Beispiele erklärt.  
Dazu gehören **Strings, Integer, Floats und Booleans**.

### 📝 Inhalte & Beispiele

```python
# 📝 String – Subskription
print("Hello"[0])

# 📝 String – Textverkettung
print("123" + "345")

# 🔢 Integer – ganze Zahlen
print(123 + 345)

# 🔢 Large Integer
print(123_456_789)

# 🔣 Float – Gleitkommazahl
print(3.14159)

# ✅ Boolean – Wahrheitswerte
print(True)
print(False


🧩 Thema: Datentypen, TypeError, Type Checking und Type Conversion
Dieser Abschnitt zeigt, wie verschiedene Datentypen in Python funktionieren,
wie TypeErrors entstehen und wie Datentypen überprüft und konvertiert werden können.
Die Beispiele helfen dabei, typische Fehler zu erkennen und zu vermeiden.

📝 Inhalte & Beispiele
# ❌ TypeError (falscher Datentyp)
# len(123)

# ✅ Kein TypeError (String)
len("Hello")

# 🔍 Type Checking
print(type("abc"))    # <class 'str'>
print(type(123))      # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>

# 🔄 Type Conversion (Umwandlung von Datentypen)
str()
int()
float()
bool()

# 👤 Benutzer-Eingabe und Länge des Namens
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))                      # int

# 🖨 Ausgabe ohne Fehler durch Type Conversion
print("Number of letters in your name: " + str(length_of_name))


🧩 Thema: Mathematische Operatoren und Rechenreihenfolge (PEMDAS)
In diesem Abschnitt werden grundlegende mathematische Operatoren in Python sowie
die Rechenreihenfolge nach der PEMDAS-Regel erklärt.
Durch die Verwendung von Klammern kann das Ergebnis einer Berechnung gezielt beeinflusst werden.

📝 Inhalte & Beispiele
# 🧮 Grundlegende Rechenoperationen
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

# 📐 Rechenreihenfolge (PEMDAS)
# P = Parentheses ()
# E = Exponents **
# MD = Multiplication or Division
# AS = Addition or Subtraction

# 🔢 Erwartete Ausgabe: 3
print(3 * (3 + 3) / 3 - 3)


🧩 **Thema:** Zahlenverarbeitung, Rundung und Formatierung in Python  
In diesem Abschnitt werden verschiedene Möglichkeiten zur Bearbeitung von Zahlen in Python
vorgestellt. Dazu gehören das Abschneiden von Dezimalstellen, das Runden von Zahlen,
Assignment-Operatoren sowie die Verwendung von f-Strings zur formatierten Ausgabe.

### 📝 Inhalte & Beispiele

```python
# 🔽 Flooring einer Zahl (Dezimalstellen entfernen)
print(int(7.98421))        # Ergebnis: 7

# 🔼 Runden einer Zahl (mathematisches Runden)
print(round(7.98421))      # Ergebnis: 8
print(round(5.4321))       # Ergebnis: 5
print(round(5.4321, 3))    # Ergebnis: 5.432

# ➕➖✖️➗ Assignment-Operatoren
score = 20
score += 5    # score = 25
score -= 3    # score = 22
score *= 2    # score = 44
score /= 4    # score = 11.0

print(score)

# 🧵 f-Strings (formatierte Ausgabe)
points = 15
height = 1.75
is_active = True

print(f"Points: {points}, Height: {height} m, Active: {is_active}")


