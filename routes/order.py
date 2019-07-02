from flask import Blueprint, session, request
import os
from werkzeug.utils import secure_filename
from pypinyin import lazy_pinyin

from lib.utils import returns, path_to_url
from services.order import cancel_order, get_order, create_order, confirm_order, create_common

order = Blueprint('order', __name__)


@order.route('/create', methods=['post'])
def order_create():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('foods') and data.__contains__('addressId') and data.__contains__('remark') and data.__contains__('shopId'):
        o = create_order(email, data['foods'], data['addressId'], data['remark'], data['shopId'])
        return returns(0, {'id': o.id}, '成功！')
    else:
        return returns(6, {}, '缺少参数！')


@order.route('/get', methods=['post'])
def order_get():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('page') and data.__contains__('limit'):
        return returns(0, {'orders': get_order(email, data['page'], data['limit'])}, '')
    else:
        return returns(6, {}, '缺少参数！')


@order.route('/cancel', methods=['post'])
def order_cancel():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('id'):
        cancel_order(data['id'])
        return returns(0, {'id': data['id']}, '')
    else:
        return returns(6, {}, '缺少参数！')


@order.route('/confirm', methods=['post'])
def order_confirm():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('id'):
        confirm_order(data['id'])
        return returns(0, {'id': data['id']}, '')
    else:
        return returns(6, {}, '缺少参数！')


@order.route('/common/upload', methods=['post'])
def common_upload():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    file = request.files['file']
    filename = secure_filename(file.filename)
    if filename.startswith('.'):
        name = file.filename.split('.')[0]
        ext = file.filename.split('.')[1]
        filename = '_'.join(lazy_pinyin(name)) + '.' + ext
    else:
        name = file.filename.split('.')[0]
        ext = file.filename.split('.')[1]
        filename = '_'.join(lazy_pinyin(name)) + '.' + ext
    new_filename = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1]
    file.save(os.path.join('/home/lcr/files', new_filename))
    return returns(0, {'url': path_to_url(new_filename)}, '成功！')


@order.route('/common', methods=['post'])
def common_create():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('id') and data.__contains__('text') and data.__contains__('imageUrl') and data.__contains__('rate'):
        c = create_common(data['id'], data['text'], data['imageUrl'], data['rate'])
        return returns(0, {'id': c.id}, '')
    else:
        return returns(6, {}, '缺少参数！')
