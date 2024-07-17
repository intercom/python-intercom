# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeletedCompanyObject"]


class DeletedCompanyObject(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the company which is given by Intercom."""

    deleted: Optional[bool] = None
    """Whether the company was deleted successfully or not."""

    object: Optional[Literal["company"]] = None
    """The type of object which was deleted. - `company`"""
