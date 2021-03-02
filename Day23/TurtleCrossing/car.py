from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self, color = "blue"):
        super().__init__(shape="square")
        self.setheading(180)
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.init_position()

    def init_position(self):
        random_y = random.randint(-240, 260)
        random_x = random.randint(-290, 290)
        self.setposition(x=random_x, y=random_y)

    def reset_position(self, color):
        random_y = random.randint(-240, 260)
        new_x = 310
        self.color(color)
        self.setposition(x=new_x, y=random_y)

    def move(self, distance):
        self.forward(distance)
