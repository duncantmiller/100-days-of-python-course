import art

def shifted_text(text, shift, direction):
    shift = _normalize_shift(shift)
    new_text = ''
    for letter in text:
        if alphabet.count(letter) > 0:
            current_position = alphabet.index(letter)
            new_position = _reposition(current_position, shift, direction)
            new_text += alphabet[new_position]
        else:
            new_text += letter
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

#TODO-1: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
