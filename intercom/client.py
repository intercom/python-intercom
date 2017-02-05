# -*- coding: utf-8 -*-

import requests


class Client(object):

    def __init__(self, personal_access_token='my_personal_access_token'):
        self.personal_access_token = personal_access_token
        self.base_url = 'https://api.intercom.io'
        self.rate_limit_details = {}
        self.http_session = requests.Session()

    @property
    def _auth(self):
        return (self.personal_access_token, '')

    @property
    def admins(self):
        from intercom.service import admin
        return admin.Admin(self)

    @property
    def companies(self):
        from intercom.service import company
        return company.Company(self)

    @property
    def conversations(self):
        from intercom.service import conversation
        return conversation.Conversation(self)

    @property
    def counts(self):
        from intercom.service import count
        return count.Count(self)

    @property
    def events(self):
        from intercom.service import event
        return event.Event(self)

    @property
    def messages(self):
        from intercom.service import message
        return message.Message(self)

    @property
    def notes(self):
        from intercom.service import note
        return note.Note(self)

    @property
    def segments(self):
        from intercom.service import segment
        return segment.Segment(self)

    @property
    def subscriptions(self):
        from intercom.service import subscription
        return subscription.Subscription(self)

    @property
    def tags(self):
        from intercom.service import tag
        return tag.Tag(self)

    @property
    def users(self):
        from intercom.service import user
        return user.User(self)

    @property
    def leads(self):
        from intercom.service import lead
        return lead.Lead(self)

    @property
    def jobs(self):
        from intercom.service import job
        return job.Job(self)

    def _execute_request(self, request, params):
        result = request.execute(self.base_url, self._auth, params)
        self.rate_limit_details = request.rate_limit_details
        return result

    def get(self, path, params):
        from intercom import request
        req = request.Request('GET', path, self.http_session)
        return self._execute_request(req, params)

    def post(self, path, params):
        from intercom import request
        req = request.Request('POST', path, self.http_session)
        return self._execute_request(req, params)

    def put(self, path, params):
        from intercom import request
        req = request.Request('PUT', path, self.http_session)
        return self._execute_request(req, params)

    def delete(self, path, params):
        from intercom import request
        req = request.Request('DELETE', path, self.http_session)
        return self._execute_request(req, params)
