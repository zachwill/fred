#!/usr/bin/env python
"""
Author: Zach Williams, <hey AT zachwill DOT com>

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = """
Fred
====

Python wrapper of the St. Louis Federal Reserve Bank's [FRED API web
service](http://api.stlouisfed.org/docs/fred/) for retrieving economic data.

FRED API Documentation:
[http://api.stlouisfed.org/docs/fred/](http://api.stlouisfed.org/docs/fred/)

Sign up for a FRED API key:
[http://api.stlouisfed.org/api_key.html](http://api.stlouisfed.org/api_key.html)
"""

setup(
    name="fred",
    version="2.5",
    description="St. Louis Federal Reserve FRED API",
    long_description=long_description,
    keywords="fred, fred api, federal reserve, st. louis fed",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    url="https://github.com/zachwill/fred",
    license="MIT",
    packages=[
        "fred"
    ],
    install_requires=[
        'relaxml',
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite="test.py",
    tests_require=[
        "mock"
    ]
)
