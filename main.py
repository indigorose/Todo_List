from flask import Flask, render_template
# request, url_for, redirect, flash, send_from_directory
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
#
# app.config['SECRET_KEY'] =
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# filename = "static/files/cheat_sheet.pdf"


# #CREATE TABLE IN DB
# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))
#
#     def check_password(self, password):
#         pass


# Line below only required once, when creating DB.
# db.create_all()
#
# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
