# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExternalPage"]


class ExternalPage(BaseModel):
    id: str
    """The unique identifier for the external page which is given by Intercom."""

    created_at: int
    """The time when the external page was created."""

    fin_availability: bool
    """Whether the external page should be used to answer questions by Fin."""

    html: str
    """The body of the external page in HTML."""

    last_ingested_at: int
    """The time when the external page was last ingested."""

    locale: Literal["en"]
    """Always en"""

    source_id: int
    """
    The unique identifier for the source of the external page which was given by
    Intercom. Every external page must be associated with a Content Import Source
    which represents the place it comes from and from which it inherits a default
    audience (configured in the UI). For a new source, make a POST request to the
    Content Import Source endpoint and an ID for the source will be returned in the
    response.
    """

    title: str
    """The title of the external page."""

    type: Literal["external_page"]
    """Always external_page"""

    updated_at: int
    """The time when the external page was last updated."""

    url: str
    """The URL of the external page.

    This will be used by Fin to link end users to the page it based its answer on.
    """

    external_id: Optional[str] = None
    """The identifier for the external page which was given by the source.

    Must be unique for the source.
    """
