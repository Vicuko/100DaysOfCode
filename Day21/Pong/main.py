from turtle import Screen
from paddle import Paddle

GAME_NAME = "TURBO PONG"
BACKGROUND_COLOR = "BLACK"
#TODO 1. Create Screen - Done
screen = Screen()
screen.title(GAME_NAME)
screen.setup(height=1.0, width=1.0)
screen.bgcolor(BACKGROUND_COLOR)
screen.listen()

#TODO 2. Create and move a paddle
player1 = Paddle()
player2 = Paddle()
#TODO 3. Create another paddle
#TODO 4. Create the ball and make it move
#TODO 5. Detect collision with the wall and bounce
#TODO 6. Detect collision with paddle
#TODO 7. Detect when paddle misses
#TODO 8. Keep Score




screen.exitonclick()