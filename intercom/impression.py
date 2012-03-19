#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from . import Intercom
from .user import UserId

class Impression(UserId):

    @classmethod
    def create(cls, user_id=None, email=None, user_ip=None, user_agent=None):
        resp = Intercom.create_impression(user_id=user_id, email=email, 
            user_ip=user_ip, user_agent=user_agent)
        return cls(resp)

    def save(self):
        print "Impression save..."
        resp = Intercom.create_impression(**self)
        self.update(resp)

    @property
    def user_ip(self):
        return dict.get(self, 'user_ip', None)

    @user_ip.setter
    def user_ip(self, user_ip):
        self['user_ip'] = user_ip

    @property
    def location(self):
        return dict.get(self, 'location', None)

    @location.setter
    def location(self, location):
        self['location'] = location

    @property
    def user_agent(self):
        return dict.get(self, 'user_agent', None)

    @user_agent.setter
    def user_agent(self, user_agent):
        self['user_agent'] = user_agent

    @property
    def unread_messages(self):
        return dict.get(self, 'unread_messages', None)
