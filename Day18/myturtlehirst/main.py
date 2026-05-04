# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color =(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


# import turtle as t
# from turtle import colormode
# t.Turtle()
# t.penup()
# t.hideturtle()
# t.forward(10)
# colormode(255)
# for i in range(5):
#     for j in range(30):
#         t.dot(10)
#         t.color(rgb_colors[j])
#         t.forward(20)
#     t.position()        
        
    
import turtle as t
import random
from turtle import colormode

colormode(255)

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

# Example colors (replace with your extracted ones)
rgb_colors = [
    (239, 83, 80), (66, 165, 245), (102, 187, 106),
    (255, 238, 88), (171, 71, 188), (255, 167, 38)
]

# starting position
tim.setpos(-200, -200)

for i in range(5):          # rows
    for j in range(30):     # columns
        tim.dot(10, random.choice(rgb_colors))  # color applied here
        tim.forward(20)
    
    # move to next row
    tim.backward(600)   # go back to start of row
    tim.left(90)
    tim.forward(20)
    tim.right(90)

screen = t.Screen()
screen.exitonclick()    