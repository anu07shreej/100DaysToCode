from turtle import Screen
#import random
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snaky = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

screen.onkey(snaky.up,"Up")
screen.onkey(snaky.down, "Down")
screen.onkey(snaky.left,"Left")
screen.onkey(snaky.right, "Right")

#snaky.move()
#start_positions = [(0,0),(-20,0),(-40,0)]
#segment_list = []

# for start in start_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(start)
#     segment_list.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snaky.move()
    if snaky.head.distance(food) < 15:
        snaky.extend()
        score.increase_score()
        score.update_scoreboard()
        food.refresh()

    if snaky.head.xcor() > 290 or snaky.head.xcor() < -290 or snaky.head.ycor() > 290 or snaky.head.ycor() < -290:
        score.game_over()
        game_is_on = False

    for seg in snaky.segments:
        if seg == snaky.head:
            pass
        elif snaky.head.distance(seg) < 10:
            score.game_over()
            game_is_on = False




screen.exitonclick()