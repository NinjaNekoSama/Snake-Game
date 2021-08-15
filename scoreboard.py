#  Copyright (c)  Purushotham Koduri
from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.color("blue4")
        with open("data.txt") as file:
            self.high_score = int(file.read())
            print(self.high_score)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score Board: {self.counter} High score: {self.high_score} ", move=False, align="center", font=("Arial", 20, "normal"))



    def refresh_score(self):
        self.clear()
        self.write(f"Score Board: {self.counter}  High score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        pass

    def reset(self):
        if self.counter > int(self.high_score):
            self.high_score = self.counter
        with open("data.txt", mode='w') as file:
            file.write(str(self.high_score))

        self.counter = 0
        self.refresh_score()