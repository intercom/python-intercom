#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from . import Intercom
from . import from_timestamp_property

class MessageThread(dict):
    _get = dict.get

    @classmethod
    def find(cls, user_id=None, email=None, thread_id=None):
        resp = Intercom.get_message_threads(user_id=user_id, email=email, 
                thread_id=thread_id)
        return [MessageThread(mt) for mt in resp]

    @classmethod
    def find_all(cls, user_id=None, email=None):
        resp = Intercom.get_message_threads(user_id=user_id, email=email)
        return [MessageThread(mt) for mt in resp]

    @classmethod
    def create(cls, user_id=None, email=None, body=None):
        resp = Intercom.create_message_thread(user_id=user_id, email=email, 
                body=body)
        return MessageThread(resp)

    @classmethod
    def reply(cls, user_id=None, email=None, thread_id=None, 
            body=None, read=None):
        resp = Intercom.reply_message_thread(user_id=user_id, email=email, 
                thread_id=thread_id, read=None, body=body)
        return MessageThread(resp)

    @property
    @from_timestamp_property
    def updated_at(self):
        return dict.get(self, 'updated_at', None)

    @property
    @from_timestamp_property
    def created_at(self):
        return dict.get(self, 'created_at', None)

    @property
    def body(self):
        return dict.get(self, 'body', None)

    @property
    def thread_id(self):
        return dict.get(self, 'thread_id', None)

    @thread_id.setter
    def thread_id(self, value):
        self['thread_id'] = value

    @property
    def read(self):
        return dict.get(self, 'read', None)

    @thread_id.setter
    def read(self, value):
        self['read'] = value

    @property
    def messages(self):
        messages = dict.get(self, 'messages', None)
        if messages:
            return [Message(m) for m in messages]

class Message(dict):

    @property
    def author(self):
        _from = self.get('from', None)
        if _from:
            return MessageAuthor(_from)

    @property
    def html(self):
        return dict.get(self, 'html', None)

    @property
    def created_at(self):
        return dict.get(self, 'created_at', None)

class MessageAuthor(dict):

    @property
    def admin(self):
        return dict.get(self, 'admin', None)

    @property
    def email(self):
        return dict.get(self, 'email', None)

    @property
    def user_id(self):
        return dict.get(self, 'user_id', None)

    @property
    def avatar_path_50(self):
        return dict.get(self, 'avatar_path_50', None)

    @property
    def name(self):
        return dict.get(self, 'name', None)

