import os

"""DB CONFIG"""

DB_DIALECT = 'postgres'
DB_DRIVER = 'psycopg2'
DB_USER = os.environ.get('DB_USER', 'extralogicdata')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'extralogicdata')
DB_HOST_DOCKER = os.environ.get('DB_HOST', '192.168.99.100')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = 'extralogicdata'

# Example [postgresql+psycopg2]://extralogicdata:extralogicdata@192.168.99.100:5432/extralogicdata
DATABASE_URI = f'{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST_DOCKER}:{DB_PORT}/{DB_NAME}'

# Heroku DATABASE_URL
database_url = os.environ.get('DATABASE_URL', DATABASE_URI)
DATABASE_URI = database_url.replace('postgres', 'postgresql')
""""""

"""App Config"""


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    # SQLALCHEMY_ECHO = True
    DEBUG = True


""""""
