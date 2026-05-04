
# different shapes by using turtle

from turtle import Turtle,Screen
import random
t = Turtle()

# t.shape("turtle")
# t.color("red")
# t.fd(100)
# t.rt(90)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(3,10):
    degree = 360/i
    for j in range(i):
        t.forward(50)
        t.right(degree)
        t.color(random.choice(colours))
        
    
screen = Screen()
screen.exitonclick()