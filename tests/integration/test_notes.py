# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Intercom
from intercom import Note
from . import delete
from . import get_or_create_user
from . import get_timestamp

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class NoteTest(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        timestamp = get_timestamp()
        cls.user = get_or_create_user(timestamp)
        cls.email = cls.user.email

    @classmethod
    def teardown_class(cls):
        delete(cls.user)

    def test_create_note(self):
        # Create a note for a user
        note = Note.create(
            body="<p>Text for the note</p>",
            email=self.email)
        self.assertIsNotNone(note.id)

    def test_find_note(self):
        # Find a note by id
        orig_note = Note.create(
            body="<p>Text for the note</p>",
            email=self.email)
        note = Note.find(id=orig_note.id)
        self.assertEqual(note.body, orig_note.body)

    def test_find_all_email(self):
        # Iterate over all notes for a user via their email address
        notes = Note.find_all(email=self.email)
        for note in notes:
            self.assertTrue(note.id is not None)
            user = note.user.load()
            self.assertEqual(user.email, self.email)
            break

    def test_find_all_id(self):
        from intercom.user import User
        user = User.find(email=self.email)

        # Iterate over all notes for a user via their email address
        for note in Note.find_all(user_id=user.user_id):
            self.assertTrue(note.id is not None)
            user = note.user.load()
            self.assertEqual(user.email, self.email)
