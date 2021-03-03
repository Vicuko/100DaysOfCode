# DATA_FILE = "./weather_data.csv"
#
# # Opening file normally:
# # with open(DATA_FILE, mode="r") as data_file:
# #     weather_list = data_file.readlines()
# # We have an issue here: we need to parse and separate all of the content in order to
# # retrieve all of the information, which can get complicated.
# # This is why, we'll use the csv module:
#
# # import csv
# #
# # with open(DATA_FILE) as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv(DATA_FILE)
# # print(type(data))
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print (data_dict)
#
# data_list = data["temp"].to_list()
# print (data_list)
#
# # temperature_average = sum(data_list) / len(data_list)
# # print (round(temperature_average, 2))
# # Another way:
# temp_average = data["temp"].mean()
# print (round(temp_average,2))
#
# temp_max = data["temp"].max()
# print (temp_max)
#
# # We can also retrieve info from the columns like this, treating it like an object:
# temp_col = data.temp
# print (temp_col)
#
# # Retrieve a row filtering by a column value:
# print (data[data.day == "Monday"])
#
# # Another example, row with highest temperature of the week:
# print (data[data.temp == data.temp.max()])
#
# # Show Mondays temperature into fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_fahrenheit = monday_temp * 9 / 5 + 32
# print (monday_temp_fahrenheit)
#
# # Now let's create a dataframe from the python dictionary:
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 64]
# }
#
# pandas_data = pandas.DataFrame(data_dict)
# print (pandas_data)
#
# # We can now convert the DataFrame into a csv file:
# data = pandas_data
# data.to_csv("new_data.csv")

# Now we'll count the number of squirrels in the central park data:
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

# Another way of retrieving the count with fewer lines of code:
squir_data = squirrel_data[squirrel_data["Primary Fur Color"].isin(["Gray", "Cinnamon", "Black"])]
grouped_squirrels = squir_data.groupby(["Primary Fur Color"]).size()
print (grouped_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")