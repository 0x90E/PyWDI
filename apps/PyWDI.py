from flask import Flask, request

from apps import user, auth
from apps.database import database_manager


def create_app():
    app = Flask(__name__)

    try:
        from config import config
    except ModuleNotFoundError:
        print("Please copy config.py from config_example.py")
        exit(1)

    app.config.from_object(config)

    user.init_app(app)
    auth.init_app(app)
    return app


def create_db():
    database_manager.init_db()


if __name__ == '__main__':
    app = create_app()
    db = create_db()

    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
