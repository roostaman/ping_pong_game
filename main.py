import turtle as t
from paddle import Paddle
from scoreboard import Scoreboard, Divider
from ball import Ball
# import time

my_screen = t.Screen()
my_screen.setup(width=800, height=460)
my_screen.bgcolor("black")
my_screen.title("Epic Ping Pong :)")
my_screen.tracer(0)

my_paddle_left = Paddle((-370, 0))
my_paddle_right = Paddle((370, 0))
my_ball = Ball()
my_scoreboard_l = Scoreboard((-40, 200))
my_scoreboard_r = Scoreboard((40, 200))
my_divider = Divider()

my_screen.update()

my_screen.listen()
my_screen.onkey(fun=my_paddle_right.go_up, key='Up')
my_screen.onkey(fun=my_paddle_right.go_down, key='Down')
my_screen.onkey(fun=my_paddle_left.go_up, key='w')
my_screen.onkey(fun=my_paddle_left.go_down, key='s')

game_on = True

while game_on:
    my_screen.update()
    my_ball.move()

    # Collision with wall checking
    if my_ball.ycor() > 210 or my_ball.ycor() < -210:
        my_ball.bounce_y()

    # Collision with paddle checking
    if ((my_ball.distance(my_paddle_right) < 60 and my_ball.xcor() > 350)
            or (my_ball.distance(my_paddle_left) < 60 and my_ball.xcor() < -350)):
        my_ball.bounce_x()

    # Reset ball position if it goes out of bounds, first r second l
    if my_ball.xcor() > 390:
        my_ball.reset_pos()
        my_scoreboard_r.add_point()

    if my_ball.xcor() < -390:
        my_ball.reset_pos()
        my_scoreboard_l.add_point()

my_screen.exitonclick()
