# Instructions
# 💪 This is a difficult challenge! 💪
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."

print("The Love Calculator is calculating your score")
name1 = input("Enter the first person's full name: ")
name2 = input("Enter the second person's full name: ")

combined_names = name1.upper() + name2.upper()

digit_one = 0
digit_one += combined_names.count("T")
digit_one += combined_names.count("R")
digit_one += combined_names.count("U")
digit_one += combined_names.count("E")

digit_two = 0
digit_two += combined_names.count("L")
digit_two += combined_names.count("O")
digit_two += combined_names.count("V")
digit_two += combined_names.count("E")

love_score = int(f"{digit_one}{digit_two}")

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
