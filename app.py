from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tdfcxlreofipuf:ff9105caefd58aa5f9d486fa9f582770295061e2c82f58ae3675dfa24ffbc280@ec2-174-129-227-51.compute-1.amazonaws.com:5432/dd9p761ii1tog0'

# 设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
app.config['UPLOAD_FOLDER'] = '/home/lcr/files'
Session(app)
db = SQLAlchemy(app)

from routes import route

route(app)

if __name__ == '__main__':
    app.run()
