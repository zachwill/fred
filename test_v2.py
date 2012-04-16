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
        fred.core.xml = Mock()
        self.get = fred.core.requests.get

    def test_fred_category(self):
        fred.category()
        expected = 'http://api.stlouisfed.org/fred/category'
        params = {'api_key': ''}
        self.get.assert_called_with(expected, params=params)

    def test_fred_category_series(self):
        fred.key('123abc')
        fred.category(series=True)
        expected = 'http://api.stlouisfed.org/fred/category/series'
        params = {'api_key': '123abc'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_category_children(self):
        fred.key('abc123')
        fred.children()
        expected = 'http://api.stlouisfed.org/fred/category/children'
        params = {'api_key': 'abc123'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_category_related(self):
        fred.related()
        expected = 'http://api.stlouisfed.org/fred/category/related'
        params = {'api_key': ''}
        self.get.assert_called_with(expected, params=params)

    def test_fred_category_series_function(self):
        fred.key('my_fred_key')
        fred.category_series()
        expected = 'http://api.stlouisfed.org/fred/category/series'
        params = {'api_key': 'my_fred_key'}
        self.get.assert_called_with(expected, params=params)

    def tearDown(self):
        os.environ['FRED_API_KEY'] = ''


class Releases(unittest.TestCase):

    def setUp(self):
        fred.core.requests = Mock()
        fred.core.xml = Mock()
        self.get = fred.core.requests.get

    def test_fred_releases(self):
        fred.key('123')
        fred.releases()
        expected = 'http://api.stlouisfed.org/fred/releases'
        params = {'api_key': '123'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_releases_with_id_calls_release(self):
        fred.key('abc')
        fred.releases('123')
        expected = 'http://api.stlouisfed.org/fred/release'
        params = {'api_key': 'abc', 'release_id': '123'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_specific_release(self):
        fred.key('my_key')
        fred.release('123')
        expected = 'http://api.stlouisfed.org/fred/release'
        params = {'api_key': 'my_key', 'release_id': '123'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_releases_dates(self):
        fred.key('123')
        fred.dates()
        expected = 'http://api.stlouisfed.org/fred/releases/dates'
        params = {'api_key': '123'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_releases_dates_with_start_and_end_keywords(self):
        fred.key('github')
        fred.dates(start='2012-01-01', end='2012-03-16')
        expected = 'http://api.stlouisfed.org/fred/releases/dates'
        params = {
            'api_key': 'github',
            'realtime_start': '2012-01-01',
            'realtime_end': '2012-03-16'
        }
        self.get.assert_called_with(expected, params=params)

    def tearDown(self):
        os.environ['FRED_API_KEY'] = ''


class Series(unittest.TestCase):

    def setUp(self):
        fred.core.requests = Mock()
        fred.core.xml = Mock()
        self.get = fred.core.requests.get

    def test_fred_series(self):
        fred.key('abc')
        fred.series()
        expected = 'http://api.stlouisfed.org/fred/series'
        params = {'api_key': 'abc'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_release(self):
        fred.key('abc')
        fred.series(releases=True)
        expected = 'http://api.stlouisfed.org/fred/series/release'
        params = {'api_key': 'abc'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_observations(self):
        fred.key('ohai')
        fred.observations()
        expected = 'http://api.stlouisfed.org/fred/series/observations'
        params = {'api_key': 'ohai'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_search(self):
        fred.key('123')
        fred.search('money stock')
        expected = 'http://api.stlouisfed.org/fred/series/search'
        params = {'api_key': '123', 'search_text': 'money stock'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_updates(self):
        fred.key('ALL THE FRED API!')
        fred.updates()
        expected = 'http://api.stlouisfed.org/fred/series/updates'
        params = {'api_key': 'ALL THE FRED API!'}
        self.get.assert_called_with(expected, params=params)

    def test_fred_series_vintage_dates(self):
        fred.key('123abc')
        fred.vintage(sort='desc')
        expected = 'http://api.stlouisfed.org/fred/series/vintagedates'
        params = {'api_key': '123abc', 'sort_order': 'desc'}
        self.get.assert_called_with(expected, params=params)

    def tearDown(self):
        os.environ['FRED_API_KEY'] = ''


if __name__ == '__main__':
    unittest.main()
