from investing.investing import Investing

from models.models import (
    Money,
    QuotationBrlUsd,
    QuotationUsdBrl,
)

from enums.enums import SwapType


class Exchange(Investing):
    async def swap_usd_to_brl(self, usd_json: QuotationUsdBrl) -> Money:
        brl_quot = self.investing_usd_to_brl()

        reals = brl_quot * usd_json.value_usd

        money = Money()

        money.value_usd = usd_json.value_usd
        money.value_brl = reals
        money.quotation = brl_quot
        money.swap_type = SwapType.USD_TO_BRL.value

        return money

    async def swap_brl_to_usd(self, brl_json: QuotationBrlUsd) -> Money:
        usd_quot = self.investing_brl_to_usd()

        dollars = usd_quot * brl_json.value_brl

        money = Money()

        money.value_brl = brl_json.value_brl
        money.value_usd = dollars
        money.quotation = usd_quot
        money.swap_type = SwapType.BRL_TO_USD.value

        return money
