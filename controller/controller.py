from models.models import Money

from flask import Response


class Controller:
    @classmethod
    async def usd_price_brl(cls) -> Response:
        pass

    @classmethod
    async def brl_price_usd(cls) -> Response:
        pass

    @classmethod
    async def usd_to_brl(cls, usd_json: Money) -> Response:
        pass

    @classmethod
    async def brl_to_usd(cls, brl_json: Money) -> Response:
        pass
