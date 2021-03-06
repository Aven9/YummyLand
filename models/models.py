from app import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.TIMESTAMP, nullable=False)

    commons = db.relationship('Common', backref='User', lazy='dynamic')
    addresses = db.relationship('Address', backref='User', lazy='dynamic')
    orders = db.relationship('Order', backref='User', lazy='dynamic')


class Address(db.Model):
    __tablename__ = 'Address'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    province = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    detail = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    user_id = db.Column(db.INTEGER, db.ForeignKey('User.id'))

    orders = db.relationship('Order', backref='Address', lazy='dynamic')


class Order(db.Model):
    __tablename__ = 'Order'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    status = db.Column(db.INTEGER, nullable=False, default=0)
    remark = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.TIMESTAMP, nullable=False)

    user_id = db.Column(db.INTEGER, db.ForeignKey('User.id'))
    address_id = db.Column(db.INTEGER, db.ForeignKey('Address.id'))
    shop_id = db.Column(db.INTEGER, db.ForeignKey('Shop.id'))

    food_numbers = db.relationship('FoodNumber', backref='Order', lazy='dynamic')


class FoodNumber(db.Model):
    __tablename__ = 'FoodNumber'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    number = db.Column(db.INTEGER, nullable=False, default=1)

    order_id = db.Column(db.INTEGER, db.ForeignKey('Order.id'))
    food_id = db.Column(db.INTEGER, db.ForeignKey('Food.id'))


class Shop(db.Model):
    __tablename__ = 'Shop'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    phone = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    introduction = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    classification = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.TIMESTAMP, nullable=False)

    orders = db.relationship('Order', backref='Order', lazy='dynamic')
    commons = db.relationship('Common', backref='Shop', lazy='dynamic')
    food_classifications = db.relationship('FoodClassification', backref='Shop', lazy='dynamic')


class Common(db.Model):
    __tablename__ = 'Common'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    text = db.Column(db.String, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    rate = db.Column(db.INTEGER, nullable=False)
    createdAt = db.Column(db.TIMESTAMP, nullable=False)

    user_id = db.Column(db.INTEGER, db.ForeignKey('User.id'))
    shop_id = db.Column(db.INTEGER, db.ForeignKey('Shop.id'))


class FoodClassification(db.Model):
    __tablename__ = 'FoodClassification'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    text = db.Column(db.String, nullable=False)
    status = db.Column(db.INTEGER, default=1)
    createdAt = db.Column(db.TIMESTAMP, nullable=False)

    shop_id = db.Column(db.INTEGER, db.ForeignKey('Shop.id'))

    foods = db.relationship('Food', backref='FoodClassification', lazy='dynamic')


class Food(db.Model):
    __tablename__ = 'Food'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    price = db.Column(db.INTEGER, nullable=False)
    name = db.Column(db.String, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.TIMESTAMP, nullable=False)
    status = db.Column(db.INTEGER, default=1)

    food_classification_id = db.Column(db.INTEGER, db.ForeignKey('FoodClassification.id'))

    food_numbers = db.relationship('FoodNumber', backref='Food', lazy='dynamic')


db.create_all()
