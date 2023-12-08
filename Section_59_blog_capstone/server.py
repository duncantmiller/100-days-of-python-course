from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = posts.json()

@app.route('/')
def home():
    return render_template("home/index.html", num=1)

@app.route('/inquiry', methods=["POST"])
def receive_data():
    name = request.form["InputName"]
    email = request.form["InputEmail"]
    message = request.form["InputMessage"]
    return f"<ul><li>Name: {name}</li><li>Email: {email}</li><li>Message: {message}</li></ul>"

@app.route('/blog')
def blog_index():
    return render_template("blog/index.html", posts=all_posts)

@app.route('/blog/<int:id>')
def blog_show(id):
    post = next((post for post in all_posts if post['id'] == id), None)
    return render_template("blog/show.html", post=post)

@app.route('/api_docs')
def api_docs():
    return render_template("api_docs/index.html", num=1)

@app.route('/api/v1/articles', methods=["GET"])
def get_articles():
    return jsonify(all_posts)

@app.route('/api/v1/articles/<int:id>', methods=["GET"])
def get_article(id):
    post = next((post for post in all_posts if post['id'] == id), None)
    return jsonify(post)

if __name__ == "__main__":
    app.run(debug=True)
