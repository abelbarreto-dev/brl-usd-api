from decimal import Decimal

from models.models import Money

from flask import Response

from exchange.exchange import Exchange

from enums.enums import SwapType

from responses.responses import (
    http_exception,
    http_response,
)


class Controller:
    exchange: Exchange = Exchange()

    @classmethod
    async def usd_price_brl(cls) -> Response:
        money = Money()

        dollar_in_brl = cls.exchange.investing_usd_to_brl()

        money.value_usd = Decimal("1.00")
        money.value_brl = dollar_in_brl
        money.quotation = dollar_in_brl
        money.swap_type = SwapType.USD_TO_BRL.value

        return http_response(
            data=money.model_dump_json(),
            status_code=201,
        )

    @classmethod
    async def brl_price_usd(cls) -> Response:
        money = Money()

        real_in_usd = cls.exchange.investing_brl_to_usd()

        money.value_brl = Decimal("1.00")
        money.value_usd = real_in_usd
        money.quotation = real_in_usd
        money.swap_type = SwapType.BRL_TO_USD.value

        return http_response(
            data=money.model_dump_json(),
            status_code=201,
        )

    @classmethod
    async def usd_to_brl(cls, usd_json: Money) -> Response:
        pass

    @classmethod
    async def brl_to_usd(cls, brl_json: Money) -> Response:
        pass
