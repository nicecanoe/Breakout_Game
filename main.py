import turtle
from turtle import Turtle
from playboard import PlayBoard
from bricks import Brick
import time
from scoreboard import ScoreBoard
from ball import Ball
from tkinter import messagebox




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
    i= 0
    for brick in bricks.bricks:
        i += 1
        if -28 < brick.ycor() - ball.ycor() < 28 and -30 < brick.xcor() - ball.xcor() < 30:
            ball.bound_brick_y()
            brick.goto(600,0)
            scoreboard.score += 1
            scoreboard.refresh()
        if -20 < brick.ycor() - ball.ycor() < 20 and -40 < brick.xcor() - ball.xcor() < 40:
            ball.bound_wall()
            brick.goto(600, 0)
            scoreboard.score += 1
            scoreboard.refresh()

    if ball.xcor() < - 387 or ball.xcor() > 387:
        ball.bound_wall()
    if ball.distance(player) < 58 and -270 < ball.ycor() < -250:
        ball.bound_brick_y()
    if ball.ycor() > 287:
        ball.bound_brick_y()
    if ball.ycor() < -270:
        messagebox.showwarning("Game Over", "YOU ARE DEAD!")
        if messagebox.askyesno("Game", "Would you like to play again?"):
            ball.the_start_position()
            player = PlayBoard((0, -270))
            scoreboard.time = scoreboard.time + 1
            scoreboard.refresh()
        else:
            game_is_on = False




screen.mainloop()