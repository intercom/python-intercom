# -*- coding: utf-8 -*-

from intercom.traits.api_resource import Resource


class Notification(Resource):

    @property
    def model(self):
        return self.data.item

    @property
    def model_type(self):
        return self.model.__class__

    @property
    def load(self):
        return self.model.load
