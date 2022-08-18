from turtle import Turtle, Screen
from PongGame.Paddle import Paddle, Ball, Scorboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))
scoreboard = Scorboard()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_on = True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 40 and ball.xcor() > 340 or ball.distance(l_paddle) < 40 and ball.xcor() > -380:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.reset_game()
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.reset_game()
        scoreboard.r_point()




screen.exitonclick()