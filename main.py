from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(ball.speed)
    screen.update()

    # cause ball to bounce after collision with top or bottom of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # cause ball to bounce after collisin with either paddle
    if ball.distance(r_paddle) < 45 and ball.xcor() > 320 or ball.distance(l_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()

    # cause ball to respawn and add score after it hit either end of screen
    if ball.xcor() > 360 or ball.xcor() < -360:
        scoreboard.update_left()
        ball.respawn()



screen.exitonclick()