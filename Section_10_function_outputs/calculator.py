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
print(f"{number1} {symbol} {number2} = {calculator_function(number1, number2)}")
