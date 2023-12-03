from flask import Flask, redirect, url_for, render_template

from flask_sqlalchemy import SQLAlchemy
from __init__ import app,db
from .models import Item

@app.route("/")
def home():
    return render_template("index.html")

#change to OurMenu
@app.route("/our_menu", methods=['POST', 'GET'])
def our_menu():
    potions = Item.query.filter(Item.category_id==2)
    SPotions = Item.query.filter(Item.category_id==3)
    eatery = Item.query.filter(Item.category_id==1)
    return render_template('our_menu.html', Potions=potions, Specialty=SPotions, Food=eatery)

if __name__ == "__main__":
    app.run(debug=True)