#PING PONG GAME

import turtle
import winsound

wn = turtle.Screen()
wn.title("Ping Pong by Ammar Taha")
wn.bgcolor("light blue")
wn.setup(width=800, height=600)
wn.tracer(0)
#SCORE
score_1 = 0
score_2 = 0
#PADDLE 1
Paddle_1 = turtle.Turtle()
Paddle_1.speed(0)
Paddle_1.shape("square")
Paddle_1.color("brown")
Paddle_1.shapesize(stretch_wid=5, stretch_len=0.5)
Paddle_1.penup()
Paddle_1.goto(-350, 0)
#PADDLE 2
Paddle_2 = turtle.Turtle()
Paddle_2.speed(0)
Paddle_2.shape("square")
Paddle_2.color("green")
Paddle_2.shapesize(stretch_wid=5, stretch_len=0.5)
Paddle_2.penup()
Paddle_2.goto(350, 0)
#BALL
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("grey")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.4
Ball.dy = -0.4
#PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1= 0          Player 2= 0", align="center", font=("Courier", 24, "normal"))
#FUNCTIONS
def Paddle_1_up():
    y = Paddle_1.ycor()
    y +=20
    Paddle_1.sety(y)

def Paddle_1_down():
    y = Paddle_1.ycor()
    y -=20
    Paddle_1.sety(y)


def Paddle_2_up():
    y = Paddle_2.ycor()
    y +=20
    Paddle_2.sety(y)

def Paddle_2_down():
    y = Paddle_2.ycor()
    y -=20
    Paddle_2.sety(y)
#KEYBOARD BINDING
wn.listen()
wn.onkeypress(Paddle_1_up, "w")
wn.onkeypress(Paddle_1_down, "s")
wn.onkeypress(Paddle_2_up, "Up")
wn.onkeypress(Paddle_2_down, "Down")
# MAIN LOOP
while True:
    wn.update()
    #BALL MOVEMENT
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)
    #BORDERS
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1= {}          Player 2= {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1= {}          Player 2= {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
    #BALL COLLISION WITH PADDELS
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < Paddle_2.ycor() + 40 and Ball.ycor() > Paddle_2.ycor() -40):
        Ball.setx(340)
        Ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < Paddle_1.ycor() + 40 and Ball.ycor() > Paddle_1.ycor() -40):
        Ball.setx(-340)
        Ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
