"""Coffee machine"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_price(key):
    """retrieves the cost from the menu dictionary"""
    return MENU[key]["cost"]

def format_dollars(amount):
    """returns a string formatted in dollars $xx.xx"""
    return f"${amount:,.2f}"

def sum_currency(pennies, nickels, dimes, quarters):
    """calculates the value of change paid"""
    return pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25

def has_paid_enough(cost, paid):
    """checks to see if the customer paid enough"""
    return cost <= paid

def calculate_change(cost, paid):
    """calculates the change due"""
    return paid - cost

def print_report(inventory):
    """Prints a report of the resources available"""
    for resource, amount in inventory.items():
        print(f"{resource}: {amount}")

def is_inventory_available_for(key, inventory):
    """return true if there are enough ingredients else return false"""
    for ingredient in MENU[key]["ingredients"]:
        if MENU[key]["ingredients"][ingredient] > inventory[ingredient]:
            return False
    return True

def update_inventory_for(key, inventory):
    """reduces resources by the proper amounts for the order"""
    for ingredient in MENU[key]["ingredients"]:
        inventory[ingredient] -= MENU[key]["ingredients"][ingredient]
    return inventory

def coffee_machine(inventory):
    """Makes your coffee"""
    order = input("Please place your order espresso/latte/cappuccino:\n")
    if order == "report":
        print_report(inventory)
        coffee_machine(inventory)
    elif order == "shutdown":
        print("Goodbye.")
    else:
        if is_inventory_available_for(order, inventory):
            order_cost = get_price(order)
            collect_money = True
            while collect_money:
                print(f"The cost of a {order} is {format_dollars(order_cost)}")
                pennies_count = int(input("How many pennies: "))
                nickels_count = int(input("How many nickels: "))
                dimes_count = int(input("How many dimes: "))
                quarters_count = int(input("How many quarters: "))
                amount_paid = sum_currency(
                    pennies_count, nickels_count, dimes_count, quarters_count
                )
                if has_paid_enough(order_cost, amount_paid):
                    collect_money = False
                else:
                    print(f"You only paid {format_dollars(amount_paid)}. I'm returning your money"
                        " please try again")
            change = calculate_change(order_cost, amount_paid)
            inventory = update_inventory_for(order, inventory)
            print(f"Your change is: {format_dollars(change)}")
            print(f"Here is your {order}. Enjoy!\n")
        else:
            print(f"Sorry I don't have enough ingredients for a {order}. Please try again.\n")
        coffee_machine(inventory)

coffee_machine(resources)
