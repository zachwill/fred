#!/usr/bin/env python

"""Unit tests for the `fred` module."""

import unittest
try:
    from urlparse import urlparse, parse_qs
except ImportError:  # pragma: no cover
    # For older versions of Python.
    from urlparse import urlparse
    from cgi import parse_qs
from mock import Mock
from fred import fred
from fred import Fred


def set_up():
    """Simplify common set up for unit tests."""
    fred.urlopen = Mock()
    fred.API_KEY = 'my_api_key'

def called_url():
    url = fred.urlopen.call_args[0][0]
    parsed_url = urlparse(url)
    results = {'path': parsed_url.path, 'query': parse_qs(parsed_url.query)}
    return results


class TestFredClassInit(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_uninitialized_api_key(self):
        self.assertEqual(Fred().api_key, 'my_api_key')

    def test_initialized_Fred_api_key(self):
        self.assertEqual(Fred('new_api_key').api_key, 'new_api_key')


class TestApiMethod(unittest.TestCase):

    def setUp(self):
        set_up()
        self.urlopen = fred.urlopen

    def test_api_called_with_category(self):
        Fred().api('category')
        results = called_url()
        self.assertEqual(results['path'], '/fred/category')
        assert 'my_api_key' in results['query']['api_key']

    def test_api_called_with_releases_and_dates(self):
        Fred().api('releases', 'dates')
        results = called_url()
        self.assertEqual(results['path'], '/fred/releases/dates')
        assert 'my_api_key' in results['query']['api_key']

    def test_api_called_with_source_releases_and_kwargs(self):
        Fred().api('source', 'releases', source_id=1)
        results = called_url()
        self.assertEqual(results['path'], '/fred/source/releases')
        assert 'my_api_key' in results['query']['api_key']
        assert '1' in results['query']['source_id']


if __name__ == '__main__':
    unittest.main()
