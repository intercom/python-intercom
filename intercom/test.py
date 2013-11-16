from intercom import Intercom
Intercom.app_id = 'uqg4fg4p'
Intercom.api_key = 'd314ecea83ae73e9e7a5605f3321dd7156bc08bd'

from intercom import User
for user in User.all():
    print user.email
