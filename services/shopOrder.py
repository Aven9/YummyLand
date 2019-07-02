from models.models import db, Order, Shop


def get_order(email):
    shop = Shop.query.filter_by(email=email).first()
    orders = Order.query.filter_by(shop_id=shop.id).all()
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


def change_order_status(order_id, new_status):
    order = Order.query.filter_by(id=order_id).first()
    order.status = new_status
    db.session.commit()
