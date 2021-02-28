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
    time.sleep(0.1)
    snake.move()

    #Detect collision between snake and food
    if snake.head.distance(food) <= 5:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        print ("Ñam ñam")

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

screen.exitonclick()