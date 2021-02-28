import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(n=0)
screen.listen()
scoreboard = Scoreboard()

def clear_all():
    t.clearscreen()
    screen.bgcolor("black")
    screen.tracer(n=0)

def reset_keys():
    screen.onkey(fun=None, key=None)
    screen.onkey(fun=None, key="Up")
    screen.onkey(fun=None, key="Down")
    screen.onkey(fun=None, key="Right")
    screen.onkey(fun=None, key="Left")

def game():
    clear_all()
    # Reset onkey events:
    reset_keys()
    snake = Snake(color="yellow")
    food = Food(color="red")
    scoreboard = Scoreboard()

    screen.onkey(fun=snake.move_up, key="Up")
    screen.onkey(fun=snake.move_down, key="Down")
    screen.onkey(fun=snake.move_right, key="Right")
    screen.onkey(fun=snake.move_left, key="Left")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.08)
        snake.move()

        #Detect collision between snake and food
        if snake.head.distance(food) <= 5:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #Detect collision with walls
        highest_cor = max(abs(snake.head.xcor()), abs(snake.head.ycor()))
        if highest_cor > 290:
            scoreboard.game_over()
            game_on = False

        #Detect collision with tail
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()

    reset_keys()
    screen.onkey(fun=game, key="")

scoreboard.startup_message()
screen.onkey(fun=game, key="")

screen.exitonclick()