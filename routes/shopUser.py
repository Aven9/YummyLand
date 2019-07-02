from flask import Blueprint, session, request
import random
import smtplib
import os
from werkzeug.utils import secure_filename
from pypinyin import lazy_pinyin
import uuid

from lib.utils import returns, send_email, path_to_url
from services.shopUser import get_shop, create_shop, get_shop_detail, modify_shop_detail, get_commons

shopUser = Blueprint('shopUser', __name__)


@shopUser.route('/verificationCode', methods=['post'])
def verification_code():
    data = request.get_json()
    if data.__contains__('email'):
        if get_shop(data['email']) is not None:
            return returns(4, {}, '账号已被注册!')
        else:
            session['code'] = random.randint(1000, 9999)
            try:
                send_email(data['email'], '验证码', '注册验证码为' + str(session['code']))
                return returns(0, {'status': 'success'}, '成功')
            except smtplib.SMTPException:
                return returns(5, {}, '邮件发送错误！')
    else:
        return returns(6, {}, '缺少参数！')


@shopUser.route('/register', methods=['post'])
def register_shop():
    data = request.get_json()
    if data.__contains__('name') and data.__contains__('email') and data.__contains__('password') and data.__contains__('code') and data.__contains__('address') and data.__contains__('classification') and data.__contains__('introduction'):
        if data['code'] == session['code']:
            shop = create_shop(data['email'], data['name'], data['password'], data['address'], data['classification'], data['introduction'])
            return returns(0, {'id': shop.id}, '')
        else:
            return returns(7, {}, '验证码错误！')
    else:
        return returns(6, {}, '缺少参数！')


@shopUser.route('/login', methods=['post'])
def login_shop():
    data = request.get_json()
    if data.__contains__('email') and data.__contains__('password'):
        shop = get_shop(data['email'])
        if shop is None:
            return returns(2, {}, '未注册账号！')
        if shop.password != data['password']:
            return returns(3, {}, '账号或密码错误')
        session['email'] = shop.email
        return returns(0, {'id': shop.id}, '')
    else:
        return returns(6, {}, '缺少参数！')


@shopUser.route('/shop/get', methods=['get'])
def shop_get_detail():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    return returns(0, get_shop_detail(email), '')


@shopUser.route('/shop/upload', methods=['get'])
def shop_image_upload():
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
    file.save(os.path.join(os.path.abspath(os.path.dirname('.')), 'static', 'files', new_filename))
    return returns(0, {'url': path_to_url(new_filename)}, '成功！')


@shopUser.route('/shop/modify', methods=['post'])
def shop_detail_modify():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if not data.__contains__('name'):
        return returns(6, {}, '缺少参数！')
    if not data.__contains__('imageUrl'):
        return returns(6, {}, '缺少参数！')
    if not data.__contains__('introduction'):
        return returns(6, {}, '缺少参数！')
    if not data.__contains__('phone'):
        return returns(6, {}, '缺少参数！')
    if not data.__contains__('address'):
        return returns(6, {}, '缺少参数！')
    if not data.__contains__('classification'):
        return returns(6, {}, '缺少参数！')
    if not data.__contains__('food'):
        return returns(6, {}, '缺少参数！')
    modify_shop_detail(email, data['name'], data['imageUrl'], data['introduction'], data['phone'], data['address'], data['classification'], data['food'])
    return returns(0, {'status': 'success'}, '成功')


@shopUser.route('/shop/common', methods=['get'])
def shop_common_get():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    return returns(0, {'commons': get_commons(email)}, '')
