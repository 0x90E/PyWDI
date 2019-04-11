from .api import Login


def init_route(api):
    api.add_resource(Login, '/login')
