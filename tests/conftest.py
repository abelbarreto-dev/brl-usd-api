import pytest

from flask import Flask

from flask.testing import FlaskClient

from typing import Generator


@pytest.fixture(scope="function")
def client() -> Generator:
    app = Flask(__name__)

    with FlaskClient(app) as test:
        yield test
