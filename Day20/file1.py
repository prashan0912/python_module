from turtle import Turtle , Screen
t= Turtle()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_poistion = [(0,0),(-20,0),(-40,0)]


for position in starting_poistion:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)



def move_left():
    t.left(90)

def move_right():
    t.left(90)

def move_up():
    t.left(90)        

def move_down():
    t.left(90)    


# create a snake body        
screen.listen() 
screen.onkey(key="w",fun=move_up)
screen.onkey(key="s",fun=move_down)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
t.speed("slow")
game_on = True
while not game_on:
    t.forward(1)
    
    
    

#love a snake
# control snake
#detect collision with food 
# create a scorecard 
#detect collision with wall 
# detect collision



screen.exitonclick()