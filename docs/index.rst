===============
python-intercom
===============

.. toctree::
    installation
    api/modules
    changelog
    development

Installation
============

Stable releases of python-intercom can be installed with 
`pip <http://pip.openplans.org>`_ or you may download a `.tgz` source 
archive from `pypi <http://pypi.python.org/pypi/python-intercom#downloads>`_.
See the :doc:`installation` page for more detailed instructions.

If you want to use the latest code, you can grab it from our 
`Git repository <http://github.com/jkeyes/python-intercom>`_, or `fork it <http://github.com/jkeyes/python-intercom>`_.

Usage
===================================

Authentication
---------------

Intercom documentation: `Authentication <http://doc.intercom.io/api/v1/#authentication>`_.

::

    from intercom import Intercom
    Intercom.app_id = 'dummy-app-id'
    Intercom.api_key = 'dummy-api-key'

Users
-----

Getting all Users
+++++++++++++++++

Intercom documentation: `Getting all Users <http://doc.intercom.io/api/v1/#getting-all-users>`_.

::

    from intercom import User
    for user in User.all():
        print user.email

Getting a User
++++++++++++++

Intercom documentation: `Getting a User <http://doc.intercom.io/api/v1/#getting-a-user>`_.

::

    user = User.find(email="ben@intercom.io")

Create a User
+++++++++++++

Intercom documentation: `Create a User <http://doc.intercom.io/api/v1/#create-a-user>`_.

::

    user = User.create(email="ben@intercom.io",
            user_id=7902,
            name="Ben McRedmond",
            created_at=datetime.now(),
            custom_data={"plan": "pro"},
            last_seen_ip="1.2.3.4",
            last_seen_user_agent="ie6")

Updating a User
+++++++++++++++

Intercom documentation: `Updating a User <http://doc.intercom.io/api/v1/#updating-a-user>`_.

::

    user = User.find(email="ben@intercom.io")
    user.name = "Benjamin McRedmond"
    user.save()

Deleting a User
+++++++++++++++

Intercom documentation: `Deleting a User <http://doc.intercom.io/api/v1/#deleting-a-user>`_.

::

    deleted_user = User.delete(email="ben@intercom.io")

Notes
-----

Creating a Note
+++++++++++++++

Intercom documentation: `Creating a Note <http://doc.intercom.io/api/v1/#creating-a-note>`_.

::

    from intercom import Note
    note = Note.create(email="ben@intercom.io", 
            body="These are a few of my favourite things.")


Tagging
-------

Getting a Tag
+++++++++++++

Intercom documentation: `Getting a Tag <http://doc.intercom.io/api/v1/#getting-a-tag>`_.

::

    from intercom import Tag
    tag = Tag.find_by_name("Free Trial")

Creating a new Tag
++++++++++++++++++

Intercom documentation: `Creating a new Tag <http://doc.intercom.io/api/v1/#create-a-new-tag>`_.

::

    from intercom import Tag
    tag = Tag.create("Free Trial")

Updating an already existing Tag
++++++++++++++++++++++++++++++++

Intercom documentation: `Updating a Tag <http://doc.intercom.io/api/v1/#update-an-already-existing-tag>`_.

::

    from intercom import Tag
    tag = Tag.find_by_name("Free Trial")
    tag.user_ids = ["abc123", "def456"]
    tag.tag_or_untag = "tag"
    tag.save()


Impressions
-----------

Creating an Impression
++++++++++++++++++++++

Intercom documentation: `Creating an Impression <http://doc.intercom.io/api/v1/#creating-an-impression>`_.

::

    from intercom import Impression
    impression = Impression.create(email="ben@intercom.io", 
            user_agent="my-awesome-android-app-v0.0.1")

Message Threads
---------------

Getting Message Threads
+++++++++++++++++++++++

Intercom documentation:  `Getting Message Threads <http://doc.intercom.io/api/v1/#getting-message-threads>`_.

::

    from intercom import MessageThread

    # all message threads
    message_threads = MessageThread.find_all(email="ben@intercom.io")

    # a specific thread
    message_threads = MessageThread.find_all(email="ben@intercom.io",
            thread_id=123)

Creating a Message Thread
+++++++++++++++++++++++++

Intercom documentation:  `Creating a Message Thread <http://doc.intercom.io/api/v1/#creating-a-message-thread>`_.

::

    message_thread = MessageThread.create(email="ben@intercom.io", 
            body="Hey Intercom, What is up?")

Replying on a Message Thread
++++++++++++++++++++++++++++

Intercom documentation:  `Replying on a Message Thread <http://doc.intercom.io/api/v1/#replying-on-a-message-thread>`_.

::

    message_thread = MessageThread.create(email="ben@intercom.io",
            thread_id=123,
            body="Not much either :(")

Events
-----------

Submitting Events
+++++++++++++++++

Intercom documentation: `Submitting Events <http://doc.intercom.io/api/v1/#submitting-events>`_.

::

    from intercom import Event
    impression = Event.create(event_name="sent-invite", 
            user_id="314159")

Development
===========

Our :doc:`development` page has detailed instructions on how to run our
tests, and to produce coverage and pylint reports.

Changelog
=========

The :doc:`changelog` keeps track of changes per release.

pydoc
=====

View the extensive `pydoc <api/modules.html>`_ which has liberal helpings of
`doctests` to display usage.

