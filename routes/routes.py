from flask import Flask, Response

FILE = "routes/routes.py"

app = Flask(FILE)


@app.get("/usd-price-brl")
async def usd_price_brl() -> Response:
    pass


@app.get("/brl-price-usd")
async def brl_price_usd() -> Response:
    pass


@app.post("/usd-to-brl")
async def usd_to_brl() -> Response:
    pass


@app.post("/brl-to-usd")
async def brl_to_usd() -> Response:
    pass
