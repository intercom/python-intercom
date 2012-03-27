========
intercom
========

.. toctree::
   :hidden:

   api/modules

Installation
============

``pip install python-intercom``

Python wrapper for the Intercom API
===================================

Authentication
---------------

More information on `docs.intercom.io <http://docs.intercom.io/api#authentication>`_.

::

    from intercom import Intercom
    Intercom.app_id = 'dummy-app-id'
    Intercom.api_key = 'dummy-api-key'

Users
-----

Getting all Users
+++++++++++++++++

More information on `docs.intercom.io <http://docs.intercom.io/api#getting_all_users>`_.

::

    from intercom import User
    for user in User.all():
        print user.email

Getting a User
++++++++++++++

More information on `docs.intercom.io <http://docs.intercom.io/api#getting_a_user>`_.

::

    user = User.find(email="ben@intercom.io")

Creating a User
+++++++++++++++

More infomation on `docs.intercom.io <http://docs.intercom.io/api#creating_a_user>`_.

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

More information on `docs.intercom.io <http://docs.intercom.io/api#updating_a_user>`_.

::

    user = User.find(email="ben@intercom.io")
    user.name = "Benjamin McRedmond"
    user.save()

Impressions
-----------

Creating an Impression
++++++++++++++++++++++

More information on `docs.intercom.io <http://docs.intercom.io/api#creating_an_impression>`_.

::

    from intercom import Impression
    impression = Impression.create(email="ben@intercom.io", 
            user_agent="my-awesome-android-app-v0.0.1")

Message Threads
---------------

Getting Message Threads
+++++++++++++++++++++++

More information on `docs.intercom.io <http://docs.intercom.io/api#getting_messages>`_.

::

    from intercom import MessageThread

    # all message threads
    message_threads = MessageThread.find_all(email="ben@intercom.io")

    # a specific thread
    message_threads = MessageThread.find_all(email="ben@intercom.io",
            thread_id=123)

Creating a Message Thread
+++++++++++++++++++++++++

::

    message_thread = MessageThread.create(email="ben@intercom.io", 
            body="Hey Intercom, What is up?")

Reply on a Message Thread
+++++++++++++++++++++++++

::

    message_thread = MessageThread.create(email="ben@intercom.io",
            thread_id=123,
            body="No much either :(")

pydoc
=====

View the extensive `pydoc <api/modules.html>`_ which has liberal helpings of
`doctests` to display usage.
