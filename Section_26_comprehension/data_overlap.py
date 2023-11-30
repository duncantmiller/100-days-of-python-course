with open("file1.txt") as file:
    content = file.read()
    file1_string_list = content.splitlines()

with open("file2.txt") as file:
    content = file.read()
    file2_string_list = content.splitlines()

file_1_numbers = [int(num) for num in file1_string_list]
file_2_numbers = [int(num) for num in file2_string_list]

common_numbers = []
for number in file_1_numbers:
    if file_2_numbers.count(number) > 0:
        common_numbers.append(number)

print(common_numbers)
