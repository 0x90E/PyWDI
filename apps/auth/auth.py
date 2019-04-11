import datetime
import time
import jwt
from flask import jsonify

from apps.user.models import User
from apps.common.http_return_format import return_fail_http_json_result, return_success_http_json_result
from config import config


class Auth():
    @staticmethod
    def encode_auth_token(user_id, login_time):
        try:
            datetime_now = datetime.datetime.utcnow()
            payload = {
                'exp': datetime_now + datetime.timedelta(seconds=config.JWT_TOKEN_EXPIRED),
                'iat': datetime_now,
                'iss': 'PyWDI',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(payload, config.JWT_SECRET_KEY, algorithm='HS256')
        except Exception as e:
            print(e)
            raise e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, config.JWT_SECRET_KEY, leeway=datetime.timedelta(seconds=config.JWT_TOKEN_EXPIRED))
            if ('data' in payload and 'id' in payload['data']):
                return True, payload

        except jwt.ExpiredSignatureError:
            error_message = 'Token expired'
        except jwt.InvalidTokenError:
            error_message = 'Token invalid'

        return False, error_message

    def authenticate(self, username, password):
        user_info = User.query.filter_by(username=username).first()
        if not user_info:
            return jsonify(return_fail_http_json_result('', 'User not found'))

        if not user_info.check_password(password):
            return jsonify(return_fail_http_json_result('', 'Wrong password'))

        login_time = int(time.time())
        user_info.login_time = login_time
        user_info.update()
        token = self.encode_auth_token(user_info.id, login_time)
        return jsonify(return_success_http_json_result(token.decode(), 'Request success'))

    def identify(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return return_fail_http_json_result('', 'No token information')

        auth_token_info = auth_header.split(" ")
        if (not auth_token_info or auth_token_info[0] != 'JWT' or len(auth_token_info) != 2):
            return return_fail_http_json_result('', 'Authorization information incorrect')

        auth_token = auth_token_info[1]
        result, payload = self.decode_auth_token(auth_token)
        if not result:
            return return_fail_http_json_result('', payload)

        user = User.get(User, payload['data']['id'])
        if not user:
            return return_fail_http_json_result('', 'User not found')

        if (user.login_time != payload['data']['login_time']):
            return return_fail_http_json_result('', 'Token has changed, Please login again')

        return return_success_http_json_result(user.id, 'Request success')
