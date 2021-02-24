import turtle as t
from snake import Snake
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(n=0)

snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.5)
    snake.move()

screen.exitonclick()