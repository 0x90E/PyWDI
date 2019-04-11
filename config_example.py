class ConfigBase:
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 5000

    DB_ENGINE_PREFIX = 'mysql+pymysql'
    DB_USER = ''
    DB_PASSWORD = ''
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_NAME = 'pywdi'

    JWT_SECRET_KEY = ''
    JWT_TOKEN_EXPIRED = 60

class Produection(ConfigBase):
    def __init__(self):
        DEBUG = False


config = ConfigBase()
