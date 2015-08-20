# -*- coding: utf-8 -*-

import time

from datetime import datetime
# from intercom import Company
from intercom import ResourceNotFound
# from intercom import User


def get_timestamp():
    now = datetime.utcnow()
    return int(time.mktime(now.timetuple()))


def get_or_create_user(client, timestamp):
    # get user
    email = '%s@example.com' % (timestamp)
    try:
        user = client.users.find(email=email)
    except ResourceNotFound:
        # Create a user
        user = client.users.create(
            email=email,
            user_id=timestamp,
            name="Ada %s" % (timestamp))
        time.sleep(5)
    return user


def get_or_create_company(client, timestamp):
    name = 'Company %s' % (timestamp)

    # get company
    try:
        company = client.companies.find(name=name)
    except ResourceNotFound:
        # Create a company
        company = client.companies.create(
            company_id=timestamp, name=name)
    return company


def delete_user(client, resource):
    try:
        client.users.delete(resource)
    except ResourceNotFound:
        # not much we can do here
        pass


def delete_company(client, resource):
    try:
        client.companies.delete(resource)
    except ResourceNotFound:
        # not much we can do here
        pass
