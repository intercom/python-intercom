#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom import User
from intercom import Intercom
from intercom import Impression
from intercom import MessageThread
#from intercom import Message

import os

from os import environ as ENV
from mock import Mock

DIRPATH = os.path.dirname(__file__)
FIXTURES = os.path.join(DIRPATH, 'fixtures')

def create_response(status, fixture=None):
    def request(*args, **kwargs):
        response = Mock()
        response.status_code = status
        if fixture:
            fixture_path = os.path.join(FIXTURES, fixture)
            response.content = open(fixture_path).read()
        return response
    return request

# Intercom.app_id = ENV['INTERCOM_APP_ID']
# Intercom.api_key = ENV['INTERCOM_API_KEY']

if __name__ == "__main__":
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    u = User.find_by_email('johnkeyes+2@gmail.com') #(email='newemail2@example.com', custom_data={'age': 42})
    print u.created_at
    u.custom_data['blah'] = 'john'
    u.custom_data['foo'] = 'tom'
    u.save()

    # print u.email, u.custom_data

    # users = User.all()
    # print len(users)
    # for u in users:
    #     print type(u)
    #     print "-"*90
    #     print u
    #     print "+"*90
    #     print u.email
    #     print u.created_at

    # from datetime import datetime
    # u.created_at = datetime.now()
    # print u.created_at
    # u.save()

    # u = User.get(email='john+7@samplc.com')
    # print u.created_at

#     # print User.get(email='newemail2@example.com')

#     msg = MessageThread.create(email='newemail2@example.com', body="Bobby Bobby")
#     impression = Impression.create(email='newemail2@example.com', user_ip='72.37.242.27',
#           user_agent='Boozilla/10.1')
#     print "+++++++>>>>", impression
#     print impression.location

#     impression = Impression()
#     impression.email = 'newemail2@example.com'
#     impression.user_ip = '209.191.122.70'
#     impression.save()

# #    msg = MessageThread.reply(email='newemail2@example.com', body="2 Some more...", thread_id='17847')



    # threads = MessageThread.find(email='newemail2@example.com') #, read=False, thread_id='17847')
    # print len(threads)
    # thread_1 = threads[0]
    # print thread_1.created_at
    # print thread_1.updated_at
    # print len(thread_1.messages)
    # print thread_1.messages[0].author.name


#     print ">>"*20
#     print msg.keys()
#     print msg.messages
#     # print type(msg.messages[0])
#     # print type(msg.messages[0]['from'])
#     print msg['updated_at']
#     print msg.updated_at
#     msg.thread_id = "123"
#     print msg['thread_id']
#     print ">>"*20
    
#     # message = Message({'from': { 'author': 'John'}})
#     # print message.author
    
# #    threads = MessageThread.find_all(email='newemail2@example.com')
#     # for th in threads:
#     #     print th
# #    print threads

# #    print MessageThread.find(email='newemail2@example.com', thread_id='17847')


#     #u.name = "Bobby Joe McGovern"
#     #u.last_seen_user_agent = "Mozilla"
# #    u.blooper = "Blooper"
#     #u.save()
#     #print ">>>", u.created_at
#     # import time


#     # inter = Intercom()

#     # email = 'john+1@example.com'

#     # # print "create"
#     # # inter.create_user(email=email, created_at=time.time())
#     # # print "\n\nupdate"
#     # #inter.update_user(email=email, custom_data={'age': '42'})
#     # # print "\n\nget"
#     # user = inter.get_user(email=email)
#     # # print "\n\ncreate impression"
#     # # inter.create_impression(email=email)
#     # print "\n\nget messages"
#     # inter.get_message_threads(email=email)
#     # # print "\n\ncreate message"
#     # # inter.create_message(email=email, body="Hi John, Python API calling.")

#     # #inter.get_users()