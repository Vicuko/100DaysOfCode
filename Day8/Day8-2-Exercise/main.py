# Write your code below this line 👇
def prime_checker(number):
    result = "It's a prime number."
    for divisor in range(2, number//2 + 1):
        if number % divisor == 0:
            result = "It's not a prime number."
            break

    print(result)


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
