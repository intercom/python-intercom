# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TicketReplyParams",
    "ContactReplyTicketIntercomUserIDRequest",
    "ContactReplyTicketUserIDRequest",
    "ContactReplyTicketEmailRequest",
    "AdminReplyTicketRequest",
    "AdminReplyTicketRequestReplyOption",
]


class ContactReplyTicketIntercomUserIDRequest(TypedDict, total=False):
    body: Required[str]
    """The text body of the comment."""

    message_type: Required[Literal["comment"]]

    type: Required[Literal["user"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 10 URLs.
    """

    created_at: int
    """The time the reply was created. If not provided, the current time will be used."""

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


class ContactReplyTicketUserIDRequest(TypedDict, total=False):
    body: Required[str]
    """The text body of the comment."""

    message_type: Required[Literal["comment"]]

    type: Required[Literal["user"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 10 URLs.
    """

    created_at: int
    """The time the reply was created. If not provided, the current time will be used."""

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


class ContactReplyTicketEmailRequest(TypedDict, total=False):
    body: Required[str]
    """The text body of the comment."""

    message_type: Required[Literal["comment"]]

    type: Required[Literal["user"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 10 URLs.
    """

    created_at: int
    """The time the reply was created. If not provided, the current time will be used."""

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


class AdminReplyTicketRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is authoring the comment."""

    message_type: Required[Literal["comment", "note", "quick_reply"]]

    type: Required[Literal["admin"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 10 URLs.
    """

    body: str
    """The text body of the reply.

    Notes accept some HTML formatting. Must be present for comment and note message
    types.
    """

    created_at: int
    """The time the reply was created. If not provided, the current time will be used."""

    reply_options: Iterable[AdminReplyTicketRequestReplyOption]
    """The quick reply options to display.

    Must be present for quick_reply message types.
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


class AdminReplyTicketRequestReplyOption(TypedDict, total=False):
    text: Required[str]
    """The text to display in this quick reply option."""

    uuid: Required[str]
    """A unique identifier for this quick reply option.

    This value will be available within the metadata of the comment ticket part that
    is created when a user clicks on this reply option.
    """


TicketReplyParams = Union[
    ContactReplyTicketIntercomUserIDRequest,
    ContactReplyTicketUserIDRequest,
    ContactReplyTicketEmailRequest,
    AdminReplyTicketRequest,
]
