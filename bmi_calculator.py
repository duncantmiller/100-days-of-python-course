def response(bmi_float):
  if bmi_float < 18.5:
    return "you are underweight"
  elif bmi_float < 25:
    return "you are normal weight"
  elif bmi_float < 25:
    return "you are normal weight"
  elif bmi_float < 30:
    return "you are slightly overweight"
  elif bmi_float < 35:
    return "you are obese"
  else:
    return "you are clinically obese"

print("Enter your height in meters")
height = input()
print("Enter your weight in meters")
weight = input()

bmi_float = int(weight) / (float((height)) ** 2)
bmi_rounded = round(bmi_float, 0)
bmi = int(bmi_rounded)
print(f"Your BMI is {bmi} and {response(bmi_float)}")
