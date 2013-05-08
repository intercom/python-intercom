# coding=utf-8
#
# Copyright 2013 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" Tag module.

>>> from intercom import Intercom
>>> Intercom.app_id = 'dummy-app-id'
>>> Intercom.api_key = 'dummy-api-key'
>>> from intercom.tag import Tag

"""

from . import Intercom


class Tag(dict):
    """ Represents a tag. """

    @classmethod
    def find(cls, **params):
        """ Find a tag using params.

        >>> tag = Tag.find(name="Free Trial")
        >>> tag.id
        >>> tag.name
        u'Free Trial'
        >>> tag.tagged_user_count
        >>> tag.color
        u'green'

        """
        resp = Intercom.get_tag(**params)
        return cls(resp)

    @classmethod
    def find_by_name(cls, name):
        """ Find a tag by name.

        >>> tag = Tag.find_by_name("Free Trial")
        >>> tag.id
        >>> tag.name
        u'Free Trial'
        >>> tag.tagged_user_count
        >>> tag.color
        u'green'

        """
        return Tag.find(name=name)

    @classmethod
    def create(
            cls, name, tag_or_untag, user_ids=None, emails=None,
            color=None):
        """ Create a new tag an optionally tag user.

        >>> tag = Tag.create(user_ids=["abc123", "def456"],
        ...        name="Free Trial", tag_or_untag="tag")
        >>> tag.id
        >>> tag.name
        u'Free Trial'
        >>> tag.tagged_user_count
        >>> tag.color
        u'green'

        """
        resp = Intercom.create_tag(
            name, tag_or_untag, user_ids=user_ids, emails=emails,
            color=color)
        return cls(resp)

    def save(self):
        """ Update a tag:

        >>> tag = Tag()
        >>> tag.user_ids = ["abc123", "def456"]
        >>> tag.name = "Free Trial"
        >>> tag.tag_or_untag = "tag"
        >>> tag.save()
        >>> tag.tagged_user_count
        >>> tag.color
        u'green'

        """
        resp = Intercom.update_tag(
            self.name, self.get('tag_or_untag', None),
            user_ids=self.get('user_ids', None),
            emails=self.get('emails', None),
            color=self.color)
        self.update(resp)

    @property
    def name(self):
        """ Get the name of the tag. """
        return dict.get(self, 'name', None)

    @name.setter
    def name(self, name):
        """ Get the name of the tag. """
        self['name'] = name

    @property
    def color(self):
        """ Get the color of the tag. """
        return dict.get(self, 'color', None)

    @color.setter
    def color(self, color):
        """ Get the color of the tag. """
        self['color'] = color

    @property
    def id(self):
        """ The id of the tag. """
        return dict.get(self, 'id', None)

    @property
    def segment(self):
        """ Get the segment of the tag. """
        return dict.get(self, 'segment', None)

    @property
    def tagged_user_count(self):
        """ Get the tagged_user_count of the tag. """
        return dict.get(self, 'tagged_user_count', None)

    @property
    def tag_or_untag(self):
        """ The tag_or_untag of the tag. """
        raise AttributeError("tag_or_untag is a write-only property")

    @tag_or_untag.setter
    def tag_or_untag(self, tag_or_untag):
        """ The tag_or_untag of the tag. """
        self['tag_or_untag'] = tag_or_untag

    @property
    def user_ids(self):
        """ The user_ids of the tag. """
        raise AttributeError("user_ids is a write-only property")

    @user_ids.setter
    def user_ids(self, user_ids):
        """ The user_ids of the tag. """
        self['user_ids'] = user_ids

    @property
    def emails(self):
        """ The emails of the tag. """
        raise AttributeError("emails is a write-only property")

    @emails.setter
    def emails(self, emails):
        """ The emails of the tag. """
        self['emails'] = emails
