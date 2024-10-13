import time
from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
car_control = Car()
scoreboard = Scoreboard()

screen.setup(600, 600)
screen.bgcolor("white")
screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_control.add_cars()
    car_control.move_cars()

    # detect collision with cars
    for car in car_control.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # if player cross the road
    if player.at_finish_line():
        player.go_to_start_position()
        car_control.level_up()
        scoreboard.increase_level()

screen.exitonclick()
