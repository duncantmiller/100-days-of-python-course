#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", encoding="utf-8") as file:
    names = file.read()
    names_list = names.splitlines()

with open("Input/Letters/starting_letter.txt", encoding="utf-8") as file:
    starting_letter = file.read()

for name in names_list:
    personalized_letter = starting_letter.replace('[name]', name)
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w", encoding="utf-8") as file:
        file.write(personalized_letter)
