#Password Generator Project
import random
import string
letters = list(string.ascii_letters)
# not sure this is really more readable than ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# but just playing
numbers = [str(num) for num in list(range(0, 10))]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_count= int(input("How many letters would you like in your password?\n"))
symbols_count = int(input(f"How many symbols would you like?\n"))
numbers_count = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""
# for count in range(0, letters_count):
#   password += letters[random.randint(0, len(letters) - 1)]

# for count in range(0, numbers_count):
#   password += numbers[random.randint(0, len(numbers) - 1)]

# for count in range(0, symbols_count):
#   password += symbols[random.randint(0, len(symbols) - 1)]

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
for count in range(0, letters_count):
  password += letters[random.randint(0, len(letters) - 1)]

for count in range(0, numbers_count):
  password += numbers[random.randint(0, len(numbers) - 1)]

for count in range(0, symbols_count):
  password += symbols[random.randint(0, len(symbols) - 1)]

characters = list(password)

random_password = []
for _ in password:
  rand_int = random.randint(0, len(characters) - 1)
  random_password.append(characters.pop(rand_int))

print("".join(random_password))
