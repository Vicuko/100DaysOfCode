############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
from replit import clear
import time
import random

all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
p_cards = []
h_cards = []


def intro():
    print(logo)
    print("Welcome to the python blackjack!")
    time.sleep(2)
    print("We'll start by dealing some cards")
    time.sleep(2)


def init_game():
    global p_cards, h_cards
    p_cards = random.choices(all_cards, k=2)
    h_cards = random.choices(all_cards, k=2)


def get_card():
    card = random.choice(all_cards)
    return card


def calculate_scores(final=False):
    if 11 in p_cards and sum(p_cards) > 21:
        p_cards[p_cards.index(11)] = 1

    if 11 in h_cards and sum(h_cards) > 21:
        h_cards[h_cards.index(11)] = 1

    if final:
        print(f"\nHouse cards: {h_cards}")
        print(f"House score: {sum(h_cards)}")
    else:
        print(f"\nHouse cards: {['X'] + h_cards[1:]}")
        print(f"House score: {sum(h_cards[1:])}")

    print(f"\nPlayer cards: {p_cards}")
    print(f"Player score: {sum(p_cards)}")


def cards_ok():
    ok = False
    if sum(p_cards) <= 21:
        ok = True
    return ok


def deal():
    game_end = False
    stop_dealing = False

    while not stop_dealing:
        deal_more = input("\nWould you like another card? (y/n) ").lower()
        if deal_more == "y":
            card = get_card()
            print("-----------------------")
            time.sleep(2)
            print(f"\nYou got {card}")
            p_cards.append(card)
            calculate_scores()

            if not cards_ok():
                print("\nOops! You're busted!")
                stop_dealing = True
                game_end = True

            elif sum(p_cards) == 21:
                stop_dealing = True

        else:
            stop_dealing = True

    return game_end


def house_deal():
    while sum(h_cards) < 17:
        card = get_card()
        print("-----------------------")
        time.sleep(2)
        print(f"\nThe house got {card}")
        h_cards.append(card)
        calculate_scores(final=True)


def print_game_result():
    if sum(p_cards) > sum(h_cards) or sum(h_cards) > 21:
        print("\nYou won!")
    elif sum(p_cards) == sum(h_cards):
        print("\nIt's a draw!")
    else:
        print("\nYou lost!")


def play_game():
    global p_cards, h_cards
    intro()

    stop_game = False
    while not stop_game:
        game_over = False
        init_game()
        calculate_scores()

        time.sleep(2)
        if sum(p_cards) < 21:
            game_over = deal()

        if not game_over:
            time.sleep(2)
            calculate_scores(final=True)
            if sum(h_cards) < 17:
                house_deal()
            time.sleep(2)
            print_game_result()
        else:
            time.sleep(2)
            print("You lost!")

        keep_playing = input("\nWould you like to play again?(y/n) ")
        if keep_playing == "n":
            stop_game = True
        else:
            clear()
            print("New game:")


play_game()
