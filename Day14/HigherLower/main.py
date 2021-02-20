from random import randint
from art import logo, vs
from game_data import data
from replit import clear

# TODO - Create a counter to count the number of correct attempts
DATA_LENGTH = len(data)

# TODO - Create a function to print the introduction content


def print_header():
    print(logo)


def print_vs():
    print(vs)

# TODO - Create a function to retrieve the next comparison


def get_next_comparison():
    a = data[randint(0, DATA_LENGTH)]
    b = data[randint(0, DATA_LENGTH)]

    same = True
    while same:
        if a["follower_count"] != b["follower_count"]:
            same = False
        else:
            b = data[randint(0, DATA_LENGTH)]
    extracted_data = [a, b]
    return extracted_data

# TODO - Create a function to print the comparison to be guessed by the user


def print_comparison(compared_accounts):
    a = compared_accounts[0]
    b = compared_accounts[1]
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print_vs()
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
    # print (f"Pssst... it's {a['name'] if a['follower_count'] > b['follower_count'] else b['name']}")


# TODO - Create a function to validate the result
def validate(guess, compared_accounts):
    correct_answer = False
    guess = guess.lower()
    result = "a" if compared_accounts[0]["follower_count"] > compared_accounts[1]["follower_count"] else "b"

    if guess == result:
        correct_answer = True

    return correct_answer


# TODO - Create a function to print message depending on guess
def print_result(right_guesses, game_over):
    clear()
    print_header()
    if not game_over:
        print(f"That's right! Current score: {right_guesses}")
    else:
        print(
            f"Sorry, that wasn't the right option... Final score: {right_guesses}")


# TODO - Create a function to handle the game process: while loop for continuous playing.
def game():
    game_over = False
    right_guesses = 0
    print_header()

    while not game_over:
        compared_accounts = get_next_comparison()
        print_comparison(compared_accounts)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = validate(guess, compared_accounts)
        if correct_answer:
            right_guesses += 1
        else:
            game_over = True
        print_result(right_guesses, game_over)


game()
