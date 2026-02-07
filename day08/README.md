## 📘 Day 8 – Funktionen mit Eingaben & Caesar Cipher

### 🧠 Lerninhalte
- Verwendung von **Funktionen mit Eingaben**
- Unterschied zwischen  
  - 🔹 **Parameter**: Name der Variable in der Funktionsdefinition  
  - 🔹 **Argument**: Tatsächlicher Wert beim Funktionsaufruf
- Praktische Anwendung von Funktionen in kleinen Programmen

---

### 🛠️ Funktionen mit Eingaben
- Funktionen fassen mehrere Codezeilen in einem Block zusammen
- Durch Eingaben in den Klammern kann das Verhalten der Funktion verändert werden
- Dieselbe Funktion kann unterschiedliche Ergebnisse liefern

---

### 🔢 Funktionen mit mehreren Eingaben
- Funktionen können **mehrere Parameter** erhalten (getrennt durch Kommas)

#### 📌 Positional Arguments
- Argumente werden der Reihenfolge nach zugewiesen
- ✔️ Kurz und einfach  
- ⚠️ Reihenfolge ist wichtig

#### 🏷️ Keyword Arguments
- Parameter werden beim Funktionsaufruf explizit benannt
- ✔️ Klarer und weniger fehleranfällig  
- ⚠️ Etwas längerer Code

---

### 🔐 Caesar Cipher – Grundidee
- Klassische Verschlüsselungsmethode aus der Zeit von **Julius Caesar**
- Jeder Buchstabe wird im Alphabet um eine bestimmte Anzahl verschoben (**Shift**)
- Sender und Empfänger müssen den gleichen Shift-Wert kennen

---

### 🧩 Caesar Cipher – Part 1 (Verschlüsseln)
- Erstellung der Funktion `encrypt(original_text, shift_amount)`
- Jeder Buchstabe wird einzeln verarbeitet
- Nutzung von `alphabet.index()` zur Positionsbestimmung
- Einsatz des **Modulo-Operators (%)**, um Index-Fehler zu vermeiden

📌 Beispiel:  
- Eingabe: `hallo`  
- Shift: `1`  
- Ausgabe: `ibmmp`

---

### 🔄 Caesar Cipher – Part 2 (Entschlüsseln & Kombination)
- **Entschlüsseln (decode)** ist das Gegenteil von Verschlüsseln
- Erstellung der Funktion `decrypt()`
- Kombination von `encrypt()` und `decrypt()` zu einer Funktion `caesar()`
- Steuerung über die Variable `encode_or_decode`
- Reduzierung von doppeltem Code und bessere Struktur

---

### ✨ Zusätzliche Features
- Beibehaltung von Zahlen, Leerzeichen und Sonderzeichen
- Anzeige eines Logos beim Start des Programms
- Möglichkeit, das Programm mit `ja / nein` neu zu starten

---

### 🎯 Lernziele
- Sicherer Umgang mit Funktionen und Eingaben
- Korrekte Verwendung von Parametern und Argumenten
- Umsetzung eines vollständigen Verschlüsselungs-/Entschlüsselungsprogramms
- Training der Problemlösungsfähigkeit durch Aufteilung in Teilprobleme
