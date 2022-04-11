from turtle import *
import turtle

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

Mercedes.penup()
Mercedes.goto(-300,0)
Mercedes.color("blue")





exitonclick()