import pandas

data = pandas.read_csv("squirrel_data.csv")

fur_colors = data["Primary Fur Color"]
print(fur_colors.value_counts())

black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])

color_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}
fur_data = pandas.DataFrame(color_dictionary)

fur_data.to_csv("squirrel_color_counts.csv")
