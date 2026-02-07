import random
from art import logo


def deal_card():
    """Gibt eine zufällige Karte aus dem Kartendeck zurück"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Nimmt eine Kartenliste und berechnet die Punktzahl"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Vergleicht die Punktzahl des Spielers mit der des Computers"""
    if u_score == c_score:
        return "Unentschieden 🙃"
    elif c_score == 0:
        return "Verloren, der Gegner hat Blackjack 😱"
    elif u_score == 0:
        return "Gewonnen mit einem Blackjack 😎"
    elif u_score > 21:
        return "Du hast überzogen. Du verlierst 😭"
    elif c_score > 21:
        return "Der Gegner hat überzogen. Du gewinnst 😁"
    elif u_score > c_score:
        return "Du gewinnst 😃"
    else:
        return "Du verlierst 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Deine Karten: {user_cards}, aktueller Punktestand: {user_score}")
        print(f"Erste Karte des Computers: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Tippe 'y', um eine weitere Karte zu ziehen, oder 'n', um zu passen: "
            )
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Deine endgültige Hand: {user_cards}, Endpunktzahl: {user_score}")
    print(
        f"Endgültige Hand des Computers: {computer_cards}, Endpunktzahl: {computer_score}"
    )
    print(compare(user_score, computer_score))


while input("Möchtest du eine Runde Blackjack spielen? Tippe 'y' oder 'n': ") == "y":
    print("\n" * 20)
    play_game()
