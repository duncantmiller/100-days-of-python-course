string_list = input("type a list of numbers").split(',')

number_list = [int(string) for string in string_list]

even_numbers = [num for num in number_list if num % 2 == 0]

print(even_numbers)
