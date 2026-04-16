letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']

number = ['0','9','8','7','6','5','4','3','2','1']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '/']

 
print("welcome to mypassword Generator");

letter_input = int(input("How many letter would you like in your password"))
symbols_input = int(input("How many letter would you like in your password"))
number_input = int(input("How many letter would you like in your password"))


# import random
# password = "";

# for i in range(0,letter_input):
#     password += random.choice(letter);

# for i in range(0,symbols_input):
#     password += random.choice(symbols);

# for i in range(0,number_input):
#     password += random.choice(number);

# print(password)   


import random
password = [];

for i in range(0,letter_input):
    password.append(random.choice(letter));

for i in range(0,symbols_input):
    password.append(random.choice(symbols));

for i in range(0,number_input):
    password.append(random.choice(number));


print(password)
print(random.shuffle(password))   
print(password);
mypassword = "";
for char in password:
     mypassword +=char;

print(mypassword) 

