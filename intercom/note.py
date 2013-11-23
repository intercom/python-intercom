# coding=utf-8
#
# Copyright 2013 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" Note module.

>>> from intercom import Intercom
>>> Intercom.app_id = 'dummy-app-id'
>>> Intercom.api_key = 'dummy-api-key'
>>> from intercom import Note

"""

from . import Intercom
from . import from_timestamp_property
from . import to_timestamp_property
from .user import User
from .user import UserId


class Note(UserId):
    """ A note on a User. """

    @classmethod
    def create(cls, user_id=None, email=None, body=None):
        """ Create a Note.

        >>> note = Note.create(email="somebody@example.com",
        ...        body="This is a note.")
        >>> note.created_at.year
        2011
        >>> note.html
        u'<p>This is a note</p>'

        """
        resp = Intercom.create_note(user_id=user_id, email=email, body=body)
        return cls(resp)

    def save(self):
        """ Create a Note from this objects properties:

        >>> note = Note()
        >>> note.email = "somebody@example.com"
        >>> note.body = "This is a note."
        >>> note.save()
        >>> note.html
        u'<p>This is a note</p>'

        """
        resp = Intercom.create_note(
            user_id=self.user_id, email=self.email, body=self.body)
        self.update(resp)

    @property
    def body(self):
        """ The body of the note. """
        return dict.get(self, 'body', None)

    @body.setter
    def body(self, body):
        """ Set the note body. """
        self['body'] = body

    @property
    def html(self):
        """ Get the html of the note – set by an API response. """
        return dict.get(self, 'html', None)

    @property
    @from_timestamp_property
    def created_at(self):
        """ Returns the datetime this note was created – set by an
        API response. """
        return dict.get(self, 'created_at', None)

    @created_at.setter
    @to_timestamp_property
    def created_at(self, created_at):
        """ Set the datetime this note was created. """
        self['created_at'] = created_at

    @property
    def user(self):
        """ Get the noted user – set by an API response. """
        data = dict.get(self, 'user', None)
        if data:
            return User(**data)
