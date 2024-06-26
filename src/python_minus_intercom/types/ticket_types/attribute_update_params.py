# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AttributeUpdateParams"]


class AttributeUpdateParams(TypedDict, total=False):
    ticket_type_id: Required[str]

    allow_multiple_values: bool
    """
    Whether the attribute allows multiple files to be attached to it (only
    applicable to file attributes)
    """

    archived: bool
    """
    Whether the attribute should be archived and not shown during creation of the
    ticket (it will still be present on previously created tickets)
    """

    description: str
    """The description of the attribute presented to the teammate or contact"""

    list_items: str
    """
    A comma delimited list of items for the attribute value (only applicable to list
    attributes)
    """

    multiline: bool
    """
    Whether the attribute allows multiple lines of text (only applicable to string
    attributes)
    """

    name: str
    """The name of the ticket type attribute"""

    required_to_create: bool
    """
    Whether the attribute is required to be filled in when teammates are creating
    the ticket in Inbox.
    """

    required_to_create_for_contacts: bool
    """
    Whether the attribute is required to be filled in when contacts are creating the
    ticket in Messenger.
    """

    visible_on_create: bool
    """Whether the attribute is visible to teammates when creating a ticket in Inbox."""

    visible_to_contacts: bool
    """
    Whether the attribute is visible to contacts when creating a ticket in
    Messenger.
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
