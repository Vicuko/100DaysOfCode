numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

name = "Angela"
letters_list = [letter for letter in name]
doubled_range = [n*2 for n in range(1,5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
caps_names = [name.upper() for name in names if len(name) < 5]
