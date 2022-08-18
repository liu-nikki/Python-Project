import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
trafic = CarManager()

screen.listen()
screen.onkey(turtle.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()  
    trafic.create_cars() 
    trafic.move()
    if turtle.ycor() > 280:
        scoreboard.level_up()
        turtle.reset_position()
        trafic.speed_up()
    
    for i in trafic.car:
        if turtle.distance(i) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
    
    
    
