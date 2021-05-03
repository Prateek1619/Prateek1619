import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'abc123ced456'
    SQLALCHEMY_DATABASE_URI = "postgresql://prateek:prateek@123@localhost:5432/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #JWT_TOKEN_EXPIRES = False
    #WTF_CSRF_ENABLED = True
    #WTF_CSRF_SECRET_KEY = os.getenv('SECRET_KEY') or 'abc123ced456'



class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True