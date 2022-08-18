from turtle import Turtle
import random

class Paddle(Turtle):
    def __init__(self,position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)

    def go_up(self):
        y = self.ycor() + 25
        self.goto(self.xcor(),y)

        
    def go_down(self):
        y = self.ycor() - 25
        self.goto(self.xcor(),y)

MOVE_SPEED =(10, 15, 20,-10, -15, -20)

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        #self.shapesize(2,2)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.1
    
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.movespeed *= 0.9
    
    def reset_game(self):
        self.goto(0, 0)
        self.movespeed = 0.1
        self.bounce_x()

class Scorboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_scoreboard()
    
    def show_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align= "center", font=("Counrier",80,"normal"))
        self.goto(100, 200)
        self.write(self.r_score, align= "center", font=("Counrier",80,"normal"))

    def l_point(self):
        self.l_score += 1
        self.show_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.show_scoreboard()


        

       