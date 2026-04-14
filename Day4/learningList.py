

a = ["Maharahshtra","kolkata","chhattisgarh","Delhi","Bihar","Jharkhand"]
print(a[0]);
print(a[1]);

print(a[-1]);
print(a[-2]);

print(a)

a.append("Karnataka")

print(a)

b = ["Kashmir","kerela","TamilNadu", "Assam"];

c = a+b;

print(c);

print(c.extend(["Tripura","Meghalay"]))

print(c)


import random
print( random.choice(a))

any_state = random.randint(2,5)

print(a[any_state]);