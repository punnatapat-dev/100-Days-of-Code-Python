import art

print(art.logo)

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Hier ist das {encode_or_decode}d Ergebnis: {output_text}")


should_continue = True

while should_continue:

    direction = input(
        "Gib 'encode' ein, um zu verschlüsseln, oder 'decode', um zu entschlüsseln:\n"
    ).lower()

    text = input("Gib deine Nachricht ein:\n").lower()
    shift = int(input("Gib die Verschiebungszahl ein:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input(
        "Gib 'ja' ein, wenn du erneut starten möchtest. Andernfalls gib 'nein' ein.\n"
    ).lower()

    if restart == "nein":
        should_continue = False
        print("Auf Wiedersehen")
