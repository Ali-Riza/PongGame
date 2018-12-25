# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech
# Part 7: Sound

import turtle
from playsound import playsound
import winsound
import pygame
import random
import tkinter
import time
import turtle as tr

Backgroundmusic = ['C:\PythonScripts\pingpong\Audios\A.mp3', 'C:\PythonScripts\pingpong\Audios\B.mp3', 'C:\PythonScripts\pingpong\Audios\C.mp3' , 'C:\PythonScripts\pingpong\Audios\D.mp3']


wn = turtle.Screen()
wn.title("Spiel: Pingpong")
wn.tracer(0)
wn.bgcolor("#484848")
playsound("C:\PythonScripts\HorrorStimme.wav")
wn.setup(width=1.0, height=1.0, startx=None, starty=None)
wn.bgpic("C:\PythonScripts\pingpong\B.gif")
	

pygame.init()
pygame.mixer.music.load(random.choice(Backgroundmusic))
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

# Zufällige Backgroundmusik


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 20
ball.dy = -20

#boarder 1
boarder = turtle.Turtle()
boarder.speed(0)
boarder.shape("square")
boarder.color("white")
boarder.shapesize(stretch_wid=29, stretch_len= 0.4)

#boarder 3
boarder = turtle.Turtle()
boarder.speed(0)
boarder.shape("square")
boarder.goto(400, 0)
boarder.color("white")
boarder.shapesize(stretch_wid=29, stretch_len= 0.4)

#boarder 3
boarder = turtle.Turtle()
boarder.speed(0)
boarder.shape("square")
boarder.goto(-400, 0)
boarder.color("white")
boarder.shapesize(stretch_wid=29, stretch_len= 0.4)

#boarder 4
boarder = turtle.Turtle()
boarder.speed(0)
boarder.shape("square")
boarder.goto(1, 295)
boarder.color("white")
boarder.shapesize(stretch_wid=0.4, stretch_len= 40)

#boarder 4
boarder = turtle.Turtle()
boarder.speed(0)
boarder.shape("square")
boarder.goto(-1, -295)
boarder.color("white")
boarder.shapesize(stretch_wid=0.4, stretch_len= 40)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("0            0", align="center", font=("Bahnschrift Light", 50, "bold"))

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 50
	paddle_a.sety(y)
	
def paddle_a_down():
	y = paddle_a.ycor()
	y -= 50
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 50
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 50
	paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "Right")
wn.onkeypress(paddle_a_down, "Left")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()	

	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

	# Border checking
    if  ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if  ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        

    if  ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{}            {}".format(score_a, score_b), align="center", font=("Bahnschrift Light", 50, "bold"))
		
		
    if  ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}            {}".format(score_a, score_b), align="center", font=("Bahnschrift Light", 50, "bold"))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        playsound("C:\PythonScripts\pingpong\Audios\Gun+Silencer.mp3")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        playsound("C:\PythonScripts\pingpong\Audios\Gun+Silencer.mp3")
		
    if  score_a == 15:
	    pen.write("Spieler 2 hat gewonnen ", align="left", font=("Courier", 18, "bold"))
	    
        
    if  score_b == 45:
        pen.write("Spieler 2 hat gewonnen ", align="right", font=("Courier", 20, "bold"))
		
	# Boarder checking padlles
    if  paddle_a.ycor() < -295:
        paddle_a.sety(-250)
		
    if  paddle_a.ycor() > 295:
        paddle_a.sety(250)
		
    if  paddle_b.ycor() < -295:
        paddle_b.sety(-250)
		
    if  paddle_b.ycor() > 295:
        paddle_b.sety(250)
		
		
		
		

	
	



