# how to generate random rgb

# random walk
from turtle import Turtle,Screen,colormode


import random

def mycolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb;
     


t = Turtle()
t.shape("turtle")
t.speed("fastest")
colormode(255)

for i in range(300):
    t.circle(100)
    t.setheading(t.heading()+5)
    t.color(mycolor())

s = Screen() 
s.exitonclick()   




# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# ########### Challenge 5 - Spirograph ########

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)




