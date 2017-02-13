Changelog
=========
* 3.0.4
   * Added `resource_type` attribute to lightweight classes. (`#153 <https://github.com/jkeyes/python-intercom/pull/153>`_)
* 3.0.3
   * Removed `count` API operation, this is supported via `client.counts` now. (`#152 <https://github.com/jkeyes/python-intercom/pull/152>`_)
* 3.0.2
   * Added multipage support for Event.find_all. (`#147 <https://github.com/jkeyes/python-intercom/pull/147>`_)
* 3.0.1
   * Added support for HTTP keep-alive. (`#146 <https://github.com/jkeyes/python-intercom/pull/146>`_)
* 3.0
* 3.0b4
   * Added conversation.mark_read method. (`#136 <https://github.com/jkeyes/python-intercom/pull/136>`_)
* 3.0b3
   * Added TokenUnauthorizedError. (`#134 <https://github.com/jkeyes/python-intercom/pull/134>`_)
   * Added UTC datetime everywhere. (`#130 <https://github.com/jkeyes/python-intercom/pull/130>`_)
   * Fixed connection error when paginating. (`#125 <https://github.com/jkeyes/python-intercom/pull/125>`_)
   * Added Personal Access Token support. (`#123 <https://github.com/jkeyes/python-intercom/pull/123>`_)
   * Fixed links to Intercom API documentation. (`#115 <https://github.com/jkeyes/python-intercom/pull/115>`_)
* 3.0b2
   * Added support for Leads. (`#113 <https://github.com/jkeyes/python-intercom/pull/113>`_)
   * Added support for Bulk API. (`#112 <https://github.com/jkeyes/python-intercom/pull/112>`_)
* 3.0b1
   * Moved to new client based approach. (`#108 <https://github.com/jkeyes/python-intercom/pull/108>`_)
* 2.1.1
   * No runtime changes.
* 2.1.0
   * Adding interface support for opens, closes, and assignments of conversations. (`#101 <https://github.com/jkeyes/python-intercom/pull/101>`_)
   * Ensuring identity_hash only contains variables with valid values. (`#100 <https://github.com/jkeyes/python-intercom/issues/100>`_)
   * Adding support for unique_user_constraint and parameter_not_found errors. (`#97 <https://github.com/jkeyes/python-intercom/issues/97>`_)
* 2.0.0
   * Added support for non-ASCII character sets. (`#86 <https://github.com/jkeyes/python-intercom/pull/86>`_)
   * Fixed response handling where no encoding is specified. (`#81 <https://github.com/jkeyes/python-intercom/pull/91>`_)
   * Added support for `None` values in `FlatStore`. (`#88 <https://github.com/jkeyes/python-intercom/pull/88>`_)
* 2.0.beta
   * Fixed `UnboundLocalError` in `Request.parse_body`. (`#72 <https://github.com/jkeyes/python-intercom/issues/72>`_)
   * Added support for replies with an empty body. (`#72 <https://github.com/jkeyes/python-intercom/issues/72>`_)
   * Fixed a bug in identifying changed attributes when creating new resources. (`#77 <https://github.com/jkeyes/python-intercom/issues/77>`_)
* 2.0.alpha
   * Added support for Intercom API v2.
   * Added support for Python 3.
* 0.2.13
   * Fixed wildcard import from `intercom`. (`#28 <https://github.com/jkeyes/python-intercom/pull/28>`_)
* 0.2.12
   * Added RTD theme to requirements.txt
* 0.2.11
   * Added support for events. (`#25 <https://github.com/jkeyes/python-intercom/pull/25>`_)
   * Using RTD theme for documentation.
   * Fixed links to Intercom API docs.
* 0.2.10
   * Added basic support for companies. (`#18 <https://github.com/jkeyes/python-intercom/pull/18>`_)
   * Fixed User.delete. (`#19 <https://github.com/jkeyes/python-intercom/pull/19>`_)
   * Fixed links to Intercom API docs.
   * Fixed doctests.
* 0.2.9
   * Added `unsubscribed_from_emails` attribute to `User` object. (`#15 <https://github.com/jkeyes/python-intercom/pull/15>`_)
   * Added support for `last_request_at` parameter in `Intercom.create_user`. (`#16 <https://github.com/jkeyes/python-intercom/issues/16>`_)
   * Added support for page, per_page, tag_id, and tag_name parameters on `Intercom.get_users`. (`#17 <https://github.com/jkeyes/python-intercom/issues/17>`_)
* 0.2.8
   * Added support for tagging. (`#13 <https://github.com/jkeyes/python-intercom/issues/13>`_)
   * Fixed installation into a clean python environment. (`#12 <https://github.com/jkeyes/python-intercom/issues/12>`_)
   * Fixed doctest.
   * Updated PEP8 formatting.
* 0.2.7
   * Fixed delete user support to send bodyless request.
   * Added support for user notes.
* 0.2.6
   * Added support for delete user.
* 0.2.5
   * Fixed consistent version numbering (docs and code).
* 0.2.4
   * Fixed handling of invalid JSON responses.
   * Fixed doctests to pass with current Intercom dummy API.
* 0.2.3
   * Fixed version number of distribution to match documentation.
* 0.2.2
   * Updated docstrings and doctests.
* 0.2.1
   * Added some docstrings.
* 0.2
   * Created source distribution. (`#2 <https://github.com/jkeyes/python-intercom/issues/2>`_)
   * Fixed error names. (`#1 <https://github.com/jkeyes/python-intercom/issues/1>`_)
* 0.1
   * Initial release.
