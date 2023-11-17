from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to the coffee machine.")
drink = False
while not drink:
  order = input(f"Please place your order ({menu.get_items()})\n")
  drink = menu.find_drink(order)

