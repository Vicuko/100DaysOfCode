FILE_LOCATION = "my_file.txt"
# To read a file we can use the built in open function:
with open(FILE_LOCATION, mode="r") as file:
    contents = file.read()
    lines = contents.split("\n")
    counter = 1
    for line in lines:
        print(f"Line{counter}:{line}")
        counter += 1

# To write into a file: (remember, it deletes everything in the file)
with open(FILE_LOCATION, mode="w") as file:
    file.write("New Text!!!")

# To append into a file: (remember, it doesnt' include line breaks)
with open(FILE_LOCATION, mode="a") as file:
    file.write("\nNew Text 2!!")