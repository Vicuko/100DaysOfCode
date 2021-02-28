from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, screen_height, screen_width, color="white", stretch=5):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.body_length = stretch * 20
        self.shapesize(stretch_wid = stretch, stretch_len=1)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.score = 0

    def move_up(self):
        if (self.ycor() + self.body_length // 2 + 20) < self.screen_height / 2:
            self.setposition(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if (self.ycor() - self.body_length // 2 - 20) > -self.screen_height / 2:
            self.setposition(self.xcor(), self.ycor() - 20)

    def set_side(self, side):
        left_pos = - self.screen_width // 2 + 30
        right_pos = self.screen_width // 2 - 40

        if side == "left":
            self.setx(left_pos)

        elif side == "right":
            self.setx(right_pos)
