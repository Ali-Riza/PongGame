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
from turtle import clearscreen
from turtle import clear
from turtle import reset
from turtle import bye
import keyboard
import os
from time import sleep

def Revange():
    bye()
    os.system("C:\PythonScripts\pingpong\pingpong.py")
	
def counter():
    pen8.write("1", align="center", font=("Bahnschrift Light", 50, "bold"))
    sleep(1)
    pen8.reset()
    pen9.write("2", align="center", font=("Bahnschrift Light", 50, "bold"))
    sleep(1)
    pen9.reset()
    pen10.write("3", align="center", font=("Bahnschrift Light", 50, "bold"))
    sleep(1)
    pen10.reset()
    pen8.hideturtle()
    pen9.hideturtle()
    pen10.hideturtle()
	
	
Backgroundmusic = ['C:\PythonScripts\pingpong\Audios\A.mp3', 'C:\PythonScripts\pingpong\Audios\B.mp3', 'C:\PythonScripts\pingpong\Audios\C.mp3' , 'C:\PythonScripts\pingpong\Audios\D.mp3', 'C:\PythonScripts\pingpong\Audios\E.mp3', 'C:\PythonScripts\pingpong\Audios\F.mp3', 'C:\PythonScripts\pingpong\Audios\G.mp3', 'C:\PythonScripts\pingpong\Audios\H.mp3', 'C:\PythonScripts\pingpong\Audios\I.mp3', 'C:\PythonScripts\pingpong\Audios\J.mp3', 'C:\PythonScripts\pingpong\Audios\K.mp3', 'C:\PythonScripts\pingpong\Audios\L.mp3', 'C:\PythonScripts\pingpong\Audios\M.mp3']
Backgroundpic = ['C:\PythonScripts\pingpong\A.gif', 'C:\PythonScripts\pingpong\B.gif', 'C:\PythonScripts\pingpong\F.gif' , 'C:\PythonScripts\pingpong\D.gif', 'C:\PythonScripts\pingpong\G.gif', 'C:\PythonScripts\pingpong\H.gif', 'C:\PythonScripts\pingpong\I.gif', 'C:\PythonScripts\pingpong\J.gif', 'C:\PythonScripts\pingpong\K.gif', 'C:\PythonScripts\pingpong\L.gif', 'C:\PythonScripts\pingpong\M.gif']

wn = turtle.Screen()
wn.title("Spiel: Pingpong")
wn.tracer(0)
wn.bgcolor("#484848")
wn.setup(width=1.0, height=1.0, startx=None, starty=None)
wn.bgpic(random.choice(Backgroundpic))

	

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
ball.dx = 4
ball.dy = -4

#boarder 1
boarder1 = turtle.Turtle()
boarder1.shape("square")
boarder1.color("white")
boarder1.shapesize(stretch_wid=29, stretch_len= 0.4)

#boarder 2
boarder2 = turtle.Turtle()
boarder2.shape("square")
boarder2.goto(400, 0)
boarder2.color("white")
boarder2.shapesize(stretch_wid=29, stretch_len= 0.4)

#boarder 3
boarder3 = turtle.Turtle()
boarder3.shape("square")
boarder3.goto(-400, 0)
boarder3.color("white")
boarder3.shapesize(stretch_wid=29, stretch_len= 0.4)

#boarder 4
boarder4 = turtle.Turtle()
boarder4.shape("square")
boarder4.goto(1, 295)
boarder4.color("white")
boarder4.shapesize(stretch_wid=0.4, stretch_len= 40)

#boarder 5
boarder5 = turtle.Turtle()
boarder5.shape("square")
boarder5.goto(-1, -295)
boarder5.color("white")
boarder5.shapesize(stretch_wid=0.4, stretch_len= 40)


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("0            0", align="center", font=("Bahnschrift Light", 50, "bold"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("green")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 300)


pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color("green")
pen3.penup()
pen3.hideturtle()
pen3.goto(0, 0)

pen4 = turtle.Turtle()
pen4.speed(0)
pen4.color("green")
pen4.penup()
pen4.hideturtle()
pen4.goto(0, -90)

pen5 = turtle.Turtle()
pen5.speed(0)
pen5.color("blue")
pen5.penup()
pen5.hideturtle()
pen5.goto(0, 300)

pen6 = turtle.Turtle()
pen6.speed(0)
pen6.color("blue")
pen6.penup()
pen6.hideturtle()
pen6.goto(0, 0)

pen7 = turtle.Turtle()
pen7.speed(0)
pen7.color("blue")
pen7.penup()
pen7.hideturtle()
pen7.goto(0, -90)

pen8 = turtle.Turtle()
pen8.speed(0)
pen8.color("green")
pen8.penup()
pen8.hideturtle()
pen8.goto(0, 0)

pen9 = turtle.Turtle()
pen9.speed(0)
pen9.color("brown")
pen9.penup()
pen9.hideturtle()
pen9.goto(0, 0)

pen10 = turtle.Turtle()
pen10.speed(0)
pen10.color("red")
pen10.penup()
pen10.hideturtle()
pen10.goto(0, 0)




counter()

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 70
	paddle_a.sety(y)
	
def paddle_a_down():
	y = paddle_a.ycor()
	y -= 70
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 70
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 70
	paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "Right")
wn.onkeypress(paddle_a_down, "Left")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(bye, "e")
wn.onkeypress(Revange, "n")



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
      

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        
		
		
    if  score_a == 15:
        ball.reset()
        boarder1.reset()
        boarder2.reset()
        boarder3.reset()
        boarder4.reset()
        boarder5.reset()
        paddle_a.reset()
        paddle_b.reset()	
        pen.reset()
        pen2.write("Grüner Spieler hat gewonnen", align="center", font=("Bahnschrift Light", 50, "bold"))
        pen3.write("Exit: Kreis", align="center", font=("Bahnschrift Light", 40, "italic"))
        pen4.write("Revange: Quadrat", align="center", font=("Bahnschrift Light", 40, "italic"))
		
    if  score_b == 15:
        ball.reset()
        boarder1.reset()
        boarder2.reset()
        boarder3.reset()
        boarder4.reset()
        boarder5.reset()
        paddle_a.reset()
        paddle_b.reset()	
        pen.reset()
        pen5.write("Blauer Spieler hat gewonnen", align="center", font=("Bahnschrift Light", 50, "bold"))
        pen6.write("Exit: Kreis", align="center", font=("Bahnschrift Light", 40, "italic"))
        pen7.write("Revange: Quadrat", align="center", font=("Bahnschrift Light", 40, "italic"))
		
		
	# Boarder checking padlles
    if  paddle_a.ycor() < -295:
        paddle_a.sety(-250)
		
    if  paddle_a.ycor() > 295:
        paddle_a.sety(250)
		
    if  paddle_b.ycor() < -295:
        paddle_b.sety(-250)
		
    if  paddle_b.ycor() > 295:
        paddle_b.sety(250)
		
		
		
		

	




