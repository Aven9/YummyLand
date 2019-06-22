from flask import Flask, render_template
from flask_session import Session
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/shop_category/<string:category>')
def shop_category(category):
    return render_template('shopCategory.html', category=category)


@app.route('/shopping_cart')
def shopping_cart():
    return render_template('shoppingCart.html')


@app.route('/setting')
def setting():
    return render_template('setting.html')
