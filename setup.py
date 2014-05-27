#
# Copyright 2012 John Keyes
#
# http://jkeyes.mit-license.org/
#

import os
import re

from setuptools import find_packages
from setuptools import setup

with file(os.path.join('intercom', 'intercom.py')) as init:
    source = init.read()
    m = re.search("__version__ = '(\d+\.\d+\.\d+)'", source, re.M)
    __version__ = m.groups()[0]

setup(
    name="python-intercom",
    version=__version__,
    description="Intercom API wrapper",
    long_description=open('README.rst').read(),
    author="John Keyes",
    author_email="john@keyes.ie",
    license="MIT License",
    url="http://github.com/jkeyes/python-intercom",
    keywords='Intercom crm python',
    classifiers=[],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"],
    zip_safe=False
)
