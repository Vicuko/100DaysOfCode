from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
for _ in range(10):
    timmy_the_turtle.left(30)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(150)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.right(100)

timmy_the_turtle.color("red")
for _ in range(10):
    timmy_the_turtle.left(30)
    timmy_the_turtle.forward(70)
    timmy_the_turtle.left(150)
    timmy_the_turtle.forward(70)
    timmy_the_turtle.right(100)
















screen = Screen()
screen.exitonclick()