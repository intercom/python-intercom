# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..types import shared_params
from .._utils import PropertyInfo

__all__ = ["TicketSearchParams", "Query"]


class TicketSearchParams(TypedDict, total=False):
    query: Required[Query]
    """Search using Intercoms Search APIs with a single filter."""

    pagination: Optional[shared_params.StartingAfterPaging]

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


Query = Union[shared_params.SingleFilterSearchRequest, shared_params.MultipleFilterSearchRequest]
