from turtle import Turtle , Screen
import time
Starting_position = [(0,0),(-20,0),(-40,0)]
segments=[]
move_distance = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for position in Starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)
                