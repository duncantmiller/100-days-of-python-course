# find the highest number in a list without using max()

numbers = [151, 145, 179, 1]

highest_number = numbers[0]
for number in numbers:
  if number > highest_number:
    highest_number = number

print(f"The highest number is: {highest_number}")
