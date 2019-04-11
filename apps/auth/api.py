from flask_restful import Resource
from flask import jsonify, request

from apps.auth.auth import Auth


class Login(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        return Auth.authenticate(Auth, username, password)
