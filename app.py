from flask import Flask, redirect, url_for, render_template

from flask_sqlalchemy import SQLAlchemy
from __init__ import app,db
from .models import Item, Cart

@app.route("/")
def home():
    return render_template("index.html")

#change to OurMenu
@app.route("/our_menu", methods=['POST', 'GET'])
def our_menu():
    products = db.session.execute(db.select(Item))
    return render_template('our_menu.html', products=products)




if __name__ == "__main__":
    app.run(debug=True)