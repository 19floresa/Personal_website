from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask instance (__name__is the current module (maybe; 90% sure))
app = Flask(__name__)
# configure app with Config class
app.config.from_object(Config)
# database
db = SQLAlchemy(app)
# migration engine
migrate = Migrate(app, db)

# from app directory
from app import routes, models
