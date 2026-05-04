from turtle import Turtle,Screen
import random
t = Turtle()
s = Screen()
# s.setup(500,400)

s.setup(width=500,height=400)

colors = ["red","green","blue","black","yellow"]
user_bet = s.textinput(title="Make your bet",prompt="which turtle is win the race? Enter a color:")
x=[-230 , -250 , -270 , -290 , -310]
my=[-100,-70,-40,-10,20]
all_turtle = []
for i in range(len(colors)):
    newt  = Turtle(shape="turtle")
    newt.color(colors[i])
    newt.penup()
    newt.goto(x=-230,y=my[i])
    all_turtle.append(newt)
    

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            # print(turtle.color())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the {winning_color} turtle is winner")
            else:
                print(f"You've lost the {winning_color} turtle is winner")    
        rd = random.randint(0,10)
        turtle.forward(rd)    

# print(all_turtle)
s.exitonclick()