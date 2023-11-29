"""imports"""
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

states_data = pandas.read_csv("50_states.csv")
score = 0
correct_guesses = []
while len(correct_guesses) < 50:
    answer = screen.textinput(
        title=f"Score: {score}/50: Guess the State", prompt="What's another state name?"
    ).title()
    if answer == "Exit":
        all_answers = pandas.DataFrame(correct_guesses, columns=['Correct Guesses'])
        all_answers.to_csv("correct_answers.csv")
        break
    data = states_data[states_data.state == answer]
    if len(data["x"]) > 0:
        score += 1
        correct_guesses.append(answer)
        writer.goto(int(data["x"]), int(data["y"]))
        writer.write(answer, move=False, align='center', font=('Arial', 8, 'normal'))
