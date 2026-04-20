# a=1

# def fun():
#     a=10
#     print("inner function ",a)
    
# fun()    
# print("outer function ",a)    





# player_health = 10

# def game():
#     def drink_potion():
#         portion_strength = 2
#         print(player_health)
#     drink_potion()
# print(player_health)   
# game()     



# how to modify global variable 


orange = 10

def myfun(myorange):
    print(f"this is inner orange {orange}")
    myorange = myorange+1;
    return myorange;
    
orange = myfun(orange)
print("this is outer ornage ",orange)

