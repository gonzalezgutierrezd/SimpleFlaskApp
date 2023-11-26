from __init__ import app, db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    discount = db.Column(db.Integer(), default=0)
    desc = db.Column(db.String(length=150), nullable=False, unique=True)

    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='Item', lazy=True)

    image_1 = db.Column(db.String(150), nullable=False, default='default1.png')
    image_2 = db.Column(db.String(150), nullable=False, default='default2.png')
    image_3 = db.Column(db.String(150), nullable=False, default='default3.png')

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = db.relationship('Item', backref='Cart', lazy=True)



  