import turtle as t

class Snake:
    def __init__(self, initial_size = 3, body_size = 20, body_shape = "square", color = "white"):
        self.body = []
        self.init_size = initial_size
        self.body_size = body_size
        self.body_shape = body_shape
        self.snake_color = color
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in range(self.init_size):
            position_x = -position * self.body_size
            self.add_segment(position_x)

    def add_segment(self, position_x, position_y=0):
        body_part = t.Turtle(self.body_shape)
        body_part.color(self.snake_color)
        body_part.penup()
        body_part.setpos(x = position_x, y = position_y)
        self.body.append(body_part)

        counter = 0
        for segment in self.body:
            print (f"Coutner: {counter}\n")
            print(segment.position())
            counter += 1

    def extend(self):
        tail_pos = self.body[-1].position()
        self.add_segment(tail_pos[0], tail_pos[1])

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            this_body_part = self.body[i]
            next_body_part = self.body[i - 1]
            next_position = next_body_part.position()
            this_body_part.goto(next_position)
        self.head.forward(self.body_size)

    def move_up(self):
        self.change_direction(90)

    def move_down(self):
        self.change_direction(270)

    def move_right(self):
        self.change_direction(0)

    def move_left(self):
        self.change_direction(180)

    def change_direction(self, new_direction):
        # We make sure the snake doesnt' go backwards:
        if abs(self.head.heading() - new_direction) != 180:
            print(new_direction)
            self.head.setheading(new_direction)
        else:
            print ("New_direction not possible! Can't go backwards...")
