from turtle import Turtle, Screen
from random import randint

screen = Screen()

screen.setup(width=800, height=600)

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtles = []

def createTurtle(color, y):
    tim = Turtle("turtle")
    tim.color(color)
    tim.penup()
    tim.speed(0)
    tim.goto(-380, -240+y)
    return tim

def move(turtle):
    turtle.forward(randint(1, 14))

while True:
    user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a color: ").lower()
    if user_bet in colors:
        break
    else:
        print(f"Please choose a color from {colors}")

for i in range(7):
    tim = createTurtle(colors[i], 80*i)
    turtles.append(tim)

run = True
while run:
    for i in range(7):
        move(turtles[i])    
        if turtles[i].xcor() >= 375:
            winner = colors[i]
            run = False
            break

if user_bet == winner:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()
