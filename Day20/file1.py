from turtle import Turtle , Screen
import time
import snake from Snake
t= Turtle()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # har bar trace nhi karega jha jha update likha hai vha vha change hoga or screen refresh hoga
starting_poistion = [(0,0),(-20,0),(-40,0)] # in coordinate se start hoga
segments = [] #these are segments mean actual address are stored in an array

# creating body of snake
for position in starting_poistion:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_on = True
# while game_on:
#     screen.update() #to update the screen after completion of sef loop 
#     time.sleep(0.1)
#     for seg in segments:
#         seg.forward(20)    

# segments[0].left(90)    



while game_on:
    screen.update()
    time.sleep(0.1)

    # move body from tail to head
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    # move head forward
    segments[0].left(90)
    segments[0].forward(20)




# def move_left():
#     t.left(90)

# def move_right():
#     t.left(90)

# def move_up():
#     t.left(90)        

# def move_down():
#     t.left(90)    


# create a snake body        
# screen.listen() 
# screen.onkey(key="w",fun=move_up)
# screen.onkey(key="s",fun=move_down)
# screen.onkey(key="a",fun=move_left)
# screen.onkey(key="d",fun=move_right)


    

#love a snake
# control snake
#detect collision with food 
# create a scorecard 
#detect collision with wall 
# detect collision



screen.exitonclick()