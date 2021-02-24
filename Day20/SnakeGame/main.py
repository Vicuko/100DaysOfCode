import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(n=0)

# Create a snake body
# The body initially consists of 3 turtles
snake = []
initial_snake_size = 3
turtle_size = 20
for i in range(initial_snake_size):
    new_turtle = t.Turtle("square")
    new_turtle.color("white")
    new_turtle.speed("slowest")
    new_turtle.penup()
    new_turtle.setpos(x= -i * turtle_size, y=0)
    snake.append(new_turtle)

game_on = True
snake_head = snake[0]
while game_on:
    screen.update()
    time.sleep(0.5)
    for i in range(len(snake)-1,0, -1):
        this_turtle = snake[i]
        next_turtle = snake[i-1]
        next_position = next_turtle.position()
        this_turtle.goto(next_position)
    snake_head.forward(turtle_size)
screen.exitonclick()