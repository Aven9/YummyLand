from models.models import db, Shop


def get_shop_by_type(shop_type, page, ):
    shops = Shop.query.filter_by(type=shop_type).offset().limit().all()
