from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.car = []
        self.create_cars() 
        self.carspeed = STARTING_MOVE_DISTANCE
    
    def create_cars(self):
        randomnumber = random.randint(1,6)
        if randomnumber == 5 or randomnumber == 3:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.car.append(new_car)

    def move(self):
        for new_car in self.car:
            new_car.backward(self.carspeed)
    
    def speed_up(self):
        self.carspeed += MOVE_INCREMENT
