from models.models import db, User
import datetime


def create_user(username, email, password):
    db.session.add(User(username=username, email=email, password=password, createdAt=datetime.datetime.now()))
    db.session.commit()


def query_user(email):
    users = User.query().filter_by(email=email).all()
    return len(users) > 0
