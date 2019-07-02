from flask import Blueprint, session, request

from lib.utils import returns
from services.shopOrder import get_order, change_order_status

shopOrder = Blueprint('shopOrder', __name__)


@shopOrder.route('/get', methods=['get'])
def shop_order_get():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    returns(0, {'orders': get_order(email)}, '')


@shopOrder.route('/confirm', methods=['post'])
def shop_order_confirm():
    email = session['email']
    data = request.get_json()
    if not data.__contains__('id'):
        return returns(6, {}, '缺少参数！')
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    change_order_status(data['id'], 1)
    returns(0, {'id': data['id']}, '')


@shopOrder.route('/send', methods=['post'])
def shop_order_send():
    email = session['email']
    data = request.get_json()
    if not data.__contains__('id'):
        return returns(6, {}, '缺少参数！')
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    change_order_status(data['id'], 2)
    returns(0, {'id': data['id']}, '')


@shopOrder.route('/cancel', methods=['post'])
def shop_order_cancel():
    email = session['email']
    data = request.get_json()
    if not data.__contains__('id'):
        return returns(6, {}, '缺少参数！')
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    change_order_status(data['id'], 5)
    returns(0, {'id': data['id']}, '')
