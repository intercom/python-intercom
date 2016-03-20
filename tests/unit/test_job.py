# -*- coding: utf-8 -*-  # noqa

import unittest

from intercom.client import Client
from mock import patch
from nose.tools import istest


class DescribeJobs(unittest.TestCase):  # noqa
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

        self.error_feed = {
            "app_id": "app_id",
            "job_id": "super_awesome_job",
            "pages": {},
            "items": []
        }

    @istest
    def it_gets_a_job(self):  # noqa
        with patch.object(Client, 'get', return_value=self.job) as mock_method:  # noqa
            self.client.jobs.find(id='super_awesome_job')
            mock_method.assert_called_once_with('/jobs/super_awesome_job', {})

    @istest
    def it_gets_a_jobs_error_feed(self):  # noqa
        with patch.object(Client, 'get', return_value=self.error_feed) as mock_method:  # noqa
            self.client.jobs.errors(id='super_awesome_job')
            mock_method.assert_called_once_with('/jobs/super_awesome_job/error', {})
