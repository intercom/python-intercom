#
# Copyright 2013 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from mock import patch
from nose.tools import raises
from unittest import TestCase

from . import create_response

from intercom.intercom import AuthenticationError
from intercom import Note

class NoteTest(TestCase):

    @raises(AuthenticationError)
    @patch('requests.request', create_response(401))
    def test_create_note_identifiers(self):
        Note.create()

    @patch('requests.request', create_response(200, 'create_note_valid.json'))
    def test_create_note_valid(self):
        note = Note.create(email='xxx@example.com')
        self.assertEqual("<p>This is the text of my note.</p>", note.html)

        # check params
        note = Note.create(email='xxx@example.com', body="home")
        self.assertEqual("<p>This is the text of my note.</p>", note.html)

    def test_properties(self):
        note = Note()
        note.body = 'xxx'
        note.email = 'xxx@example.com'
        note.user_id = '123'

        self.assertEqual('xxx', note.body)
        self.assertEqual('xxx@example.com', note.email)
        self.assertEqual('123', note.user_id)

    @patch('requests.request', create_response(200, 'create_note_valid.json'))
    def test_save(self):
        note = Note(email='xxx@example.com')
        note.save()
        self.assertEqual(None, note.created_at)
        self.assertEqual('123', note.user.user_id)
        self.assertEqual("<p>This is the text of my note.</p>", note.html)
