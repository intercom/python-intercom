# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataAttribute"]


class DataAttribute(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the data attribute which is given by Intercom.

    Only available for custom attributes.
    """

    admin_id: Optional[str] = None
    """Teammate who created the attribute. Only applicable to CDAs"""

    api_writable: Optional[bool] = None
    """Can this attribute be updated through API"""

    archived: Optional[bool] = None
    """Is this attribute archived. (Only applicable to CDAs)"""

    created_at: Optional[int] = None
    """The time the attribute was created as a UTC Unix timestamp"""

    custom: Optional[bool] = None
    """Set to true if this is a CDA"""

    data_type: Optional[Literal["string", "integer", "float", "boolean", "date"]] = None
    """The data type of the attribute."""

    description: Optional[str] = None
    """Readable description of the attribute."""

    full_name: Optional[str] = None
    """Full name of the attribute.

    Should match the name unless it's a nested attribute. We can split full_name on
    `.` to access nested user object values.
    """

    label: Optional[str] = None
    """Readable name of the attribute (i.e. name you see in the UI)"""

    model: Optional[Literal["contact", "company", "conversation"]] = None
    """
    Value is `contact` for user/lead attributes, `company` for company attributes
    and `conversation` for conversation attributes..
    """

    name: Optional[str] = None
    """Name of the attribute."""

    options: Optional[List[str]] = None
    """List of predefined options for attribute value."""

    type: Optional[Literal["data_attribute"]] = None
    """Value is `data_attribute`."""

    ui_writable: Optional[bool] = None
    """Can this attribute be updated in the UI"""

    updated_at: Optional[int] = None
    """The time the attribute was last updated as a UTC Unix timestamp"""
