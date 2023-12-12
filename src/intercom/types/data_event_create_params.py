# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["DataEventCreateParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    body: Required[object]


class Variant1(TypedDict, total=False):
    body: Required[object]


class Variant2(TypedDict, total=False):
    body: Required[object]


DataEventCreateParams = Union[Variant0, Variant1, Variant2]
