from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
import time

screen = Screen()
 
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
game = True


while game:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
     
    #detect car collision with the car
    for random_car in car.all_cars:
        if random_car.distance(player) < 20:
            game = False
            scoreboard.game_over()

    #detect player finish the game and level up
    if player.finish_game():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_score()

screen.exitonclick() 