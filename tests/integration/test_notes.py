# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client
from . import delete_user
from . import get_or_create_user
from . import get_timestamp

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class NoteTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        timestamp = get_timestamp()
        cls.user = get_or_create_user(intercom, timestamp)
        cls.email = cls.user.email

    @classmethod
    def teardown_class(cls):
        delete_user(intercom, cls.user)

    def test_create_note(self):
        # Create a note for a user
        note = intercom.notes.create(
            body="<p>Text for the note</p>",
            email=self.email)
        self.assertIsNotNone(note.id)

    def test_find_note(self):
        # Find a note by id
        orig_note = intercom.notes.create(
            body="<p>Text for the note</p>",
            email=self.email)
        note = intercom.notes.find(id=orig_note.id)
        self.assertEqual(note.body, orig_note.body)

    def test_find_all_email(self):
        # Iterate over all notes for a user via their email address
        notes = intercom.notes.find_all(email=self.email)
        for note in notes:
            self.assertTrue(note.id is not None)
            user = intercom.users.load(note.user)
            self.assertEqual(user.email, self.email)
            break

    def test_find_all_id(self):
        user = intercom.users.find(email=self.email)

        # Iterate over all notes for a user via their email address
        for note in intercom.notes.find_all(user_id=user.user_id):
            self.assertTrue(note.id is not None)
            user = intercom.users.load(note.user)
            self.assertEqual(user.email, self.email)
