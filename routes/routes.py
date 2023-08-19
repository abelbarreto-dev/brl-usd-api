from flask import (
    Response,
    request,
)

from models.models import (
    QuotationBrlUsd,
    QuotationUsdBrl,
)

from flask_app.flask_app import create_app

from controller.controller import Controller

from decorators.error_control import json_error_handler

app = create_app()


@app.get("/usd-price-brl")
async def usd_price_brl() -> Response:
    return await Controller.usd_price_brl()


@app.get("/brl-price-usd")
async def brl_price_usd() -> Response:
    return await Controller.brl_price_usd()


@app.post("/usd-to-brl")
@json_error_handler
async def usd_to_brl():
    usd_json = QuotationUsdBrl.model_validate(request.json)

    return await Controller.usd_to_brl(usd_json)


@app.post("/brl-to-usd")
async def brl_to_usd(brl_json: QuotationBrlUsd) -> Response:
    pass
