# this is how you work out whether a particular year is a leap year:
# on every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder
# unless the year is also divisible by 400 with no remainder

print("Welcome to the leap year bot")

year = int(input("Enter the year you want to check: "))

leap_year = False

if year % 4 == 0:
  leap_year = True
  if year % 100 == 0:
    leap_year = False
    if year % 400 == 0:
      leap_year = True

result = "is" if leap_year else "is not"
print(f"The year {year} {result} a leap year")
