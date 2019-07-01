from models.models import db, User
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
