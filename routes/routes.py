from flask import (
    Response,
    request,
)

from models.models import (
    Money,
    QuotationBrlUsd,
    QuotationUsdBrl,
)

from flask_app.flask_app import create_app

from controller.controller import Controller

app = create_app()


@app.get("/usd-price-brl")
async def usd_price_brl() -> Response:
    return await Controller.usd_price_brl()


@app.get("/brl-price-usd")
async def brl_price_usd() -> Response:
    return await Controller.brl_price_usd()


@app.post("/usd-to-brl")
async def usd_to_brl():
    usd_json = QuotationUsdBrl.model_validate(request.json)

    return await Controller.usd_to_brl(usd_json)


@app.post("/brl-to-usd")
async def brl_to_usd(brl_json: QuotationBrlUsd) -> Response:
    pass
