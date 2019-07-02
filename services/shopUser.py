from models.models import db, Shop, FoodClassification, Food, User
import datetime


def get_shop(email):
    return Shop.query.filter_by(email=email).first()


def create_shop(email, name, password, address, classification, introduction):
    shop = Shop(email=email, name=name, password=password, imageUrl='', address=address, classification=classification, introduction=introduction, createdAt=datetime.datetime.now())
    db.session.add(shop)
    db.session.commit()
    return shop


def get_shop_detail(email):
    shop = Shop.query.filter_by(email=email).first()
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
        'address': shop.address,
        'classification': shop.classification,
        'food': data
    }


def modify_shop_detail(email, name, imageUrl, introduction, phone, address, classification, foods):
    shop = Shop.query.filter_by(email=email).first()
    for c in shop.food_classifications:
        for food in c.foods:
            food.status = 0
        c.status = 0
    shop.name = name
    shop.imageUrl = imageUrl
    shop.introduction = introduction
    shop.phone = phone
    shop.address = address
    shop.classification = classification
    for cs in foods:
        c = FoodClassification.query.filter_by(text=cs, shop_id=shop.id).first()
        if c is None:
            c = FoodClassification(text=cs, status=1, createdAt=datetime.datetime.now())
            shop.food_classifications.append(c)
        for f in foods[cs]:
            c.foods.append(Food(price=f['price'], name=f['name'], imageUrl=f['imageUrl'], createdAt=datetime.datetime.now(), status=1))
    db.session.commit()


def get_commons(email):
    shop = Shop.query.filter_by(email=email).first()
    data = []
    for common in shop.commons:
        data.append({
            'id': common.id,
            'username': User.query.filter_by(id=common.user_id).first().username,
            'text': common.text,
            'imageUrl': common.imageUrl,
            'rate': common.rate,
            'createdAt': common.createdAt
        })
    return data

