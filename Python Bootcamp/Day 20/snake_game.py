from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

start_positions = [(0,0),(-20,0),(-40,0)]
segment_list = []

for start in start_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(start)
    segment_list.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segment_list:
        seg.forward(20)








screen.exitonclick()