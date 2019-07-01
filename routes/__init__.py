from .user import user


def route(app):
    app.register_blueprint(user, url_prefix='/user')
