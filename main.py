import turtle
import pandas
from states import States

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_names = data.state

correct_guesses = []


while len(correct_guesses) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_names:
            if state not in correct_guesses:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for state in state_names:
        if answer_state == state and answer_state not in correct_guesses:
            correct_guesses.append(state)
            state_data = data[data.state == answer_state]
            x_coordinate = int(state_data.x)
            y_coordinate = int(state_data.y)
            full_coor = (x_coordinate, y_coordinate)

            revealed_state = States(full_coor, state)
            print(correct_guesses)



