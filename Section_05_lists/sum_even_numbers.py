print("The even number calculator adds up all even numbers between 1 and the number you enter.")
max_number = int(input("Enter any number: "))

total = 0
for number in range(2, max_number + 1, 2):
  total += number

print(f"The total is: {total}")

