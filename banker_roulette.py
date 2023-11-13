# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
number_of_names = len(names)
buyer = names[random.randint(0, number_of_names - 1)]

print(f"{buyer} is going to buy the meal today!")
