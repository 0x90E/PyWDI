from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(app):
    db_engine_prefix = app.config['DB_ENGINE_PREFIX']
    db_user = app.config['DB_USER']
    db_password = app.config['DB_PASSWORD']
    db_host = app.config['DB_HOST']
    db_port = app.config['DB_PORT']
    db_name = app.config['DB_NAME']
    db_engine = '{}://{}:{}@{}:{}/{}'.format(db_engine_prefix, db_user, db_password, db_host, db_port, db_name)

    engine = create_engine(db_engine, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base.query = db_session.query_property()

    import apps.auth.models
    Base.metadata.create_all(bind=engine)
