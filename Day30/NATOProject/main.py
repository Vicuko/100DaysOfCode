import pandas as pd
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for index,row in data.iterrows()}
print(data_dict)

word = input("Please introduce the word for the NATO phonetic code:").upper()
result = [data_dict[letter] for letter in word]
print (result)
