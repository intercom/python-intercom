# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentImportSourceUpdateParams"]


class ContentImportSourceUpdateParams(TypedDict, total=False):
    sync_behavior: Required[Literal["api", "automated", "manual"]]
    """
    If you intend to create or update External Pages via the API, this should be set
    to `api`. You can not change the value to or from api.
    """

    url: Required[str]
    """The URL of the content import source.

    This may only be different from the existing value if the sync behavior is API.
    """

    status: Literal["active", "deactivated"]
    """The status of the content import source."""
