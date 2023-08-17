from flask import Response, abort


def http_response(
        message: str,
        status_code: int = 201,
) -> Response:
    return Response(
        {
            "message": message
        },
        status=status_code,
        content_type="Application/json"
    )


def http_exception(
        message: str,
        status_code: int = 400
) -> None:
    abort(status_code, message)
