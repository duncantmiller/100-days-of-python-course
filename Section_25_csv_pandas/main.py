import pandas

data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"].to_list()
print(temperatures)
average_temp = sum(temperatures) / len(temperatures)
print(f"average temperature: {int(average_temp)}")
