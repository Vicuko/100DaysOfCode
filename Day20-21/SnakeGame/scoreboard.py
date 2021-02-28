from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_TYPE = "normal"

class Scoreboard(Turtle):
    def __init__(self, color = "white"):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(color)
        self.setposition(0, 270)
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def reset_score(self):
        self.socre = 0
        self.print_score()

    def print_score(self):
        score_text = f"Score: {self.score}"
        self.clear()
        self.write(score_text, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.setposition(0,0)
        game_over_text = "Game Over!"
        self.write(game_over_text, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))