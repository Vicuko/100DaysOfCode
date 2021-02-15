print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("It's New Year and you just wake up in the middle of moving train.")
print("You look to both sides and see that the train is completely wrecked.")
print(
    "On your right, you can see water way below, on your left, there is a balloon flying next to the train."
)
choice_1 = input(
    "Which way do you go? Left or Right? (Type L or R as your response) ")

if choice_1 == "L":
    print(
        "You take the jump into the balloon and manage to let it loose and begin your journey into the air."
    )
    print(
        "In middair, you see there is a electricity cable hanging that could hit against the balloon."
    )
    print("You can hit the gas or just wait and hope for the best.")
    choice_2 = input("What do you choose? G for gas or W for waiting? ")

    if choice_2 == "W":
        print(
            "You cross your fingers and wait for the best. Luckily for you, a breeze of wind pushes the balloon away from the wires.\Moments later, you manage to land the balloon in a safe place"
        )
        print(
            "Out of nowhere, a man comes to you and asks you to choose between the 4 animals accompanying him. One will lead to a treasure, he sates. The remaining to a shameful death."
        )
        print(
            "There is no turning back. The animals are a chicken, a dog, a cow and horse"
        )
        choice_3 = input(
            "Which one do you choose? Chicken (C), Dog (D), Cow (W) or Horse (H)? "
        )

        if choice_3 == "C":
            print(
                "The chicken come running and jumps on to your face and bites your eyes off... Game Over."
            )
        elif choice_3 == "D":
            print(
                "The dog barks twice, suddenly the earth trembles, and a shiny treasure appears right in front of you. Congratulations! You've won!"
            )
        elif choice_3 == "W":
            print(
                "The cow makes some noises and out of nowhere, a bull comes out and strongly gores you against a tree... Game Over."
            )
        else:
            print(
                "The horse slowly turns around and suddenly kicks you twice. You fly over the air and end up hitting your head against a rock... Game Over."
            )
    else:
        print(
            "You hit the gas, but there was another wire hanging right above you couldn't see. The balloon touches the wire and sets on fire, falling rapidly to the ground... Game Over."
        )

else:
    print(
        "You take the jump but in middair you realize it's too shallow and you crush against the ground... Game Over."
    )
