from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

GAME_NAME = "TURBO PONG"
BACKGROUND_COLOR = "BLACK"

# TODO 1. Create Screen - Done
screen = Screen()
screen.title(GAME_NAME)
screen.setup(height=1.0, width=1.0)
screen.bgcolor(BACKGROUND_COLOR)
screen.tracer(n=0)
screen.listen()

# TODO 2. Create and move a paddle - Done
# TODO 3. Create another paddle - Done
# Prompt user for player name
screen_height = screen.window_height()
screen_width = screen.window_width()
player1 = Paddle(screen_height=screen_height, screen_width=screen_width)
player2 = Paddle(screen_height=screen_height, screen_width=screen_width)

# TODO 4. Create the ball and make it move - Done
ball = Ball(color="green")
scoreboard = Scoreboard(screen_width=screen_width, screen_height=screen_height)

player1.set_side(side="left")
player2.set_side(side="right")

screen.onkey(fun=player1.move_up, key="w")
screen.onkey(fun=player1.move_down, key="s")
screen.onkey(fun=player2.move_up, key="Up")
screen.onkey(fun=player2.move_down, key="Down")


def ball_wall_collision():
    ball_y = ball.ycor()

    if ball_y >= screen_height // 2 - 20:
        ball.bounce(side="top")
    elif ball_y <= -screen_height // 2 + 20:
        ball.bounce(side="bottom")


def ball_paddle_collision():

    if  ball.distance(player1) <= (player1.body_length // 2):
        if 15 > abs(player1.xcor() - ball.xcor()) >= 10:
            ball.bounce("left")

    elif  ball.distance(player2) <= (player2.body_length // 2):
        if 15 > abs(player2.xcor() - ball.xcor()) >= 10:
            ball.bounce("right")

def point_score():
    score = False

    if player1.xcor() - 10 > ball.xcor():
        player2.score += 1
        score = True

    elif player2.xcor() + 10 < ball.xcor():
        player1.score += 1
        score = True

    return score

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # TODO 5. Detect collision with the wall and bounce - Done
    ball_wall_collision()
    # TODO 6. Detect collision with paddle - Done
    ball_paddle_collision()
    # TODO 7. Detect when paddle misses - Done
    if point_score():
        # TODO 8. Keep Score - Done
        ball.restart()
        scoreboard.update_score(player1.score, player2.score)

screen.exitonclick()
