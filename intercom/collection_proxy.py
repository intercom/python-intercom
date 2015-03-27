# -*- coding: utf-8 -*-

import six
from intercom import HttpError


class CollectionProxy(six.Iterator):

    def __init__(self, cls, collection, finder_url, finder_params={}):
        # needed to create class instances of the resource
        self.collection_cls = cls

        # needed to reference the collection in the response
        self.collection = collection

        # the original URL to retrieve the resources
        self.finder_url = finder_url

        # the params to filter the resources
        self.finder_params = finder_params

        # an iterator over the resources found in the response
        self.resources = None

        # a link to the next page of results
        self.next_page = None

    def __iter__(self):
        return self

    def __next__(self):
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

        instance = self.collection_cls(**resource)
        return instance

    def __getitem__(self, index):
        for i in range(index):
            six.next(self)
        return six.next(self)

    def get_first_page(self):
        # get the first page of results
        return self.get_page(self.finder_url, self.finder_params)

    def get_next_page(self):
        # get the next page of results
        return self.get_page(self.next_page)

    def get_page(self, url, params={}):
        # get a page of results
        from intercom import Intercom

        # if there is no url stop iterating
        if url is None:
            raise StopIteration

        response = Intercom.get(url, **params)
        if response is None:
            raise HttpError('Http Error - No response entity returned')

        collection = response[self.collection]
        # if there are no resources in the response stop iterating
        if collection is None:
            raise StopIteration

        # create the resource iterator
        self.resources = iter(collection)
        # grab the next page URL if one exists
        self.next_page = self.extract_next_link(response)

    def paging_info_present(self, response):
        return 'pages' in response and 'type' in response['pages']

    def extract_next_link(self, response):
        if self.paging_info_present(response):
            paging_info = response["pages"]
            return paging_info["next"]
