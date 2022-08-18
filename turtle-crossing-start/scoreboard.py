from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(-230,270)
        self.write(f"Level:{self.score} ", align= "center", font= FONT)
        self.hideturtle()

    def level_up(self):
        self.clear()
        self.score += 1
        self.write(f"Level:{self.score} ", align= "center", font= FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER ", align= "center", font= FONT)
