# how to generate random rgb

# random walk
from turtle import Turtle,Screen,colormode


random_degree = [25,75,104,327]
import random


def mycolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb;
     


t = Turtle()
t.shape("turtle")
t.pensize(15)
t.speed("fastest")
colormode(255)

for i in range(500):
    t.forward(20)
    t.right(random.choice(random_degree))
    t.color(mycolor())

s = Screen() 
s.exitonclick()   