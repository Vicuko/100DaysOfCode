from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, color="red"):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        random_heading = random.choice([random.randint(10, 170), random.randint(190, 350)])
        self.setheading(random_heading)

    def move(self):
        self.forward(5)

    def bounce(self, side):
        random_trajectory_mod = random.randint(-5, 5)
        if side == "right":
            heading_difference = 180 - self.heading()

        elif side == "top":
            heading_difference = 90 - self.heading()

        elif side == "left":
            heading_difference = 360 - self.heading()

        elif side == "bottom":
            heading_difference = 270 - self.heading()

        new_heading = (self.heading() + 180) % 360 + heading_difference * 2

        if side == "right" or side == "left":
            new_heading += (random_trajectory_mod) % 360
        else:
            new_heading %= 360

        self.setheading(new_heading)

    def restart(self):
        self.setposition(0, 0)
        random_heading = random.randint(0, 359)
        self.setheading(random_heading)
