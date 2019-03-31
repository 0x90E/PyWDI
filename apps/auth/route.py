from .views import User


def init_route(api):
    api.add_resource(User, '/<string:user_id>')