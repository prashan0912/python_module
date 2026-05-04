from turtle import Turtle ,Screen, colormode
import random

t = Turtle()
t.color("red")
t.shape("arrow")


colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t.pensize(10)
for i in range(10):
    for j in range(10):
        t.circle(3)
        t.color(random.choice(random_color()))
        t.pendown()
        t.forward(2)
        t.pendown()
        
        
        

s = Screen()
s.exitonclick()

