print("Enter your height in meters")
height = input()
print("Enter your weight in meters")
weight = input()

bmi_float = int(weight) / (float((height)) ** 2)
bmi_rounded = round(bmi_float, 0)
bmi = int(bmi_rounded)
print("Your BMI is %s" %bmi)
