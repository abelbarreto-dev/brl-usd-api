from re import match

from decimal import Decimal

from exceptions.money_except import MoneyException


REGEXES = {
    "money": r"^[0-9]+(?:\.[0-9]{2})?$"
}


def money_checker(money: Decimal) -> None:
    money_str = str(money)

    money_regex = REGEXES["money"]

    if not match(money_regex, money_str):
        raise MoneyException(money_str)
