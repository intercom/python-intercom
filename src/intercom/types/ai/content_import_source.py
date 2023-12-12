# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ContentImportSource"]


class ContentImportSource(BaseModel):
    id: int
    """The unique identifier for the content import source which is given by Intercom."""

    created_at: int
    """The time when the content import source was created."""

    last_synced_at: int
    """The time when the content import source was last synced."""

    status: Literal["active", "deactivated"]
    """The status of the content import source."""

    sync_behavior: Literal["api", "automatic", "manual"]
    """
    If you intend to create or update External Pages via the API, this should be set
    to `api`.
    """

    type: Literal["content_import_source"]
    """Always external_page"""

    updated_at: int
    """The time when the content import source was last updated."""

    url: str
    """The URL of the root of the external source."""
