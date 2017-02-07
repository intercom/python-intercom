===============
python-intercom
===============

.. toctree::
    :hidden:

    installation
    faq
    changelog
    development
    api/modules

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

Authorization
-------------

Intercom documentation: `Personal Access Tokens <https://developers.intercom.com/reference#personal-access-tokens-1>`_.

::

    from intercom.client import Client
    intercom = Client(personal_access_token='my_personal_access_token')

Users
-----

Create or Update User
+++++++++++++++++++++

Intercom documentation: `Create or Update Users <https://developers.intercom.io/reference#create-or-update-user>`_.

::

    intercom.users.create(user_id='1234', email='bob@example.com')

Updating the Last Seen Time
+++++++++++++++++++++++++++

Intercom documentation: `Updating the Last Seen Time <https://developers.intercom.io/reference#updating-the-last-seen-time>`_.

::

    user = intercom.users.create(used_id='25', last_request_at=datetime.utcnow())

List Users
++++++++++

Intercom documentation: `List Users <https://developers.intercom.io/reference#list-users>`_.

::

    for user in intercom.users.all():
        ...

List by Tag, Segment, Company
+++++++++++++++++++++++++++++

Intercom documentation: `List by Tag, Segment, Company <https://developers.intercom.io/reference#list-by-tag-segment-company>`_.

::

    # tag request
    intercom.users.find_all(tag_id='30126')
    
    # segment request
    intercom.users.find_all(segment_id='30126')


View a User
+++++++++++

Intercom documentation: `View a User <https://developers.intercom.io/reference#view-a-user>`_.

::

    # ID request
    intercom.users.find(id='1')
    
    # User ID request
    intercom.users.find(user_id='1')
    
    # Email request
    intercom.users.find(email='bob@example.com')

Delete a User
+++++++++++++

Intercom documentation: `Deleting a User <https://developers.intercom.io/reference#delete-a-user>`_.

::

    # ID Delete Request
    user = intercom.users.find(id='1')
    deleted_user = intercom.users.delete(user)
    
    # User ID Delete Request
    user = intercom.users.find(user_id='1')
    deleted_user = intercom.users.delete(user)
    
    # Email Delete Request
    user = intercom.users.find(email='bob@example.com')
    deleted_user = intercom.users.delete(user)


Companies
---------

Create or Update Company
++++++++++++++++++++++++

Intercom documentation: `Create or Update Company <https://developers.intercom.io/reference#create-or-update-company>`_.

::

    intercom.companies.create(company_id=6, name="Blue Sun", plan="Paid")

List Companies
++++++++++++++

Intercom documentation: `List Companies <https://developers.intercom.io/reference#list-companies>`_.

::

    for company in intercom.companies.all():
        ...

List by Tag or Segment
++++++++++++++++++++++

Intercom documentation: `List by Tag or Segment <https://developers.intercom.io/reference#list-by-tag-or-segment>`_.

::

    # tag request
    intercom.companies.find(tag_id="1234")

    # segment request
    intercom.companies.find(segment_id="4567")

View a Company
++++++++++++++

Intercom documentation: `View a Company <https://developers.intercom.io/reference#view-a-company>`_.

::

    intercom.companies.find(id="41e66f0313708347cb0000d0")

List Company Users
++++++++++++++++++

Intercom documentation: `List Company Users <https://developers.intercom.io/reference#list-company-users>`_.

::

    company = intercom.companies.find(id="41e66f0313708347cb0000d0")
    for user in company.users:
        ...

Admins
------

List Admins
+++++++++++

Intercom documentation: `List Admins <https://developers.intercom.io/reference#list-admins>`_.

::

    for admin in intercom.admins.all():
        ...

Tags
----

Create and Update Tags
++++++++++++++++++++++

Intercom documentation: `Create and Update Tags <https://developers.intercom.io/reference#create-and-update-tags>`_.

::

    # Create Request
    tag = intercom.tags.create(name='Independentt')
    
    # Update Request
    intercom.tags.tag_users(name='Independent', id=tag.id)
    

Tag or Untag Users & Companies
++++++++++++++++++++++++++++++

Intercom documentation: `Tag or Untag Users & Companies <https://developers.intercom.io/reference#tag-or-untag-users-companies-leads-contacts>`_.

::

    # Multi-User Tag Request
    intercom.tags.tag_users('Independent', ["42ea2f1b93891f6a99000427", "42ea2f1b93891f6a99000428"])
    
    # Untag Request
    intercom.tags.untag_users('blue', ["42ea2f1b93891f6a99000427"])

Delete a Tag
++++++++++++

Intercom documentation: `Delete a Tag <https://developers.intercom.io/reference#delete-a-tag>`_.

::

    intercom.tags.delete()


List Tags for an App
++++++++++++++++++++

Intercom Documentation: `List Tags for an App <https://developers.intercom.io/reference#list-tags-for-an-app>`_.

