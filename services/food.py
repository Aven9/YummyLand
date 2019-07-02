from models.models import Shop, User


def get_shop_by_type(shop_type, page, number):
    shops = Shop.query.filter_by(type=shop_type).offset((page - 1) * number).limit(number).all()
    data = []
    for shop in shops:
        data.append({
            'id': shop.id,
            'name': shop.name,
            'imageUrl': shop.imageUrl,
            'introduction': shop.introduction
        })
    return data


def get_shop_by_name(name, page, number):
    shops = Shop.query.filter_by(Shop.name.like("%"+name+"%")).offset((page - 1) * number).limit(number).all()
    data = []
    for shop in shops:
        data.append({
            'id': shop.id,
            'name': shop.name,
            'imageUrl': shop.imageUrl,
            'introduction': shop.introduction
        })
    return data


def get_shop(shop_id):
    shop = Shop.query.filter_by(id=shop_id).first()
    data = {}
    for classification in shop.food_classifications:
        if classification.status == 1:
            foods = []
            for food in classification.foods:
                if food.status == 1:
                    foods.append({
                        'id': food.id,
                        'name': food.name,
                        'price': food.price,
                        'imageUrl': food.imageUrl
                    })
            data[classification.text] = foods
    return {
        'id': shop.id,
        'name': shop.name,
        'imageUrl': shop.imageUrl,
        'introduction': shop.introduction,
        'phone': shop.phone,
        'food': data
    }


def get_common(shop_id):
    shop = Shop.query.filter_by(id=shop_id).first()
    data = []
    for common in shop.commons:
        data.append({
            'username': User.query.filter_by(id=common.user_id).first().username,
            'text': common.text,
            'imageUrl': common.imageUrl,
            'rate': common.rate,
            'createdAt': common.createdAt
        })
    return data
