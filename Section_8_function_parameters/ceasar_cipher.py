import art

def shifted_text(text, shift, direction):
    shift = _normalize_shift(shift)
    new_text = ''
    for letter in text:
        current_position = alphabet.index(letter)
        new_position = _reposition(current_position, shift, direction)
        new_text += alphabet[new_position]
    return new_text

def _reposition(current_position, shift, direction):
    if direction == "decode":
        shift *= -1
    return _normalize_position(current_position + shift)

def _normalize_shift(shift):
    if shift > 26:
        wraps = int(shift / 26)
        shift -= wraps * 26
    return shift

def _normalize_position(position):
    if position > 25:
        position -= 26
    return position

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
go = "yes"
while go == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        print(f"The {direction}d text is:\n{shifted_text(text, shift, direction)}")
    else:
        print("Invalide encryption option, must be 'encode' or 'decode'")
    go = input("Would you like to keep encrypting messages? Type: 'yes' or 'no'\n")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

#TODO-3: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
