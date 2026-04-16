# Caesar Cipher 




# x = "10"
# y = int(x)
# print(y, type(y))  # 10 <class 'int'>




alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z'];


direction = input("Enter 'encode' to encrypt  and type 'decode' to decrypt")# encode
original_text = input("Enter the word to encrypt :") # abcd -> defg
shifted_position = int(input("Enter the value of shiftopertion: ")) #3

def encrypt(original_text,shift_amt):
    cipher_text = "";
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amt
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position];
    print(cipher_text);

def decypher(original_text,shift_amt):
    output_text = "";
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amt
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position];
    print(output_text);


if(direction == "encode"):
    encrypt(original_text,shifted_position);
else:
    decypher(original_text,shifted_position);
