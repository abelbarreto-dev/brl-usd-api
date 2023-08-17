from re import match

from decimal import Decimal


REGEXES = {
    "money": r"^[0-9]+(?:\.[0-9]{2})?$"
}


def money_checker(money: Decimal) -> None:
    money_str = str(money)

    money_regex = REGEXES["money"]

    exception_msg = f"error: the value '{money_str}' is not valid for money."

    if not match(money_regex, money_str):
        raise Exception(exception_msg)
