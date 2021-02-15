# 1. Create a greeting for your program.
greeting = "Hi there! Welcome to the Super Band Generator!!"
print(greeting)
# 2. Ask the user for the city that they grew up in.
city_question = "Tell me, in what city did you grow up?\n"
city = input(city_question)
# 3. Ask the user for the name of a pet.
pet_name_question = "Sweet, now tell me a name of a pet you've had.\n(If you didn't you can just tell me your favorite pet name)\n"
pet_name = input(pet_name_question)
# 4. Combine the name of their city and pet and show them their band name.
band_name_proposal = "Nice! Here is your band name proposal: "
name_combination = city + " " + pet_name
print(band_name_proposal + name_combination)
# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
