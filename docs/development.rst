Development
===========

Running the tests
-----------------

Run all of the (nose) tests:

::

    nosetests --with-coverage --cover-package=intercom tests

Run the unit tests:

::

    nosetests tests -e integration

Run the integration tests (using the dummy `app_id` and `api_key`):

::

    nosetests tests -e unit

Doctests
--------

Run all of the doctests:

::

    ./bin/doctest

Run the doctests in a specific module:

::

    ./bin/doctest intercom/user.py

Code coverage
-------------

Generate a code coverage report:

::

    nosetests --with-coverage --cover-package=intercom tests

Pylint
------

Generate a pylint report for a specific module:

::

    pylint --rcfile=pylint.conf intercom/user.py

Generate a full pylint report:

::

    pylint --rcfile=pylint.conf intercom


Dependencies
------------

* `nose <http://readthedocs.org/docs/nose/en/latest/>`_ – makes unit testing easier.
* `coverage <http://nedbatchelder.com/code/coverage/>`_ – code coverage.
* `mock <http://www.voidspace.org.uk/python/mock/>`_ – patching methods for unit testing.
* `pylint <http://www.logilab.org/857>`_ – source code analyzer.
* `Sphinx <http://sphinx.pocoo.org/>`_ – documentation decorator.
* `Pygments <http://pygments.org/>`_ – Python syntax highlighting for documentation.
* `docutils <http://docutils.sourceforge.net/>`_ – reStructuredText support.
* `Jinja <http://jinja.pocoo.org/docs/>`_ – templating language.

