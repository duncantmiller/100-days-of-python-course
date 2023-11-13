print("Welcome to the odd or even bot")
number = int(input("Enter a number: "))

if number % 2 == 0:
  odd_or_even = "even"
else:
  odd_or_even = "odd"

print(f"{number} is an {odd_or_even} number!")
