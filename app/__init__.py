from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# flask instance (__name__is the current module (maybe; 90% sure))
app = Flask(__name__)
# configure app with Config class
app.config.from_object(Config)
# database
db = SQLAlchemy(app)
# migration engine
migrate = Migrate(app, db)
# user login state manager
login = LoginManager(app)
# tell the manager what func logs in user so it can use @login_requried
login.login_view = 'login'

# from app directory
from app import routes, models
