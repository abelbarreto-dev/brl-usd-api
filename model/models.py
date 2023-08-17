from pydantic import BaseModel

from decimal import Decimal


class Money(BaseModel):
    value_brl: Decimal = Decimal("0.00")
    value_usd: Decimal = Decimal("0.00")


class QuotationUsdBrl(BaseModel):
    value_in_brl: Decimal
    usd_price: Decimal
    value_usd: Decimal = Decimal("1.00")


class QuotationBrlUsd(BaseModel):
    value_in_usd: Decimal
    brl_price: Decimal
    value_brl: Decimal = Decimal("1.00")
