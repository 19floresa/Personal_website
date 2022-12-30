import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '45fdff43DD0KKLIASGHF5f4d'
