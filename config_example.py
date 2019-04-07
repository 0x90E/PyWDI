class ConfigBase:
    DEBUG = True

    DB_ENGINE_PREFIX = 'mysql+pymysql'
    DB_USER = ''
    DB_PASSWORD = ''
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_NAME = 'pywdi'


class Produection(ConfigBase):
    def __init__(self):
        DEBUG = False


Config = ConfigBase
