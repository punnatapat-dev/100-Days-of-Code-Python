import random

# ===== ASCII ART =====
thai_art = r"""
  _______ _           _
 |__   __| |         (_)
    | |  | |__   __ _ _ 
    | |  | '_ \ / _` | |
    | |  | | | | (_| | |
    |_|  |_| |_|\__,_|_|
        THAI FOOD
"""

german_art = r"""
   ____                             
  / ___| ___ _ __ _ __ ___   __ _ _ __
 | |  _ / _ \ '__| '_ ` _ \ / _` | '_ \
 | |_| |  __/ |  | | | | | | (_| | | | |
  \____|\___|_|  |_| |_| |_|\__,_|_| |_|
        DEUTSCHES ESSEN
"""

japan_art = r"""
      _                                 
     | | __ _ _ __   __ _ _ __          
  _  | |/ _` | '_ \ / _` | '_ \         
 | |_| | (_| | |_) | (_| | | | |        
  \___/ \__,_| .__/ \__,_|_| |_|        
             |_|                        
          JAPAN FOOD
"""

# ===== Food Lists =====
thai_foods = ["Pad Thai", "Som Tam", "Green Curry", "Tom Yum", "Khao Man Gai"]
german_foods = ["Bratwurst", "Schnitzel", "Currywurst", "Döner", "Kartoffelsalat"]
japanese_foods = ["Ramen", "Sushi", "Udon", "Katsu Curry", "Onigiri"]

# ===== User Input =====
category = int(input(
    "Wähle eine Essenskategorie:\n"
    "1 = Thai\n"
    "2 = Deutsch\n"
    "3 = Japanisch\n"
))

# ===== Logic =====
if category < 1 or category > 3:
    print("Ungültige Auswahl.")

elif category == 1:
    print(thai_art)
    print("Essensvorschlag:", random.choice(thai_foods))

elif category == 2:
    print(german_art)
    print("Essensvorschlag:", random.choice(german_foods))

else:
    print(japan_art)
    print("Essensvorschlag:", random.choice(japanese_foods))
