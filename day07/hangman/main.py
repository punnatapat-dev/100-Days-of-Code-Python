import random

from hangman_words import word_list
from hangman_art import stages, logo

# Anzahl der Leben
lives = 6

# Spiel-Logo anzeigen
print(logo)

# Zufälliges Wort auswählen
chosen_word = random.choice(word_list)

# Platzhalter mit Unterstrichen erstellen
word_length = len(chosen_word)
display = "_" * word_length
print("Zu erratendes Wort: " + display)

# Spielstatus
game_over = False
correct_letters = []

# Haupt-Spielschleife
while not game_over:

    print(
        f"\n**************************** {lives}/6 LEBEN ÜBRIG ****************************"
    )
    guess = input("Rate einen Buchstaben: ").lower()

    # Prüfen, ob der Buchstabe schon geraten wurde
    if guess in correct_letters:
        print(f"Du hast den Buchstaben '{guess}' bereits geraten.")
        print(stages[lives])
        continue

    new_display = ""

    # Wort aktualisieren
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    # Richtigen Buchstaben speichern
    if guess in chosen_word:
        correct_letters.append(guess)
    else:
        lives -= 1
        print(f"Der Buchstabe '{guess}' ist nicht im Wort. Du verlierst ein Leben.")

    display = new_display
    print("Zu erratendes Wort: " + display)

    # Verloren
    if lives == 0:
        game_over = True
        print(stages[lives])
        print(f"\n*********************** DU HAST VERLOREN ***********************")
        print(f"Das richtige Wort war: {chosen_word}")

    # Gewonnen
    if "_" not in display:
        game_over = True
        print(
            "\n**************************** DU HAST GEWONNEN ****************************"
        )

    # Hangman-Zeichnung anzeigen
    if not game_over:
        print(stages[lives])
