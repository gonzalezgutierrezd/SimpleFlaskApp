# this file was used to update my database when I wanted to add custom images to my database for the specialty potions

from __init__ import app, db
from models import Category, Item

with app.app_context():
    # grabbing the 8th specialty potion which is "Treasure Clove"
    treasure = Item.query.filter(Item.id==8).first()
    # updating their image_1 column with the name of my image file
    treasure.image_1='TreasureClover.png'
    db.session.commit()





  