from flask.testing import FlaskClient

from os import getenv

from decimal import Decimal

from json import loads

from models.models import (
    Money,
    QuotationUsdBrl,
    QuotationBrlUsd,
)

from enums.enums import SwapType

from tests.conftest import client


def test_usd_to_brl_success(client: FlaskClient) -> None:
    url_link = "/usd-to-brl"

    content_type = getenv("CONTENT_TYPE")

    usd_json = QuotationUsdBrl(
        value_usd=Decimal("5.00")
    )

    response = client.post(
        url_link,
        data=usd_json.model_dump_json(),
        content_type=content_type,
    )

    assert response.status_code == 201

    usd_obj = loads(response.data)

    money = Money.model_validate(usd_obj)

    assert money.value_usd == usd_json.value_usd
    assert money.swap_type == SwapType.USD_TO_BRL