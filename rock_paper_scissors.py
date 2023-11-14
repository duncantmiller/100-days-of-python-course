import random

print("Play rock, paper, scissors against the computer!")

player_choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors: "))

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

print(f"You chose {choices[player_choice]}. Computer chose {choices[computer_choice]}. {result_message}.")
