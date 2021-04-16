from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong")
s.tracer(0)

ball = Ball()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
scoreboard = Scoreboard()
# p = Paddle(282,250)

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")

s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.collide_wall()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.collide_paddle()

    # Detects if the right paddle missies the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detects if the left paddle missies the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # check the winner and stops the game
    if scoreboard.l_score == 5:
        game_is_on = False
        scoreboard.winner("Left")
    if scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.winner("Right")

s.exitonclick()
