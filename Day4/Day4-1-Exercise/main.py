# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

print("Let's toss a coin!")

random_result = random.randint(0, 1)
possible_results = ["Head", "Tails"]
print(f"It landed on {possible_results[random_result]}")
