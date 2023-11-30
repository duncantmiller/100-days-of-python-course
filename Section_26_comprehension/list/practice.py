numbers = range(2, 5)
new_numbers = [number * 2 for number in numbers]
print(new_numbers)

names = "tim john david mike frank".split()
short_names = [name for name in names if len(name) < 5]
print(short_names)
