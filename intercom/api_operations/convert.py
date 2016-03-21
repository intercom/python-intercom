# -*- coding: utf-8 -*-


class Convert(object):

    def convert(self, contact, user):
        self.client.post(
            '/contacts/convert',
            {
                'contact': {'user_id': contact.user_id},
                'user': self.identity_hash(user)
            }
        )
