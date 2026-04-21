# def my_function():
#     for i in range(1,21):
#         if i==20:
#             print("you got it")

# my_function()
#             #here the value of i is going from 0 to 19
#             # so it never reach to the goal
            
            
            
# Reproduce the Debug
# import random

# dice_images = ["1","2","3","4","5","6"]

# dice_num  = random.randint(0,5);
# print(dice_images[dice_num])
            
            
            
# play computer and Evaluate Each line 


# year =int(input("what your year of birth :"))

# if year > 1980 and year < 1994:
#     print("you are a millennial");
# else:
#     print("You are a Gen Z")
            
            
            
###########################################


# year =int(input("what your year of birth :"))

# if year > 1980 and year < 1994:
#     print("you are a millennial");
# elif year >= 1994:
#     print("You are a Gen Z")
            
            
############################################

# try:
#     age =int(input("what your age :"))
# except ValueError:
#     print("you have to put the valid number . please try with number")    
#     age =int(input("what your year of birth :"))

# if age < 18:
#     print(f"you can drive at after {18-age} years")



#############################################

import random 
import maths 


def  mutate(a_list):
    b_list = [] 
    new_item =0
    
    for item in a_list:
        new_item = item*2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item,item)
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])    
        
        
# level of solve problem        
# take break 
# do debug
# ask from friends
# run often
# ask stack overflow 
# ask ai 
        
# more be professional more bigger bug we face        