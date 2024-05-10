import turtle as t

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(position)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_score()


class Divider(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, -220)
        self.pendown()
        self.setheading(90)
        self.draw_spaced()

    def draw_spaced(self):
        for i in range(23):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
