from models.models import db, Shop
from lib.utils import path_to_url
import datetime


def get_shop(email):
    return Shop.query.filter_by(email=email).first()


def create_shop(email, name, password):
    shop = Shop
