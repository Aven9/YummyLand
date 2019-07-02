from flask import Blueprint, session, request

from lib.utils import returns
from services.food import get_shop_by_type, get_shop_by_name, get_shop, get_common

food = Blueprint('shop', __name__)


@food.route('/shop/getByType', methods=['post'])
def get_by_type():
    data = request.get_json()
    if data.__contains__('type') and data.__contains__('page') and data.__contains__('limit'):
        return returns(0, {'shops': get_shop_by_type(data['type'], data['page'], data['limit'])}, '')
    else:
        return returns(6, {}, '缺少参数！')


@food.route('/shop/getByName', methods=['post'])
def get_by_name():
    data = request.get_json()
    if data.__contains__('name') and data.__contains__('page') and data.__contains__('limit'):
        return returns(0, {'shops': get_shop_by_name(data['name'], data['page'], data['limit'])}, '')
    else:
        return returns(6, {}, '缺少参数！')


@food.route('/shop/get', methods=['post'])
def shop_get():
    data = request.get_json()
    if data.__contains__('id'):
        return returns(0, get_shop(data['id']), '')
    else:
        return returns(6, {}, '缺少参数！')


@food.route('/shop/common', methods=['post'])
def common_get():
    data = request.get_json()
    if data.__contains__('id'):
        return returns(0, {'commons': get_common(data['id'])}, '')
    else:
        return returns(6, {}, '缺少参数！')
