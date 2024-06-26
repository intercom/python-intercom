# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .data_attribute import DataAttribute

__all__ = ["DataAttributeList"]


class DataAttributeList(BaseModel):
    data: Optional[List[DataAttribute]] = None
    """A list of data attributes"""

    type: Optional[Literal["list"]] = None
    """The type of the object"""
