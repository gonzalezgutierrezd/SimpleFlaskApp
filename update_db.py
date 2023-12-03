from __init__ import app, db
from models import Category, Item

with app.app_context():
    treasure = Item.query.filter(Item.id==8).first()
    treasure.image_1='TreasureClover.png'
    db.session.commit()



  