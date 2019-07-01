from flask import Blueprint, session, request
import random
import smtplib

from ..lib.utils import returns, send_email

user = Blueprint('user', __name__)


@user.route('/verificationCode', method=['post'])
def verification_code():
    data = request.get_json()
    if data.__contains__('email'):
        session['code'] = random.randint(1000, 9999)
        try:
            send_email(data['email'], '验证码', session['code'])
            return returns(0, {}, '成功')
        except smtplib.SMTPException:
            return returns(5, {}, '邮件发送错误！')
    else:
        return returns(6, {}, '缺少参数！')


@user.route('/register', method=['post'])
def register():
    data = request.get_json()
    if data.__contains__('email') and data.__contains__('username') and data.__contains__('password') and data.__contains__('code'):
        if data['code'] == session['code']:
            return returns(0, {}, '成功！')
        else:
            return returns(7, {}, '验证码错误！')
    else:
        return returns(6, {}, '缺少参数！')


