from flask.testing import FlaskClient

from decimal import Decimal

from json import loads

from models.models import (
    Money,
    QuotationUsdBrl,
    QuotationBrlUsd,
)

from enums.enums import SwapType

from tests.conftest import client
