from turtle import Turtle, Screen

import random

speeds = [5,15,20,40,10,50]
screen = Screen()
screen.setup(500,400)
race_on = False

tim = Turtle()
tim.color('goldenrod')
tim.shape("turtle")
tim.penup()
tim.goto(-220,120)

tom = Turtle()
tom.color('medium orchid')
tom.shape("turtle")
tom.penup()
tom.goto(-220,70)

tum = Turtle()
tum.color('indigo')
tum.shape("turtle")
tum.penup()
tum.goto(-220,20)

tam = Turtle()
tam.color('spring green')
tam.shape("turtle")
tam.penup()
tam.goto(-220,-30)

temu = Turtle()
temu.color('red')
temu.shape("turtle")
temu.penup()
temu.goto(-220,-80)

turtles =[tim, tom, tum,tam,temu]
user_bet = screen.textinput(title='Make your bet.', prompt="Which turtle will win the race?: ")
if user_bet:
    race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > 230:
            race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print("You're right!")
            else:
                print(f"The winner is {winner}")
        dist = random.randint(1, 10)
        t.forward(dist)


screen.listen()
#screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()