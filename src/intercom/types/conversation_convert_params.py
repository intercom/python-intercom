# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConversationConvertParams"]


class ConversationConvertParams(TypedDict, total=False):
    ticket_type_id: Required[str]
    """The ID of the type of ticket you want to convert the conversation to"""

    attributes: Dict[str, Union[Optional[str], float, bool, List[object]]]
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
