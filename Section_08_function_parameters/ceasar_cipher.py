import art

def shifted_text(text, shift, direction):
    shift = _normalize_shift(shift)
    new_text = ''
    for character in text:
        new_text += _new_character(character, shift, direction)
    return new_text

def _new_character(character, shift, direction):
    if alphabet.count(character) > 0:
        current_position = alphabet.index(character)
        new_position = _reposition(current_position, shift, direction)
        character = alphabet[new_position]
    return character

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
