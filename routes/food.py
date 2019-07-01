from flask import Blueprint, session, request

from lib.utils import returns

shop = Blueprint('shop', __name__)


@shop.route('/shop/getByType', methods=['post'])
def get_by_type():
    data = request.get_json()
    if data.__contains__('type'):
        return returns(0, {}, '')
    else:
        return returns(6, {}, '缺少参数！')
