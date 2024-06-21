# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PartAttachment"]


class PartAttachment(BaseModel):
    content_type: Optional[str] = None
    """The content type of the attachment"""

    filesize: Optional[int] = None
    """The size of the attachment"""

    height: Optional[int] = None
    """The height of the attachment"""

    name: Optional[str] = None
    """The name of the attachment"""

    type: Optional[str] = None
    """The type of attachment"""

    url: Optional[str] = None
    """The URL of the attachment"""

    width: Optional[int] = None
    """The width of the attachment"""
