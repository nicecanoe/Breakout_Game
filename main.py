import turtle
from turtle import Turtle
from playboard import PlayBoard
from bricks import Brick
import time
from scoreboard import ScoreBoard
from ball import Ball




screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("BreakOut Game")
screen.bgcolor("black")
screen.tracer(0)

bricks = Brick()
player = PlayBoard((0,-270))
scoreboard = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkey(player.go_left,"Left")
screen.onkey(player.go_right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.001)
    ball.move()

screen.mainloop()