from turtle import Turtle

FONT_SIZE = 24
FONT_FAMILY = "Arial"
FONT_TYPE = "bold"
ALIGNMENT = "center"

class Scoreboard():
    def __init__(self, screen_width, screen_height, color = "white", p1_name = "Player 1", p2_name = "Player 2"):
        self.screen = (screen_width, screen_height)
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.score_1 = Turtle()
        self.score_2 = Turtle()
        self.painter = Turtle()
        self.initialize_board(color = color)

    def initialize_board(self, color):
        self.score_1.color(color)
        self.score_2.color(color)
        self.painter.color(color)

        self.score_1.hideturtle()
        self.score_2.hideturtle()
        self.painter.hideturtle()

        self.score_1.penup()
        self.score_2.penup()
        self.painter.penup()

        self.painter.width(3)

        self.score_1.setposition(self.screen[0] // 2 - 40, self.screen[1] - 20)
        self.score_2.setposition(self.screen[0] // 2 + 40, self.screen[1] - 20)

        self.score_1.write("0", align=ALIGNMENT, font=(FONT_FAMILY, FONT_SIZE, FONT_TYPE))
        self.score_2.write("0", align=ALIGNMENT, font=(FONT_FAMILY, FONT_SIZE, FONT_TYPE))

        self.draw_midline()

    def update_score(self, p1_score, p2_score):
        self.score_1.clear()
        self.score_2.clear()

        self.score_1.write(f"{p1_score}", align=ALIGNMENT, font=(FONT_FAMILY, FONT_SIZE, FONT_TYPE))
        self.score_2.write(f"{p2_score}", align=ALIGNMENT, font=(FONT_FAMILY, FONT_SIZE, FONT_TYPE))


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



