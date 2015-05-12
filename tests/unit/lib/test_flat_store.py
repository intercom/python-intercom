# -*- coding: utf-8 -*-

import unittest
from intercom.lib.flat_store import FlatStore
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import istest


class IntercomFlatStore(unittest.TestCase):

    @istest
    def it_raises_if_you_try_to_set_or_merge_in_nested_hash_structures(self):
        data = FlatStore()
        with assert_raises(ValueError):
            data["thing"] = [1]
        with assert_raises(ValueError):
            data["thing"] = {1: 2}
        with assert_raises(ValueError):
            FlatStore(**{"1": {2: 3}})

    @istest
    def it_raises_if_you_try_to_use_a_non_string_key(self):
        data = FlatStore()
        with assert_raises(ValueError):
            data[1] = "something"

    @istest
    def it_sets_and_merges_valid_entries(self):
        data = FlatStore()
        data["a"] = 1
        data["b"] = 2
        eq_(data["a"], 1)
        eq_(data["b"], 2)
        data = FlatStore(a=1, b=2)
        eq_(data["a"], 1)
        eq_(data["b"], 2)

    @istest
    def it_sets_null_entries(self):
        data = FlatStore()
        data["a"] = None
        eq_(data["a"], None)
