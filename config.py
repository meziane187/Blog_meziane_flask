import os
from dotenv import load_dotenv
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config(object):
    DEBUG=os.environ.get('DEBUG')
    TESTING=os.environ.get('TESTING')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    FLASK_ENV=os.environ.get('FLASK_ENV')
    FLASK_DEBUG=os.environ.get('FLASK_DEBUG')
    FLASK_APP=os.environ.get('FLASK_APP')


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'
    LOG_LEVEL = 'DEBUG'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'development'
    LOG_LEVEL = 'DEBUG'


