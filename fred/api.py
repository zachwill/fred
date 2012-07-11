"""
Simplified functions for using the Fred API.
"""

import os
from .core import Fred


def key(api_key):
    os.environ['FRED_API_KEY'] = api_key
    return Fred()


#####################
# Category
#####################

def category(**kwargs):
    """Get a category."""
    if 'series' in kwargs:
        kwargs.pop('series')
        path = 'series'
    else:
        path = None
    return Fred().category(path, **kwargs)


def categories(identifier, **kwargs):
    """Just in case someone misspells the method."""
    kwargs['category_id'] = identifier
    return category(**kwargs)


def children(**kwargs):
    """Get child categories for a specified parent category."""
    return Fred().category('children', **kwargs)


def related(identifier, **kwargs):
    """Get related categories for a specified category."""
    kwargs['category_id'] = identifier
    return Fred().category('related', **kwargs)


def category_series(identifier, **kwargs):
    """Get the series in a category."""
    kwargs['category_id'] = identifier
    return Fred().category('series', **kwargs)


#####################
# Releases
#####################

def release(release_id, **kwargs):
    """Get the release of economic data."""
    kwargs['release_id'] = release_id
    return Fred().release(**kwargs)


def releases(release_id=None, **kwargs):
    """Get all releases of economic data."""
    if not 'id' in kwargs and release_id is not None:
        kwargs['release_id'] = release_id
        return Fred().release(**kwargs)
    return Fred().releases(**kwargs)


def dates(**kwargs):
    """Get release dates for economic data."""
    return Fred().releases('dates', **kwargs)


#####################
# Series
#####################

def series(identifier=None, **kwargs):
    """Get an economic data series."""
    if identifier:
        kwargs['series_id'] = identifier
    if 'release' in kwargs:
        kwargs.pop('release')
        path = 'release'
    elif 'releases' in kwargs:
        kwargs.pop('releases')
        path = 'release'
    else:
        path = None
    return Fred().series(path, **kwargs)


def observations(identifier, **kwargs):
    """Get an economic data series."""
    kwargs['series_id'] = identifier
    return Fred().series('observations', **kwargs)


def search(text, **kwargs):
    """Get economic data series that match keywords."""
    kwargs['search_text'] = text
    return Fred().series('search', **kwargs)


def updates(**kwargs):
    """Get economic data series sorted in descending order."""
    return Fred().series('updates', **kwargs)


def vintage(identifier, **kwargs):
    """
    Get the dates in history when a series' data values were revised or new
    data values were released.
    """
    kwargs['series_id'] = identifier
    return Fred().series('vintagedates', **kwargs)


#####################
# Sources
#####################

def source(source_id=None, **kwargs):
    """Get a source of economic data."""
    if source_id is not None:
        kwargs['source_id'] = source_id
    elif 'id' in kwargs:
        source_id = kwargs.pop('id')
        kwargs['source_id'] = source_id
    if 'releases' in kwargs:
        kwargs.pop('releases')
        path = 'releases'
    else:
        path = None
    return Fred().source(path, **kwargs)


def sources(source_id=None, **kwargs):
    """Get the sources of economic data."""
    if source_id or 'id' in kwargs:
        return source(source_id, **kwargs)
    return Fred().sources(**kwargs)
