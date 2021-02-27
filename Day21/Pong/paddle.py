from turtle import Turtle

class Paddle:

    def __init__(self, color = "white", length=4):
        self.body = []
        self.create_paddle(length, color)

    def create_paddle(self, length, color):
        head_pos = (length * 20) // 2 - 10
        for index in range (length):
            new_part = Turtle(shape="square")
            new_part.color(color)
            new_part.penup()
            new_part.setpos(x = 0, y = head_pos - 20 * index)