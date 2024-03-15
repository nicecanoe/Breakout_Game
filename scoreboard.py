from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.time = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-0,250)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"the score: {self.score} the time you try: {self.time}", False, 'center', ('Arial', 24, 'normal'))