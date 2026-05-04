from turtle import Turtle, Screen


t =Turtle()
screen =Screen()


def move_up():
    t.bk(10)
def move_left():
    t.lt(10)    
def move_right():
    t.rt(10)   
def move_down():
    t.rt(10)          
def move_forward():
    t.forward(20)
    
def clear_up():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
        
screen.listen() 
screen.onkey(key="w",fun=move_up)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="s",fun=move_down)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="space",fun=move_forward)
screen.onkey(key="c",fun=clear_up)


screen.exitonclick()   