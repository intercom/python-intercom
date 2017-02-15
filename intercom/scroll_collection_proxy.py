# -*- coding: utf-8 -*-
"""Proxy for the Scroll API."""
import six
from intercom import HttpError


class ScrollCollectionProxy(six.Iterator):
    """A proxy to iterate over resources returned by the Scroll API."""

    def __init__(self, client, resource_class, resource_name, scroll_url):
        """Initialise the proxy."""
        self.client = client

        # resource name
        self.resource_name = resource_name

        # resource class
        self.resource_class = resource_class

        # the original URL to retrieve the resources
        self.scroll_url = scroll_url

        # the identity of the scroll, extracted from the response
        self.scroll_param = None

        # an iterator over the resources found in the response
        self.resources = None

        # a link to the next page of results
        self.next_page = None

    def __iter__(self):
        """Return self as the proxy has __next__ implemented."""
        return self

    def __next__(self):
        """Return the next resource from the response."""
        if self.resources is None:
            # get the first page of results
            self.get_first_page()

        # try to get a resource if there are no more in the
        # current resource iterator (StopIteration is raised)
        # try to get the next page of results first
        try:
            resource = six.next(self.resources)
        except StopIteration:
            self.get_next_page()
            resource = six.next(self.resources)

        instance = self.resource_class(**resource)
        return instance

    def __getitem__(self, index):
        """Return an exact item from the proxy."""
        for i in range(index):
            six.next(self)
        return six.next(self)

    def get_first_page(self):
        """Return the first page of results."""
        return self.get_page(self.scroll_param)

    def get_next_page(self):
        """Return the next page of results."""
        return self.get_page(self.scroll_param)

    def get_page(self, scroll_param=None):
        """Retrieve a page of results from the Scroll API."""
        if scroll_param is None:
            response = self.client.get(self.scroll_url, {})
        else:
            response = self.client.get(self.scroll_url, {'scroll_param': scroll_param})

        if response is None:
            raise HttpError('Http Error - No response entity returned')

        # create the resource iterator
        collection = response[self.resource_name]
        self.resources = iter(collection)
        # grab the next page URL if one exists
        self.scroll_param = self.extract_scroll_param(response)

    def records_present(self, response):
        """Return whether there are resources in the response."""
        return len(response.get(self.resource_name)) > 0

    def extract_scroll_param(self, response):
        """Extract the scroll_param from the response."""
        if self.records_present(response):
            return response.get('scroll_param')
