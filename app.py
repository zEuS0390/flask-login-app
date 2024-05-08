from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from datetime import timedelta

from db import db, User

bcrypt = Bcrypt()
login_manager = LoginManager()
mqtt = Mqtt()
socketio = SocketIO()

def create_app():
  app = Flask(__name__)

  app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=1) # set the session cookie expiration by 1 day
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
  app.config["SECRET_KEY"] = "52deae35d7cc4ca4dec68135d1da56eb"
  app.config['MQTT_BROKER_URL'] = 'localhost'
  app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
  app.config['MQTT_USERNAME'] = 'user'  # set the username here if you need authentication for the broker
  app.config['MQTT_PASSWORD'] = 'pass123'  # set the password here if the broker demands authentication

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mqtt.init_app(app)
  socketio.init_app(app)

  with app.app_context():
    db.create_all()

  return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
