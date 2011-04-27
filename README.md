Fred
====

Python wrapper of the St. Louis Federal Reserve Bank's [FRED API web
service](http://api.stlouisfed.org/docs/fred/) for retrieving economic data.

FRED API Documentation: [http://api.stlouisfed.org/docs/fred/](http://api.stlouisfed.org/docs/fred/)


Usage
-----

Without your API key saved in the `fred_api_key.py` file:

    >>> from fred import Fred
    >>> Fred('my_api_key').category(category_id=125)

With your API key saved in the `fred_api_key` file:

    >>> from fred import Fred
    >>> Fred().category(category_id=125)
