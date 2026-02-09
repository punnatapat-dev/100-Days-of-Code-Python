from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Funktion zum Überprüfen der Vermutung des Benutzers
def check_answer(user_guess, actual_answer, turns):
    """Überprüft die Vermutung und gibt die verbleibenden Versuche zurück."""
    if user_guess > actual_answer:
        print("Zu hoch.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Zu niedrig.")
        return turns - 1
    else:
        print(f"Richtig! Die gesuchte Zahl war {actual_answer}.")


# Funktion zum Festlegen des Schwierigkeitsgrades
def set_difficulty():
    level = input("Wähle einen Schwierigkeitsgrad. Tippe 'easy' oder 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Zufällige Zahl zwischen 1 und 100 wählen
    print("Willkommen beim Zahlenratespiel!")
    print("Ich denke an eine Zahl zwischen 1 und 100.")
    answer = randint(1, 100)
    print(f"Pssst, die richtige Antwort ist {answer}")

    turns = set_difficulty()

    # Wiederhole das Raten, solange die Antwort falsch ist
    guess = 0
    while guess != answer:
        print(f"Du hast noch {turns} Versuche, um die Zahl zu erraten.")
        # Benutzer gibt eine Vermutung ab
        guess = int(input("Gib deine Vermutung ein: "))
        # Versuche reduzieren, wenn die Vermutung falsch ist
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("Du hast keine Versuche mehr. Du hast verloren.")
            return
        elif guess != answer:
            print("Versuche es noch einmal.")


game()
