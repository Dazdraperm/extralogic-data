import os

"""DB CONFIG"""

DB_DIALECT = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_NAME = 'extralogicdata'
DB_USER = os.environ.get('DB_USER', 'postgres'),
DB_PASSWORD = os.environ.get('DB_PASSWORD', '123321'),
DB_HOST_LOCAL = os.environ.get('DB_HOST', '127.0.0.1'),
DB_HOST_DOCKER = os.environ.get('DB_HOST', '192.168.99.100'),
DB_PORT = os.environ.get('DB_PORT', '5432'),

if os.environ.get('DOCKER').lower() == 'true':
    DB_HOST = DB_HOST_DOCKER
else:
    DB_HOST = DB_HOST_LOCAL

DATABASE_URI = f'{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

""""""
