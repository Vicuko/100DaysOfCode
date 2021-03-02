from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, level=1):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(-280, 260)
        self.level = level
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write(f"Game over!", align="center", font=FONT)
