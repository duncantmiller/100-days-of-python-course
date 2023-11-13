print("Welcome to the rollercoaster!")
height = int(input("Enter your height in inches: "))

if height >= 48:
  print("You can ride the rollercoaster")
  age = int(input("Enter your age in years: "))
  if age < 12:
    price = 5
  elif age <= 18:
    price = 7
  else:
    price = 12
  want_photos = input("Do you want photos? Answer yes or no: ")
  if want_photos == "yes":
    price += 3
  print(f"Please pay ${price}.00 to ride this ride")
else:
  print("Sorry you are not tall enough")
