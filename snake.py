#  Copyright (c)  Purushotham Koduri

from turtle import Turtle,Screen
import random

my_positions = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
my_colors = ['violet', 'red', 'indigo', 'blue', 'green', 'yellow', 'orange', 'coral']

class Snake:

    def __init__(self):
        self.turtle_objects = []
        self.create_snake()
        self.head = self.turtle_objects[0]

    def create_snake(self):
        for position in my_positions:
            self.add_segment(position)

    def add_segment(self,position):
        turtle = Turtle("square")
        turtle.color(random.choice(my_colors))
        turtle.penup()
        turtle.goto(position)
        self.turtle_objects.append(turtle)

    def extend(self):
        self.add_segment(self.turtle_objects[-1].position())


    def move(self):
        for segment in range(len(self.turtle_objects)-1, 0, -1):
            new_x = self.turtle_objects[segment-1].xcor()
            new_y= self.turtle_objects[segment-1].ycor()
            self.turtle_objects[segment].goto(new_x, new_y)
        self.turtle_objects[0].forward(DISTANCE)

    def move_right(self):
        if self.turtle_objects[0].heading() != LEFT:
            self.turtle_objects[0].setheading(RIGHT)

    def move_left(self):
        if self.turtle_objects[0].heading() != RIGHT:
            self.turtle_objects[0].setheading(LEFT)

    def move_up(self):
        if self.turtle_objects[0].heading() != DOWN:
            self.turtle_objects[0].setheading(UP)

    def move_down(self):
        if self.turtle_objects[0].heading() != UP:
            self.turtle_objects[0].setheading(DOWN)



    def reset(self):
        for seg in self.turtle_objects:
            seg.goto(1000,1000)
        self.turtle_objects.clear()
        self.create_snake()
        self.head= self.turtle_objects[0]



