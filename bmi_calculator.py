print("Enter your height in meters")
height = input()
print("Enter your weight in meters")
weight = input()

bmi_float = int(weight) / (float((height)) ** 2)
bmi = int(bmi_float)
print("Your BMI is " + str(bmi))
