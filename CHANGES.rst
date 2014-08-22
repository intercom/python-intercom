=========
Changelog
=========

* 0.2.11
   * support for events. `#25 <https://github.com/jkeyes/python-intercom/pull/25>`_. (https://github.com/mekza)
   * using RTD theme for documentation.
   * updated links to Intercom API docs.
* 0.2.10
   * basic support for companies. `#18 <https://github.com/jkeyes/python-intercom/pull/18>`_. (https://github.com/cameronmaske)
   * fixed User.delete. `#19 <https://github.com/jkeyes/python-intercom/pull/19>`_. (https://github.com/cameronmaske)
   * updated links to Intercom API docs.
   * Doctest fixes.
* 0.2.9
   * `unsubscribed_from_emails` attribute added to `User` object. `#15 <https://github.com/jkeyes/python-intercom/pull/15>`_. (https://github.com/sdorazio)
   * `last_request_at` parameter supported in `Intercom.create_user`. `#16 <https://github.com/jkeyes/python-intercom/issues/16>`_.
   * page, per_page, tag_id, and tag_name parameters support on `Intercom.get_users`. `#17 <https://github.com/jkeyes/python-intercom/issues/17>`_.
* 0.2.8
   * Added support for tagging `#13 <https://github.com/jkeyes/python-intercom/issues/13>`_.
   * Now installs into a clean python environment (https://github.com/vrachil) `#12 <https://github.com/jkeyes/python-intercom/issues/12>`_.
   * Doctest fix.
   * PEP8 formatting.
* 0.2.7
   * Update delete user support to send bodyless request.
   * Add support for user notes.
* 0.2.6
   * Support for delete user.
* 0.2.5
   * Consistent version numbering (docs and code).
* 0.2.4
   * Handle invalid JSON responses. (https://github.com/marselester)
   * Fix to doctests to pass with current Intercom dummy API.
* 0.2.3
   * Fixed version number of distribution to match documentation.
* 0.2.2
   * Finished docstrings and doctests.
* 0.2.1
   * Added some docstrings.
* 0.2
   * created source distribution `#2 <https://github.com/jkeyes/python-intercom/issues/2>`_.
   * renamed errors `#1 <https://github.com/jkeyes/python-intercom/issues/1>`_.
* 0.1
   * initial release
