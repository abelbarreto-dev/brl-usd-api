from functools import wraps

from os import getenv

from flask import (
    jsonify,
    make_response,
)

from dotenv import load_dotenv

load_dotenv()


def json_error_handler(func):
    content_type = getenv("CONTENT_TYPE")

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            error_message = {
                "message": ve.args[0]
            }

            response = make_response(jsonify(error_message), 400)
            response.headers["Content-Type"] = content_type
            return response

    return wrapper
