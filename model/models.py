from pydantic import BaseModel

from decimal import Decimal


class Money(BaseModel):
    value_brl: Decimal = Decimal("0.00")
    value_usd: Decimal = Decimal("0.00")
