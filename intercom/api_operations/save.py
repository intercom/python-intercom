# -*- coding: utf-8 -*-
"""Operation to create or save an instance of a particular resource."""

from intercom import utils


class Save(object):
    """A mixin that provides `create` and `save` functionality."""

    def create(self, **params):
        """Create an instance of the resource from the supplied parameters."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        response = self.client.post("/%s/" % (collection), params)
        if response:  # may be empty if we received a 202
            return self.collection_class(**response)

    def save(self, obj):
        """Save the instance of the resource."""
        collection = utils.resource_class_to_collection_name(
            obj.__class__)
        params = obj.attributes
        if self.id_present(obj) and not self.posted_updates(obj):
            # update
            response = self.client.put('/%s/%s' % (collection, obj.id), params)
        else:
            # create
            params.update(self.identity_hash(obj))
            response = self.client.post('/%s' % (collection), params)
        if response:
            return obj.from_response(response)

    def id_present(self, obj):
        """Return whether the obj has an `id` attribute with a value."""
        return getattr(obj, 'id', None) and obj.id != ""

    def posted_updates(self, obj):
        """Return whether the updates to this object have been posted to Intercom."""
        return getattr(obj, 'update_verb', None) == 'post'

    def identity_hash(self, obj):
        """Return the identity_hash for this object."""
        identity_vars = getattr(obj, 'identity_vars', [])
        parts = {}
        for var in identity_vars:
            id_var = getattr(obj, var, None)
            if id_var:  # only present id var if it is not blank or None
                parts[var] = id_var
        return parts
