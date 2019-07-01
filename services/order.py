from models.models import Order, FoodNumber, User, db, Common
import datetime


def create_order(email, foods, address_id, remark):
    user = User.query.filter_by(email=email).first()
    order = Order(status=0, remark=remark, address_id=address_id)
    for food in foods:
        order.food_numbers.append(FoodNumber(number=food.number, food_id=food.id))
    user.orders.append(order)
    db.session.commit()
    return order


def get_order(email, page, numbers):
    user = User.query.filter_by(email=email).first()
    orders = Order.query.filter_by(user_id=user.id).offset((page - 1) * numbers).limit(numbers).all()
    data = []
    for order in orders:
        foods = []
        for food_number in order.food_numbers:
            food = food_number.food
            foods.append({
                'id': food.id,
                'name': food.name,
                'price': food.price,
                'imageUrl': food.imageUrl,
                'number': food_number.number
            })
        data.append({
            'id': order.id,
            'foods': foods,
            'address': {
                'name': order.Address.name,
                'phone': order.Address.phone,
                'province': order.Address.province,
                'city': order.Address.city,
                'detail': order.Address.detail
            },
            'status': order.status,
            'createdAt': order.createdAt,
            'remark': order.remark
        })


def cancel_order(order_id):
    order = Order.query.filter_by(id=order_id).first()
    order.status = 4
    db.session.commit()


def confirm_order(order_id):
    order = Order.query.filter_by(id=order_id).first()
    order.status = 3
    db.session.commit()


def create_common(order_id, text, image_url, rate):
    shop = Order.query.filter_by(id=order_id).first().food_numbers.Food.FoodClassification.Shop
    c = Common(text=text, imageUrl=image_url, rate=rate, createdAt=datetime.datetime.now())
    shop.commons.append(c)
    db.session.commit()
    return c
