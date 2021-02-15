# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
divisible_by_4 = (year % 4 == 0)
divisible_by_100 = (year % 100 == 0)
divisible_by_400 = (year % 400 == 0)

message = "Not leap year."
if (divisible_by_4 and not divisible_by_100) or (divisible_by_400):
    message = "Leap year."

print(message)
