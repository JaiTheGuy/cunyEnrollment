import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    MONGODB_SETTINGS = { 'db' : 'CUNY_First' }


    