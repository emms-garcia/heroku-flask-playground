import os

from playground.utils.env import ENV_KEY


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'super-secret'


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.environ.get('SECRET_KEY')


CONFIG = dict(
    DEVELOPMENT=DevelopmentConfig,
    PRODUCTION=ProductionConfig,
).get(os.environ.get(ENV_KEY), DevelopmentConfig)
