def encrypt(text, shift):
    encrypted_text = ''
    for letter in text:
        current_position = alphabet.index(letter)
        new_position = current_position + shift
        encrypted_text += alphabet[new_position]
    return encrypted_text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    print(encrypt(text, shift))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
