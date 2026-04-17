operden1 = int(input("Enter the value of operator 1: "))
operend2 = int(input("Enter the value of operator 2: "))

opertation = input("Enter the value of operation(add, div, sub, mod, mul) : ")

output = None
def fun(operden1,operend2,opertation):
    if(opertation == "add"):
        output = operden1 + operend2
        return output
    elif(opertation == "sub"):
        output = operden1 - operend2
        return output
    elif(opertation == "mod"):
        output = operden1 % operend2
        return output

    elif(opertation == "mul"):
        output = operden1 * operend2
        return output

    elif(opertation == "div"):
        output = operden1 / operend2
        return output
    else:
        print("invalid input")


kuch = fun(operden1,operend2,opertation)

print(kuch)