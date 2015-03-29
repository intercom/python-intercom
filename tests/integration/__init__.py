# -*- coding: utf-8 -*-

import time

from datetime import datetime
from intercom import Company
from intercom import ResourceNotFound
from intercom import User


def get_timestamp():
    now = datetime.utcnow()
    return int(time.mktime(now.timetuple()))


def get_or_create_user(timestamp):
    # get user
    email = '%s@example.com' % (timestamp)
    try:
        user = User.find(email=email)
    except ResourceNotFound:
        # Create a user
        user = User.create(
            email=email,
            user_id=timestamp,
            name="Ada %s" % (timestamp))
        time.sleep(5)
    return user


def get_or_create_company(timestamp):
    name = 'Company %s' % (timestamp)

    # get company
    try:
        company = Company.find(name=name)
    except ResourceNotFound:
        # Create a company
        company = Company.create(
            company_id=timestamp, name=name)
    return company


def delete(resource):
    try:
        resource.delete()
    except ResourceNotFound:
        # not much we can do here
        pass
