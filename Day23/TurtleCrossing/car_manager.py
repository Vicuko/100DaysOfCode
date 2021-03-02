from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.traffic = []
        self.create_traffic()

    def create_traffic(self):
        for _ in range(30):
            car = Car(color=random.choice(COLORS))
            self.traffic.append(car)

    def move_traffic(self, level=0):
        move_distance = STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT * 0.5
        for car in self.traffic:
            car.move(move_distance)
            if car.xcor() <= -300:
                car.reset_position(color=random.choice(COLORS))


