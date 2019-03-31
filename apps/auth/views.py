from flask_restful import Resource




class User(Resource):
    def get(self, user_id):
        return {user_id: 'hello {}'.format(user_id)}
