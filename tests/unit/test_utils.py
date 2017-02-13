# -*- coding: utf-8 -*-
"""Unit test module for utils.py."""
import unittest

from intercom.utils import define_lightweight_class
from nose.tools import eq_
from nose.tools import istest


class UserTest(unittest.TestCase):  # noqa

    @istest
    def it_has_a_resource_type(self):  # noqa
        Avatar = define_lightweight_class('avatar', 'Avatar')  # noqa
        eq_('avatar', Avatar.resource_type)
        avatar = Avatar()
        eq_('avatar', avatar.resource_type)
