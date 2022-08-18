import random
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

class Snake:
    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        starting_position = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_position:
            self.add_segment(position)
            
    def add_segment(self,position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.snake.append(t)
    
    def extend(self):
        self.add_segment(self.snake[-1].position())
    

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            x = self.snake[i-1].xcor()
            y = self.snake[i-1].ycor()
            self.snake[i].goto(x,y)
        self.head.forward(20)
    
    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
    
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("SnakeGame/data.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score} Highest Score:{self.highest_score}", align= "center", font=("Arial",24,"normal"))
        self.hideturtle()
    
    def reset_game(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("SnakeGame/data.txt",mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.clear()
        self.write(f"Score:{self.score} Highest Score:{self.highest_score}", align= "center", font=("Arial",24,"normal"))
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER ", align= "center", font=("Arial",24,"normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score} Highest Score:{self.highest_score}", align= "center", font=("Arial",24,"normal"))


        
s = Snake()
f = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.left,"Left")
screen.onkey(s.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    s.move()   

    #Detect collision with food.     
    if s.head.distance(f) < 15:
        f.refresh()
        s.extend()
        scoreboard.increase_score()
    
    #Detect collision with wall.
    if s.head.xcor() > 290 or s.head.xcor() < -290 or s.head.ycor() > 290 or s.head.ycor() < -290:
        scoreboard.reset_game()
        s.reset()
    
    #Detect collision with tail.
    for segment in s.snake[1:]:
        if s.head.distance(segment) < 10:
            scoreboard.reset_game()
            s.reset()
        

screen.exitonclick()