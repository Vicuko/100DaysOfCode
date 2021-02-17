############DEBUGGING#####################

# # Describe Problem
def my_function():
  #The issue here was that the last number in the range
  #isn't included in the loop, therefore we need to increase
  #it by 1 so that the loop may reach the value of 20
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
#The issue is that randint does include the last number
#therefore the bug was getting an out of range index(6)
#for a list that goes from 0 to 5
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# # Play Computer
#The issue in question is whether someone born in 1994
#is a millenial or a gen z. Depending on the answer
#the code should be modified to include the year in such
#generation. In this case, I'll include it in gen z:
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# # Fix the Errors
#There are 3 issues:
# 1. Indent block for print line.
# 2. Convert to fstring in print to include variable.
# 3. Convert input to int in order to compare it with a number.
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")

#Print is Your Friend
#Used print to validate if the variables where changing.
# The issue was in the word_per_page line. It was evaluating
# the value to the input instead of assigning it.
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print (pages)
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
# After debugging in pythontutor, we can see that 
# the append line needed to be indented.
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])