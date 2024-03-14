from turtle import Turtle

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks = []
        self.create_brick()

    def create_brick(self):
        for i in range(5):
            for j in range(13):
                new_segment = Turtle("square")
                new_segment.shapesize(stretch_len=3,stretch_wid=2)
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(j*62-370, 0+(i*42))
                self.bricks.append(new_segment)