print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("\nYou are walking down a dark path deep in the forest. You come to a fork in the road.")
left_or_right = input("Do you want to go left or right? Type L or R: ").upper()

if left_or_right == "L":
  print("\nAfter several miles of hiking the trail opens out onto the beach. You can see the trail continue up ahead further down the beach, but the tide is in and the trail is blocked.")
  swim_or_wait = input("Do you want to swim to the trail or wait for the tide to go out? Type S or W: ").upper()
  if swim_or_wait == "W":
    print("\nGood choice, the tide has now receded and you are able to continue. You pick up the trail and soon come to fence three doors, a red door, a blue door and a yellow door.")
    which_door = input("Which door do you want to enter? Type R, B or Y: ").upper()
    if which_door == "Y":
      print("\nCongratulations you found the treasure!")
    else:
      print("Sorry you've been eaten by ants. Game over.")
  else:
    print("Sorry you've been eaten by a shark. Game over.")
else:
  print("Sorry, you've been eaten by a bear. Game over.")
