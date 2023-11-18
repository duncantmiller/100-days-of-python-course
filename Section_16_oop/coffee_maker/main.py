"""import Menu, CoffeeMaker, MoneyMachine"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def format_dollars(amount):
    """returns a string formatted in dollars $xx.xx"""
    return f"${amount:,.2f}"

def make_if_funds_collected(drink):
    """Only make coffee if we can collect funds"""
    if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

def collect_funds_and_make(drink):
    """collect the funds and make the coffee"""
    if coffee_maker.is_resource_sufficient(drink):
        print(f"A latte costs {format_dollars(drink.cost)}")
        make_if_funds_collected(drink)
    else:
        print(f"We can't make a {drink.name}. Please try again.")

def process(order):
    """Run the whole order process then restart the machine"""
    drink = False
    while not drink:
      drink = menu.find_drink(order)
    collect_funds_and_make(drink)
    new_order()

def print_reports():
    """Print all the reports and restart the machine"""
    coffee_maker.report()
    money_machine.report()
    new_order()

def shutdown():
    """Say goodbye and don't restart the machine"""
    print("Goodbye.")

def new_order():
    """Process a full order"""
    print("\nWelcome to the coffee machine.")
    order = input(f"Please place your order ({menu.get_items()})\n")
    if order == "report":
        print_reports()
    elif order == "shutdown":
        shutdown()
    else:
        process(order)

new_order()
