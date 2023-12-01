import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index, row) in nato_df.iterrows()}
word = input("Type a word to see it spelled in Nato phonetics:\n").upper()
codes = [nato_dictionary[letter] for letter in word]

print(codes)
