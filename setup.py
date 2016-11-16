#
# Copyright 2012 John Keyes
#
# http://jkeyes.mit-license.org/
#

import os
import re

from setuptools import find_packages
from setuptools import setup

with open(os.path.join('intercom', '__init__.py')) as init:
    source = init.read()
    m = re.search("__version__ = '(.*)'", source, re.M)
    __version__ = m.groups()[0]

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name="python-intercom",
    version=__version__,
    description="Intercom API wrapper",
    long_description=long_description,
    author="John Keyes",
    author_email="john@keyes.ie",
    license="MIT License",
    url="http://github.com/jkeyes/python-intercom",
    keywords='Intercom crm python',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests", "inflection", "certifi", "six", "pytz"],
    zip_safe=False
)
