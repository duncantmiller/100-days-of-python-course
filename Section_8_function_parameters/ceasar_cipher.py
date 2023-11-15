def encrypt(text, shift):
    shift = _normalize_shift(shift)
    encrypted_text = ''
    for letter in text:
        current_position = alphabet.index(letter)
        new_position = _normalize_position(current_position + shift)
        encrypted_text += alphabet[new_position]
    return encrypted_text

def decrypt(text, shift):
    shift = _normalize_shift(shift)
    decrypted_text = ''
    for letter in text:
        current_position = alphabet.index(letter)
        new_position = _normalize_position(current_position - shift)
        decrypted_text += alphabet[new_position]
    return decrypted_text

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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    print(encrypt(text, shift))
elif direction == "decode":
    print(decrypt(text, shift))

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
