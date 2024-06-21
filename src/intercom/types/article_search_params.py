# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

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

    intercom_version: Annotated[
        Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ],
        PropertyInfo(alias="Intercom-Version"),
    ]
    """
    Intercom API version.By default, it's equal to the version set in the app
    package.
    """
