# To play, just hit the run button at the top!

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

decission = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if 0 <= decission < 3:
    print(f"You chose: {options[decission]}")

    computer_decission = random.randint(0, len(options) - 1)
    print(f"Computer chose:\n{options[computer_decission]}")

    if computer_decission > decission or computer_decission - decission == -2:
        print("You lose")

    elif computer_decission == decission:
        print("It's a tie")

    else:
        print("You win")

else:
    print("Sorry, that number was not an option")
