#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
NAMES_DIR = "./Input/Names/invited_names.txt"
LETTER_DIR = "./Input/Letters/starting_letter.txt"

with open(NAMES_DIR, mode="r") as file:
    names = file.readlines()

with open(LETTER_DIR, mode="r") as file:
    letter = file.read()

for name in names:
    stripped_name = name.strip()
    new_file_dir = f"./Output/ReadyToSend/letter_for_{stripped_name}.txt"
    letter_text = letter.replace("[name]", f"{stripped_name}")
    with open(new_file_dir, mode="w") as file:
        file.write(letter_text)
