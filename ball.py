from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + + self.ymove
        self.goto(new_x , new_y)

    def collide_wall(self):
        self.ymove *= -1

    def collide_paddle(self):
        self.xmove *= -1
        self.speed()
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.collide_paddle()
        self.move_speed = 0.1




