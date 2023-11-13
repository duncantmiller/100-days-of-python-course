bill_amount = float(input("Enter the total bill abount $"))
tip_amount = int(input("What percentage tip would you like to give? 15, 20 or 25? "))
people = int(input("How many people to split the bill? "))

total = bill_amount * (1 + (tip_amount / 100))
rounded_total = round(total, 2)

per_person = (rounded_total / people)
per_person_rounded = round(per_person, 2)

print(f"Each person should pay ${per_person_rounded}")
