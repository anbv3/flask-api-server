import logging

from flask import Blueprint, request, current_app

from app.common import global_share

monitor = Blueprint('controllers', __name__)


@monitor.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@monitor.route('/alive', methods=['GET'])
def is_alive():
    alive = request.args.get('alive')
    if alive is None:
        if not global_share.is_alive:
            return '', 500
    else:
        global_share.is_alive = __str_to_bool(alive)
    return '', 200


def __str_to_bool(s):
    if s is True or s is False:
        return s
    s = str(s).strip().lower()
    return s not in ['false', 'f', 'n', '0', '']


@monitor.route('/hello')
def hello_world():
    logging.debug(current_app.config['DEBUG'])
    return 'Hello World!'
