# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CompanyCreateParams"]


class CompanyCreateParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """The unique identifier for the company which is given by Intercom"""
