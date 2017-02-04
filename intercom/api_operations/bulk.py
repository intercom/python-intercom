# -*- coding: utf-8 -*-
"""Support for the Intercom Bulk API.

Ref: https://developers.intercom.io/reference#bulk-apis
"""

from intercom import utils


def item_for_api(method, data_type, item):
    """Return a Bulk API item."""
    return {
        'method': method,
        'data_type': data_type,
        'data': item
    }


class Submit(object):
    """Provide Bulk API support to subclasses."""

    def submit_bulk_job(self, create_items=[], delete_items=[], job_id=None):
        """Submit a Bulk API job."""
        from intercom import event
        from intercom.errors import HttpError
        from intercom.job import Job

        if self.collection_class == event.Event and delete_items:
            raise Exception("Events do not support bulk delete operations.")
        data_type = utils.resource_class_to_name(self.collection_class)
        collection_name = utils.resource_class_to_collection_name(self.collection_class)
        create_items = [item_for_api('post', data_type, item) for item in create_items]
        delete_items = [item_for_api('delete', data_type, item) for item in delete_items]

        bulk_request = {
            'items': create_items + delete_items
        }
        if job_id:
            bulk_request['job'] = {'id': job_id}

        response = self.client.post('/bulk/%s' % (collection_name), bulk_request)
        if not response:
            raise HttpError('HTTP Error - No response entity returned.')
        return Job().from_response(response)


class LoadErrorFeed(object):
    """Provide access to Bulk API error feed for a specific job."""

    def errors(self, id):
        """Return errors for the Bulk API job specified."""
        from intercom.errors import HttpError
        from intercom.job import Job
        response = self.client.get("/jobs/%s/error" % (id), {})
        if not response:
            raise HttpError('Http Error - No response entity returned.')
        return Job.from_api(response)
