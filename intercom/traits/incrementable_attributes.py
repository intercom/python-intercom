# -*- coding: utf-8 -*-


class IncrementableAttributes(object):

    def increment(self, key, value=1):
        existing_value = self.custom_attributes.get(key, 0)
        self.custom_attributes[key] = existing_value + value
