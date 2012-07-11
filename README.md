fred
====

Python wrapper of the St. Louis Federal Reserve Bank's [FRED API web
service](http://api.stlouisfed.org/docs/fred/) for retrieving economic data.

FRED API Documentation:
[http://api.stlouisfed.org/docs/fred/](http://api.stlouisfed.org/docs/fred/)

Sign up for a FRED API key:
[http://api.stlouisfed.org/api_key.html](http://api.stlouisfed.org/api_key.html)

### API Key ###

You can save your API key, and have it automatically accessible, on the command line:

    $ export FRED_API_KEY=my_api_key


Usage
-----

This wrapper hopes to make working with the Fred API as easy as
possible.

```python
>>> import fred

# Save your FRED API key.
>>> fred.key('my_fred_api_key')


# Interact with economic data categories.
>>> fred.category()

>>> fred.categories()

>>> fred.children()

>>> fred.related()

>>> fred.category(series=True)

>>> fred.category_series()


# Interact with economic data releases.
>>> fred.releases()

>>> fred.release(250)

>>> fred.dates()


# Interact with economic data series.
>>> fred.series(series_id="GNPCA")

>>> fred.series(release=True)

>>> fred.observations(series_id="AAA")

>>> fred.search('search term')

>>> fred.updates()

>>> fred.vintage(series_id="AAA")


# Query economic data sources.
>>> fred.sources()

>>> fred.source(23)
```

**NOTE**: Normally, data is returned in dictionary format instead of XML. If you're
looking for XML output, however, just pass in the `xml=True` keyword argument.

```python
>>> import fred

>>> fred.releases(xml=True)
```
