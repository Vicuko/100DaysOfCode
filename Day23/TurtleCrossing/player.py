from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, color="green", shape="turtle"):
        super().__init__(shape=shape)
        self.color(color)
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        self.level = 0

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE_Y:
            self.restart()
            self.level += 1

    def restart(self):
        self.setposition(STARTING_POSITION)
