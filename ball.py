from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.1
        self.the_start_position()

    def the_start_position(self):
        self.goto(0, -200)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bound_brick_y(self):
        self.y_move *= -1

    def bound_wall(self):
        self.x_move *= -1


