from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.speed(0)
        self.goto(0, 320)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """Updating Score Board"""
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        """Increasing Score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self) -> None:
        """Print out Game Over"""
        self.home()
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)