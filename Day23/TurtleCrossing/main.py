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
car_manager = CarManager()

screen.onkey(player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Check if player has reached the finish line
    if player.finished():
        player.restart()
        scoreboard.level += 1
        scoreboard.show_level()

    # Move traffic
    car_manager.move_traffic(scoreboard.level)
