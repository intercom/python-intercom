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

Authentication
---------------

Intercom documentation: `Authentication <http://api.intercom.io/docs#authentication>`_.

::

    from intercom import Intercom
    Intercom.app_id = 'dummy-app-id'
    Intercom.app_api_key = 'dummy-api-key'

Users
-----

Create or Update User
+++++++++++++++++++++

Intercom documentation: `Create or Update Users <https://doc.intercom.io/api/#create-or-update-user>`_.

::

    from intercom import User
    User.create(id='1234', email='bob@example.com')

Updating the Last Seen Time
+++++++++++++++++++++++++++

Intercom documentation: `Updating the Last Seen Time <https://doc.intercom.io/api/#updating-the-last-seen-time>`_.

::

    user = User.create(used_id='25', last_request_at=datetime.now())

List Users
++++++++++

Intercom documentation: `List Users <https://doc.intercom.io/api/#list-users>`_.

::

    for user in User.all():
        ...

List by Tag, Segment, Company
+++++++++++++++++++++++++++++

Intercom documentation: `List by Tag, Segment, Company <https://doc.intercom.io/api/#list-by-tag-segment-company>`_.

::

    # tag request
    User.find_all(tag_id='30126')
    
    # segment request
    User.find_all(segment_id='30126')


View a User
+++++++++++

Intercom documentation: `View a User <https://doc.intercom.io/api/#view-a-user>`_.

::

    # ID request
    User.find(id='1')
    
    # User ID request
    User.find(user_id='1')
    
    # Email request
    User.find(email='bob@example.com')

Delete a User
+++++++++++++

Intercom documentation: `Deleting a User <https://doc.intercom.io/api/#delete-a-user>`_.

::

    # ID Delete Request
    deleted_user = User.find(id='1').delete()
    
    # User ID Delete Request
    deleted_user = User.find(user_id='1').delete()
    
    # Email Delete Request
    deleted_user = User.find(email='bob@example.com').delete()


Companies
---------

Create or Update Company
++++++++++++++++++++++++

Intercom documentation: `Create or Update Company <https://doc.intercom.io/api/#create-or-update-company>`_.

::

    Company.create(company_id=6, name="Blue Sun", plan="Paid")

List Companies
++++++++++++++

Intercom documentation: `List Companies <https://doc.intercom.io/api/#list-companies>`_.

::

    for company in Company.all():
        ...

List by Tag or Segment
++++++++++++++++++++++

Intercom documentation: `List by Tag or Segment <https://doc.intercom.io/api/#list-by-tag-or-segment>`_.

::

    # tag request
    Company.find(tag_id="1234")

    # segment request
    Company.find(segment_id="4567")

View a Company
++++++++++++++

Intercom documentation: `View a Company <https://doc.intercom.io/api/#view-a-company>`_.

::

    Company.find(id="41e66f0313708347cb0000d0")

List Company Users
++++++++++++++++++

Intercom documentation: `List Company Users <https://doc.intercom.io/api/#list-company-users>`_.

::

    company = Company.find(id="41e66f0313708347cb0000d0")
    for user in company.users:
        ...

Admins
------

List Admins
+++++++++++

Intercom documentation: `List Admins <https://doc.intercom.io/api/#list-admins>`_.

::

    from intercom import Admin
    for admin in Admin.all():
        ...

Tags
----

Create and Update Tags
++++++++++++++++++++++

Intercom documentation: `Create and Update Tags <https://doc.intercom.io/api/?ruby#create-and-update-tags>`_.

::

    from intercom import Tag
    
    # Create Request
    tag = Tag.create(name='Independentt')
    
    # Update Request
    Tag.tag_users(name='Independent', id=tag.id)
    

Tag or Untag Users & Companies
++++++++++++++++++++++++++++++

Intercom documentation: `Tag or Untag Users & Companies <https://doc.intercom.io/api/#tag-or-untag-users--companies>`_.

::

    # Multi-User Tag Request
    Tag.tag_users('Independent', ["42ea2f1b93891f6a99000427", "42ea2f1b93891f6a99000428"])
    
    # Untag Request
    Tag.untag_users('blue', ["42ea2f1b93891f6a99000427"])

Delete a Tag
++++++++++++

Intercom documentation: `Delete a Tag <https://doc.intercom.io/api/?ruby#delete-a-tag>`_.

::

    tag.delete()


List Tags for an App
++++++++++++++++++++

Intercom Documentation: `List Tags for an App <https://doc.intercom.io/api/#list-tags-for-an-app>`_.

::

    for tag in Tag.all():
        ...

Segments
--------

