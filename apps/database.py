from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import config

Base = declarative_base()


class DatabaseManager:
    def __init__(self):
        self.db_session = None

    def init_db(self):
        db_engine_prefix = config.DB_ENGINE_PREFIX
        db_user = config.DB_USER
        db_password = config.DB_PASSWORD
        db_host = config.DB_HOST
        db_port = config.DB_PORT
        db_name = config.DB_NAME
        db_engine = '{}://{}:{}@{}:{}/{}'.format(db_engine_prefix, db_user, db_password, db_host, db_port, db_name)

        engine = create_engine(db_engine, convert_unicode=True)
        self.db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
        Base.query = self.db_session.query_property()

        import apps.user.models
        Base.metadata.create_all(bind=engine)

    def get_db_session(self):
        return self.db_session


database_manager = DatabaseManager()
