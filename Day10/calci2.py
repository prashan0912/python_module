

operden1 = int(input("Enter the value of operator 1: "))
operend2 = int(input("Enter the value of operator 2: "))

opertation = input("Enter the value of operation(add, div, sub, mod, mul) : ")


# def fun(operden1,operend2,opertation):

#     if(opertation == "add"):
#         output = operden1 + operend2
#         return output
#     elif(opertation == "sub"):
#         output = operden1 - operend2
#         return output



#     elif(opertation == "mod"):
#         output = operden1 % operend2
#         return output

#     elif(opertation == "mul"):
#         output = operden1 * operend2
#         return output

#     elif(opertation == "div"):
#         output = operden1 / operend2
#         return output

#     else:
#         print("invalid input")
#         print(output)

num1 = operden1
num2 = operend2

def addition(num1,num2):
     return num1 + num2;
 
def substraction(num1,num2):
    return num1 - num2;

def multiplication(num1,num2):
    return num1 * num2;

def divide(num1,num2):
    return num1 / num2;

 
dictionary = {
    '+': addition,
    '-':substraction,
    '*':multiplication,
    '/':divide
} 

print(dictionary[opertation](num1,num2))
        