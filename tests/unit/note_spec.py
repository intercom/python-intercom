import httpretty
import json
import re
from describe import expect
from intercom import Note

post = httpretty.POST
r = re.compile


class DescribeIntercomNote:

    @httpretty.activate
    def it_creates_a_note(self):
        data = {
            'body': '<p>Note to leave on user</p>',
            'created_at': 1234567890
        }
        httpretty.register_uri(
            post, r(r'/notes/$'), body=json.dumps(data))
        note = Note.create(body="Note to leave on user")
        expect(note.body) == "<p>Note to leave on user</p>"

    @httpretty.activate
    def it_sets_gets_allowed_keys(self):
        params = {
            'body': 'Note body',
            'email': 'me@example.com',
            'user_id': 'abc123'
        }
        params_keys = params.keys()
        params_keys.sort()

        note = Note(**params)
        note_dict = note.to_dict
        note_keys = note_dict.keys()
        note_keys.sort()

        expect(params_keys) == note_keys
        for key in params_keys:
            expect(getattr(note, key)) == params[key]
