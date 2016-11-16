FAQ
===

How do I start a session?
-------------------------

::

    user = intercom.users.create(email='bingo@example.com')
    # register a new session
    user.new_session = True
    intercom.users.save(user)
