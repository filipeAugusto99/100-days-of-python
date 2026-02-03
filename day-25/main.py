# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()

# sum_temp = 0
#
# for temp in temp_list:
#     sum_temp += temp
#
# average_temp = sum_temp / len(temp_list)
#
# print(average_temp)

# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns
# print(data["condition"])
# print(data.condition)

# get data in row
# max_data = data["temp"].max()
# print(data[data.temp == max_data])
#
# monday = data[data.day == "Monday"]
# # print(monday.temp)
#
# monday_temp = monday.temp[0]
# monday_temp_F = (monday_temp * 9/5) + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260203.csv")

data_dict = data.to_dict()

colors_list = data["Primary Fur Color"].to_list()

count_color_grey = 0
count_color_red = 0
count_color_black = 0

for color in colors_list:

    if color == "Gray":
        count_color_grey += 1

    if color == "Cinnamon":
        count_color_red += 1

    if color == "Black":
        count_color_black += 1

data_colors = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [count_color_grey, count_color_red, count_color_black]
}

data = pandas.DataFrame(data_colors)
data.to_csv("squirrel_count.csv")