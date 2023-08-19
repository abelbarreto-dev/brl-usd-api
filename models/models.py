from pydantic import BaseModel

from decimal import Decimal

from typing import Optional

from enums.enums import SwapType


class Money(BaseModel):
    value_brl: Decimal = Decimal("0.00")
    value_usd: Decimal = Decimal("0.00")
    swap_type: Optional[SwapType] = None
    quotation: Optional[Decimal] = None


class QuotationUsdBrl(BaseModel):
    value_usd: Decimal


class QuotationBrlUsd(BaseModel):
    value_brl: Decimal
