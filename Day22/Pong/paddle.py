from turtle import Turtle


class Paddle:

    def __init__(self, screen_height, screen_width, color="white", length=4):
        self.body = []
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.create_paddle(length, color)
        self.score = 0

    def create_paddle(self, length, color):
        head_pos = (length * 20) // 2 - 10

        for index in range(length):
            new_part = Turtle(shape="square")
            new_part.color(color)
            new_part.penup()
            new_part.setpos(x=0, y=head_pos - 20 * index)
            self.body.append(new_part)

    def move_up(self):
        highest_part_y = self.body[0].ycor()
        if highest_part_y + 20 < self.screen_height / 2:

            for part in self.body:
                part_x = part.xcor()
                part_y = part.ycor()
                part.setposition(part_x, part_y + 20)

    def move_down(self):
        lowest_part_y = self.body[-1].ycor()
        if lowest_part_y - 20 >= -(self.screen_height / 2):

            for part in self.body:
                part_x = part.xcor()
                part_y = part.ycor()
                part.setposition(part_x, part_y - 20)

    def set_side(self, side):
        left_pos = - self.screen_width // 2 + 30

        right_pos = self.screen_width // 2 - 40

        if side == "left":
            for part in self.body:
                part.setx(left_pos)
        elif side == "right":
            for part in self.body:
                part.setx(right_pos)
