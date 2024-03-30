from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor: int) -> None:
        super().__init__("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_cor, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
    
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)