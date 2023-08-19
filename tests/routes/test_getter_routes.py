from flask.testing import FlaskClient

from decimal import Decimal

from json import loads

from models.models import Money

from enums.enums import SwapType

from tests.conftest import client


def test_usd_to_brl_success(client: FlaskClient) -> None:
    url_link = "/usd-price-brl"

    response = client.get(url_link)

    assert response.status_code == 201

    data_obj = loads(response.data)

    money = Money.model_validate(data_obj)

    assert money.value_usd == Decimal("1.00")
    assert money.swap_type == SwapType.USD_TO_BRL
    assert money.value_brl == money.quotation


def test_brl_to_usd_success(client: FlaskClient) -> None:
    url_link = "/brl-price-usd"

    response = client.get(url_link)

    assert response.status_code == 201

    data_obj = loads(response.data)

    money = Money.model_validate(data_obj)

    assert money.value_brl == Decimal("1.00")
    assert money.swap_type == SwapType.BRL_TO_USD
    assert money.value_usd == money.quotation
