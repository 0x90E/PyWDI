from flask import Flask

from apps import auth, database


def create_app():
    app = Flask(__name__)

    try:
        from config import Config
    except ModuleNotFoundError:
        print("Please copy config.py from config_example.py")
        exit(1)

    app.config.from_object(Config)
    auth.init_app(app)
    return app


def create_db(app):
    database.init_db(app)


if __name__ == '__main__':
    app = create_app()
    db = create_db(app)
    app.run(debug=app.config['DEBUG'])
