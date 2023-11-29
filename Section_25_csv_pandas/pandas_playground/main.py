import pandas

def c_to_f(x):
    x = x * 1.8 + 32
    return float(x)

data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"].to_list()
print(temperatures)
print(f"average temperature: {int(data['temp'].mean())}")
print(f"highest temperature: {data['temp'].max()}")
print(f"conditions: {data.condition}")
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
day = data[data.temp == data.temp.max()]
print(day.condition)

# monday's temp in f
day = data[data.day == "Monday"]
temp = day.temp.apply(c_to_f)
print(temp[0])

#create a dataframe from scratch

data_dict = {
    "students": ["Mark", "Tim", "Duncan"],
    "scores": [50, 60, 100]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
