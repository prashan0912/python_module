

# randonmization
import random 
a = random.randint(1,10)
print(a);
b = random.random();
print(b);

#############################################
import my_module;
print(my_module.my_favourate_num);


#############################################

randam_float  = random.uniform(10,20);
#The uniform() method returns a random floating number between the two specified numbers (both included).
print(randam_float)


#############################################

# geads and tails
b = random.randint(0,1);
if b == 0:
    print("head");
else:
    print("tail");    