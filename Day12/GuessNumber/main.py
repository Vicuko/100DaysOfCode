# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random


def calculate_attempts(level):
    if level == "easy":
        attempts = 10
    elif level == "hard":
        attempts = 5
    return attempts


def choose_number():
    number = random.randint(1, 100)
    return number


def get_high_low(guess, number):
    if guess > number:
        return "high"
    else:
        return "low"


def print_result(attempts, number):
    if attempts > 0:
        print(f"Woohoo! You got it, it was {number}")
    else:
        print("That was close! Keep trying!")


def play_game():
    print(logo)
    print("Welcome to NumGuess!!")
    print("I'm thinking of a number between 1 and 100")
    number = choose_number()
    level = input(
        "What level do you want to play? Easy (10 attempts) or Hard (5 attempts)? ").lower()
    attempts = calculate_attempts(level)

    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            break
        else:
            print(f"Too {get_high_low(guess, number)}")
            attempts -= 1

    print_result(attempts, number)


play_game()
