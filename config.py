import os

# location to put database if it doesnt exit
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # cryptographic key: used to generate secret keys
    SECRET_KEY = os.environ.get('SECRET_KEY') or '45fdff43DD0KKLIASGHF5f4d'
    
    # location of database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    # Deactivate sending the application a signal every time their is an update to the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
