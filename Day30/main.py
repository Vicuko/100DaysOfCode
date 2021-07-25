#FileNotFound error

try:
    file = open("mysuperfile.txt")
    a_dictionary = {"my_key": "Value"}
    print (a_dictionary["my_key"])

except FileNotFoundError:
    file = open("mysuperfile.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed.")