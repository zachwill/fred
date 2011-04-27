#!/usr/bin/env python

"""
FRED API documentation: http://api.stlouisfed.org/docs/fred/

Main file for interacting with the FRED API.
"""

from urllib import urlencode
try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json
try:
    from urllib2 import urlopen
except ImportError: # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen

from fred_api_key import API_KEY


class Fred(object):
    """An easy-to-use Python wrapper over the St. Louis FRED API."""

    def __init__(self, api_key=''):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
        self.base_url = 'http://api.stlouisfed.org/fred'

    def api(self, parent, child=None, **kwargs):
        """Fred's API."""
        url = [self.base_url]
        if child:
            url.append('/%s/%s' % (parent, child))
        else:
            url.append('/%s' % parent)
        kwargs.update({'api_key': self.api_key})
        url.extend(['?', urlencode(kwargs)])
        data = urlopen(''.join(url)).read()
        data_dict = self._xml_to_json(data)
        return data_dict

    def _xml_to_json(self, xml):
        """Internal method to clean up returned data?"""
        return xml
