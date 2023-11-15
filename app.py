from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    discount = db.Column(db.Integer(), default=0)
    stock = db.Column(db.Integer(), nullable=False)
    desc = db.Column(db.String(length=150), nullable=False, unique=True)

    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='posts', lazy=True)

    image_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image.jpg')

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/orderAhead.html")
def orderAhead():
    return render_template("orderAhead.html")


#@app.route("/admin")
#def admin():
#    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)