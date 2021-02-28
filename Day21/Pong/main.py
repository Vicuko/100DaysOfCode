from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

GAME_NAME = "TURBO PONG"
BACKGROUND_COLOR = "BLACK"
#TODO 1. Create Screen - Done
screen = Screen()
screen.title(GAME_NAME)
screen.setup(height=1.0, width=1.0)
screen.bgcolor(BACKGROUND_COLOR)
screen.tracer(n=0)
screen.listen()

#TODO 2. Create and move a paddle - Done
#TODO 3. Create another paddle - Done
#Prompt user for player name
screen_height = screen.window_height()
screen_width = screen.window_width()
player1 = Paddle(screen_height = screen_height, screen_width = screen_width)
player2 = Paddle(screen_height = screen_height, screen_width = screen_width)

player1.set_side(side="left")
player2.set_side(side="right")

screen.onkey(fun=player1.move_up, key="w")
screen.onkey(fun=player1.move_down, key="s")
screen.onkey(fun=player2.move_up, key="Up")
screen.onkey(fun=player2.move_down, key="Down")

#TODO 4. Create the ball and make it move - Done
ball = Ball(color="green")

def ball_wall_collision():
    ball_x = ball.xcor()
    ball_y = ball.ycor()

    if ball_y >= screen_height // 2 - 20:
        ball.bounce(side="top")
    elif ball_y <= -screen_height // 2 + 20:
        ball.bounce(side="bottom")

def ball_paddle_collision():
    for part in player1.body:
        part_x = part.xcor()
        if ball.distance(part) <= 20 and part_x < ball.xcor():
            ball.bounce("left")

    for part in player2.body:
        part_x = part.xcor()
        if ball.distance(part) <= 20 and part_x > ball.xcor():
            ball.bounce("right")

def point_score():
    score = False

    if player1.body[0].xcor() > ball.xcor():
        player2.score += 1
        score = True

    elif player2.body[0].xcor() < ball.xcor():
        player1.score += 1
        score = True

    return score

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # TODO 5. Detect collision with the wall and bounce - Done
    ball_wall_collision()
    # TODO 6. Detect collision with paddle - Done
    ball_paddle_collision()
    # TODO 7. Detect when paddle misses
    if point_score():
    # TODO 8. Keep Score
        ball.restart()
        scoreboard.update()

screen.exitonclick()