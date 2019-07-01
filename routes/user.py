import uuid
from flask import Blueprint, session, request
import random
import smtplib
import os
from werkzeug.utils import secure_filename
from pypinyin import lazy_pinyin

from lib.utils import returns, send_email
from services.user import create_user, query_user, login, get_user, modify_user, change_image_url, get_address, add_address, modify_address, delete_address

user = Blueprint('user', __name__)


@user.route('/verificationCode', methods=['post'])
def verification_code():
    data = request.get_json()
    if data.__contains__('email'):
        if query_user(data['email']) is False:
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


@user.route('/register', methods=['post'])
def register():
    data = request.get_json()
    if data.__contains__('email') and data.__contains__('username') and data.__contains__('password') and data.__contains__('code'):
        if data['code'] == session['code']:
            create_user(data['username'], data['email'], data['password'])
            return returns(0, {'status': 'success'}, '成功！')
        else:
            return returns(7, {}, '验证码错误！')
    else:
        return returns(6, {}, '缺少参数！')


@user.route('/login', methods=['post'])
def login():
    data = request.get_json()
    if data.__contains__('email') and data.__contains__('password'):
        if login(data['email'], data['password']) is True:
            return returns(3, {}, '账号或密码错误')
        else:
            session['email'] = data['email']
            return returns(0, {'status': 'success'}, '成功！')
    return returns(6, {}, '缺少参数！')


@user.route('/userInfo/get', methods=['get'])
def user_info_get():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    one = get_user(email)
    user_info = {
        "username": one.username,
        "email": one.email,
        "imageUrl": one.imageUrl,
        "birthday": one.birthday
    }
    return returns(0, user_info, '成功！')


@user.route('/userInfo/modify', methods=['post'])
def user_info_modify():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('username') and data.__contains__('birthday'):
        modify_user(data['username'], email, data['birthday'])
        return returns(0, {'status': 'success'}, '成功！')
    else:
        return returns(6, {}, '缺少参数！')


@user.route('/userInfo/upload', methods=['post'])
def user_info_upload():
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
    change_image_url(email, new_filename)
    return returns(0, {'status': 'success'}, '成功！')


@user.route('/address/get', methods=['get'])
def address_get():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    return returns(0, {'address': get_address(email)}, '')


@user.route('/address/modify', methods=['post'])
def address_modify():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('name') and data.__contains__('phone') and data.__contains__('province') and data.__contains__('city') and data.__contains__('detail') and data.__contains__('id'):
        modify_address(email, data['id'], data['name'], data['phone'], data['province'], data['city'], data['detail'])
        return returns(0, {'status': 'success'}, '成功！')
    else:
        return returns(6, {}, '缺少参数！')


@user.route('/address/add', methods=['post'])
def address_add():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('name') and data.__contains__('phone') and data.__contains__('province') and data.__contains__('city') and data.__contains__('detail'):
        add_address(email, data['name'], data['phone'], data['province'], data['city'], data['detail'])
        return returns(0, {'status': 'success'}, '成功！')
    else:
        return returns(6, {}, '缺少参数！')


@user.route('/address/delete', methods=['post'])
def address_delete():
    email = session['email']
    if email is None:
        return returns(1, {}, '未登录或登陆过期')
    data = request.get_json()
    if data.__contains__('id'):
        delete_address(email, data['id'])
        return returns(0, {'status': 'success'}, '成功！')
    else:
        return returns(6, {}, '缺少参数！')
