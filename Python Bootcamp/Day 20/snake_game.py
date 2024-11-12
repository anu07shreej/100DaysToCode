from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

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
    screen.update()
    time.sleep(0.2)
    for seg_num in range(len(segment_list)-1, 0, -1):
        new_x = segment_list[seg_num - 1].xcor()
        new_y = segment_list[seg_num - 1].ycor()
        segment_list[seg_num].goto(new_x,new_y)
    segment_list[0].forward(20)
    segment_list[0].left(90)



screen.exitonclick()