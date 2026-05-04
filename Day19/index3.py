from turtle import Turtle,Screen

t = Turtle()
s = Screen()
# s.setup(500,400)

s.setup(width=500,height=400)
scr = s.textinput(title="Make your bet",prompt="While turtle will win the race ? Enter a color: ")
t.color(scr)
print(scr)
s.exitonclick()