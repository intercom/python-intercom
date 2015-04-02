# -*- coding: utf-8 -*-

import unittest

from intercom import Intercom
from intercom import Note
from mock import patch
from nose.tools import eq_
from nose.tools import istest


class NoteTest(unittest.TestCase):

    @istest
    def it_creates_a_note(self):
        data = {
            'body': '<p>Note to leave on user</p>',
            'created_at': 1234567890
        }
        with patch.object(Intercom, 'post', return_value=data) as mock_method:
            note = Note.create(body="Note to leave on user")
            mock_method.assert_called_once_with('/notes/', body="Note to leave on user")  # noqa
            eq_(note.body, "<p>Note to leave on user</p>")

    @istest
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
