from os import getenv

from bs4 import BeautifulSoup

from dotenv import load_dotenv

from responses.responses import http_exception

from abc import ABC

from decimal import Decimal

from requests import (
    get as urlopen, Response,
)


class Investing(ABC):
    _HTML_PARSER: str = "html.parser"

    def _make_request(self, url) -> Response:
        data_site = urlopen(url)

        status_code = data_site.status_code

        if status_code not in (200,):
            http_exception(
                "problem to access investing.com website",
                status_code,
            )

        return data_site

    def _get_quotation(self, url: str = None) -> Decimal:
        investing = self._make_request(url).content

        extract = BeautifulSoup(investing, self._HTML_PARSER)

        span_tag = extract.find_all(
            "span",
            {
                "class": "text-2xl"
            },
            True
        )

        money_str = span_tag[0].text

        money_str = money_str.replace(",", ".")

        return Decimal(money_str)

    def investing_usd_to_brl(
            self,
            deps: bool = load_dotenv(),
            url: str = getenv("USD_TO_BRL")
    ) -> Decimal:
        reals = self._get_quotation(url)

        return reals

    def investing_brl_to_usd(
            self,
            deps: bool = load_dotenv(),
            url: str = getenv("BRL_TO_USD")
    ) -> Decimal:
        dollars = self._get_quotation(url)

        return dollars
