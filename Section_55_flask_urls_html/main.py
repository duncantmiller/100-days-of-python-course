from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(1, 10)

def make_bold(function):
    def bold_wrapper():
        return f"<b>{function()}</b>"
    return bold_wrapper

def make_h1(function):
    def h1_wrapper(**kwargs):
        return f"<h1>{function(**kwargs)}</h1>"
    return h1_wrapper

def check_guess(function):
    def guess_wrapper(**kwargs):
        if kwargs["number"] == random_number:
            return f"{function(**kwargs)} is right!"
        else:
            return f"Nope {function(**kwargs)}  is wrong try again."
    return guess_wrapper

@app.route('/name/<username>')
@make_h1
def hello(username):
    return f"hello {username}"

@app.route('/bye')
@make_bold
def bye():
    return "Bye"

@app.route('/guess/<int:number>')
@check_guess
def guess(number):
    return f"{number}"

if __name__ == "__main__":
    app.run(debug=True)
