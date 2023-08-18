from os import getenv

from dotenv import load_dotenv


class Exchange:
    _usd_to_brl: str = None
    _brl_to_usd: str = None

    def __init__(self) -> None:
        load_dotenv()
        self._usd_to_brl = getenv("USD_TO_BRL")
        self._brl_to_usd = getenv("BRL_TO_USD")
