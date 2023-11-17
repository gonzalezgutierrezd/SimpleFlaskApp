from __init__ import app,db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    discount = db.Column(db.Integer(), default=0)
    #stock = db.Column(db.Integer(), nullable=False)
    desc = db.Column(db.String(length=150), nullable=False, unique=True)

    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='Item', lazy=True)

    image_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image.jpg')

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)

with app.app_context():
    db.create_all()
    food_cat = Category(id=1, name='Eatery')
    potions_cat = Category(id=2, name='Potions')
    specialty_potions = Category(id=3, name='Specialty Potions')
    supplies_cat = Category(id=4, name='Supplies')
    other_cat = Category(id=5, name='Other')
    latte_item = Item(id=1, name='Latte', price=5.0, desc='The most simple form of our Draught of Soul. 2 shots of magic bean extract with delicious frothed milk.', category_id=2)
  