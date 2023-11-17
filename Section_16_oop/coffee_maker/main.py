from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def format_dollars(amount):
    """returns a string formatted in dollars $xx.xx"""
    return f"${amount:,.2f}"

def collect_funds_and_make(drink):
    if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

def process_order(drink):
    if coffee_maker.is_resource_sufficient(drink):
        print(f"A latte costs {format_dollars(drink.cost)}")
        collect_funds_and_make(drink)
    else:
        print(f"We can't make a {drink.name}. Please try again.")

def new_order():
    print("\nWelcome to the coffee machine.")
    order = input(f"Please place your order ({menu.get_items()})\n")
    if order == "report":
        coffee_maker.report()
        new_order()
    elif order == "shutdown":
        print("Goodbye.")
    else:
        drink = False
        while not drink:
          drink = menu.find_drink(order)
        process_order(drink)
        new_order()

new_order()
