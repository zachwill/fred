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
from fred.xml2dict import xml2dict


def set_up():
    """Simplify common set up for unit tests."""
    fred.urlopen = Mock()
    fred.xml2dict = Mock()
    fred.API_KEY = 'my_api_key'

def called_url():
    url = fred.urlopen.call_args[0][0]
    parsed_url = urlparse(url)
    results = {'path': parsed_url.path, 'query': parse_qs(parsed_url.query)}
    return results


class TestXML2Dict(unittest.TestCase):

    def setUp(self):
        self.xml = '<?xml version="1.0" encoding="utf-8" ?>'

    def test_simple_xml_to_dict(self):
        xml = self.xml + '<a><b>5</b><c>9</c></a>'
        expected_output = {'a': {'b': '5', 'c': '9'}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_to_list_of_values(self):
        xml = self.xml + '<a><b>1</b><b>2</b><b>3</b></a>'
        expected_output = {'a': {'b': ['1', '2', '3']}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_to_mixture_of_lists_and_dicts(self):
        xml = self.xml + '<a><b>1</b><b>2</b><c><d>3</d></c></a>'
        expected_output = {'a': {'b': ['1', '2'], 'c': {'d': '3'}}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_attributes_retained(self):
        xml = self.xml + '<numbers one="1" two="2" />'
        expected_output = {'numbers': {'one': '1', 'two': '2'}}
        self.assertEqual(xml2dict(xml), expected_output)


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

    def test_api_called_with_category(self):
        Fred().api('category')
        results = called_url()
        self.assertEqual(results['path'], '/fred/category')
        assert 'my_api_key' in results['query']['api_key']

    def test_api_called_with_releases_and_dates(self):
        Fred().api('releases', 'dates')
        results = called_url()
        self.assertEqual(results['path'], '/fred/releases/dates')

    def test_api_called_with_source_releases_and_kwargs(self):
        Fred().api('source', 'releases', source_id=1)
        results = called_url()
        self.assertEqual(results['path'], '/fred/source/releases')
        assert '1' in results['query']['source_id']

    def test_new_api_key_for_api_called_with_series_updates(self):
        Fred('new_api_key').api('series', 'updates', filter_value='regional')
        results = called_url()
        self.assertEqual(results['path'], '/fred/series/updates')
        assert 'regional' in results['query']['filter_value']


class TestCategoryMethod(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_category_empty_call(self):
        Fred().category()
        results = called_url()
        self.assertEqual(results['path'], '/fred/category')
        assert 'my_api_key' in results['query']['api_key']


class TestReleasesMethod(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_releases_empty_call(self):
        Fred().releases()
        results = called_url()
        self.assertEqual(results['path'], '/fred/releases')
        assert 'my_api_key' in results['query']['api_key']


class TestReleaseMethod(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_release_empty_call(self):
        Fred().release()
        results = called_url()
        self.assertEqual(results['path'], '/fred/release')
        assert 'my_api_key' in results['query']['api_key']

    def test_release_dates(self):
        Fred().release('dates')
        results = called_url()
        self.assertEqual(results['path'], '/fred/release/dates')

    def test_release_sources(self):
        Fred().release('sources', release_id=51)
        results = called_url()
        self.assertEqual(results['path'], '/fred/release/sources')
        assert '51' in results['query']['release_id']


class TestSeriesMethod(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_series_empty_call(self):
        Fred().series()
        results = called_url()
        self.assertEqual(results['path'], '/fred/series')
        assert 'my_api_key' in results['query']['api_key']


class TestSourcesMethod(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_sources_empty_call(self):
        Fred().sources()
        results = called_url()
        self.assertEqual(results['path'], '/fred/sources')
        assert 'my_api_key' in results['query']['api_key']


class TestSourceMethod(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_source_empty_call(self):
        Fred().source()
        results = called_url()
        self.assertEqual(results['path'], '/fred/source')
        assert 'my_api_key' in results['query']['api_key']


if __name__ == '__main__':
    unittest.main()
