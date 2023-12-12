# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ArticleSearchParams"]


class ArticleSearchParams(TypedDict, total=False):
    help_center_id: int
    """The ID of the Help Center to search in."""

    highlight: bool
    """Return a highlighted version of the matching content within your articles.

    Refer to the response schema for more details.
    """

    phrase: str
    """The phrase within your articles to search for."""

    state: str
    """The state of the Articles returned. One of `published`, `draft` or `all`."""
