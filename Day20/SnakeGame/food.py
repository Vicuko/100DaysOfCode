from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, shape="circle", color="blue", speed = "fastest", height=10, width=10):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.shapesize(stretch_len=height/20, stretch_wid=width/20)
        self.color(color)
        self.speed(speed)
        possible_coords = list(range(-280, 280, 20))
        random_x = random.choice(possible_coords)
        random_y = random.choice(possible_coords)
        self.setposition(random_x, random_y)
