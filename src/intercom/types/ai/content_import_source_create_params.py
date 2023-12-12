# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentImportSourceCreateParams"]


class ContentImportSourceCreateParams(TypedDict, total=False):
    sync_behavior: Required[Literal["api"]]
    """
    If you intend to create or update External Pages via the API, this should be set
    to `api`.
    """

    url: Required[str]
    """The URL of the content import source."""

    status: Literal["active", "deactivated"]
    """The status of the content import source."""
