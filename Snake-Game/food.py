from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed(0)
        self.color("blue")
        self.refresh()

    def refresh(self) -> None:
        """Create new food piece randomly on game board"""
        self.goto(randint(-335, 335), randint(-335, 335))