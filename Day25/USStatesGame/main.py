import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=740, height=500)
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_coords(x,y):
#     print (x,y)
#
# turtle.onscreenclick(get_mouse_coords)

states_writer = turtle.Turtle()
states_writer.penup()
states_writer.hideturtle()
correct_states = []
states_data = pd.read_csv("./50_states.csv")

while len(correct_states) < 50:

    if correct_states:
        answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    answer_in_tables = (states_data.state == answer_state)
    if answer_in_tables.any() and answer_state not in correct_states:
        x_coord = int(states_data[answer_in_tables].x)
        y_coord = int(states_data[answer_in_tables].y)
        states_writer.setposition(x= x_coord, y=y_coord)
        states_writer.write(answer_state, align="center")
        correct_states.append(answer_state)


missing_states = states_data[~states_data.state.isin(correct_states)].state
missing_states.to_csv("states_to_learn.csv")
print (missing_states)