# constructing object and accessing their attributes and methods
from turtle import Turtle , Screen

# class -> object()
timmy = Turtle();   # here turtle is class and timmy is object
print(timmy)
timmy.shape()
timmy.color("red")
timmy.forward(100)
timmy.circle(200)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.window_width())
my_screen.exitonclick()

