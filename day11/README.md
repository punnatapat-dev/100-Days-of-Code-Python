## 📘 Day 11 ♠️ Blackjack (21) 

Blackjack ist das **erste Capstone Project** des Python-Kurses.  
Ziel ist es, **alle bisher gelernten Inhalte** zu kombinieren  
und ein spielbares Blackjack-Spiel über die **Konsole** zu erstellen.

---

## 🎯 Ziel des Spiels
- Der Spieler soll eine Punktzahl **möglichst nahe an 21** erreichen
- **Nicht über 21 gehen**
- Bei mehr als 21 → **Bust** → sofort verloren

---

## 🃏 Kartenwerte
- Karten **2–10** → Wert entsprechend der Zahl
- **Bube / Dame / König** → jeweils **10 Punkte**
- **Ass (Ace)** → **11 oder 1**
  - Startwert: 11
  - Wird automatisch zu 1, wenn die Punktzahl über 21 liegt

---

## 👤 Spieler & Dealer
- Spieler und Dealer erhalten zu Beginn **je 2 Karten**
- Die zweite Karte des Dealers ist **verdeckt**
- Spieler kann wählen:
  - **Hit** → weitere Karte ziehen
  - **Stand** → stehen bleiben
- Dealer:
  - Muss Karten ziehen, wenn die Punktzahl **unter 17** liegt
- Gleiche Punktzahl → **Unentschieden (Draw)**

---

## ⚙️ House Rules (Vereinfachte Version)
- Kartenliste:
  `[2,3,4,5,6,7,8,9,10,10,10,10,11]`
- Ass startet mit dem Wert **11**
- **Unendliches Deck** (Karten werden nach dem Ziehen nicht entfernt)
- Jede Karte hat die gleiche Wahrscheinlichkeit
- Keine echte Casino-Probability-Berechnung

---

## 🧮 Punkteberechnung (`calculate_score`)
Aufgabe:
- Nimmt eine Kartenliste entgegen
- Gibt die berechnete Punktzahl zurück

Wichtige Logik:
- Verwendung von `sum(cards)`
- **Blackjack-Erkennung**:
  - Genau 2 Karten und Summe = 21
  - Rückgabewert `0` als Symbol für Blackjack

Ass-Logik:
- Wenn `11` in der Kartenliste ist und `sum > 21`:
  - `remove(11)`
  - `append(1)`

---

## 🛑 Spielende (Game Over)
Das Spiel endet sofort, wenn:
- Spieler Blackjack hat (`score == 0`)
- Dealer Blackjack hat
- Spieler **Bust** ist (`score > 21`)

Kontrollvariable:
- `is_game_over = False`
- Wird auf `True` gesetzt, wenn eine Bedingung erfüllt ist

---

## 🔁 Spiel-Schleife (Game Loop)
- Das Spiel läuft in einer `while not is_game_over` Schleife
- Nach jedem Kartenziehen:
  - Punktzahl neu berechnen
  - Blackjack / Bust prüfen
  - Spieler nach Hit oder Stand fragen

---

## 🤖 Dealer-Logik
- Dealer spielt **erst nachdem der Spieler Stand gewählt hat**
- `while`-Schleife:
  - `computer_score < 17`
  - `computer_score != 0`
- Dealer zieht Karten, bis die Bedingungen nicht mehr erfüllt sind

---

## ⚖️ Ergebnisvergleich (`compare`)
Funktion `compare(u_score, c_score)`:
- Gibt das Spielergebnis als Text zurück

Reihenfolge der Bedingungen ist **sehr wichtig**:
1. Gleiche Punktzahl → Draw
2. Dealer Blackjack → Spieler verliert
3. Spieler Blackjack → Spieler gewinnt
4. Spieler Bust → Spieler verliert
5. Dealer Bust → Spieler gewinnt
6. Höhere Punktzahl → Spieler gewinnt
7. Sonst → Spieler verliert

⚠️ Parameter `u_score` und `c_score` verwenden  
→ verhindert **Variable Shadowing**

---

## 🖨️ Ausgabe der Ergebnisse
Nach Spielende anzeigen:
- Alle Karten des Spielers + Punktzahl
- Alle Karten des Dealers + Punktzahl
- Ergebnistext aus `compare()`

---

## 🔁 Spiel neu starten
- Gesamte Spiellogik in `play_game()` kapseln
- Benutzer fragen:
  - `'y'` → neues Spiel starten
  - `'n'` → Programm beenden
- Bildschirm leeren mit `"\n" * 20`
- Logo bei jedem Neustart anzeigen

---

## 💡 Gelernte Konzepte
- Funktionen & Rückgabewerte
- Listen und Datenmanipulation
- While-Schleifen & Boolean-Flags
- Komplexe Bedingungslogik
- Strukturiertes Problem-Solving
- Saubere Programmstruktur

---

## 🏁 Fazit
Blackjack ist ein anspruchsvolles, aber extrem wichtiges Projekt.  
Es zeigt klar, wie **alle Python-Grundlagen zusammenspielen**  
und bildet eine starke Basis für weitere, komplexere Projekte.

Wenn nicht alles sofort klar ist – **kein Problem**.  
Wiederholen = echtes Lernen ♠️
