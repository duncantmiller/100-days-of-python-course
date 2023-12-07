from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def bold_wrapper():
        return f"<b>{function()}</b>"
    return bold_wrapper

def make_h1(function):
    def h1_wrapper(**kwargs):
        return f"<h1>{function(**kwargs)}</h1>"
    return h1_wrapper

@app.route('/name/<username>')
@make_h1
def hello(username):
    return f"hello {username}"

@app.route('/bye')
@make_bold
def bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True)
