from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_TYPE = "normal"

class Scoreboard(Turtle):
    def __init__(self, color = "white"):
        super().__init__()
        self.score = 0
        self.highscore = self.get_high_score_data()
        self.hideturtle()
        self.color(color)
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def reset_score(self):
        self.score = 0
        self.print_score()

    def print_score(self):
        score_text = f"Score: {self.score}   High score: {self.highscore}"
        self.setposition(0, 270)
        self.clear()
        self.write(score_text, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.setposition(0,0)
        game_over_text = "Game Over!"
        restart_text = "Press any key to play again!"
        self.write(game_over_text, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
        self.setposition(0, -20)
        self.write(restart_text, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
        if self.score > self.highscore:
            self.highscore = self.score
            self.store_high_score()
            self.print_score()

    def startup_message(self):
        self.setposition(0, 0)
        startup_text = "Press any key to start the game"
        self.write(startup_text, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def get_high_score_data(self):
        with open("data.txt", mode="r") as file:
            content = file.read()
            if content:
                return int(content)
            else:
                return 0

    def store_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")