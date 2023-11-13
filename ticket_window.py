print("Welcome to the rollercoaster!")
height = int(input("Enter your height in inches: "))

if height >= 48:
  print("You can ride the rollercoaster")
  age = int(input("Enter your age in years: "))
  if age < 12:
    price = 5
    age_category = "Child"
  elif age <= 18:
    price = 7
    age_category = "Youth"
  elif age >= 45 and age <= 55:
    price = 0
    age_category = "Midlife crisis"
  else:
    price = 12
    age_category = "Adult"
  print (f"{age_category} tickets are ${price}.00")
  want_photos = input("Do you want photos? Answer yes or no: ")
  if want_photos == "yes":
    price += 3
  print(f"Please pay ${price}.00 to ride this ride")
else:
  print("Sorry you are not tall enough")
