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
import pdb

def deal(number):
    return random.choices(cards, k=number)

def total(cards):
    return sum(cards)

def is_bust(cards):
    return total(cards) > 21

def must_deal(cards):
    return total(cards) < 17

def deal_and_update_hand(cards):
    cards.append(deal(1)[0])
    cards = revalue_aces_if_bust(cards)
    return cards

def print_card_message(user, cards):
    if user == "dealer":
        name = "Dealer"
    else:
        name = "Your"
    print(f"{name} cards are:")
    print(f"{cards} (total {total(cards)})")

def print_winner_message(player_cards, dealer_cards, balance, bet):
    winner = determine_winner(player_cards, dealer_cards)
    balance = update_player_balance(balance, bet, winner)
    message = "You win." if winner == "player" else "Dealer wins, you loose."
    print(message)
    print_balance_message(balance)
    return balance

def determine_winner(player_cards, dealer_cards):
    if is_bust(player_cards):
        return "dealer"
    elif is_bust(dealer_cards) or total(player_cards) > total(dealer_cards):
        return "player"
    else:
        return "dealer"

def revalue_aces_if_bust(cards):
    if is_bust(cards):
        cards = [1 if card == 11 else card for card in cards]
    return cards

def print_balance_message(balance):
    print(f"Your balance is ${balance}")

def update_player_balance(balance, bet, winner):
    if winner == "player":
        balance += bet
    else:
        balance -= bet
    return balance

def blackjack(balance):
    bet = int(input("How much do you want to bet:\n$"))
    player_cards = deal(2)
    dealer_cards = deal(2)
    print_card_message("player", player_cards)
    keep_dealing = True
    while keep_dealing:
        print("Dealer showing")
        print(dealer_cards[1])
        action = input(f"You have {total(player_cards)} do you want to hit or stay? Type 'h' of 's':\n")
        if action == "h":
            player_cards = deal_and_update_hand(player_cards)
            print_card_message("player", player_cards)
            if is_bust(player_cards):
                keep_dealing = False
                print("Sorry you bust.")
        else:
            keep_dealing = False

    if not is_bust(player_cards):
        print_card_message("dealer", dealer_cards)
        while must_deal(dealer_cards):
            dealer_cards = deal_and_update_hand(dealer_cards)
            print_card_message("player", player_cards)
            print_card_message("dealer", dealer_cards)
            if is_bust(dealer_cards):
                print("Dealer busts.")

    balance = print_winner_message(player_cards, dealer_cards, balance, bet)

    return balance

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_balance = 1000

print(f"Welcome to the PyCasino.")
print_balance_message(player_balance)

should_play = True
while should_play:
    player_balance = blackjack(player_balance)
    print_balance_message(player_balance)
    should_play_again = input("Do you want to keep playing? Type 'y' of 'n':\n")
    if should_play_again == "n":
        should_play = False
        print(f"Your final balance is {player_balance}. Goodbye it's been a pleasure having you at PyCasino.")

