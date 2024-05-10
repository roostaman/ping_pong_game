import turtle as t


class Paddle(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        y = self.ycor()
        y += 25
        self.sety(y)

    def go_down(self):
        y = self.ycor()
        y -= 25
        self.sety(y)
