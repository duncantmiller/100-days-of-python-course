from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import json

app = Flask(__name__)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
db = SQLAlchemy()
db.init_app(app)

##CREATE TABLE
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(500), nullable=False)
    body = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()
    # articles = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    # all_articles = articles.json()

    # for article in all_articles:
    #     new_article = Article(
    #             title=article["title"],
    #             subtitle=article["subtitle"],
    #             body=article["body"],
    #         )
    #     db.session.add(new_article)
    #     db.session.commit()

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
    result = db.session.execute(db.select(Article).order_by(Article.title))
    articles = result.scalars().all()
    return render_template("blog/index.html", articles=articles)

@app.route('/blog/<int:id>')
def blog_show(id):
    article = db.get_or_404(Article, id)
    return render_template("blog/show.html", article=article)

@app.route('/api_docs')
def api_docs():
    return render_template("api_docs/index.html", num=1)

@app.route('/api/v1/articles', methods=["GET"])
def get_articles():
    result = db.session.execute(db.select(Article).order_by(Article.title))
    articles = result.scalars().all()
    return jsonify(articles=[article.to_dict() for article in articles])

@app.route('/api/v1/articles/<int:id>', methods=["GET"])
def get_article(id):
    article = db.get_or_404(Article, id)
    return jsonify(article.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
