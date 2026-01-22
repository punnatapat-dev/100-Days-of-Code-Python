print(r'''
************************************ 
       ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/
      

*******************************************
  
''')



print("Willkommen zu einem faulen Sonntagmorgen.☕😴")
print("Deine Mission ist es, den Morgen stressfrei zu überleben.")

choice1 = input(
    "Du wachst auf und hörst deinen Wecker. "
    'Willst du "schlummern" oder "aufstehen"?\n'
).lower()

if choice1 == "aufstehen":
    choice2 = input(
        "Du bist in der Küche. "
        'Willst du "kaffee machen" oder "wieder ins bett gehen"?\n'
    ).lower()

    if choice2 == "kaffee machen":
        choice3 = input(
            "Die Kaffeemaschine ist bereit. "
            "Wähle dein Getränk: latte, espresso oder tee.\n"
        ).lower()

        if choice3 == "latte":
            print("Zu viel Milch. Zu wenig Kaffee. Spiel vorbei 😅")
        elif choice3 == "espresso":
            print("Perfekte Wahl! Du bist wach und glücklich. Du hast gewonnen ☕🎉")
        elif choice3 == "tee":
            print("Ganz nett, aber du schläfst wieder ein. Spiel vorbei 😴")
        else:
            print("Dieses Getränk gibt es nicht. Spiel vorbei.")
    else:
        print("Du hast zu lange geschlafen und den Tag verpasst. Spiel vorbei 😴")

else:
    print("Du hast verschlafen und das Frühstück verpasst. Spiel vorbei.")
