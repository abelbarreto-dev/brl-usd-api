from pydantic import BaseModel

from decimal import Decimal

from typing import Optional

from enums.enums import SwapType


class Money(BaseModel):
    value_brl: Decimal = Decimal("0.00")
    value_usd: Decimal = Decimal("0.00")
    swap_type: Optional[SwapType] = None


class QuotationUsdBrl(BaseModel):
    value_in_brl: Decimal
    usd_price: Decimal
    value_usd: Decimal = Decimal("1.00")


class QuotationBrlUsd(BaseModel):
    value_in_usd: Decimal
    brl_price: Decimal
    value_brl: Decimal = Decimal("1.00")
