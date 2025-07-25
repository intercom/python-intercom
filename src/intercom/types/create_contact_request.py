# This file was auto-generated by Fern from our API Definition.

import typing

from .create_contact_request_with_email import CreateContactRequestWithEmail
from .create_contact_request_with_external_id import CreateContactRequestWithExternalId
from .create_contact_request_with_role import CreateContactRequestWithRole

CreateContactRequest = typing.Union[
    CreateContactRequestWithEmail, CreateContactRequestWithExternalId, CreateContactRequestWithRole
]
