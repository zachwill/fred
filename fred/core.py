"""
FRED API documentation: http://api.stlouisfed.org/docs/fred/

Core functionality for interacting with the FRED API.
"""

import os
from itertools import ifilter

import requests
from relaxml import xml


class Fred(object):
    """An easy-to-use Python wrapper over the St. Louis FRED API."""

    def __init__(self, api_key='', xml_output=False):
        if 'FRED_API_KEY' in os.environ:
            self.api_key = os.environ['FRED_API_KEY']
        else:
            self.api_key = api_key
        self.xml = xml_output
        self.endpoint = 'http://api.stlouisfed.org/fred/'

    def _create_path(self, *args):
        """Create the URL path with the Fred endpoint and given arguments."""
        args = ifilter(None, args)
        path = self.endpoint + '/'.join(args)
        return path

    def get(self, *args, **kwargs):
        """Perform a GET request againt the Fred API endpoint."""
        location = args[0]
        params = self._get_keywords(location, kwargs)
        url = self._create_path(*args)
        request = requests.get(url, params=params)
        content = request.content
        self._request = request
        return self._output(content)

    def _get_keywords(self, location, keywords):
        """Format GET request's parameters from keywords."""
        if 'xml' in keywords:
            keywords.pop('xml')
            self.xml = True
        if 'id' in keywords:
            if location != 'series':
                location = location.rstrip('s')
            key = '%s_id' % location
            value = keywords.pop('id')
            keywords[key] = value
        if 'start' in keywords:
            time = keywords.pop('start')
            keywords['realtime_start'] = time
        if 'end' in keywords:
            time = keywords.pop('end')
            keywords['realtime_end'] = time
        if 'sort' in keywords:
            order = keywords.pop('sort')
            keywords['sort_order'] = order
        keywords['api_key'] = self.api_key
        return keywords

    def _output(self, content):
        """Return the output from a given GET request."""
        if self.xml:
            return content
        return xml(content)

    def category(self, path=None, **kwargs):
        """
        Get a specific category.

        >>> Fred().category(category_id=125)
        """
        return self.get('category', path, **kwargs)

    def release(self, path=None, **kwargs):
        """
        Get a release of economic data.

        >>> Fred().release('series', release_id=51)
        """
        return self.get('release', path, **kwargs)

    def releases(self, path=None, **kwargs):
        """
        Get all releases of economic data.

        >>> Fred().releases('dates', limit=10)
        """
        return self.get('releases', path, **kwargs)

    def series(self, path=None, **kwargs):
        """
        Get economic series of data.

        >>> Fred().series('search', search_text="money stock")
        """
        return self.get('series', path, **kwargs)

    def source(self, path=None, **kwargs):
        """
        Get a single source of economic data.

        >>> Fred().source(source_id=51)
        """
        return self.get('source', path, **kwargs)

    def sources(self, path=None, **kwargs):
        """
        Get all of FRED's sources of economic data.

        >>> Fred().sources()
        """
        return self.get('sources', path, **kwargs)

