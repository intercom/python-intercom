# -*- coding: utf-8 -*-

import httpretty
import json
import re
import unittest

from intercom import Note
from nose.tools import eq_
from nose.tools import istest

post = httpretty.POST
r = re.compile


class NoteTest(unittest.TestCase):

    @istest
    @httpretty.activate
    def it_creates_a_note(self):
        data = {
            'body': '<p>Note to leave on user</p>',
            'created_at': 1234567890
        }
        httpretty.register_uri(
            post, r(r'/notes/$'), body=json.dumps(data))
        note = Note.create(body="Note to leave on user")
        eq_(note.body, "<p>Note to leave on user</p>")

    @istest
    @httpretty.activate
    def it_sets_gets_allowed_keys(self):
        params = {
            'body': 'Note body',
            'email': 'me@example.com',
            'user_id': 'abc123'
        }
        params_keys = list(params.keys())
        params_keys.sort()

        note = Note(**params)
        note_dict = note.to_dict
        note_keys = list(note_dict.keys())
        note_keys.sort()

        eq_(params_keys, note_keys)
        for key in params_keys:
            eq_(getattr(note, key), params[key])
