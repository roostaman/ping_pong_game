import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.goto(0, 0)
        self.dx = 4
        self.dy = 4

    def move(self):
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
