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

URL_USD_BRL = "/usd-to-brl"
URL_BRL_USD = "/brl-to-usd"
CONTENT_TYPE = getenv("CONTENT_TYPE")


def test_usd_to_brl_success(client: FlaskClient) -> None:
    usd_json = QuotationUsdBrl(
        value_usd=Decimal("5.00")
    )

    response = client.post(
        URL_USD_BRL,
        data=usd_json.model_dump_json(),
        content_type=CONTENT_TYPE,
    )

    assert response.status_code == 201

    usd_obj = loads(response.data)

    money = Money.model_validate(usd_obj)

    assert money.value_usd == usd_json.value_usd
    assert money.swap_type == SwapType.USD_TO_BRL


def test_usd_to_brl_failure_case_1(client: FlaskClient) -> None:
    usd_json = QuotationUsdBrl(
        value_usd=Decimal("5.5")
    )

    response = client.post(
        URL_USD_BRL,
        data=usd_json.model_dump_json(),
        content_type=CONTENT_TYPE,
    )

    assert response.status_code == 400


def test_usd_to_brl_failure_case_2(client: FlaskClient) -> None:
    usd_json = QuotationUsdBrl(
        value_usd=Decimal("15.512")
    )

    response = client.post(
        URL_USD_BRL,
        data=usd_json.model_dump_json(),
        content_type=CONTENT_TYPE,
    )

    assert response.status_code == 400


def test_usd_to_brl_failure_case_3(client: FlaskClient) -> None:
    usd_json = QuotationUsdBrl(
        value_usd=Decimal("-5.54")
    )

    response = client.post(
        URL_USD_BRL,
        data=usd_json.model_dump_json(),
        content_type=CONTENT_TYPE,
    )

    assert response.status_code == 400


def test_brl_to_usd_success(client: FlaskClient) -> None:
    brl_json = QuotationBrlUsd(
        value_brl=Decimal("5.00")
    )

    response = client.post(
        URL_BRL_USD,
        data=brl_json.model_dump_json(),
        content_type=CONTENT_TYPE,
    )

    assert response.status_code == 201

    usd_obj = loads(response.data)

    money = Money.model_validate(usd_obj)

    assert money.value_brl == brl_json.value_brl
    assert money.swap_type == SwapType.BRL_TO_USD


def test_brl_to_usd_failure_case_1(client: FlaskClient) -> None:
    brl_json = QuotationBrlUsd(
        value_brl=Decimal("5.5")
    )

    response = client.post(
        URL_BRL_USD,
        data=brl_json.model_dump_json(),
        content_type=CONTENT_TYPE,
    )

    assert response.status_code == 400


def test_brl_to_usd_failure_case_2(client: FlaskClient) -> None:
    brl_json = QuotationBrlUsd(
        value_brl=Decimal("15.512")
    )

    response = client.post(
        URL_BRL_USD,
        data=brl_json.model_dump_json(),
        content_type=CONTENT_TYPE,
    )

    assert response.status_code == 400


def test_brl_to_usd_failure_case_3(client: FlaskClient) -> None:
    brl_json = QuotationBrlUsd(
        value_brl=Decimal("-5.54")
    )

    response = client.post(
        URL_BRL_USD,
        data=brl_json.model_dump_json(),
        content_type=CONTENT_TYPE,
    )

    assert response.status_code == 400
