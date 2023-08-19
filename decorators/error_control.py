from functools import wraps

from werkzeug.exceptions import HTTPException

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
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as ve:
            error_message = {
                "message": ve.description
            }

            response = make_response(jsonify(error_message), ve.code)
            response.headers["Content-Type"] = content_type
            return response

    return wrapper
