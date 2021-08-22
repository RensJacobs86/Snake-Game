from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 260)
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def point_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


