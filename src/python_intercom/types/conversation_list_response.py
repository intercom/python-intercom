# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .news.newsfeed import Newsfeed
from .news.news_item import NewsItem

__all__ = ["ConversationListResponse"]

ConversationListResponse = Union[NewsItem, Newsfeed]
