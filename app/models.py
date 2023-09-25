from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id= db.column(db.Integer, primary_key=True)
    username = db.column(db.String(80), unique=True,nullable=False)
    email = db.column(db.String(120), unique=True,nullable=False)
    password = db.column(db.String(80), unique=True,nullable=False)
    phone_number = db.column(db.integer(10), nullable=False)

    address = db.relationship('user_address',backref='user')

class User_address(db.Model):
    id= db.column(db.Integer, primary_key=True)
    location_address = db.column(db.String(80), unique=True,nullable=False)
    street_name = db.column(db.String(80), unique=True,nullable=False)
    city = db.column(db.String(80), unique=True,nullable=False)
    county = db.column(db.String(80), unique=True,nullable=False)
    user_id = db.column(db.integer(10), db.ForeignKey('user.id'), nullable=False)



#################Restraurant#####################

class Restaurant(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.string(80), unique=True, nullable=False)
    location = db.column(db.string(80), unique=True, nullable=False)
    contact = db.column(db.string(80), unique=True, nullable=False)

    menus = db.relationship('Menu',backref='restaurant', lazy=True)

class Menu(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.string(80), unique=True, nullable=False)
    category = db.column(db.string(80), unique=True, nullable=False)
    status =db.column(db.Boolean, default=True)
    restaurant_id = db.column(db.Integer, db.ForeignKey('restaurant_id'), nullable=False)

    menu_items = db.relationship('Menu_item',backref='menu', lazy=True)

class Menu_item(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.string(80), unique=True, nullable=False)
    price = db.column(db.Float, unique=True, nullable=False)
    description = db.column(db.string(80), unique=True, nullable=False)
    menu_id = db.column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    
    order_item = db.relationship('Order_item',backref='menu_item', lazy=True)

#################Order#####################

class Order(db.Model):
    id = db.column(db.Integer, primary_key=True)
    user_id = db.column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    delivery_address_id = db.column(db.Integer, db.ForeignKey('user_address.id'), nullable=False)
    total = db.column(db.Float, unique=True, nullable=False)

    order_items = db.relationship('Order_item',backref='order', lazy=True)


class Order_item(db.Model):
    id = db.column(db.Integer, primary_key=True)
    menu_item_id = db.column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    order_id = db.column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    quantity = db.column(db.Integer, default=1, nullable=False) 