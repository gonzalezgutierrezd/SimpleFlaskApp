from flask import Flask, redirect, url_for, render_template

from flask_sqlalchemy import SQLAlchemy
from __init__ import app,db
from .models import Item

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/our_menu", methods=['POST', 'GET'])
def our_menu():
    # queries db by the category corresponding to "potions" and stores results in potions
    potions = Item.query.filter(Item.category_id==2)
    # queries db by the category corresponding to "specialty potions" and stores results in SPotions
    SPotions = Item.query.filter(Item.category_id==3)
    # queries db by the category corresponding to "eatery" and stores results in eatery
    eatery = Item.query.filter(Item.category_id==1)
    # renders the menu html file and passses my pre-categorized items from my table
    return render_template('our_menu.html', Potions=potions, Specialty=SPotions, Food=eatery)

if __name__ == "__main__":
    app.run(debug=True)