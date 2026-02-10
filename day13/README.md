## 🐞 Debugging – Wichtige Zusammenfassung

Debugging ist der Prozess des **Findens und Behebens von Fehlern (Bugs)** im Code.  
Es ist eine der wichtigsten Fähigkeiten für Programmierer.  
Bugs sind **kein persönlicher Fehler**, sondern ein natürlicher Teil des Lern-  
und Entwicklungsprozesses.

---

### 1️⃣ Problem klar beschreiben (Describe the problem)
- Code **Zeile für Zeile** lesen
- Sich fragen: *Was soll der Code tun? Was tut er gerade?*
- Vorsicht vor **falschen Annahmen**  
  (z. B. `range()` enthält den oberen Wert **nicht**)

---

### 2️⃣ Bug reproduzierbar machen (Reproduce the bug)
- Bugs, die nur manchmal auftreten, sind am schwierigsten
- Herausfinden, **welcher Input oder welche Bedingung** den Fehler auslöst
- Sobald der Bug reproduzierbar ist → **viel einfacher zu beheben**

---

### 3️⃣ „Computer spielen“ (Play Computer)
- Code gedanklich Schritt für Schritt durchgehen
- `if / elif / else` Bedingungen prüfen: **True oder False?**
- Oft entdeckt man so Fälle, für die **keine Bedingung definiert ist**

---

### 4️⃣ Errors immer zuerst beheben
- Fehler im Editor → Fehlermeldung und betroffene Zeile lesen
- Fehler in der Konsole → Fehlermeldung kopieren und recherchieren
- `try-except` verwenden, um Code robuster gegenüber unerwartetem Input zu machen

---

### 5️⃣ Print richtig einsetzen (Print is your best friend)
- Variablen mit `print()` ausgeben, um den Programmzustand zu prüfen
- Hilft, den Punkt zu finden, an dem Werte unerwartet werden
- Sehr häufiger Bug:
  - `==` statt `=` (Vergleich vs. Zuweisung)

---

### 6️⃣ Debugger verwenden
- Breakpoints setzen, um den Code anzuhalten
- Tools wie:
  - Step Over
  - Step Into
  - Step Into My Code
- Variablenwerte in **Echtzeit** beobachten
- Besonders hilfreich bei Loops und größeren Projekten

---

### 7️⃣ Pausen machen (Take a break)
- Zu langes Starren auf Code macht blind für Fehler
- Pause machen, schlafen oder später erneut anschauen
- Probleme werden oft plötzlich **klarer**

---

### 8️⃣ Andere um Hilfe bitten
- Mitschüler, Entwicklerfreunde, Discord, Communities
- Andere sind nicht an die gleichen Annahmen gebunden
- Nicht peinlich – beide Seiten lernen dabei

---

### 9️⃣ Code häufig ausführen
- Nicht zu viel Code schreiben und erst am Ende ausführen
- Kleine Änderung → Run → Ergebnis prüfen
- Bei mehreren Bugs: **einen nach dem anderen beheben**

---

### 🔟 Stack Overflow sinnvoll nutzen
- Zuerst suchen, bevor man fragt
- Fragen stellen, wenn man wirklich alles versucht hat
- Ein zentrales Werkzeug für jeden Programmierer

---

## 💡 Wichtiges Mindset
- Bugs ≠ schlechter Programmierer
- Jeder gefixte Bug = **eine Trainingseinheit fürs Gehirn**
- Je mehr Bugs man behebt → **desto besser wird man**
