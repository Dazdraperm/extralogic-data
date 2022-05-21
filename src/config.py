import os

"""DB CONFIG"""

DB_DIALECT = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_NAME = 'extralogicdata'
DB_USER = os.environ.get('DB_USER', 'extralogicdata')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'extralogicdata')
DB_HOST_DOCKER = os.environ.get('DB_HOST', '192.168.99.100')
DB_PORT = os.environ.get('DB_PORT', '5432')

DATABASE_URI = f'{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST_DOCKER}:{DB_PORT}/{DB_NAME}'

""""""
