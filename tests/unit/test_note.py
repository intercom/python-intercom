#
# Copyright 2013 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from datetime import datetime
from intercom import Note
from nose.tools import eq_


def test_properties():
    note = Note()
    note.body = 'xxx'
    note.email = 'xxx@example.com'
    note.user_id = '123'
    note.created_at = datetime.fromtimestamp(1331764344)

    eq_(note.body, 'xxx')
    eq_(note.email, 'xxx@example.com')
    eq_(note.user_id, '123')
