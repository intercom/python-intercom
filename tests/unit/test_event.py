# -*- coding: utf-8 -*-

import time
import unittest

from datetime import datetime
from intercom.client import Client
from intercom.user import User
from mock import patch
from nose.tools import istest


class EventTest(unittest.TestCase):

    def setUp(self):  # noqa
        self.client = Client()
        now = time.mktime(datetime.utcnow().timetuple())
        self.user = User(
            email="jim@example.com",
            user_id="12345",
            created_at=now,
            name="Jim Bob")
        self.created_time = now - 300

    @istest
    def it_creates_an_event_with_metadata(self):
        data = {
            'event_name': 'Eventful 1',
            'created_at': self.created_time,
            'email': 'joe@example.com',
            'metadata': {
                'invitee_email': 'pi@example.com',
                'invite_code': 'ADDAFRIEND',
                'found_date': 12909364407
            }
        }

        with patch.object(Client, 'post', return_value=data) as mock_method:
            self.client.events.create(**data)
            mock_method.assert_called_once_with('/events/', data)

    @istest
    def it_creates_an_event_without_metadata(self):
        data = {
            'event_name': 'sale of item',
            'email': 'joe@example.com',
        }
        with patch.object(Client, 'post', return_value=data) as mock_method:
            self.client.events.create(**data)
            mock_method.assert_called_once_with('/events/', data)

class DescribeBulkOperations(unittest.TestCase):  # noqa
    def setUp(self):  # noqa
        self.client = Client()

        self.job = {
            "app_id": "app_id",
            "id": "super_awesome_job",
            "created_at": 1446033421,
            "completed_at": 1446048736,
            "closing_at": 1446034321,
            "updated_at": 1446048736,
            "name": "api_bulk_job",
            "state": "completed",
            "links": {
                "error": "https://api.intercom.io/jobs/super_awesome_job/error",
                "self": "https://api.intercom.io/jobs/super_awesome_job"
            },
            "tasks": [
                {
                    "id": "super_awesome_task",
                    "item_count": 2,
                    "created_at": 1446033421,
                    "started_at": 1446033709,
                    "completed_at": 1446033709,
                    "state": "completed"
                }
            ]
        }

        self.bulk_request = {
            "items": [
                {
                    "method": "post",
                    "data_type": "event",
                    "data": {
                        "event_name": "ordered-item",
                        "created_at": 1438944980,
                        "user_id": "314159",
                        "metadata": {
                            "order_date": 1438944980,
                            "stripe_invoice": "inv_3434343434"
                        }
                    }
                },
                {
                    "method": "post",
                    "data_type": "event",
                    "data": {
                        "event_name": "invited-friend",
                        "created_at": 1438944979,
                        "user_id": "314159",
                        "metadata": {
                            "invitee_email": "pi@example.org",
                            "invite_code": "ADDAFRIEND"
                        }
                    }
                }
            ]
        }

        self.events = [
            {
                "event_name": "ordered-item",
                "created_at": 1438944980,
                "user_id": "314159",
                "metadata": {
                    "order_date": 1438944980,
                    "stripe_invoice": "inv_3434343434"
                }
            },
            {
                "event_name": "invited-friend",
                "created_at": 1438944979,
                "user_id": "314159",
                "metadata": {
                    "invitee_email": "pi@example.org",
                    "invite_code": "ADDAFRIEND"
                }
            }
        ]

    @istest
    def it_submits_a_bulk_job(self):  # noqa
        with patch.object(Client, 'post', return_value=self.job) as mock_method:  # noqa
            self.client.events.submit_bulk_job(create_items=self.events)
            mock_method.assert_called_once_with('/bulk/events', self.bulk_request)

    @istest
    def it_adds_events_to_an_existing_bulk_job(self):  # noqa
        self.bulk_request['job'] = {'id': 'super_awesome_job'}
        with patch.object(Client, 'post', return_value=self.job) as mock_method:  # noqa
            self.client.events.submit_bulk_job(
                create_items=self.events, job_id='super_awesome_job')
            mock_method.assert_called_once_with('/bulk/events', self.bulk_request)

    @istest
    def it_does_not_submit_delete_jobs(self):  # noqa
        with self.assertRaises(Exception):
            self.client.events.submit_bulk_job(delete_items=self.events)
