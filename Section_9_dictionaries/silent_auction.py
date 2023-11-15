import os

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def store_bid(bids, name, amount):
    bids[name] = amount
    return bids

def winning_bid(bids):
    highest_amount = 0
    for key in bids:
        bid_amount = bids[key]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            bid_winner = key
    return {
        "name": bid_winner,
        "amount": highest_amount
    }

print("Welcome to the silent auction program.")
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    amount = int(input("What's your bid?: $"))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bids = store_bid(bids, name, amount)
    if more_bidders == "yes":
        continue_bidding = True
        clear()
    else:
        continue_bidding = False
        winner = winning_bid(bids)
        print(f"The winner is {winner['name']} with a bid of ${winner['amount']}")
        print("Goodbye.")

# Instructions
# The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

# Welcome to the secret auction program.
# What is your name?: Angela

# What's your bid?: $123

# Are there any other bidders? Type 'yes' or 'no'.
# yes

# If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid.

# The winner is Elon with a bid of $55000000000

# Use your knowledge of Python dictionaries and loops to solve this challenge.