::

    for intercom.tags in Tag.all():
        ...

Segments
--------

List Segments
+++++++++++++

Intercom Documentation: `List Segments <https://developers.intercom.io/reference#list-segments>`_.

::

    for segment in intercom.segments.all():
        ...

View a Segment
++++++++++++++

Intercom Documentation: `View a Segment <https://developers.intercom.io/reference#view-a-segment>`_.

::

    intercom.segments.find(id='1234')

Notes
-----

Create a Note
+++++++++++++

Intercom documentation: `Create a Note <https://developers.intercom.io/reference#create-a-note>`_.

::

    intercom.notes.create(email="joe@exampe.com", body="Text for the note")


List Notes for a User
+++++++++++++++++++++

Intercom documentation: `List Notes for a User <https://developers.intercom.io/reference#list-notes-for-a-user>`_.

::

    # User ID Request
    for note in intercom.notes.find_all(user_id='123'):
        ...
    
    # User Email Request
    for note in intercom.notes.find_all(email='foo@bar.com'):
        ...

View a Note
+++++++++++

Intercom documentation: `View a Note <https://developers.intercom.io/reference#view-a-note>`_.

::

    intercom.notes.find(id='1234')

Events
------

Submitting Events
+++++++++++++++++

Intercom documentation: `Submitting Events <https://developers.intercom.io/reference#submitting-events>`_.

::

    intercom.events.create(event_name="Eventful 1", email=user.email, created_at=1403001013)


Counts
------

Getting counts
++++++++++++++

Intercom documentation: `Getting Counts <https://developers.intercom.io/reference#getting-counts>`_.

::

    # Conversation Admin Count
    intercom.counts.for_type(type='converation', count='admin')
    
    # User Tag Count
    intercom.counts.for_type(type='user', count='tag')
    
    # User Segment Count
    intercom.counts.for_type(type='user', count='segment')

    # Company Tag Count
    intercom.counts.for_type(type='company', count='tag')

    # Company User Count
    intercom.counts.for_type(type='company', count='user')
    
    # Global App Counts
    intercom.counts.for_type()

Conversations
-------------

Admin Initiated Conversation
++++++++++++++++++++++++++++

Intercom documentation: `Admin Initiated Conversation <https://developers.intercom.io/reference#admin-initiated-conversation>`_.

::

    message_data = {
        'message_type': 'email',
        'subject': 'This Land',
        'body': "Har har har! Mine is an evil laugh!",
        'template': "plain",
        'from': {
            'type': "admin",
            'id': "394051"
        },
        'to': {
            'type': "user",
            'id': "536e564f316c83104c000020"
        }
    }
    intercom.messages.create(**message_data)

User Initiated Conversation
+++++++++++++++++++++++++++

Intercom documentation: `User Initiated Conversation <https://developers.intercom.io/reference#user-or-contact-initiated-conversation>`_.

::

    message_data = {
        'from': {
            'type': "user",
            'id': "536e564f316c83104c000020"
        },
        'body': "Hey"
    }
    intercom.messages.create(**message_data)

List Conversations
++++++++++++++++++

Intercom documentation: `List Conversations <https://developers.intercom.io/reference#list-conversations>`_.

::

    intercom.conversations.find_all(type='admin', id=25, open=True)


Get a Single Conversation
+++++++++++++++++++++++++

Intercom documentation: `Get a Single Conversation <https://developers.intercom.io/reference#get-a-single-conversation>`_.

::

    intercom.conversations.find(id='147')

Replying to a Conversation
++++++++++++++++++++++++++

Intercom documentation: `Replying to a Conversation <https://developers.intercom.io/reference#replying-to-a-conversation>`_.

::

    conversation.reply(type='user', email='bob@example.com', message_type='comment', body='foo')


Marking a Conversation as Read
++++++++++++++++++++++++++++++

Intercom documentation: `Marking a Conversation as Read <https://developers.intercom.io/reference#marking-a-conversation-as-read>`_.

::

    conversation.read = True
    conversation.save()


Webhooks and Notifications
--------------------------

Manage Subscriptions
++++++++++++++++++++

Intercom documentation: `Manage Subscriptions <https://developers.intercom.io/reference#manage-subscriptions>`_.

::

    intercom.subscriptions.create(service_type='web', url='http://example.com', topics=['all'])


View a Subscription
+++++++++++++++++++

Intercom documentation: `View a Subscription <https://developers.intercom.io/reference#view-a-subscription>`_.

::

    intercom.subscriptions.find(id='123')

List Subscriptions
++++++++++++++++++

Intercom documentation: `List Subscriptions <https://developers.intercom.io/reference#list-subscriptions>`_.

::

    for subscription in intercom.subscriptions.all():
        ...

Development
===========

Our :doc:`development` page has detailed instructions on how to run our
tests, and to produce coverage and pylint reports.

Changelog
=========

The :doc:`changelog` keeps track of changes per release.
