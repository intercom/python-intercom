FAQ
===

How do I start a session?
-------------------------

::

    user = User.create(email='bingo@example.com')
    # register a new session
    user.new_session = True
    user.save()
