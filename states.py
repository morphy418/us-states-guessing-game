from turtle import Turtle

FONT = ("Arial", 10, "normal")

class States(Turtle):
    def __init__(self, coor, name):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(coor)
        self.write(name, align="center", font=FONT)
