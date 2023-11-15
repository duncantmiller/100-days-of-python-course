def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

calculator_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

number1 = int(input("What is the first number: "))
number2 = int(input("What is the second number: "))
print("Operations available:")
for symbol in calculator_functions:
    print(symbol)
symbol = input("What operation symbol would you like to perform?: ")
calculator_function = calculator_functions[symbol]
answer = calculator_function(number1, number2)
print(f"{number1} {symbol} {number2} = {answer}")
more_calculations = input(
    f"Would you like to continue performing calculations on {answer}? Type 'yes' or 'no'\n"
)
if more_calculations == "yes":
    continue_calculation = True
else:
    continue_calculation = False
    print("Goodbye.")
while continue_calculation:
    number2 = int(input("What is the second number: "))
    for symbol in calculator_functions:
        print(symbol)
    symbol = input("What operation symbol would you like to perform?: ")
    calculator_function = calculator_functions[symbol]
    new_answer = calculator_function(answer, number2)
    print(f"{answer} {symbol} {number2} = {new_answer}")
    more_calculations = input(
        f"Would you like to continue performing calculations on {answer}? Type 'yes' or 'no'\n"
    )
    if more_calculations == "yes":
        continue_calculation = True
    else:
        continue_calculation = False
        print("Goodbye.")
