import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_count = 0  # or len(data[data["Primary Fur Color"] == "Black"])
gray_count = 0  # or len(data[data["Primary Fur Color"] == "Gray"])
red_count = 0  # or len(data[data["Primary Fur Color"] == "Cinnamon"])

color_list = data["Primary Fur Color"].tolist()

for color in color_list:
    if color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        red_count += 1
    elif color == "Black":
        black_count += 1

color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_count, red_count, black_count]
}

color_data = pandas.DataFrame(color_dict)
color_data.to_csv("squirrel_count.csv")
