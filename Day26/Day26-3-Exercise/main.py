
file1_content = list()
file2_content = list()
# Open uses read mode by default:
with open("file1.txt") as file1:
    file1_content = file1.readlines();

with open("file2.txt") as file2:
    file2_content = file2.readlines();

result = [int(number) for number in file1_content if number in file2_content]
# Write your code above 👆

print(result)


