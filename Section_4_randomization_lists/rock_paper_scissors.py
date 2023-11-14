import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_images = [rock, paper, scissors]

print("Play rock, paper, scissors against the computer!")

player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors:\n"))

while player_choice < 0 or player_choice > 2:
  player_choice = int(input("You typed an invalid option. Type 0 for rock, 1 for paper or 2 for scissors:\n"))


computer_choice = random.randint(0, 2)

choices = ["Rock", "Paper", "Scissors"]

result_message = ""
if player_choice == computer_choice:
  result_message = "Draw"
elif player_choice == 0:
  if computer_choice == 1:
    result_message = "You loose, paper covers rock"
  else:
    result_message = "You win, rock smashes scissors"
elif player_choice == 1:
  if computer_choice == 0:
    result_message = "You win, paper covers rock"
  else:
    result_message = "You loose, rock smashes scissors"
elif player_choice == 2:
  if computer_choice == 0:
    result_message = "You loose, rock smashes scissors"
  else:
    result_message = "You win, scissors cut paper"

print(f"\nYou chose {choices[player_choice]}.")

print(ascii_images[player_choice])

print(f"Computer chose {choices[computer_choice]}.")

print(ascii_images[computer_choice])

print(f"{result_message}.")
