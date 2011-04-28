Fred
====

Python wrapper of the St. Louis Federal Reserve Bank's [FRED API web
service](http://api.stlouisfed.org/docs/fred/) for retrieving economic data.

FRED API Documentation:
[http://api.stlouisfed.org/docs/fred/](http://api.stlouisfed.org/docs/fred/)

Sign up for a FRED API key:
[http://api.stlouisfed.org/api_key.html](http://api.stlouisfed.org/api_key.html)


Usage
-----

Without your API key saved in the `fred_api_key.py` file:

    >>> from fred import Fred
    >>> Fred('my_api_key').category(category_id=125)

With your API key saved in the `fred_api_key` file:

    >>> from fred import Fred
    >>> Fred().category(category_id=125)


### Methods

`category` -- Get economic data for a specific category.

    >>> Fred().category(category_id=120)


`releases` -- Get all releases of economic data.

    >>> Fred().releases('dates', limit=10)


`release` -- Get economic data for a specific release.

    >>> Fred().release('series', release_id=51)


`series` -- Get economic series of data.

    >>> Fred().series('search', search_text="money stock")


`sources` -- Get all of FRED's sources of economic data.

    >>> Fred().sources()


`source` -- Get a single source of economic data.

    >>> Fred().source(source_id=51)


`api` -- Generic way of interacting with the FRED API.

    >>> Fred().api('release', 'dates', release_id=51)


Normally, data is returned in dictionary format instead of XML. If you're
looking for XML output, however, just pass in an `xml_output=True` argument to a
method.

    >>> Fred().releases(xml_output=True)


License
-------

**Author**: Zach Williams

All code released under [the Unlicense](http://unlicense.org/) (a.k.a. Public
Domain).
