# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ReplyCreateParams",
    "ContactReplyIntercomUserIDRequest",
    "ContactReplyEmailRequest",
    "ContactReplyUserIDRequest",
    "AdminReplyConversationRequest",
    "AdminReplyConversationRequestAttachmentFile",
]


class ContactReplyIntercomUserIDRequest(TypedDict, total=False):
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


class ContactReplyEmailRequest(TypedDict, total=False):
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


class ContactReplyUserIDRequest(TypedDict, total=False):
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


class AdminReplyConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is authoring the comment."""

    message_type: Required[Literal["comment", "note"]]

    type: Required[Literal["admin"]]

    attachment_files: Iterable[AdminReplyConversationRequestAttachmentFile]
    """A list of files that will be added as attachments.

    You can include up to 10 files
    """

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


class AdminReplyConversationRequestAttachmentFile(TypedDict, total=False):
    content_type: str
    """The content type of the file"""

    data: str
    """The base64 encoded file data."""

    name: str
    """The name of the file."""


ReplyCreateParams = Union[
    ContactReplyIntercomUserIDRequest,
    ContactReplyEmailRequest,
    ContactReplyUserIDRequest,
    AdminReplyConversationRequest,
]
