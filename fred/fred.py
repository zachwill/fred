#!/usr/bin/env python

"""
FRED API documentation: http://api.stlouisfed.org/docs/fred/

Main file for interacting with the FRED API.
"""

try:
    from urllib import urlencode
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import urlencode

try:
    from urllib2 import urlopen
except ImportError: # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen

try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json

from xml2dict import xml2dict
from fred_api_key import API_KEY


class Fred(object):
    """An easy-to-use Python wrapper over the St. Louis FRED API."""

    def __init__(self, api_key=''):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
        self.base_url = 'http://api.stlouisfed.org/fred'

    def api(self, parent, child=None, xml_output=False, **kwargs):
        """
        Method to interact with FRED's API.

        >>> Fred().api('series', 'release', series_id='IRA')
        """
        url = [self.base_url]
        if child:
            url.append('/%s/%s' % (parent, child))
        else:
            url.append('/%s' % parent)
        kwargs.update({'api_key': self.api_key})
        url.extend(['?', urlencode(kwargs)])
        data = urlopen(''.join(url)).read()
        if xml_output:
            return data
        data_dict = self._xml_to_dict(data)
        return data_dict

    def _xml_to_dict(self, xml):
        """Internal method to clean up returned data."""
        return xml2dict(xml)

    def category(self, child=None, **kwargs):
        """
        Get a specific category.

        >>> Fred().category(category_id=125)
        """
        return self.api('category', child, **kwargs)

    def releases(self, child=None, **kwargs):
        """
        Get all releases of economic data.

        >>> Fred().releases('dates', limit=10)
        """
        return self.api('releases', child, **kwargs)

    def release(self, child=None, **kwargs):
        """
        Get a release of economic data.

        >>> Fred().release('series', release_id=51)
        """
        return self.api('release', child, **kwargs)

    def series(self, child=None, **kwargs):
        """
        Get economic series of data.

        >>> Fred().series('search', search_text="money stock")
        """
        return self.api('series', child, **kwargs)

    def sources(self, child=None, **kwargs):
        """
        Get all of FRED's sources of economic data.

        >>> Fred().sources()
        """
        return self.api('sources', child, **kwargs)

    def source(self, child=None, **kwargs):
        """
        Get a single source of economic data.

        >>> Fred().source(source_id=51)
        """
        return self.api('source', child, **kwargs)
