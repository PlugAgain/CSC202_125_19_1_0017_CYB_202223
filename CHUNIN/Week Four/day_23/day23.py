#writing day 23 code below here

import time
from turtle import Screen
from player_23 import Player
from carmanager_23 import CarManager
from scoreboard_day23 import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_car()
    car_manager.move_car()

    if player.ycor() > 310:
        scoreboard.player_point()
        player.starting_position()
        car_manager.increase_speed()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()