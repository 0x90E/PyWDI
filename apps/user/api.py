from flask_restful import Resource
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from apps.user.models import User
from apps.auth.auth import Auth
from apps.common.http_return_format import return_fail_http_json_result, return_success_http_json_result


class Users(Resource):
    def get(self):
        result = Auth.identify(Auth, request)
        if (result['status'] and result['data']):
            user = User.get(User, result['data'])
            returnUser = {
                'id': user.id,
                'name': user.username,
                'email': user.email
            }
            result = return_success_http_json_result(returnUser, "Request success")
        return jsonify(result)


class UserRegister(Resource):
    def post(self):
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            user = User(username, email)
            user.set_password(password)
            user.add(user)
            if user.id:
                return_user_info = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
                return jsonify(return_success_http_json_result(return_user_info, 'Register success'))
            else:
                return jsonify(return_fail_http_json_result('', 'Register failed'))

        except IntegrityError:
            return jsonify(return_fail_http_json_result('', 'username or email has been registered'))
