print("Thank you for choosing Python Pizza Deliveries")

size = input("What size pizza would you like? Enter S, M or L: ")
add_pepperoni = input("Would you like to add pepperoni? Enter Y or N: ")
extra_cheese = input("Would you like extra cheese? Entery Y or N:")

price = 0

if size == "S":
  price += 15
elif size == "M":
  price += 20
elif size == "L":
  price += 25

if add_pepperoni == "Y" and size == "S":
  price += 2
elif add_pepperoni == "Y":
  price += 3

if extra_cheese == "Y":
  price += 1

print(f"Your total price is: ${price}.00")
