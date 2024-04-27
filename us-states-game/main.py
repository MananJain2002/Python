import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()

data = pd.read_csv("./50_states.csv")
all_states = data["state"].tolist()
answer_state=""

guessed_states = set()
while len(guessed_states) < 50 and answer_state != "Exit":
    t.penup()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state in all_states:
        x = int(data[data["state"] == answer_state]["x"].iloc[0])
        y = int(data[data["state"] == answer_state]["y"].iloc[0])
        print(x,y)
        t.goto(x, y)
        t.pendown()
        t.write(answer_state)

missing_states = []
for state in all_states:
    if screen not in guessed_states:
        missing_states.append(state)

new_data = pd.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")