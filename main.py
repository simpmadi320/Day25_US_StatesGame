import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

total_states = 50
correct_answers = 0

while correct_answers < total_states:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    data = pandas.read_csv("50_states.csv")
    result = data[data["state"] == answer_state]

    if not result.empty:
        x = result["x"].values[0]
        y = result["y"].values[0]
        print(answer_state + ": " + str(x) + ", " + str(y))
        t = turtle.Turtle()
        t.penup()
        t.goto(x, y)
        t.hideturtle()
        t.write(answer_state)
        correct_answers += 1

turtle.mainloop()
