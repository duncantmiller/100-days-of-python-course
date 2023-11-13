print("enter your age")
age = input()
end_years = 90

years_left = end_years - int(age)
weeks_left = years_left * 52
print(f"You only have {weeks_left} weeks left until you are {end_years} old!")
