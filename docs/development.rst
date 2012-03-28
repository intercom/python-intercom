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
    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    intercom                     21      0   100%   
    intercom.impression          25      0   100%   
    intercom.intercom            85      0   100%   
    intercom.message_thread      64      0   100%   
    intercom.user               125      0   100%   
    -------------------------------------------------------
    TOTAL                       320      0   100%   
    -------------------------------------------------------

Pylint
------

Generate a pylint report for a specific module:

::

    pylint --rcfile=pylint.conf intercom/user.py

Generate a full pylint report:

::

    pylint --rcfile=pylint.conf intercom

