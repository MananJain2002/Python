import colorgram, random
from turtle import Turtle, Screen

colors = colorgram.extract('image.jpg', 32)

color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors][4:]

print(color_list)

t = Turtle()
screen = Screen()

screen.colormode(255)

t.hideturtle()
t.speed(0)
t.penup()
t.goto(-250, -250)

for i in range(10):
    for j in range(10):
        t.pencolor(random.choice(color_list))
        t.pendown()
        t.dot(20)
        t.penup()
        t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.right(180)



screen.exitonclick()