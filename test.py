"""
Tests for V2 of Fred API wrapper.
"""

import os
import unittest

import fred
from mock import Mock


class Category(unittest.TestCase):

    def setUp(self):
        fred.core.requests = Mock()
        fred.core.json = Mock()
        self.get = fred.core.requests.get

    def test_fred_category(self):
        fred.category()
        expected = 'https://api.stlouisfed.org/fred/category'
        params = {'api_key': '', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_category_series(self):
        fred.key('123abc')
        fred.category(series=True)
        expected = 'https://api.stlouisfed.org/fred/category/series'
        params = {'api_key': '123abc', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_category_children(self):
        fred.key('abc123')
        fred.children()
        expected = 'https://api.stlouisfed.org/fred/category/children'
        params = {'api_key': 'abc123', 'category_id': None, 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_category_related(self):
        fred.related(32073)
        expected = 'https://api.stlouisfed.org/fred/category/related'
        params = {'api_key': '', 'category_id': 32073, 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_category_series_function(self):
        fred.key('my_fred_key')
        fred.category_series(123)
        expected = 'https://api.stlouisfed.org/fred/category/series'
        params = {'api_key': 'my_fred_key', 'category_id': 123, 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def tearDown(self):
        os.environ['FRED_API_KEY'] = ''


class Releases(unittest.TestCase):

    def setUp(self):
        fred.core.requests = Mock()
        fred.core.json = Mock()
        self.get = fred.core.requests.get

    def test_fred_releases(self):
        fred.key('123')
        fred.releases()
        expected = 'https://api.stlouisfed.org/fred/releases'
        params = {'api_key': '123', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_releases_with_id_calls_release(self):
        fred.key('abc')
        fred.releases('123')
        expected = 'https://api.stlouisfed.org/fred/release'
        params = {'api_key': 'abc', 'release_id': '123', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_specific_release(self):
        fred.key('my_key')
        fred.release('123')
        expected = 'https://api.stlouisfed.org/fred/release'
        params = {'api_key': 'my_key', 'release_id': '123', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_releases_dates(self):
        fred.key('123')
        fred.dates()
        expected = 'https://api.stlouisfed.org/fred/releases/dates'
        params = {'api_key': '123', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_releases_dates_with_start_and_end_keywords(self):
        fred.key('github')
        fred.dates(start='2012-01-01', end='2012-03-16')
        expected = 'https://api.stlouisfed.org/fred/releases/dates'
        params = {
            'api_key': 'github',
            'realtime_start': '2012-01-01',
            'realtime_end': '2012-03-16',
            'file_type': 'json'
        }
        self.get.assert_called_with(expected, params=params)

    def tearDown(self):
        os.environ['FRED_API_KEY'] = ''


class Series(unittest.TestCase):

    def setUp(self):
        fred.core.requests = Mock()
        fred.core.json = Mock()
        self.get = fred.core.requests.get

    def test_fred_series(self):
        fred.key('abc')
        fred.series()
        expected = 'https://api.stlouisfed.org/fred/series'
        params = {'api_key': 'abc', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_release(self):
        fred.key('abc')
        fred.series(releases=True)
        expected = 'https://api.stlouisfed.org/fred/series/release'
        params = {'api_key': 'abc', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_observations(self):
        fred.key('ohai')
        fred.observations("AAA")
        expected = 'https://api.stlouisfed.org/fred/series/observations'
        params = {'api_key': 'ohai', 'series_id': 'AAA', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_search(self):
        fred.key('123')
        fred.search('money stock')
        expected = 'https://api.stlouisfed.org/fred/series/search'
        params = {'api_key': '123', 'search_text': 'money stock', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_updates(self):
        fred.key('ALL THE FRED API!')
        fred.updates()
        expected = 'https://api.stlouisfed.org/fred/series/updates'
        params = {'api_key': 'ALL THE FRED API!', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_vintage_dates(self):
        fred.key('123abc')
        fred.vintage('AAA', sort='desc')
        expected = 'https://api.stlouisfed.org/fred/series/vintagedates'
        params = {
            'api_key': '123abc',
            'series_id': 'AAA',
            'sort_order': 'desc',
            'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def tearDown(self):
        os.environ['FRED_API_KEY'] = ''


class Sources(unittest.TestCase):

    def setUp(self):
        fred.core.requests = Mock()
        fred.core.json = Mock()
        self.get = fred.core.requests.get

    def test_fred_sources(self):
        fred.key('moar fred')
        fred.sources()
        expected = 'https://api.stlouisfed.org/fred/sources'
        params = {'api_key': 'moar fred', 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_sources_accidentally_passed_source_id(self):
        fred.key('123')
        fred.sources(123)
        expected = 'https://api.stlouisfed.org/fred/source'
        params = {'api_key': '123', 'source_id': 123, 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_source(self):
        fred.key('123')
        fred.source(25)
        expected = 'https://api.stlouisfed.org/fred/source'
        params = {'api_key': '123', 'source_id': 25, 'file_type': 'json'}
        self.get.assert_called_with(expected, params=params)

    def tearDown(self):
        os.environ['FRED_API_KEY'] = ''

if __name__ == '__main__':
    unittest.main()
