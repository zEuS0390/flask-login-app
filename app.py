from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from db import db, User

bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
  app = Flask(__name__)

  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
  app.config["SECRET_KEY"] = "my-secret"

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)

  with app.app_context():
    db.create_all()

  return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))