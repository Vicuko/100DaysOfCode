import pandas as pd
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for index,row in nato_data.iterrows()}
print(data_dict)

def generate_phonetics():
    word = input("Please introduce the word for the NATO phonetic code:").upper()
    try:
        result = [data_dict[letter] for letter in word]

    except KeyError as error_message:
        print(f"{error_message} is not a letter in the alphabet. Please, introduce only letters")
        generate_phonetics()

    else:
        print(result)

generate_phonetics()
