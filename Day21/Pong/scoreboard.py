from turtle import Turtle

FONT_SIZE = 36
FONT_FAMILY = "Comic Sans MS"
FONT_TYPE = "bold"
ALIGNMENT = "center"

class Scoreboard():
    def __init__(self, screen_width, screen_height, color = "white", p1_name = "Player 1", p2_name = "Player 2"):
        self.screen = (screen_width, screen_height)
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.scores = Turtle()
        self.painter = Turtle()
        self.initialize_board(color = color)

    def initialize_board(self, color):
        self.scores.color(color)
        self.painter.color(color)

        self.scores.hideturtle()
        self.painter.hideturtle()

        self.scores.penup()
        self.painter.penup()

        self.painter.width(3)

        self.scores.setposition(x = 0, y =self.screen[1] // 2 - 50)

        self.scores.write("0   0", align=ALIGNMENT, font=(FONT_FAMILY, FONT_SIZE, FONT_TYPE))

        self.draw_midline()

    def update_score(self, p1_score, p2_score):
        self.scores.clear()

        self.scores.write(f"{p1_score}   {p2_score}", align=ALIGNMENT, font=(FONT_FAMILY, FONT_SIZE, FONT_TYPE))

    def draw_midline(self):
        position_start = self.screen[1] // 2 - 40
        position_end = - self.screen[1] // 2
        self.painter.setposition(x = 0, y = position_start)
        self.painter.setheading(270)

        while self.painter.ycor() > position_end:
            self.painter.pendown()
            self.painter.forward(10)
            self.painter.penup()
            self.painter.forward(10)



