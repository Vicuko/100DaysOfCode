import functools
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
if len(two_digit_number) == 2:
    digit_one = int(two_digit_number[0])
    digit_two = int(two_digit_number[1])
    print(digit_one + digit_two)

print(functools.reduce(lambda a, b: int(a)+int(b), two_digit_number))
