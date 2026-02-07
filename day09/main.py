from art import logo

print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Der Gewinner ist {winner} mit einem Gebot von {highest_bid} €")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("Wie heißt du?: ")
    price = int(input("Wie hoch ist dein Gebot?: €"))
    bids[name] = price

    should_continue = input("Gibt es weitere Bieter? Tippe 'ja' oder 'nein'.\n").lower()

    if should_continue == "nein":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "ja":
        print("\n" * 20)
