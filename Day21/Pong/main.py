from turtle import Screen
from paddle import Paddle
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

#TODO 2. Create and move a paddle
#Prompt user for player name
screen_height = screen.window_height()
print ("Screen height: ", screen_height)
player1 = Paddle(screen_height = screen_height)
player2 = Paddle(screen_height = screen_height)

screen.onkey(fun=player1.move_up, key="w")
screen.onkey(fun=player1.move_down, key="s")
screen.onkey(fun=player2.move_up, key="Up")
screen.onkey(fun=player2.move_down, key="Down")

#TODO 3. Create another paddle
#TODO 4. Create the ball and make it move
#TODO 5. Detect collision with the wall and bounce
#TODO 6. Detect collision with paddle
#TODO 7. Detect when paddle misses
#TODO 8. Keep Score

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    #ball.move()



screen.exitonclick()