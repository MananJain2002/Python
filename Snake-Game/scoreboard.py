from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.penup()
        self.speed(0)
        self.goto(0, 320)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """Updating Score Board"""
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        """Increasing Score"""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.score))
        self.score = 0
        self.update_scoreboard()