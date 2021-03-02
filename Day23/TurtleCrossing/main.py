import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move_forward, key="Up")
game_level = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.finished():
        player.restart()
        game_level += 1
        scoreboard.level_update(game_level)

