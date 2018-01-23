from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.debug = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:13540144151@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = 'dafads42325ads'
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/upload/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/upload/user/")
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_buleprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_buleprint, url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404