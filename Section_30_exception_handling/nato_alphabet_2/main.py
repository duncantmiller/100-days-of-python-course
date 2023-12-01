import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index, row) in nato_df.iterrows()}

def generate_code():
    """generate the phonetic code and handle non letters"""
    word = input("Type a word to see it spelled in Nato phonetics:\n").upper()
    try:
        codes = [nato_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_code()
    else:
        print(codes)

generate_code()
