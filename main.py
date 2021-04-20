from flask import Flask, request, jsonify
from waitress import serve
from paste.translogger import TransLogger
from config import logger
from rphelpers import log_payload, create_response, is_authenticated, unauthorized
from functools import wraps

# APP CONFIG
api = Flask(__name__)
api_name = "py-webhook"
api_version = "v1"

# REQUEST PATH
base_path = f'/api/{api_version}/{api_name}'

# MAIN ENTRY POINT
if __name__ == '__main__':
    try:
        serve(TransLogger(api, logger=logger), host='0.0.0.0', port=5000, threads=16)
    except Exception as ex:
        logger.exception(ex)


# BASIC AUTHENTICATION WRAPPER
def requires_basic_authentication(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            auth = request.authorization
            if not auth or not is_authenticated(auth.username, auth.password):
                return unauthorized()
            return f(*args, **kwargs)
        except Exception as e:
            logger.exception(e)

    return wrapper


# CORS CHECKPOINT
@api.route(f'{base_path}/events', methods=['OPTIONS'])
def pre_flight():
    return create_response({}), 200


@api.route(f'{base_path}/events', methods=['POST'])
def process_event():
    try:
        payload = request.json
        log_payload("REQUEST BODY", payload)

        # APPLICATION LOGIC HERE #

        return create_response({
            "status": "success"
        }), 200

    except Exception as e:
        logger.exception(e)
