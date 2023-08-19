from decimal import Decimal

from models.models import (
    Money,
    QuotationBrlUsd,
    QuotationUsdBrl,
)

from flask import Response

from exchange.exchange import Exchange

from enums.enums import SwapType

from validator.validator import money_checker

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

        return http_response(money.model_dump_json())

    @classmethod
    async def brl_price_usd(cls) -> Response:
        money = Money()

        real_in_usd = cls.exchange.investing_brl_to_usd()

        money.value_brl = Decimal("1.00")
        money.value_usd = real_in_usd
        money.quotation = real_in_usd
        money.swap_type = SwapType.BRL_TO_USD.value

        return http_response(money.model_dump_json())

    @classmethod
    async def usd_to_brl(cls, usd_json: QuotationUsdBrl) -> Response:
        try:
            money_checker(usd_json.value_usd)
        except ValueError as ve:
            http_exception(ve.args[0])

        money = await cls.exchange.swap_usd_to_brl(usd_json)

        return http_response(money.model_dump_json())

    @classmethod
    async def brl_to_usd(cls, brl_json: QuotationBrlUsd) -> Response:
        pass
