import colorgram
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.shape('arrow')

color_list =[]
colors = colorgram.extract('image.jpg', 40)
for color in colors:
       col= color.rgb
       r = int(col.r)
       g = int(col.g)
       b = int(col.b)
       rgb = (r,g,b)
       color_list.append(rgb)



def draw_solid_circle():
    r_color = random.choice(color_list)
    tim.dot(20,r_color)

tim.speed('fastest')
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

rows = 10
columns = 10
for j in range(columns):
    for i in range(rows):
        draw_solid_circle()
        tim.forward(50)
    tim.left(180)
    tim.penup()
    tim.forward(50*rows)
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    #tim.pendown()






screen.exitonclick()
