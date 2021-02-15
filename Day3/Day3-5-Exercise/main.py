# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names = name1 + " " + name2
names = names.lower()

counter = 0
for letter in "true":
    counter += names.count(letter)
tens = counter * 10

counter = 0
for letter in "love":
    counter += names.count(letter)

units = counter

total = round(tens + units)

if total < 10 or total > 90:
    message = ", you go together like coke and mentos."
elif 40 < total < 50:
    message = ", you are alright together."
else:
    message = "."

print(f"Your score is {total}{message}")
