from turtle import *
import turtle
import random
import time

#creating screen
screen = turtle.Screen()
screen.bgcolor("black")

#creating racer 1
Mercedes = Turtle()
Mercedes.color("Blue")
Mercedes.shape("square")

#creating racer 2
redBull = Turtle()
redBull.color("Red")
redBull.shape("square")

#moving racers to start
Mercedes.penup()
Mercedes.goto(-300,0)
redBull.penup()
redBull.goto(-300,30)

#drawing finishline using Racer1
Mercedes.goto(300,-250)
Mercedes.left(90)
Mercedes.pendown()
Mercedes.color("white")
Mercedes.forward(500)

#writing "Finish Line"
Mercedes.pensize(10)
Mercedes.color("white")
Mercedes.write("Finish Line!", font =("Verdana", 10 , "bold"))

#moving racer1 back
Mercedes.penup()
Mercedes.goto(-300,0)
Mercedes.color("blue")
Mercedes.right(90)

#showing choice to bet to the player
print("Welcome to F1!")
bet = textinput("","""Welcome to F1, Which racer do you think will win?
type 1 for blue or type 2 for red            
""")

#creating 2 dices with random numbers from 1-6
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

#if a racer cresses finish line it shows that they have won
for i in range(30):
    if Mercedes.position() > (300,250):
        print("Mercedes is the winner!")
        if int(bet) == 1:
            print("your bet was right")
        else:
            print("Sorry, you were wrong")
        break
    elif redBull.position() > (300,-250):
        print("RedBull is the winner!")
        if int(bet) == 2:
            print("your bet was right")
        else:
            print("Sorry, you were wrong")
        break
    else:
        Mercedes.forward(20*dice1)
        time.sleep(0.5)
        redBull.forward(20*dice2)
        time.sleep(0.5)





exitonclick()