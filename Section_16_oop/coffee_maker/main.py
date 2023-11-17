from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


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
        if coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)
        else:
            print(f"We can't make a {drink.name}. Please try again.")
        new_order()
new_order()
