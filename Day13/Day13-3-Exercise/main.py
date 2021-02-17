# The first if required an "and" instead of an "or"
# The remaining ifs needed to become an "elif" so they wouldn't run if
# any of the previous if's had run before

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])