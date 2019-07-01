from models.models import db, User, Address
from lib.utils import path_to_url
import datetime


def create_user(username, email, password):
    db.session.add(User(username=username, email=email, password=password, imageUrl='', birthday = '', createdAt=datetime.datetime.now()))
    db.session.commit()


def query_user(email):
    user = User.query.filter_by(email=email).first()
    return user is None


def login(email, password):
    user = User.query.filter_by(email=email, password=password).first()
    return user is None


def get_user(email):
    return User.query.filter_by(email=email).first()


def modify_user(username, email, birthday):
    user = User.query.filter_by(email=email).first()
    user.username = username
    user.birthday = birthday
    db.session.commit()


def change_image_url(email, filename):
    user = User.query.filter_by(email=email).first()
    user.imageUrl = path_to_url(filename)
    db.session.commit()


def get_address(email):
    user = User.query.filter_by(email=email).first()
    data = []
    for address in user.addresses:
        data.append({
            'id': address.id,
            'name': address.name,
            'phone': address.phone,
            'province': address.province,
            'city': address.city,
            'detail': address.detail
        })
    return data


def add_address(email, name, phone, province, city, detail):
    user = User.query.filter_by(email=email).first()
    user.addresses.append(Address(name=name, phone=phone, province=province, city=city, detail=detail))
    db.session.commit()


def modify_address(email, address_id, name, phone, province, city, detail):
    user = User.query.filter_by(email=email).first()
    address = Address.query.filter_by(id=address_id).first()
    if address.user_id == user.id:
        address.name = name
        address.phone = phone
        address.province = province
        address.city = city
        address.detail = detail
    db.session.commit()


def delete_address(email, address_id):
    user = User.query.filter_by(email=email).first()
    address = Address.query.filter_by(id=address_id).first()
    if address.user_id == user.id:
        db.session.delete(address)
        db.session.commit()
