# python-intercom
=================

Python bindings for the Intercom API (https://api.intercom.io).

[API Documentation](https://api.intercom.io/docs).

[Package Documentation](http://readthedocs.org/docs/python-intercom/).

## Upgrading information

Version 2 of python-intercom is **not backwards compatible** with previous versions.

One change you will need to make as part of the upgrade is to set `Intercom.app_api_key` and not set `Intercom.api_key`.

## Installation

    pip install python-intercom

## Basic Usage

### Configure your access credentials

```python
Intercom.app_id = "my_app_id"
Intercom.app_api_key = "my-super-crazy-api-key"
```


### Resources

Resources this API supports:

    https://api.intercom.io/users
    https://api.intercom.io/companies
    https://api.intercom.io/tags
    https://api.intercom.io/notes
    https://api.intercom.io/segments
    https://api.intercom.io/events
    https://api.intercom.io/conversations
    https://api.intercom.io/messages
    https://api.intercom.io/counts
    https://api.intercom.io/subscriptions

Additionally, the library can handle incoming webhooks from Intercom and convert to `intercom` models.

### Examples


#### Users

``` python
from intercom import User
# Find user by email
user = User.find(email="bob@example.com")
# Find user by user_id
user = User.find(user_id="1")
# Find user by id
user = User.find(id="1")
# Create a user
user = User.create(email="bob@example.com", name="Bob Smith")
# Update custom_attributes for a user
user.custom_attributes["average_monthly_spend"] = 1234.56
user.save()
# Perform incrementing
user.increment('karma')
user.save()
# Iterate over all users
for user in User.all()
    ...
```

#### Admins

``` python
from intercom import Admin
# Iterate over all admins
for admin in Admin.all()
    ...
```

#### Companies

``` python
from intercom import Company
from intercom import User
# Add a user to one or more companies
user = User.find(email="bob@example.com")
user.companies = [
    {company_id 6, name "Intercom"},
    {company_id 9, name "Test Company"}
]
user.save()
# You can also pass custom attributes within a company as you do this
user.companies = [
    {
        id6,
        name "Intercom", custom_attributes {
            referral_source "Google"
        } 
    } 
]
user.save()
# Find a company by company_id
company = Company.find(company_id="44")
# Find a company by name
company = Company.find(name="Some company")
# Find a company by id
company = Company.find(id="41e66f0313708347cb0000d0")
# Update a company
company.name = 'Updated company name'
company.save()
# Iterate over all companies
for company in Company.all()
    ...
# Get a list of users in a company
company.users
```

#### Tags

``` python
from intercom import Tag
# Tag users
tag = Tag.tag_users('blue', ["42ea2f1b93891f6a99000427"])
# Untag users
Tag.untag_users('blue', ["42ea2f1b93891f6a99000427"])
# Iterate over all tags
for tag in Tag.all()
    ...
# Iterate over all tags for user
Tag.find_all_for_user(id='53357ddc3c776629e0000029')
Tag.find_all_for_user(email='declan+declan@intercom.io')
Tag.find_all_for_user(user_id='3')
# Tag companies
tag = Tag.tag_companies('red', ["42ea2f1b93891f6a99000427"])
# Untag companies
Tag.untag_users('blue', ["42ea2f1b93891f6a99000427"])
# Iterate over all tags for company
Tag.find_all_for_company(id='43357e2c3c77661e25000026')
Tag.find_all_for_company(company_id='6')
```

#### Segments

``` python
from intercom import Segment
# Find a segment
segment = Segment.find(id=segment_id)
# Update a segment
segment.name = 'Updated name'
segment.save()
# Iterate over all segments
for segment in Segment.all():
    ...
```

#### Notes

``` python
# Find a note by id
note = Note.find(id=note)
# Create a note for a user
note = Note.create(
    body="<p>Text for the note</p>",
    email='joe@example.com')
# Iterate over all notes for a user via their email address
for note in Note.find_all(email='joe@example.com'):
    ...
# Iterate over all notes for a user via their user_id
for note in Note.find_all(user_id='123'):
    ...
```

#### Conversations

``` python
from intercom import Conversation
# FINDING CONVERSATIONS FOR AN ADMIN
# Iterate over all conversations (open and closed) assigned to an admin
for convo in Conversation.find_all(type='admin', id='7'):
    ...
# Iterate over all open conversations assigned to an admin
for convo Conversation.find_all(type='admin', id=7, open=True):
    ...
# Iterate over closed conversations assigned to an admin
for convo Conversation.find_all(type='admin', id=7, open=False):
    ...
# Iterate over closed conversations for assigned an admin, before a certain moment in time
for convo in Conversation.find_all(
        type='admin', id= 7, open= False, before=1374844930):
    ...

# FINDING CONVERSATIONS FOR A USER
# Iterate over all conversations (read + unread, correct) with a user based on the users email
for convo in Conversation.find_all(email='joe@example.com',type='user'):
    ...
# Iterate over through all conversations (read + unread) with a user based on the users email
for convo in Conversation.find_all(
        email='joe@example.com', type='user', unread=False):
    ...
# Iterate over all unread conversations with a user based on the users email
for convo in Conversation.find_all(
        email='joe@example.com', type='user', unread=true):
    ...

# FINDING A SINGLE CONVERSATION
conversation = Conversation.find(id='1')

# INTERACTING WITH THE PARTS OF A CONVERSATION
# Getting the subject of a part (only applies to email-based conversations)
conversation.rendered_message.subject
# Get the part_type of the first part
conversation.conversation_parts[0].part_type
# Get the body of the second part
conversation.conversation_parts[1].body

# REPLYING TO CONVERSATIONS
# User (identified by email) replies with a comment
conversation.reply(
    type='user', email='joe@example.com',
    message_type= comment', body='foo')
# Admin (identified by email) replies with a comment
conversation.reply(
    type='admin', email='bob@example.com', 
    message_type='comment', body='bar')

# MARKING A CONVERSATION AS READ
conversation.read = True
conversation.save()
```

#### Counts

``` python
from intercom import Count
# Get Conversation per Admin
conversation_counts_for_each_admin = Count.conversation_counts_for_each_admin()
for count in conversation_counts_for_each_admin:
    print "Admin: %s (id: %s) Open: %s Closed: %s" % (
        count.name, count.id, count.open, count.closed)
# Get User Tag Count Object
Count.user_counts_for_each_tag()
# Get User Segment Count Object
Count.user_counts_for_each_segment()
# Get Company Segment Count Object
Count.company_counts_for_each_segment()
# Get Company Tag Count Object
Count.company_counts_for_each_tag()
# Get Company User Count Object
Count.company_counts_for_each_user()
# Get total count of companies, users, segments or tags across app
Company.count()
User.count()
Segment.count()
Tag.count()
```

#### Full loading of and embedded entity

``` python
    # Given a converation with a partial user, load the full user. This can be done for any entity
    conversation.user.load()
```

#### Sending messages

``` python
# InApp message from admin to user
Message.create({
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
Message.create({
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
Message.create({
    "from": {
        "type": "user",
        "id": "536e564f316c83104c000020"
    },
    "body": "halp"
})
```

#### Events

``` python
from intercom import Event
Event.create(
    event_name="invited-friend",
    created_at=time.mktime(),
    email=user.email,
    metadata={
        "invitee_email": "pi@example.org",
        "invite_code": "ADDAFRIEND",
        "found_date": 12909364407
    }
)
```

Metadata Objects support a few simple types that Intercom can present on your behalf

``` python
Event.create(
    event_name="placed-order",
    email=current_user.email,
    created_at=1403001013
    metadata={
        "order_date": time.mktime(),
        "stripe_invoice": 'inv_3434343434',
        "order_number": {
            "value": '3434-3434',
            "url": 'https://example.org/orders/3434-3434'
        },
        "price": {
            "currency": 'usd',
            "amount": 2999
        }
    }
)
```

The metadata key values in the example are treated as follows-
- order_date: a Date (key ends with '_date').
- stripe_invoice: The identifier of the Stripe invoice (has a 'stripe_invoice' key)
- order_number: a Rich Link (value contains 'url' and 'value' keys)
- price: An Amount in US Dollars (value contains 'amount' and 'currency' keys)

### Subscriptions

Subscribe to events in Intercom to receive webhooks.

``` python
from intercom import Subscription
# create a subscription
Subscription.create(url="http://example.com", topics=["user.created"])

# fetch a subscription
Subscription.find(id="nsub_123456789")

# list subscriptions
Subscription.all()
```

### Webhooks

``` python
from intercom import Notification
# create a payload from the notification hash (from json).
payload = Intercom::Notification.new(notification_hash)

payload.type
# 'user.created'

payload.model_type
# User

user = payload.model
# Instance of User
```

Note that models generated from webhook notifications might differ slightly from models directly acquired via the API. If this presents a problem, calling `payload.load` will load the model from the API using the `id` field.


### Errors
You do not need to deal with the HTTP response from an API call directly. If there is an unsuccessful response then an error that is a subclass of `intercom.Error` will be raised. If desired, you can get at the http_code of an `Error` via it's `http_code` method.

The list of different error subclasses are listed below. As they all inherit off `Error` you can choose to except `Error` or the more specific error subclass:

```python
AuthenticationError
ServerError
ServiceUnavailableError
ResourceNotFound
BadRequestError
RateLimitExceeded
AttributeNotSetError # Raised when you try to call a getter that does not exist on an object
```
