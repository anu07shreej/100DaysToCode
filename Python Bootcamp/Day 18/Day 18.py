from turtle import Turtle, Screen
#import heroes
import random

tim = Turtle()
screen = Screen()

tim.shape('arrow')
#-----DRAW a SQUARE
# for i in range(20):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

# def draw_shape(sides):
#     for i in range(sides):
#         tim.forward(100)
#         tim.left(360/sides)

#draw_shape(10)

#-------------------------- SPIROGRAPH ------------------------
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    print(color)
    return color

def draw_circle(radius):
    color = random_color()
    screen.colormode(255)
    tim.pencolor(color)

    tim.circle(radius)

def draw_spiral(radius):
    for i in range(72):
        #tim.left(i)
        draw_circle(radius)
        current_heading = tim.heading()
        tim.setheading(current_heading + 5)

tim.speed('fastest')

draw_spiral(200)






screen.exitonclick()
