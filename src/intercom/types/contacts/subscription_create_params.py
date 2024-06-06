# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the subscription which is given by Intercom"""

    consent_type: Required[str]
    """The consent_type of a subscription, opt_out or opt_in."""
