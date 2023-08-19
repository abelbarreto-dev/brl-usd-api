import pytest

from main import app

from flask.testing import FlaskClient

from typing import Generator


@pytest.fixture(scope="function")
def client() -> Generator:
    with FlaskClient(app) as test:
        yield test
