# 📘 Day 4 – Randomization in Python

## 🎲 Random Module
In diesem Kapitel geht es um Zufälligkeit (Randomization) in Python.
Da Computer deterministisch arbeiten, nutzt Python sogenannte Pseudo-Zufallszahlen,
die mithilfe mathematischer Algorithmen erzeugt werden.

## Random-Modul importieren
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

## Beispiel: Münzwurf (Heads or Tails)

Variante 1 – mit randint:

    import random

    if random.randint(0, 1) == 0:
        print("Heads")
    else:
        print("Tails")

Variante 2 – mit random():

    import random

    if random.random() < 0.5:
        print("Heads")
    else:
        print("Tails")

