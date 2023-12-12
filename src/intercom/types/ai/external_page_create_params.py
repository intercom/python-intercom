# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalPageCreateParams"]


class ExternalPageCreateParams(TypedDict, total=False):
    html: Required[str]
    """The body of the external page in HTML."""

    locale: Required[Literal["en"]]
    """Always en"""

    source_id: Required[int]
    """
    The unique identifier for the source of the external page which was given by
    Intercom. Every external page must be associated with a Content Import Source
    which represents the place it comes from and from which it inherits a default
    audience (configured in the UI). For a new source, make a POST request to the
    Content Import Source endpoint and an ID for the source will be returned in the
    response.
    """

    title: Required[str]
    """The title of the external page."""

    url: Required[str]
    """The URL of the external page.

    This will be used by Fin to link end users to the page it based its answer on.
    """

    external_id: str
    """The identifier for the external page which was given by the source.

    Must be unique for the source.
    """

    fin_availability: bool
    """Whether the external page should be used to answer questions by Fin."""