List Segments
+++++++++++++

Intercom Documentation: `List Segments <https://doc.intercom.io/api/#list-segments>`_.

::

    from intercom import Segment
    
    for segment in Segment.all():
        ...

View a Segment
++++++++++++++

Intercom Documentation: `View a Segment <https://doc.intercom.io/api/#view-a-segment>`_.

::

    Segment.find(id='1234')

Notes
-----

Create a Note
+++++++++++++

Intercom documentation: `Create a Note <https://doc.intercom.io/api/#create-a-note>`_.

::

    from intercom import Note
    
    Note.create(email="joe@exampe.com", body="Text for the note")


List Notes for a User
+++++++++++++++++++++

Intercom documentation: `List Notes for a User <https://doc.intercom.io/api/#list-notes-for-a-user>`_.

::

    # User ID Request
    for note in Note.find_all(user_id='123'):
        ...
    
    # User Email Request
    for note in Note.find_all(email='foo@bar.com'):
        ...

View a Note
+++++++++++

Intercom documentation: `View a Note <https://doc.intercom.io/api/#view-a-note>`_.

::

    Note.find(id='1234')

Events
------

Submitting Events
+++++++++++++++++

Intercom documentation: `Submitting Events <https://doc.intercom.io/api/#submitting-events>`_.

::

    from intercom import Event
    Event.create(event_name="Eventful 1", email=user.email, created_at=1403001013)


Counts
------

Getting counts
++++++++++++++

Intercom documentation: `Creating a Tag <https://doc.intercom.io/api/#getting-counts>`_.

::

    from intercom import Count
    
    # Conversation Admin Count
    Count.conversation_counts_for_each_admin
    
    # User Tag Count
    Count.user_counts_for_each_tag
    
    # User Segment Count
    Count.user_counts_for_each_segment
    
    # Company Segment Count
    Count.company_counts_for_each_segment
    
    # Company Tag Count
    Count.company_counts_for_each_tag
    
    # Company User Count
    Count.company_counts_for_each_user
    
    # Global App Counts
    Company.count
    User.count
    Segment.count
    Tag.count

Conversations
-------------

Admin Initiated Conversation
++++++++++++++++++++++++++++

Intercom documentation: `Admin Initiated Conversation <https://doc.intercom.io/api/#admin-initiated-conversation>`_.

::

    from intercom import Message
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
    Message.create(**message_data)

User Initiated Conversation
+++++++++++++++++++++++++++

Intercom documentation: `User Initiated Conversation <https://doc.intercom.io/api/#user-initiated-conversation>`_.

::

    message_data = {
        'from': {
            'type': "user",
            'id': "536e564f316c83104c000020"
        },
        'body': "Hey"
    }
    Message.create(**message_data)

List Conversations
++++++++++++++++++

Intercom documentation: `List Conversations <https://doc.intercom.io/api/#list-conversations>`_.

::

    from intercom import Conversation
    Conversation.find_all(type='admin', id=25, open=True)


Get a Single Conversation
+++++++++++++++++++++++++

Intercom documentation: `Get a Single Conversation <https://doc.intercom.io/api/#get-a-single-conversation>`_.

::

    Conversation.find(id='147')

Replying to a Conversation
++++++++++++++++++++++++++

Intercom documentation: `Replying to a Conversation <https://doc.intercom.io/api/#replying-to-a-conversation>`_.

::

    conversation.reply(type='user', email='bob@example.com', message_type='comment', body='foo')


Marking a Conversation as Read
++++++++++++++++++++++++++++++

Intercom documentation: `Marking a Conversation as Read <https://doc.intercom.io/api/#marking-a-conversation-as-read>`_.

::

    conversation.read = True
    conversation.save()


Webhooks and Notifications
--------------------------

Manage Subscriptions
++++++++++++++++++++

Intercom documentation: `Manage Subscriptions <https://doc.intercom.io/api/#manage-subscriptions>`_.

::

    from intercom import Subscription
    Subscription.create(service_type='web', url='http://example.com', topics=['all'])


View a Subscription
+++++++++++++++++++

Intercom documentation: `View a Subscription <https://doc.intercom.io/api/#view-a-subscription>`_.

::

    Subscription.find(id='123')

List Subscriptions
++++++++++++++++++

Intercom documentation: `List Subscriptions <https://doc.intercom.io/api/#list-subscriptions>`_.

::

    for subscription in Subscription.all():
        ...

Development
===========

Our :doc:`development` page has detailed instructions on how to run our
tests, and to produce coverage and pylint reports.

Changelog
=========

The :doc:`changelog` keeps track of changes per release.
