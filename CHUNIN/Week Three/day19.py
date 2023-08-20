#Writing my day 19 code below here

#Turtle race game
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_left():
    new_heading =tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.home()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()