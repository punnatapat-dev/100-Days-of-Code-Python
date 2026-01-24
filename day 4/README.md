# 📘 Day 4 – Randomization in Python

## 🎲 Random Module
In diesem Kapitel geht es um Zufälligkeit (Randomization) in Python.
Da Computer deterministisch arbeiten, nutzt Python sogenannte Pseudo-Zufallszahlen,
die mithilfe mathematischer Algorithmen erzeugt werden.

## 🧩Random-Modul importieren
Bevor Zufallsfunktionen verwendet werden können, muss das Modul importiert werden:

    import random

## Zentrale Funktionen

### random.randint(a, b)
- Erzeugt eine ganze Zufallszahl
- Wertebereich: von a bis b (inklusive)
- Geeignet für: Auswahl aus festen Möglichkeiten

Beispiele:

    random.randint(1, 6)   # Würfel
    random.randint(0, 1)   # Kopf oder Zahl

### random.random()
- Erzeugt eine Zufalls-Gleitkommazahl
- Wertebereich: 0 ≤ Zahl < 1
- Geeignet für: Wahrscheinlichkeiten und Prozentrechnungen

Beispiele:

    random.random()        # z.B. 0.348
    random.random() < 0.5  # 50 % Wahrscheinlichkeit

## Merkhilfe
- randint() → diskrete Auswahl (z.B. Würfel, Kopf/Zahl)
- random() → Wahrscheinlichkeiten / Prozentwerte

## Beispiel: Münzwurf (Kopf or Zahl)

Variante 1 – mit randint:

    import random

    if random.randint(0, 1) == 0:
        print("Kopf")
    else:
        print("Zahl")

Variante 2 – mit random():

    import random

    if random.random() < 0.5:
        print("Kopf")
    else:
        print("Zahl")
---

## 🧩Zufällige Auswahl aus einer Liste (random.choice vs random.randint)

Dafür gibt es in Python zwei gängige Möglichkeiten:
- `random.choice()`
- `random.randint()` in Kombination mit einem Index

Beide Methoden sind korrekt und liefern zufällige Ergebnisse.

---

## Beispiel-Liste

    friend = ["Almond", "Joghurt", "Taohoo", "Kieke"]

---

## Variante 1 – random.choice()

    import random
    print(random.choice(friend))

### Erklärung
- `random.choice()` wählt **direkt ein zufälliges Element** aus der Liste aus
- Kein Index notwendig
- Sehr kurze und gut lesbare Lösung

### Eigenschaften
- Einfach
- Übersichtlich
- Empfohlen, wenn man die Funktion kennt

---

## Variante 2 – random.randint() + Index

    import random

    random_index = random.randint(0, len(friend) - 1)
    print(friend[random_index])

### Erklärung
- `random.randint()` erzeugt eine zufällige Zahl
- Diese Zahl wird als **Index** für die Liste verwendet
- Listen beginnen in Python immer bei Index 0

### Eigenschaften
- Etwas mehr Code
- Logisch nachvollziehbar
- Ebenfalls vollkommen korrekt

---

## Wichtiger Hinweis zu eckigen Klammern [ ]
Beim Zugriff auf ein Element in einer Liste sind eckige Klammern notwendig:

    friend[random_index]

- `[ ]` werden benutzt, um ein Element aus einer Liste zu holen
- `( )` werden benutzt, um eine Funktion auszuführen

---

## Vergleich der beiden Methoden

| Methode | Vorteil | Nachteil |
|-------|--------|---------|
| random.choice() | Kurz und klar | Funktion muss bekannt sein |
| random.randint() | Logik gut sichtbar | Mehr Code notwendig |

---

## Fazit
Beide Methoden liefern das gleiche Ergebnis.
In der Praxis wird häufig `random.choice()` verwendet, da der Code kürzer und besser lesbar ist.
Wichtig ist nicht, alles auswendig zu lernen, sondern zu verstehen, **wie Listen und Zufall zusammenarbeiten**.

---
## 📋 Python Lists 

In diesem Abschnitt geht es um die **Python List**, eine wichtige **Datenstruktur**.
Listen werden verwendet, um **mehrere zusammengehörige Daten** in einer einzigen Variable zu speichern.
Dabei behalten Listen immer eine **feste Reihenfolge**.

--

## Was ist eine List?
Eine List ist eine Sammlung von Werten, die:
- in **eckigen Klammern [ ]** steht
- mehrere Elemente enthalten kann
- durch **Kommas** getrennt ist
- eine feste Reihenfolge besitzt
--
## Beispiel: Städte in Nordrhein-Westfalen (NRW)

Anstatt viele einzelne Variablen zu verwenden, können Städte in NRW in einer Liste gespeichert werden:

    cities_nrw = ["Köln", "Düsseldorf", "Dortmund", "Essen", "Bochum"]

Alle Städte gehören zusammen und werden deshalb in einer List gespeichert.

## Reihenfolge in Listen
Die Reihenfolge der Elemente in einer List ist wichtig.
Jedes Element hat einen sogenannten **Index**.

- Das erste Element hat den Index 0
- Das zweite Element hat den Index 1
- Das dritte Element hat den Index 2

Beispiel:
    cities_nrw[0]  → Köln
    cities_nrw[1]  → Düsseldorf

Programmiersprachen beginnen fast immer mit dem Zählen bei 0.

## Negative Indizes
Man kann auch vom Ende der Liste zählen:

    cities_nrw[-1] → Bochum
    cities_nrw[-2] → Essen

- -1 ist das letzte Element
- -2 ist das vorletzte Element

## Elemente in einer List ändern
Ein einzelnes Element kann direkt geändert werden:

    cities_nrw[1] = "Bonn"

Jetzt ist „Düsseldorf“ durch „Bonn“ ersetzt.

--
## Elemente zu einer List hinzufügen

### append()
Fügt **ein Element am Ende** der Liste hinzu:

    cities_nrw.append("Münster")

---

### extend()
Fügt **mehrere Elemente** aus einer anderen Liste hinzu:

    cities_nrw.extend(["Aachen", "Bielefeld"])

---

## 💡Merkhilfe
- Lists speichern **mehrere zusammengehörige Werte**
- Lists haben immer eine **Reihenfolge**
- Der erste Index ist **0**
- Mit append() wird **ein Element** hinzugefügt
- Mit extend() werden **mehrere Elemente** hinzugefügt

---




