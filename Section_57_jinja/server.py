from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = posts.json()

@app.route('/')
def home():
    return render_template("index.html", num=1)

@app.route('/blog')
def blog_index():
    return render_template("blog/index.html", posts=all_posts)

@app.route('/blog/<int:id>')
def blog_show(id):
    post = next((post for post in all_posts if post['id'] == id), None)
    return render_template("blog/show.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
