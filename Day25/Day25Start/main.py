DATA_FILE = "./weather_data.csv"

# Opening file normally:
# with open(DATA_FILE, mode="r") as data_file:
#     weather_list = data_file.readlines()
# We have an issue here: we need to parse and separate all of the content in order to
# retrieve all of the information, which can get complicated.
# This is why, we'll use the csv module:

# import csv
#
# with open(DATA_FILE) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv(DATA_FILE)
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print (data_dict)

data_list = data["temp"].to_list()
print (data_list)

# temperature_average = sum(data_list) / len(data_list)
# print (round(temperature_average, 2))
# Another way:
temp_average = data["temp"].mean()
print (round(temp_average,2))

temp_max = data["temp"].max()
print (temp_max)

# We can also retrieve info from the columns like this, treating it like an object:
temp_col = data.temp
print (temp_col)

# Retrieve a row filtering by a column value:
print (data[data.day == "Monday"])

# Another example, row with highest temperature of the week:
print (data[data.temp == data.temp.max()])