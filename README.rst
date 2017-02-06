python-intercom
===============

|PyPI Version| |PyPI Downloads| |Travis CI Build| |Coverage Status|

Python bindings for the Intercom API (https://api.intercom.io).

`API Documentation <https://developers.intercom.com/reference>`__.

`Package
Documentation <http://readthedocs.org/docs/python-intercom/>`__.

Upgrading information
---------------------

Version 3 of python-intercom is **not backwards compatible** with
previous versions.

Version 3 moves away from a global setup approach to the use of an
Intercom Client.

Installation
------------

::

    pip install python-intercom

Basic Usage
-----------

Configure your client
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from intercom.client import Client
    intercom = Client(personal_access_token='my_personal_access_token')

Note that certain resources will require an extended scope access token : `Setting up Personal Access Tokens <https://developers.intercom.com/docs/personal-access-tokens>`_

Resources
~~~~~~~~~

Resources this API supports:

::

    https://api.intercom.io/users
    https://api.intercom.io/contacts
    https://api.intercom.io/companies
    https://api.intercom.io/counts
    https://api.intercom.io/tags
    https://api.intercom.io/notes
    https://api.intercom.io/segments
    https://api.intercom.io/events
    https://api.intercom.io/conversations
    https://api.intercom.io/messages
    https://api.intercom.io/subscriptions
    https://api.intercom.io/jobs
    https://api.intercom.io/bulk

Examples
~~~~~~~~

Users
^^^^^

.. code:: python

    # Find user by email
    user = intercom.users.find(email="bob@example.com")
    # Find user by user_id
    user = intercom.users.find(user_id="1")
    # Find user by id
    user = intercom.users.find(id="1")
    # Create a user
    user = intercom.users.create(email="bob@example.com", name="Bob Smith")
    # Delete a user
    user = intercom.users.find(id="1")
    deleted_user = intercom.users.delete(user)
    # Update custom_attributes for a user
    user.custom_attributes["average_monthly_spend"] = 1234.56
    intercom.users.save(user)
    # Perform incrementing
    user.increment('karma')
    intercom.users.save(user)
    # Iterate over all users
    for user in intercom.users.all():
        ...

    # Bulk operations.
    # Submit bulk job, to create users, if any of the items in create_items match an existing user that user will be updated
    intercom.users.submit_bulk_job(create_items=[{'user_id': 25, 'email': 'alice@example.com'}, {'user_id': 25, 'email': 'bob@example.com'}])
    # Submit bulk job, to delete users
    intercom.users.submit_bulk_job(delete_items=[{'user_id': 25, 'email': 'alice@example.com'}, {'user_id': 25, 'email': 'bob@example.com'}])
    # Submit bulk job, to add items to existing job
    intercom.users.submit_bulk_job(create_items=[{'user_id': 25, 'email': 'alice@example.com'}], delete_items=[{'user_id': 25, 'email': 'bob@example.com'}], 'job_id': 'job_abcd1234')

Admins
^^^^^^

.. code:: python

    # Iterate over all admins
    for admin in intercom.admins.all():
        ...

Companies
^^^^^^^^^

.. code:: python

    # Add a user to one or more companies
    user = intercom.users.find(email='bob@example.com')
    user.companies = [
        {'company_id': 6, 'name': 'Intercom'},
        {'company_id': 9, 'name': 'Test Company'}
    ]
    intercom.users.save(user)
    # You can also pass custom attributes within a company as you do this
    user.companies = [
        {
            'id': 6,
            'name': 'Intercom',
            'custom_attributes': {
                'referral_source': 'Google'
            }
        }
    ]
    intercom.users.save(user)
    # Find a company by company_id
    company = intercom.companies.find(company_id='44')
    # Find a company by name
    company = intercom.companies.find(name='Some company')
    # Find a company by id
    company = intercom.companies.find(id='41e66f0313708347cb0000d0')
    # Update a company
    company.name = 'Updated company name'
    intercom.companies.save(company)
    # Iterate over all companies
    for company in intercom.companies.all():
        ...
    # Get a list of users in a company
    intercom.companies.users(company.id)

Tags
^^^^

.. code:: python

    # Tag users
    tag = intercom.tags.tag_users(name='blue', users=[{'email': 'test1@example.com'}])
    # Untag users
    intercom.tags.untag_users(name='blue', users=[{'user_id': '42ea2f1b93891f6a99000427'}])
    # Iterate over all tags
    for tag in intercom.tags.all():
        ...
    # Tag companies
    tag = intercom.tags.tag(name='blue', companies=[{'id': '42ea2f1b93891f6a99000427'}])

Segments
^^^^^^^^

.. code:: python

    # Find a segment
    segment = intercom.segments.find(id=segment_id)
    # Iterate over all segments
    for segment in intercom.segments.all():
        ...

Notes
^^^^^

.. code:: python

    # Find a note by id
    note = intercom.notes.find(id=note)
    # Create a note for a user
    note = intercom.notes.create(
        body="<p>Text for the note</p>",
        email='joe@example.com')
    # Iterate over all notes for a user via their email address
    for note in intercom.notes.find_all(email='joe@example.com'):
        ...
    # Iterate over all notes for a user via their user_id
    for note in intercom.notes.find_all(user_id='123'):
        ...

Conversations
^^^^^^^^^^^^^

.. code:: python

    # FINDING CONVERSATIONS FOR AN ADMIN
    # Iterate over all conversations (open and closed) assigned to an admin
    for convo in intercom.conversations.find_all(type='admin', id='7'):
        ...
    # Iterate over all open conversations assigned to an admin
    for convo in intercom.conversations.find_all(type='admin', id=7, open=True):
        ...
    # Iterate over closed conversations assigned to an admin
    for convo intercom.conversations.find_all(type='admin', id=7, open=False):
        ...
    # Iterate over closed conversations for assigned an admin, before a certain
    # moment in time
    for convo in intercom.conversations.find_all(
            type='admin', id= 7, open= False, before=1374844930):
        ...

    # FINDING CONVERSATIONS FOR A USER
    # Iterate over all conversations (read + unread, correct) with a user based on
    # the users email
    for convo in intercom.onversations.find_all(email='joe@example.com',type='user'):
        ...
    # Iterate over through all conversations (read + unread) with a user based on
    # the users email
    for convo in intercom.conversations.find_all(
            email='joe@example.com', type='user', unread=False):
        ...
    # Iterate over all unread conversations with a user based on the users email
    for convo in intercom.conversations.find_all(
            email='joe@example.com', type='user', unread=true):
        ...

    # FINDING A SINGLE CONVERSATION
    conversation = intercom.conversations.find(id='1')

    # INTERACTING WITH THE PARTS OF A CONVERSATION
    # Getting the subject of a part (only applies to email-based conversations)
    conversation.rendered_message.subject
    # Get the part_type of the first part
    conversation.conversation_parts[0].part_type
    # Get the body of the second part
    conversation.conversation_parts[1].body

    # REPLYING TO CONVERSATIONS
    # User (identified by email) replies with a comment
    intercom.conversations.reply(
        type='user', email='joe@example.com',
        message_type='comment', body='foo')
    # Admin (identified by email) replies with a comment
    intercom.conversations.reply(
        type='admin', email='bob@example.com',
        message_type='comment', body='bar')
    # User (identified by email) replies with a comment and attachment
    intercom.conversations.reply(id=conversation.id, type='user', email='joe@example.com', message_type='comment', body='foo', attachment_urls=['http://www.example.com/attachment.jpg'])

    # Open
    intercom.conversations.open(id=conversation.id, admin_id='123')

    # Close
    intercom.conversations.close(id=conversation.id, admin_id='123')

    # Assign
    intercom.conversations.assign(id=conversation.id, admin_id='123', assignee_id='124')

    # Reply and Open
    intercom.conversations.reply(id=conversation.id, type='admin', admin_id='123', message_type='open', body='bar')

    # Reply and Close
    intercom.conversations.reply(id=conversation.id, type='admin', admin_id='123', message_type='close', body='bar')

    # ASSIGNING CONVERSATIONS TO ADMINS
    intercom.conversations.reply(id=conversation.id, type='admin', assignee_id=assignee_admin.id, admin_id=admin.id, message_type='assignment')

    # MARKING A CONVERSATION AS READ
    intercom.conversations.mark_read(conversation.id)

Full loading of an embedded entity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    # Given a conversation with a partial user, load the full user. This can be
    # done for any entity
    intercom.users.load(conversation.user)

Sending messages
^^^^^^^^^^^^^^^^

.. code:: python

    # InApp message from admin to user
    intercom.messages.create(**{
        "message_type": "inapp",
        "body": "What's up :)",
        "from": {
            "type": "admin",
            "id": "1234"
        },
        "to": {
            "type": "user",
            "id": "5678"
        }
    })

    # Email message from admin to user
    intercom.messages.create(**{
        "message_type": "email",
        "subject": "Hey there",
        "body": "What's up :)",
        "template": "plain", # or "personal",
        "from": {
            "type": "admin",
            "id": "1234"
        },
        "to": {
            "type": "user",
            "id": "536e564f316c83104c000020"
        }
    })

    # Message from a user
    intercom.messages.create(**{
        "from": {
            "type": "user",
            "id": "536e564f316c83104c000020"
        },
        "body": "halp"
    })

    # Message from admin to contact
    intercom.messages.create(**{
        'body': 'How can I help :)',
        'from': {
            'type': 'admin',
            'id': '1234'
        },
        'to': {
            'type': 'contact',
            'id': '536e5643as316c83104c400671'
        }
    })

    # Message from a contact
    intercom.messages.create(**{
        'from' => {
            'type': 'contact',
            'id': '536e5643as316c83104c400671'
        },
        'body': 'halp'
    })

Events
^^^^^^

.. code:: python

    intercom.events.create(
        event_name='invited-friend',
        created_at=time.mktime(),
        email=user.email,
        metadata={
            'invitee_email': 'pi@example.org',
            'invite_code': 'ADDAFRIEND',
            'found_date': 12909364407
        }
    )

    # Retrieve event list for user with id:'123abc'
    intercom.events.find_all(type='user', "intercom_user_id"="123abc)

Metadata Objects support a few simple types that Intercom can present on
your behalf

.. code:: python

    intercom.events.create(
        event_name="placed-order",
        email=current_user.email,
        created_at=1403001013
        metadata={
            'order_date': time.mktime(),
            'stripe_invoice': 'inv_3434343434',
            'order_number': {
                'value': '3434-3434',
                'url': 'https://example.org/orders/3434-3434'
            },
            'price': {
                'currency': 'usd',
                'amount': 2999
            }
        }
    )

The metadata key values in the example are treated as follows-

-  order\_date: a Date (key ends with '\_date').
-  stripe\_invoice: The identifier of the Stripe invoice (has a
   'stripe\_invoice' key)
-  order\_number: a Rich Link (value contains 'url' and 'value' keys)
-  price: An Amount in US Dollars (value contains 'amount' and
   'currency' keys)

Bulk operations.

.. code:: python

    # Submit bulk job, to create events
    intercom.events.submit_bulk_job(create_items: [
        {
            'event_name': 'ordered-item',
            'created_at': 1438944980,
            'user_id': '314159',
            'metadata': {
                'order_date': 1438944980,
                'stripe_invoice': 'inv_3434343434'
            }
        },
        {
            'event_name': 'invited-friend',
            'created_at': 1438944979,
            'user_id': '314159',
            'metadata': {
                'invitee_email': 'pi@example.org',
                'invite_code': 'ADDAFRIEND'
            }
        }
    ])

    # Submit bulk job, to add items to existing job
    intercom.events.submit_bulk_job(create_items=[
        {
            'event_name': 'ordered-item',
            'created_at': 1438944980,
            'user_id': '314159',
            'metadata': {
                'order_date': 1438944980,
                'stripe_invoice': 'inv_3434343434'
            }
        },
        {
            'event_name': 'invited-friend',
            'created_at': 1438944979,
            'user_id': "314159",
            'metadata': {
                'invitee_email': 'pi@example.org',
                'invite_code': 'ADDAFRIEND'
            }
        }
        ], job_id='job_abcd1234')

Contacts
^^^^^^^^

Contacts represent logged out users of your application.

.. code:: python

    # Create a contact
    contact = intercom.contacts.create(email="some_contact@example.com")

    # Update a contact
    contact.custom_attributes['foo'] = 'bar'
    intercom.contacts.save(contact)

    # Find contacts by email
    contacts = intercom.contacts.find_all(email="some_contact@example.com")

    # Convert a contact into a user
    intercom.contacts.convert(contact, user)

    # Delete a contact
    intercom.contacts.delete(contact)

Counts
^^^^^^

.. code:: python

    # App-wide counts
    intercom.counts.for_app()

    # Users in segment counts
    intercom.counts.for_type(type='user', count='segment')

Subscriptions
~~~~~~~~~~~~~

Subscribe to events in Intercom to receive webhooks.

.. code:: python

    # create a subscription
    intercom.subscriptions.create(url='http://example.com', topics=['user.created'])

    # fetch a subscription
    intercom.subscriptions.find(id='nsub_123456789')

    # list subscriptions
    intercom.subscriptions.all():
        ...

Bulk jobs
^^^^^^^^^

.. code:: python

    # fetch a job
    intercom.jobs.find(id='job_abcd1234')

    # fetch a job's error feed
    intercom.jobs.errors(id='job_abcd1234')

Errors
~~~~~~

You do not need to deal with the HTTP response from an API call
directly. If there is an unsuccessful response then an error that is a
subclass of ``intercom.Error`` will be raised. If desired, you can get
at the http\_code of an ``Error`` via it's ``http_code`` method.

The list of different error subclasses are listed below. As they all
inherit off ``IntercomError`` you can choose to except ``IntercomError``
or the more specific error subclass:

.. code:: python

    AuthenticationError
    ServerError
    ServiceUnavailableError
    ServiceConnectionError
    ResourceNotFound
    BadGatewayError
    BadRequestError
    RateLimitExceeded
    MultipleMatchingUsersError
    HttpError
    UnexpectedError

Rate Limiting
~~~~~~~~~~~~~

Calling your clients ``rate_limit_details`` returns a dict that contains
details about your app's current rate limit.

.. code:: python

    intercom.rate_limit_details
    # {'limit': 180, 'remaining': 179, 'reset_at': datetime.datetime(2014, 10, 07, 14, 58)}

Running the Tests
-----------------

Unit tests:

.. code:: bash

    nosetests tests/unit

Integration tests:

.. code:: bash

    INTERCOM_PERSONAL_ACCESS_TOKEN=xxx nosetests tests/integration

.. |PyPI Version| image:: https://img.shields.io/pypi/v/python-intercom.svg
   :target: https://pypi.python.org/pypi/python-intercom
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/python-intercom.svg
   :target: https://pypi.python.org/pypi/python-intercom
.. |Travis CI Build| image:: https://travis-ci.org/jkeyes/python-intercom.svg
   :target: https://travis-ci.org/jkeyes/python-intercom
.. |Coverage Status| image:: https://coveralls.io/repos/jkeyes/python-intercom/badge.svg?branch=master
   :target: https://coveralls.io/r/jkeyes/python-intercom?branch=master
