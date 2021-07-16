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
guesses = []


def user_answer():
    if len(guesses) == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    else:
        answer_state = screen.textinput(title=f"{len(guesses)} / {NUMBER_OF_STATES} Guess the State", prompt="What's another state's name?")
    capitalized_answer = answer_state.title()
    return capitalized_answer


states_data = pandas.read_csv("50_states.csv")
LIST_OF_STATES = states_data.state.to_list()


def check_answer(u_answer):
    for state in LIST_OF_STATES:
        if u_answer == state:
            write_state(u_answer)
            guesses.append(u_answer)


def write_state(state):
    tim.penup()
    state_row = states_data[states_data.state == state]
    x_cor = int(state_row.x)
    y_cor = int(state_row.y)
    tim.goto(x_cor, y_cor)
    tim.write(f"{state}", )


game_is_on = True
while game_is_on:
    check_answer(user_answer())
