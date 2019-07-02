from .user import user
from .shopOrder import shopOrder
from .order import order
from .food import food
from .shopUser import shopUser


def route(app):
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(order, url_prefix='/order')
    app.register_blueprint(food, url_prefix='/food')
    app.register_blueprint(shopUser, url_prefix='/shopUser')
    app.register_blueprint(shopOrder, url_prefix='/shopOrder')
