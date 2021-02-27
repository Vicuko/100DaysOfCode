from turtle import Turtle

class Paddle:

    def __init__(self, screen_height, color = "white", length=4):
        self.body = []
        self.screen_height = screen_height
        self.create_paddle(length, color)

    def create_paddle(self, length, color):
        head_pos = (length * 20) // 2 - 10
        print(f"Head pos: {head_pos}")
        for index in range (length):
            new_part = Turtle(shape="square")
            new_part.color(color)
            new_part.penup()
            new_part.setpos(x = 0, y = head_pos - 20 * index)
            self.body.append(new_part)

    def move_up(self):
        highest_part_y = self.body[0].ycor()
        if highest_part_y + 20 < self.screen_height/2:
            print(highest_part_y - 20)
            for part in self.body:
                part_x = part.xcor()
                part_y = part.ycor()
                part.goto(part_x, part_y + 20)

    def move_down(self):
        lowest_part_y = self.body[-1].ycor()
        if lowest_part_y - 20 >= -(self.screen_height/2):
            print(lowest_part_y - 20)
            for part in self.body:
                part_x = part.xcor()
                part_y = part.ycor()
                part.goto(part_x, part_y - 20)