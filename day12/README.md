## 🎯 Number Guessing Game 

🧠 Zentrale Konzepte im Projekt
- Local Scope vs Global Scope
- Verwendung von `return` statt direkter Änderung von globalen Variablen
- Einsatz von Global Constants
- Zerlegung eines großen Problems in kleinere Funktionen
- Steuerung des Programmablaufs mit einer `while`-Schleife

🕹️ Spielablauf – Überblick
- Das Programm wählt zufällig eine Zahl zwischen **1 und 100**
- Eine Willkommensnachricht wird angezeigt
- Der Benutzer wählt den Schwierigkeitsgrad
  - Easy → **10 Versuche**
  - Hard → **5 Versuche**
- Der Benutzer gibt eine Zahl ein
- Das Programm überprüft die Eingabe
  - Too high / Too low / Correct
- Bei falscher Antwort wird die Anzahl der Versuche reduziert
- Das Spiel endet, wenn:
  - die Zahl richtig erraten wird → **Gewonnen**
  - keine Versuche mehr übrig sind → **Verloren**

⚙️ Global Constants
EASY_LEVEL_TURNS = 10  
HARD_LEVEL_TURNS = 5  

Warum Global Constants?
- Werte ändern sich nicht
- Änderungen sind an einer zentralen Stelle möglich
- Erhöht Lesbarkeit und verhindert versehentliche Änderungen in Funktionen

🔢 Zufällige Zahl erzeugen
`from random import randint`  
`answer = randint(1, 100)`

- `randint()` erzeugt eine Zufallszahl
- Sowohl **1 als auch 100** sind enthalten
- Die Zahl bleibt während des gesamten Spiels gleich

Wichtige Idee:
- Keine Nutzung von globalen Variablen
- Kommunikation ausschließlich über `return`

Wichtige Punkte:
- Versuche werden **nur bei falscher Antwort** reduziert
- Keine Änderung globaler Variablen
- Docstring erklärt Zweck der Funktion

🧠 Wichtige Lernpunkte
- Globale Variablen nicht direkt in Funktionen verändern
- `return` zur Kommunikation zwischen Funktionen nutzen
- Große Probleme in kleine, verständliche Schritte aufteilen
- Code so schreiben, dass er leicht nachvollziehbar ist
- Schwierige Aufgaben fördern echtes Lernen

✨ Erweiterungsmöglichkeiten
- Hinzufügen von ASCII Art (`art.py`)
- Neustart-Funktion (Replay)
- Verbesserung der Texte und User Experience
- Anpassung des Zahlenbereichs (z. B. 1–1000)
