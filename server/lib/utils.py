from flask import jsonify


def returns(code, data, msg):
    return jsonify({'code': code, 'data': data, 'msg': msg})
