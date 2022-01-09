import turtle
import pandas

Screen = turtle.Screen()
Screen.title("Can you name all the Indian States?")
image = "map.gif"
Screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("29_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 30:

    answer_state = Screen.textinput(title=f"{len(guessed_states)}/30 the state", prompt="What is the next state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in missing_states:
            if state not in guessed_states:
                missing_states.append(state)
                print(missing_states)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv()
            print(new_data)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
