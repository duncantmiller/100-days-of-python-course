import csv

with open("weather_data.csv") as file:
    weather_data = csv.reader(file)
    temperatures = []
    for row in weather_data:
        temperature = row[1]
        if temperature != "temp":
            temperatures.append(int(temperature))
    print(temperatures)
