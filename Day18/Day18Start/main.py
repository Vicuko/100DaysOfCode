from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()

tim.shape("turtle")
tim.color("blue")
tom.shape("circle")
tom.color("green")

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

for _ in range(9):
    tim.left(30)
    disc_line(tim, 50)
    tim.left(150)
    disc_line(tim, 50)
    tim.right(100)

tim.color("red")
for _ in range(9):
    tim.left(30)
    tim.forward(70)
    tim.left(150)
    tim.forward(70)
    tim.right(100)

for _ in range(4):
    tom.right(90)
    tom.forward(100)










screen = Screen()
screen.exitonclick()
