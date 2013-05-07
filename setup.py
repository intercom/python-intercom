#
# Copyright 2012 John Keyes
#
# http://jkeyes.mit-license.org/
#

from setuptools import find_packages
from setuptools import setup

__version__ = "0.2.8"

setup(
    name="python-intercom",
    version=__version__,
    description="Intercom API wrapper",
    long_description=open('README').read(),
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
