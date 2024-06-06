# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "TicketReplyParams",
    "ContactReplyIntercomUserIDRequest",
    "ContactReplyUserIDRequest",
    "ContactReplyEmailRequest",
    "AdminReplyTicketRequest",
    "AdminReplyTicketRequestReplyOption",
]


class ContactReplyIntercomUserIDRequest(TypedDict, total=False):
    body: Required[str]
    """The text body of the comment."""

    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""

    message_type: Required[Literal["comment"]]

    type: Required[Literal["user"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 5 URLs.
    """


class ContactReplyUserIDRequest(TypedDict, total=False):
    body: Required[str]
    """The text body of the comment."""

    message_type: Required[Literal["comment"]]

    type: Required[Literal["user"]]

    user_id: Required[str]
    """The external_id you have defined for the contact."""

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 5 URLs.
    """


class ContactReplyEmailRequest(TypedDict, total=False):
    body: Required[str]
    """The text body of the comment."""

    email: Required[str]
    """The email you have defined for the user."""

    message_type: Required[Literal["comment"]]

    type: Required[Literal["user"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 5 URLs.
    """


class AdminReplyTicketRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is authoring the comment."""

    message_type: Required[Literal["comment", "note", "quick_reply"]]

    type: Required[Literal["admin"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 5 URLs.
    """

    body: str
    """The text body of the reply.\nNotes accept some HTML formatting.

    Must be present for comment and note message types.
    """

    reply_options: Iterable[AdminReplyTicketRequestReplyOption]
    """The quick reply options to display.

    Must be present for quick_reply message types.
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
    ContactReplyIntercomUserIDRequest, ContactReplyUserIDRequest, ContactReplyEmailRequest, AdminReplyTicketRequest
]
