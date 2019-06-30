from flask import Flask
from flask_session import Session
from .routes import route

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

route(app)

if __name__ == '__main__':
    app.run()
