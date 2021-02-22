from turtle import Turtle, Screen
import random

tim = Turtle()
tom = Turtle()

tim.shape("turtle")
tim.color("blue")
tom.shape("circle")
tom.color("green")

colours_palette = ["blue","chartreuse", "magenta", "sky blue", "yellow", "black", "dodger blue"]

def draw_shape(turtle, side_num):
    angle = 360 / side_num
    for _ in range(side_num):
        turtle.right(angle)
        turtle.forward(100)

def disc_line(turtle, length):
    remainder = length % 10
    lines_num = length // 10
    for i in range(lines_num):
        if i % 2 == 0:
            turtle.up()
        else:
            turtle.down()
        turtle.forward(10)
    if turtle.isdown():
        turtle.up()
    else:
        turtle.down()
    turtle.forward(remainder)

def random_walk(turtle, length, colors = ["blue"]):
    angles = list(range(0,360,90))
    turtle.color(random.choice(colors))
    turtle.right(random.choice(angles))
    turtle.forward(length)


# for _ in range(9):
#     tim.left(30)
#     disc_line(tim, 50)
#     tim.left(150)
#     disc_line(tim, 50)
#     tim.right(100)
#
# tim.right(15)
#
#
# tim.color("red")
# for _ in range(9):
#     tim.left(30)
#     tim.forward(70)
#     tim.left(150)
#     tim.forward(70)
#     tim.right(100)
#
# for _ in range(4):
#     tom.right(90)
#     tom.forward(100)

# Draw several shapes overlaid:
# max_sides_num = 12
#
# for side_num in range(3, max_sides_num+1):
#     tim.color(colours_palette[side_num % len(colours_palette)])
#     draw_shape(tim, side_num)

# Draw a random walk:
tim.speed("fast")
tim.width(10)
for _ in range(100):
    random_walk(tim, 20, colours_palette)









screen = Screen()
screen.exitonclick()
