#
# Copyright 2013 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from datetime import datetime
from intercom import Note
from sure import expect


def test_properties():
    note = Note()
    note.body = 'xxx'
    note.email = 'xxx@example.com'
    note.user_id = '123'
    note.created_at = datetime.fromtimestamp(1331764344)

    expect(note.body).to.equal('xxx')
    expect(note.email).to.equal('xxx@example.com')
    expect(note.user_id).to.equal('123')
