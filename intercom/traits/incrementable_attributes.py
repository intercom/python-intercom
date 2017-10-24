# -*- coding: utf-8 -*-


class IncrementableAttributes(object):

    def increment(self, key, value=1):
        existing_value = self.custom_attributes.get(key, 0)
        if existing_value is None:
            existing_value = 0
        self.custom_attributes[key] = existing_value + value
