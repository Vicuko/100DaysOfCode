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
ball = Ball(color="green", speed = 10)

def ball_wall_collision():
    ball_x = ball.xcor()
    ball_y = ball.ycor()

    if ball_x >= screen_width // 2 - 20:
        print ("Player 1 scores!!")
    elif ball_x <= - screen_width // 2 + 20:
        print("Player 2 scores!!")
    elif ball_y >= screen_height // 2 - 20:
        ball.bounce(side="top")
    elif ball_y <= -screen_height // 2 + 20:
        ball.bounce(side="bottom")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # TODO 5. Detect collision with the wall and bounce
    ball_wall_collision()


    # TODO 6. Detect collision with paddle
    # TODO 7. Detect when paddle misses
    # TODO 8. Keep Score

screen.exitonclick()