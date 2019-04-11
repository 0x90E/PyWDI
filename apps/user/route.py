from .api import Users, UserRegister


def init_route(api):
    api.add_resource(Users, '/users')
    api.add_resource(UserRegister, '/register')
