# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

intro_message = "Welcome to the tip calculator!\n"
print(intro_message)

bill_question = "What was the total bill? $"
bill_amount = float(input(bill_question))

tip_question = "What percentage tip would you like to give? 10, 12 or 15? "
tip_percentage = float(input(tip_question))

number_of_people_question = "How many people to split the bill? "
number_of_people = int(input(number_of_people_question))

bill_plus_tip = bill_amount * (1 + tip_percentage/100)
bill_per_person = bill_plus_tip / number_of_people

# bill_per_person_rounded = round(bill_per_person, 2)
bill_per_person_rounded = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${bill_per_person_rounded}")


my_readable_int = 123_456_789
