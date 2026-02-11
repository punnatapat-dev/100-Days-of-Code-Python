from art import logo, vs
from game_data import data
import random


def formatiere_daten(konto):
    """Nimmt die Kontodaten und gibt ein druckbares Format zurück."""
    konto_name = konto["name"]
    konto_beschreibung = konto["description"]
    konto_land = konto["country"]
    return f"{konto_name}, {konto_beschreibung}, aus {konto_land}"


def pruefe_antwort(tipp, a_follower, b_follower):
    """Nimmt den Tipp des Users und die Follower-Zahlen und gibt True/False zurück."""
    if a_follower > b_follower:
        return tipp == "a"
    else:
        return tipp == "b"


print(logo)

punktzahl = 0
spiel_laueft = True

# Zufälliges Konto aus den Spieldaten generieren
konto_b = random.choice(data)

# Spiel wiederholbar machen
while spiel_laueft:

    # B wird zum nächsten A
    konto_a = konto_b
    konto_b = random.choice(data)

    # Sicherstellen, dass A und B nicht gleich sind
    while konto_a == konto_b:
        konto_b = random.choice(data)

    print(f"Vergleiche A: {formatiere_daten(konto_a)}.")
    print(vs)
    print(f"Gegen B: {formatiere_daten(konto_b)}.")

    # User nach einem Tipp fragen
    tipp = input("Wer hat mehr Follower? Tippe 'A' oder 'B': ").lower()

    # Bildschirm leeren
    print("\n" * 20)
    print(logo)

    # Follower-Zahlen holen
    a_follower_count = konto_a["follower_count"]
    b_follower_count = konto_b["follower_count"]

    # Prüfen, ob der Tipp richtig ist
    ist_richtig = pruefe_antwort(tipp, a_follower_count, b_follower_count)

    # Feedback + Punktestand
    if ist_richtig:
        punktzahl += 1
        print(f"Richtig! Aktueller Punktestand: {punktzahl}.")
    else:
        print(f"Leider falsch. Endpunktestand: {punktzahl}.")
        spiel_laueft = False
