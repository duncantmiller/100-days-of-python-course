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
      new_order()
new_order()
