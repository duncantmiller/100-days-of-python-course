from flask import Flask

app = Flask(__name__)

@app.route('/name/<username>')
def hello(username):
    return f"hello {username}"

if __name__ == "__main__":
    app.run(debug=True)
