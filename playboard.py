from turtle import Turtle

class PlayBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def go_left(self):
        if self.xcor() > -350:
            new_x = self.xcor() - 25
            self.goto(new_x,self.ycor())

    def go_right(self):
        if self.xcor() < 350:
            new_x = self.xcor() + 25
            self.goto(new_x,self.ycor())