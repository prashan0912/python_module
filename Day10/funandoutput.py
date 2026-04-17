operden1 = int(input("Enter the value of operator 1: "))
operend2 = int(input("Enter the value of operator 2: "))

opertation = input("Enter the value of operation(add, div, sub, mod, mul) : ")

if(opertation == "add"):
    output = operden1 + operend2
elif(opertation == "sub"):
    output = operden1 - operend2
    
elif(opertation == "mod"):
    output = operden1 % operend2
elif(opertation == "mul"):
    output = operden1 * operend2
elif(opertation == "div"):
    output = operden1 / operend2
else:
    print("invalid input")
print(output)


#title 
a = "hello my name is prashant sahu ";
print(a.title());
print("hello")

