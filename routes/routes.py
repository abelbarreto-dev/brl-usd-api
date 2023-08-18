from flask import Flask, Response

from models.models import Money

from controller.controller import Controller

app = Flask(__name__)


@app.get("/usd-price-brl")
async def usd_price_brl() -> Response:
    return await Controller.usd_price_brl()


@app.get("/brl-price-usd")
async def brl_price_usd() -> Response:
    pass


@app.post("/usd-to-brl")
async def usd_to_brl(usd_json: Money) -> Response:
    pass


@app.post("/brl-to-usd")
async def brl_to_usd(brl_json: Money) -> Response:
    pass
