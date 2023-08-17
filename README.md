# BRL USD API
A Python project with web scrapping to get dollar current value in real or swap them and vice versa.
This software only works with **US Dollar <> Brazilian Real** swap operations.

That's a Rest API.

## Summary

* [Dependencies](#dependencies)
* [API Routes](#api-routes)
* [Models](#models)
* [How to Run](#how-to-run)

## Dependencies
It is a list of known project dependencies, you can find all of them at
[requirements.txt](requirements.txt) file.

```pythonset
{
  "Python3.x",
  "Pydantic",
  "Flusk",
  "BeautifulSoap4",
}
```

## API Routes
See each route and each HTTP method.
* GET `/usd-price-brl`
  * How much is US Dollar in Brazilian Real
* GET `/brl-price-usd`
  * How much is Brazilian Real in US Dollar
* POST `/usd-to-brl`
  * Swap from US Dollar to Brazilian Real
* POST `/brl-to-usd`
  * Swap from Brazilian Real to US Dollar

## Models
See the models used at this project to make a request, you need:

```
Real to Dollar, you send Brazilian Reals then receive US Dollars;
```
```json
{
  "value_brl": "0.00"
}
```

```
Dollar to Real, you send US Dollars then receive Brazilian Reals;
```
```json
{
  "value_usd": "0.00"
}
```

## How to Run
Just run the file [main.py](main.py) and use a software to make requests for each route.
You can find our routes at [API Routes](#api-routes).

That's All Folks!
