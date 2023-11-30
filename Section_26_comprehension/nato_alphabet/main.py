import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter:row.code for (index, row) in nato_df.iterrows()}

print(nato_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Type a word to see it spelled in Nato phonetics:\n").upper()

codes = [nato_dictionary[letter] for letter in word]

print(codes)
