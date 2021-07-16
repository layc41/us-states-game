import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
NUMBER_OF_STATES = 50
tim = turtle.Turtle()
tim.hideturtle()
states_data = pandas.read_csv("50_states.csv")
LIST_OF_STATES = states_data.state.to_list()
guesses = []


def user_answer():
    answer_state = screen.textinput(title=f"{len(guesses)} / {NUMBER_OF_STATES} Guess the State",
                                    prompt="What's another state's name?").title().strip()
    return answer_state


def check_answer(state):
    if state in LIST_OF_STATES:
        tim.penup()
        state_row = states_data[states_data.state == state]
        tim.goto(int(state_row.x), int(state_row.y))
        tim.write(state)
        guesses.append(state)


while len(guesses) < 50:
    answer = user_answer()
    if answer == "Exit":
        missing_states = []
        for state in LIST_OF_STATES:
            if state not in guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    check_answer(answer)


