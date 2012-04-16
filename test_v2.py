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


if __name__ == '__main__':
    unittest.main()
