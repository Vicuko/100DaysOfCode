DATA_FILE = "./weather_data.csv"

# Opening file normally:
# with open(DATA_FILE, mode="r") as data_file:
#     weather_list = data_file.readlines()
# We have an issue here: we need to parse and separate all of the content in order to
# retrieve all of the information, which can get complicated.
# This is why, we'll use the csv module:

import csv

with open(DATA_FILE) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# import pandas
#
# pandas.read_csv(DATA_FILE)