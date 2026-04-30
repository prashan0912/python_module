# from turtle import Turtle , Screen
# t = Turtle();
# screen = Screen();
# t.shape("turtle")
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.fd(200)
# screen.exitonclick()


# import turtle

# t = turtle.Turtle()
# t.speed(3)
# colors = ["red", "purple", "blue", "green", "orange", "yellow"]
# turtle.bgcolor("black")
# for i in range(6):
#     t.pencolor(colors[i])
#     t.forward(100)
#     t.left(60)
# t.penup() 
# t.rt(90) 
# t.forward(100)
# t.pendown()
# t.forward(100)

    
# turtle.done()

##############################################################################
# from turtle import Turtle,Screen
# import random
# tim = Turtle()

# color_pool = [
#     "Red", "Blue", "Green", "Yellow", "Purple", 
#     "Orange", "Pink", "Brown", "Cyan", "Magenta", 
#     "Lime", "Teal", "Lavender", "Gold", "Crimson"
# ]

# screen = Screen()
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle =  360/num_sides;
#         tim.forward(50);
#         tim.rt(angle)

# for shape_side_n in range(3,11):
#     tim.color(random.choices(color_pool))
#     draw_shape(shape_side_n)       
    

# ###################################################

# import turtle as t
# import random
# tim = t.Turtle()
# direction = [0,90,180,270]
# tim.pensize(10)
# def random_color():
#     r=random.randint(0,255);
#     g=random.randint(0,255);
#     b=random.randint(0,255);
#     random_color = (r,g,b)
#     return random_color

# color_pool = [
#     "Red", "Blue", "Green", "Yellow", "Purple", 
#     "Orange", "Pink", "Brown", "Cyan", "Magenta", 
#     "Lime", "Teal", "Lavender", "Gold", "Crimson"
# ]
# sc = t.Screen()
# sc.colormode(255)
# tim.speed(100)    
# for i in range(200):
#     # tim.color(random.choice(color_pool))
#     tim.color(random_color())
#     tim.forward(10)
#     tim.setheading(random.choice(direction))
    
# sc.exitonclick()


################################################


# import turtle

# # Setup screen
# screen = turtle.Screen()
# screen.bgcolor("white")

# # Create turtle
# pen = turtle.Turtle()
# pen.speed(0)
# pen.width(2)

# # Colors for rangoli
# colors = ["red", "yellow", "green", "blue", "orange", "purple"]

# # Function to draw a petal
# def draw_petal(radius):
#     for _ in range(2):
#         pen.circle(radius, 60)
#         pen.left(120)

# # Draw rangoli
# for i in range(36):
#     pen.color(colors[i % len(colors)])
#     draw_petal(100)
#     pen.left(10)

# # Hide turtle and finish
# pen.hideturtle()
# turtle.done()


##################################################


import turtle as t
import random
tim = t.Turtle()
tim.pensize(1)

def random_color():
    r=random.randint(0,255);
    g=random.randint(0,255);
    b=random.randint(0,255);
    random_color = (r,g,b)
    return random_color

sc = t.Screen()
sc.colormode(255)
tim.speed(100)    
for i in range(200):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading()+10)
sc.exitonclick()