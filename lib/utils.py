from flask import jsonify
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def returns(code, data, msg):
    return jsonify({'code': code, 'data': data, 'msg': msg})


def send_email(to_account, subject, content):
    # 1. 实例化SMTP
    smtp = smtplib.SMTP()

    # 2. 链接邮件服务器
    smtp.connect("smtp.163.com")

    # 3. 配置发送邮箱的用户名和密码
    smtp.login("yunnnzhan@163.com", "yunzhan123456")

    # 4. 配置发送内容msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = "yunnnzhan@163.com"
    msg['To'] = to_account

    # 5. 配置发送邮箱，接受邮箱，以及发送内容
    smtp.sendmail("yunnnzhan@163.com", to_account, msg.as_string())

    # 6. 关闭邮件服务
    smtp.quit()


def path_to_url(path):
    return 'http://127.0.0.1:5000/static/files/' + path
