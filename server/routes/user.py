from flask import Blueprint, session, request
import random

from ..lib.utils import returns

user = Blueprint('user', __name__)


@user.route('/verificationCode', method=['post'])
def verification_code():
    data = request.get_json()
    if data.__contains__('email'):
        session['code'] = random.randint(1000, 9999)

    else:
        returns(4, {}, '账号已被注册！')



