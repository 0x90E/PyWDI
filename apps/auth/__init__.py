from flask import Blueprint
from flask_restful import Api

from .route import init_route


def init_app(app):
    api_bp = Blueprint('api_user', __name__, url_prefix="/api/user")
    api = Api(api_bp)
    init_route(api)
    app.register_blueprint(api_bp)
