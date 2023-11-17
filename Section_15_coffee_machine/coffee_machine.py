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

def print_report(resources):
    """Prints a report of the resources available"""
    for resource, amount in resources.items():
        print(f"{resource}: {amount}")

def are_resources_available_for(key, resources):
    """return true if there are enough ingredients else return false"""
    for ingredient in MENU[key]["ingredients"]:
        if MENU[key]["ingredients"][ingredient] > resources[ingredient]:
            return False
    return True

def update_resources_for(key, resources):
    """reduces resources by the proper amounts for the order"""
    for ingredient in MENU[key]["ingredients"]:
        resources[ingredient] -= MENU[key]["ingredients"][ingredient]
    return resources

def coffee_machine():
    """Makes your coffee"""
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    order = input("Please place your order espresso/latte/cappuccino:\n")
    if order == "report":
        print_report(resources)
        coffee_machine()
    elif order == "shutdown":
        print("Goodbye.")
    else:
        if are_resources_available_for(order, resources):
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
            resources = update_resources_for(order, resources)
            print(f"Your change is: {format_dollars(change)}")
            print(f"Here is your {order}. Enjoy!\n")
        else:
            print(f"Sorry I don't have enough ingredients for a {order}. Please try again.\n")
        coffee_machine()

coffee_machine()
