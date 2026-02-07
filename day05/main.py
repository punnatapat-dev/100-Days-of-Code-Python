import random


adjectives = [
    "freundlich", "ruhig", "schnell", "mutig", "klar",
    "modern", "digital", "stark", "kreativ", "smart"
]

nouns = [
    "User", "Student", "Coder", "Entwickler", "Engineer",
    "Denker", "Lerner", "Adler", "Wolf", "Tiger"
]

symbols = ["_", "."]                 
numbers = list("0123456789")

print("Willkommen zum Benutzername-Generator!\n")


nr_adjectives = int(input("Wie viele Adjektive möchtest du im Benutzernamen?\n"))
nr_nouns = int(input("Wie viele Nomen möchtest du?\n"))
nr_symbols = int(input("Wie viele Symbole (_ oder .) möchtest du?\n"))
nr_numbers = int(input("Wie viele Zahlen möchtest du?\n"))


username_list = []

for _ in range(nr_adjectives):
    username_list.append(random.choice(adjectives))

for _ in range(nr_nouns):
    username_list.append(random.choice(nouns))

for _ in range(nr_symbols):
    username_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    username_list.append(random.choice(numbers))

# Optional: show before/after shuffle (for learning)
print("\nVor dem Mischen:", username_list)
random.shuffle(username_list)
print("Nach dem Mischen:", username_list)

username = ""
for part in username_list:
    username += part

print(f"\n✅ Dein Benutzername ist: {username}")
