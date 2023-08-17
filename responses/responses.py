from flask import Response, abort

from typing import Any


def http_response(
        data: Any,
        status_code: int = 201,
) -> Response:
    return Response(
        response=data,
        status=status_code,
        content_type="Application/json"
    )


def http_exception(
        message: str,
        status_code: int = 400
) -> None:
    abort(status_code, message)
