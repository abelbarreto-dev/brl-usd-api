# BRL USD API
A Python project with web scraping to get dollar current value in real or swap them and vice versa.
This software only works with **US Dollar <> Brazilian Real** swap operations.

This project do a web scraping from the website [Investing](https://br.investing.com/).

That's a Rest API.

## Summary

* [Dependencies](#dependencies)
* [API Routes](#api-routes)
* [Models](#models)
* [How to Run](#how-to-run)
* [Install Dependencies](#install-dependencies)
* [Install Dependencies Quickly](#install-dependencies-quickly)

## Dependencies
It is a list of known project dependencies, you can find all of them at
[requirements.txt](requirements.txt) file.

```pythonset
{
  "Python3.x",
  "Pip",
  "Python Dotenv",
  "Pydantic",
  "Requests",
  "Flusk",
  "BeautifulSoap4",
}
```

To install these dependencies, see:
* [Install Dependencies](#install-dependencies)
* [Install Dependencies Quickly](#install-dependencies-quickly)

The 2nd point teach how to install it fast. You can make a choice,
but you must to know, **it's required!**

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
> **IMPORTANT:** before you run, please see [install dependencies](#install-dependencies)
> or [install quickly](#install-dependencies-quickly), after
> you can: RENAME or DUPLICATE [.env.example](.env.example) as `.env`. 

Please  Don't edit this file, it has important *hyperlinks*, if you do it,
this application will not work else you change the logic used here.

Just run the file [main.py](main.py) and use a software to make requests for each route.
You can find our routes at [API Routes](#api-routes).

> Some details: I recommend you use a virtual python environment
> interpreter to test this application. See more in:
> [python venv docs](https://docs.python.org/3/library/venv.html).


## Install Dependencies
See these details of how to install dependencies, FIRSTLY step by step, AFTER
how to install it quickly.

<details>
  <summary>
    Python
  </summary>
  <details>
      <summary>
        Windows
      </summary>
      <a href="https://www.python.org/downloads/windows/" target="_blank">Python Windows</a>
  </details>
  <details>
      <summary>
        MacOS
      </summary>
      <a href="https://www.python.org/downloads/macos/" target="_blank">Python MacOS</a>
  </details>
  <details>
      <summary>
        Linux
      </summary>
      Pre Installed.
  </details>
</details>

<details>
  <summary>
    Install Pip
  </summary>
  <code>pip3 install pip --upgrade</code>
</details>

<details>
  <summary>
    Python DotEnv
  </summary>
  <code>pip install python-dotenv</code>
</details>

<details>
  <summary>
    Flask
  </summary>
  <code>pip install Flask</code>
</details>

<details>
  <summary>
    BeautifulSoap 4
  </summary>
  <code>pip install beautifulsoup4</code>
</details>

<details>
  <summary>
    Pydantic
  </summary>
  <code>pip install pydantic</code>
</details>

<details>
  <summary>
    Requests
  </summary>
  <code>pip install requests</code>
</details>

## Install Dependencies Quickly
This project has a file named [requirements.txt](requirements.txt),
where you find a list of project dependencies. To install it quickly,
you can run the following command:

```commandline
pip install -r requirements.txt
```

That's All Folks!
