from flask import Flask


def create_app() -> Flask:
    brynn = Flask(__name__)

    return brynn
