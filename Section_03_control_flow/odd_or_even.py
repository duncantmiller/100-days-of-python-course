print("Welcome to the odd or even bot")
number = int(input("Enter a number: "))

odd_or_even = "even" if number % 2 == 0 else "odd"

print(f"{number} is an {odd_or_even} number!")
