# -*- coding: utf-8 -*-
"""Operation to convert a contact into a user."""


class Convert(object):
    """A mixin that provides `convert` functionality."""

    def convert(self, contact, user):
        """Convert the specified contact into the specified user."""
        self.client.post(
            '/contacts/convert',
            {
                'contact': {'user_id': contact.user_id},
                'user': self.identity_hash(user)
            }
        )
