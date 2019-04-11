def return_success_http_json_result(data, msg):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def return_fail_http_json_result(data, msg):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }
