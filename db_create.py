from __init__ import app, db
from models import Category, Item

with app.app_context():
    db.create_all()
    food_cat = Category(id=1, name='Eatery')
    db.session.add(food_cat)

    potions_cat = Category(id=2, name='Draught of Soul Potions')
    db.session.add(potions_cat)

    specialty_potions = Category(id=3, name='Specialty Potions')
    db.session.add(specialty_potions)

    supplies_cat = Category(id=4, name='Supplies')
    db.session.add(supplies_cat)

    other_cat = Category(id=5, name='Other')
    db.session.add(other_cat)

    latte_item = Item(id=1, name='Latte', price=5.0, desc='Draught of Soul with delicious frothed milk and light layer of foam.', category_id=2)
    db.session.add(latte_item)

    flat_white = Item(id=2, name='Flat White', price=3.5, desc='Draught of Soul with steamed milk. Slightly stronger than a latte.', category_id=2)
    db.session.add(flat_white)

    cortado = Item(id=3, name='Cortado', price=2.5, desc='2:1 ratio of steamed milk to Draught of Soul.', category_id=2)
    db.session.add(cortado)

    cappuccino = Item(id=4, name='Cappuccino', price=3.5, desc='Draught of Soul with steamed milk, and microfoam.', category_id=2)
    db.session.add(cappuccino)

    espresso = Item(id=5, name='Magic Bean Extract', price=3.5, desc='Simply a shot of Draught of Soul.', category_id=2)
    db.session.add(espresso)

    rice_licquer1 = Item(id=6, name='Rice Licquer', price=4.0, desc='Our alchemical take on horchata.', category_id=3)
    db.session.add(rice_licquer1)

    rice_licquer2 = Item(id=7, name='Rice Licquer (Soul Infused)', price=5.0, desc='Our Rice Licquer infused with Draught of Soul.', category_id=3)
    db.session.add(rice_licquer2)

    treasure_clove = Item(id=8, name='Treasure Clove', price=5.0, desc='Latte base with hints of cinnamon, nutmeg, and buttery caramel topped with cookie crumbles.', category_id=3)
    db.session.add(treasure_clove)

    mexica = Item(id=9, name="Mexica's Brew", price=5.0, desc='Our Draught of Soul infused with rich chocolate and frothed milk. Try it a la Tlanchana.', category_id=3)
    db.session.add(mexica)

    fullmetal = Item(id=10, name="The Fullmetal Alchemist", price=3.10, desc='Named after one of the greatest alchemists this is a DEFINITELY NOT short glass of Draught of Soul diluted with water. NO MILK.', category_id=3)
    db.session.add(fullmetal)

    witchFinger = Item(id=11, name="Witch's Fingers", price=3.0, desc='3 chocolate dipped "fingers" with almond nails. No witches harmed in the making of this snack.', category_id=1)
    db.session.add(witchFinger)

    lembas = Item(id=12, name="Lembas Bread", price=4.50, desc='An elvish delicacy from Middle-Earth. Pleasantly sweet and bready, this is a perfect heart treat for travelers.', category_id=1)
    db.session.add(lembas)

    dragonNuts = Item(id=13, name="Dragon Roasted Nuts", price=3.0, desc='These nuts pack some serious heat from a blend of spices including cinnamon, ginger, cloves, cumin, chili powder, red pepper flakes, black pepper, and cayenne pepper.', category_id=1)
    db.session.add(dragonNuts)

    db.session.commit()


  