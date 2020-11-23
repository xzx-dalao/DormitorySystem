from flask import Response, jsonify, make_response

# 定义返回json格式


def format(success=True, data='', msg=''):
    res = {
        'data': data,
        'describe': msg,
        "meta": {
            '请求状态': success,
            "status": 200
        }
    }
    return res
def format_false(success=True, data='', msg=''):
    res = {
            'data': data,
            'describe': msg,
            "meta": {
                '请求状态': success,
                "status": 201
            }
        }
    return res

def format_full(success=True, data='', msg=''):
    res = {
            'data': data,
            'describe': msg,
            "meta": {
                '请求状态': success,
                "status": 202
            }
        }
    return res

def format_nofind(success=True, data='', msg=''):
    res = {
            'data': data,
            'describe': msg,
            "meta": {
                '请求状态': success,
                "status": 203
            }
        }
    return res


def format_iscunzai(success=True, data='', msg=''):
    res = {
            'data': data,
            'describe': msg,
            "meta": {
                '请求状态': success,
                "status": 204
            }
        }
    return res