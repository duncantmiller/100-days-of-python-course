import pandas

data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"].to_list()
print(temperatures)
print(f"average temperature: {int(data['temp'].mean())}")
