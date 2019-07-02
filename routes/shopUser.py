from flask import Blueprint, session, request

from lib.utils import returns, send_email

shopUser = Blueprint('shopUser', __name__)


@shopUser.route('/verificationCode', methods=['post'])
def verification_code():
    data = request.get_json()

