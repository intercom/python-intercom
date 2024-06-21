# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversationConvertParams"]


class ConversationConvertParams(TypedDict, total=False):
    ticket_type_id: Required[str]
    """The ID of the type of ticket you want to convert the conversation to"""

    attributes: Dict[str, Union[Optional[str], float, bool, Iterable[object]]]
    """The attributes set on the ticket.

    When setting the default title and description attributes, the attribute keys
    that should be used are `_default_title_` and `_default_description_`. When
    setting ticket type attributes of the list attribute type, the key should be the
    attribute name and the value of the attribute should be the list item id,
    obtainable by [listing the ticket type](ref:get_ticket-types). For example, if
    the ticket type has an attribute called `priority` of type `list`, the key
    should be `priority` and the value of the attribute should be the guid of the
    list item (e.g. `de1825a0-0164-4070-8ca6-13e22462fa7e`).
    """

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
