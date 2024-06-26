from turtle import Turtle
import random

COLORS = ["red", "green", "yellow", "blue", "orange", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car():

    def __init__(self):
         self.all_cars = []
         self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
                car.backward(self.car_speed)

    def level_up(self):
         self.car_speed += MOVE_INCREMENT            
        

