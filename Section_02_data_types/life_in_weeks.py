print("enter your age")
age = int(input())
end_years = 90

if age < end_years:
  years_left = end_years - age
  weeks_left = years_left * 52
  print(f"You only have {weeks_left} weeks left until you are {end_years} years old!")
elif age == end_years:
  print(f"Congratulations, you've reached {end_years} years old (the end is near)!")
else:
  years_over = age - end_years
  weeks_over = years_over * 52
  print(f"You are already {weeks_over} weeks over expiration ({end_years} years)!")
