############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# used 0 hints... guess I'm a python double black diamond expert

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

def deal(number):
    return random.choices(cards, k=number)

def total(cards):
    return sum(cards)

def is_bust(cards):
    return total(cards) > 21

def must_deal(cards):
    return total(cards) < 17

def deal_and_update_hand(hand):
    hand.append(deal(1)[0])

def print_cards(cards):
    user = "Your" if cards == player_cards else "Dealer"
    print(f"{user} cards are:")
    print(f"{cards} (total {total(cards)})")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = deal(2)
dealer_cards = deal(2)
print_cards(player_cards)
keep_dealing = True
while keep_dealing:
    print("Dealer showing")
    print(dealer_cards[1])
    action = input(f"You have  do you want to hit or stay? Type 'h' of 's':\n")
    if action == "h":
        deal_and_update_hand(player_cards)
        print_cards(player_cards)
        if is_bust(player_cards):
            keep_dealing = False
            print("Sorry you bust.")
    else:
        keep_dealing = False

if not is_bust(player_cards):
    print_cards(dealer_cards)

    while must_deal(dealer_cards):
        deal_and_update_hand(dealer_cards)
        print_cards(dealer_cards)
        if is_bust(dealer_cards):
            print("Dealer busts.")

if is_bust(dealer_cards):
    print("You win.")
elif is_bust(player_cards):
    print("Dealer wins, you loose.")
elif total(player_cards) > total(dealer_cards):
    print("You win.")
else:
    print("Dealer wins, you loose.")
