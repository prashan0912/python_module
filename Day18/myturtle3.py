# random walk
from turtle import Turtle,Screen


random_degree = [25,75,104,327]
import random

t = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
t.shape("turtle")
t.width(30)
t.pensize(15)
t.speed("fastest")
for i in range(500):
    t.forward(20)
    t.right(random.choice(random_degree))
    t.color(random.choice(colours))

s = Screen() 
s.exitonclick()   