alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Enter 'encode' to encrypt and 'decode' to decrypt: ")
original_text = input("Enter the text: ").lower()
shift_amt = int(input("Enter shift value: "))


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print("Encrypted:", cipher_text)


def decrypt(text, shift):
    output_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print("Decrypted:", output_text)


if direction == "encode":
    encrypt(original_text, shift_amt)
elif direction == "decode":
    decrypt(original_text, shift_amt)
else:
    print("Invalid input")