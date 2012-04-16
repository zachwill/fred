"""
Simplified functions for using the Fred API.
"""

from .core import Fred


def key(api_key):
    os.environ['FRED_API_KEY'] = api_key


#####################
# Category
#####################

def category(**kwargs):
    """Get a category."""
    return 'category'


def children(**kwargs):
    """Get child categories for a specified parent category."""
    return 'category'


def related(**kwargs):
    """Get related categories for a specified category."""
    return 'category'


def category_series(**kwargs):
    """Get the series in a category."""
    return 'category'


#####################
# Releases
#####################

def releases(id=None, **kwargs):
    """Get all releases of economic data."""
    if not 'id' in kwargs and id is not None:
        kwargs['id'] = id
    return 'releases'


def dates(**kwargs):
    """Get release dates for economic data."""
    return 'releases'


#####################
# Series
#####################

def series(**kwargs):
    """Get an economic data series."""
    if 'release' in kwargs:
        return 'release'
    return 'series'


def observations(**kwargs):
    """Get an economic data series."""
    return 'series'


def search(**kwargs):
    """Get economic data series that match keywords."""
    return 'series'


def updates(**kwargs):
    """Get economic data series sorted in descending order."""
    return 'series'


def vintage(**kwargs):
    """
    Get the dates in history when a series' data values were revised or new
    data values were released.
    """
    return 'series'


#####################
# Sources
#####################

def sources(**kwargs):
    """Get the sources of economic data."""
    if 'release' in kwargs:
        return 'releases'
    return 'sources'
