# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from .tags import Tags, AsyncTags, TagsWithRawResponse, AsyncTagsWithRawResponse
from .notes import Notes, AsyncNotes, NotesWithRawResponse, AsyncNotesWithRawResponse
from ...types import (
    ContactList,
    ContactDeleted,
    ContactArchived,
    ContactUnarchived,
    contact_merge_params,
    contact_create_params,
    contact_search_params,
    contact_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .segments import (
    Segments,
    AsyncSegments,
    SegmentsWithRawResponse,
    AsyncSegmentsWithRawResponse,
)
from .companies import (
    Companies,
    AsyncCompanies,
    CompaniesWithRawResponse,
    AsyncCompaniesWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .subscriptions import (
    Subscriptions,
    AsyncSubscriptions,
    SubscriptionsWithRawResponse,
    AsyncSubscriptionsWithRawResponse,
)
from ..._base_client import make_request_options
from ...types.shared import Contact

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Contacts", "AsyncContacts"]


class Contacts(SyncAPIResource):
    companies: Companies
    notes: Notes
    segments: Segments
    subscriptions: Subscriptions
    tags: Tags
    with_raw_response: ContactsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.companies = Companies(client)
        self.notes = Notes(client)
        self.segments = Segments(client)
        self.subscriptions = Subscriptions(client)
        self.tags = Tags(client)
        self.with_raw_response = ContactsWithRawResponse(self)

    def create(
        self,
        *,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        custom_attributes: Optional[object] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_seen_at: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        owner_id: Optional[int] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        role: str | NotGiven = NOT_GIVEN,
        signed_up_at: Optional[int] | NotGiven = NOT_GIVEN,
        unsubscribed_from_emails: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """You can create a new contact (ie.

        user or lead).

        Args:
          avatar: An image URL containing the avatar of a contact

          custom_attributes: The custom attributes which are set for the contact

          email: The contacts email

          external_id: A unique identifier for the contact which is given to Intercom

          last_seen_at: The time when the contact was last seen (either where the Intercom Messenger was
              installed or when specified manually)

          name: The contacts name

          owner_id: The id of an admin that has been assigned account ownership of the contact

          phone: The contacts phone

          role: The role of the contact.

          signed_up_at: The time specified for when a contact signed up

          unsubscribed_from_emails: Whether the contact is unsubscribed from emails

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts",
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "custom_attributes": custom_attributes,
                    "email": email,
                    "external_id": external_id,
                    "last_seen_at": last_seen_at,
                    "name": name,
                    "owner_id": owner_id,
                    "phone": phone,
                    "role": role,
                    "signed_up_at": signed_up_at,
                    "unsubscribed_from_emails": unsubscribed_from_emails,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """
        You can fetch the details of a single contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def update(
        self,
        id: str,
        *,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        custom_attributes: Optional[object] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_seen_at: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        owner_id: Optional[int] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        role: str | NotGiven = NOT_GIVEN,
        signed_up_at: Optional[int] | NotGiven = NOT_GIVEN,
        unsubscribed_from_emails: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """You can update an existing contact (ie.

        user or lead).

        Args:
          avatar: An image URL containing the avatar of a contact

          custom_attributes: The custom attributes which are set for the contact

          email: The contacts email

          external_id: A unique identifier for the contact which is given to Intercom

          last_seen_at: The time when the contact was last seen (either where the Intercom Messenger was
              installed or when specified manually)

          name: The contacts name

          owner_id: The id of an admin that has been assigned account ownership of the contact

          phone: The contacts phone

          role: The role of the contact.

          signed_up_at: The time specified for when a contact signed up

          unsubscribed_from_emails: Whether the contact is unsubscribed from emails

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/contacts/{id}",
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "custom_attributes": custom_attributes,
                    "email": email,
                    "external_id": external_id,
                    "last_seen_at": last_seen_at,
                    "name": name,
                    "owner_id": owner_id,
                    "phone": phone,
                    "role": role,
                    "signed_up_at": signed_up_at,
                    "unsubscribed_from_emails": unsubscribed_from_emails,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactList:
        """You can fetch a list of all contacts."""
        return self._get(
            "/contacts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactList,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactDeleted:
        """
        You can delete a single contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactDeleted,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactArchived:
        """
        You can archive a single contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/contacts/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactArchived,
        )

    def merge(
        self,
        *,
        from_: str | NotGiven = NOT_GIVEN,
        into: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """
        You can merge a contact with a `role` of `lead` into a contact with a `role` of
        `user`.

        Args:
          from_: The unique identifier for the contact to merge away from. Must be a lead.

          into: The unique identifier for the contact to merge into. Must be a user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts/merge",
            body=maybe_transform(
                {
                    "from_": from_,
                    "into": into,
                },
                contact_merge_params.ContactMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def search(
        self,
        *,
        query: contact_search_params.Query,
        pagination: Optional[contact_search_params.Pagination] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactList:
        """
        You can search for multiple contacts by the value of their attributes in order
        to fetch exactly who you want.

        To search for contacts, you need to send a POST request to
        `https://api.intercom.io/contacts/search`. This will accept a query object in
        the body which will define your filters in order to search for contacts.

        > 🚧 Why is there a delay when creating contacts and searching for them?
        >
        > If a contact has recently been created, there is a possibility that it will
        > not yet be available when searching. This means that it may not appear in the
        > response. This delay can take a few minutes. If you need to be instantly
        > notified then you could use webhooks instead, which you'd currently have to
        > iterate on to see if they match your search filters.

        > 🚧 Nesting & Limitations
        >
        > You can nest these filters in order to get even more granular insights that
        > pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        > limitations to the amount of multiple's there can be:
        >
        > - There's a limit of max 2 nested filters
        > - There's a limit of max 15 filters for each AND or OR group

        > 🚧 Searching for Timestamp Fields

        > All timestamp fields (created_at, updated_at etc.) are indexed as Dates for
        > Contact Search queries; Datetime queries are not currently supported. This
        > means you can only query for timestamp fields by day - not hour, minute or
        > second. For example, if you search for all Contacts with a created_at value
        > greater (>) than 1577869200 (the UNIX timestamp for January 1st, 2020 9:00
        > AM), that will be interpreted as 1577836800 (January 1st, 2020 12:00 AM). The
        > search results will then include Contacts created from January 2nd, 2020 12:00
        > AM onwards. If you'd like to get contacts created on January 1st, 2020 you
        > should search with a created_at value equal (=) to 1577836800 (January 1st,
        > 2020 12:00 AM). This behaviour applies only to timestamps used in search
        > queries. The search results will still contain the full UNIX timestamp and be
        > sorted accordingly.

        ### Accepted Fields

        Most key listed as part of the Contacts Model are searchable, whether writeable
        or not. The value you search for has to match the accepted type, otherwise the
        query will fail (ie. as `created_at` accepts a date, the `value` cannot be a
        string such as `"foorbar"`).

        | Field                              | Type                           |
        | ---------------------------------- | ------------------------------ |
        | id                                 | String                         |
        | role                               | String<br>Accepts user or lead |
        | name                               | String                         |
        | avatar                             | String                         |
        | owner_id                           | Integer                        |
        | email                              | String                         |
        | phone                              | String                         |
        | formatted_phone                    | String                         |
        | external_id                        | String                         |
        | created_at                         | Date (UNIX Timestamp)          |
        | signed_up_at                       | Date (UNIX Timestamp)          |
        | updated_at                         | Date (UNIX Timestamp)          |
        | last_seen_at                       | Date (UNIX Timestamp)          |
        | last_contacted_at                  | Date (UNIX Timestamp)          |
        | last_replied_at                    | Date (UNIX Timestamp)          |
        | last_email_opened_at               | Date (UNIX Timestamp)          |
        | last_email_clicked_at              | Date (UNIX Timestamp)          |
        | language_override                  | String                         |
        | browser                            | String                         |
        | browser_language                   | String                         |
        | os                                 | String                         |
        | location.country                   | String                         |
        | location.region                    | String                         |
        | location.city                      | String                         |
        | unsubscribed_from_emails           | Boolean                        |
        | marked_email_as_spam               | Boolean                        |
        | has_hard_bounced                   | Boolean                        |
        | ios_last_seen_at                   | Date (UNIX Timestamp)          |
        | ios_app_version                    | String                         |
        | ios_device                         | String                         |
        | ios_app_device                     | String                         |
        | ios_os_version                     | String                         |
        | ios_app_name                       | String                         |
        | ios_sdk_version                    | String                         |
        | android_last_seen_at               | Date (UNIX Timestamp)          |
        | android_app_version                | String                         |
        | android_device                     | String                         |
        | android_app_name                   | String                         |
        | andoid_sdk_version                 | String                         |
        | segment_id                         | String                         |
        | tag_id                             | String                         |
        | custom_attributes.{attribute_name} | String                         |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts/search",
            body=maybe_transform(
                {
                    "query": query,
                    "pagination": pagination,
                },
                contact_search_params.ContactSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactList,
        )

    def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactUnarchived:
        """
        You can unarchive a single contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/contacts/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUnarchived,
        )


class AsyncContacts(AsyncAPIResource):
    companies: AsyncCompanies
    notes: AsyncNotes
    segments: AsyncSegments
    subscriptions: AsyncSubscriptions
    tags: AsyncTags
    with_raw_response: AsyncContactsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.companies = AsyncCompanies(client)
        self.notes = AsyncNotes(client)
        self.segments = AsyncSegments(client)
        self.subscriptions = AsyncSubscriptions(client)
        self.tags = AsyncTags(client)
        self.with_raw_response = AsyncContactsWithRawResponse(self)

    async def create(
        self,
        *,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        custom_attributes: Optional[object] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_seen_at: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        owner_id: Optional[int] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        role: str | NotGiven = NOT_GIVEN,
        signed_up_at: Optional[int] | NotGiven = NOT_GIVEN,
        unsubscribed_from_emails: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """You can create a new contact (ie.

        user or lead).

        Args:
          avatar: An image URL containing the avatar of a contact

          custom_attributes: The custom attributes which are set for the contact

          email: The contacts email

          external_id: A unique identifier for the contact which is given to Intercom

          last_seen_at: The time when the contact was last seen (either where the Intercom Messenger was
              installed or when specified manually)

          name: The contacts name

          owner_id: The id of an admin that has been assigned account ownership of the contact

          phone: The contacts phone

          role: The role of the contact.

          signed_up_at: The time specified for when a contact signed up

          unsubscribed_from_emails: Whether the contact is unsubscribed from emails

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts",
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "custom_attributes": custom_attributes,
                    "email": email,
                    "external_id": external_id,
                    "last_seen_at": last_seen_at,
                    "name": name,
                    "owner_id": owner_id,
                    "phone": phone,
                    "role": role,
                    "signed_up_at": signed_up_at,
                    "unsubscribed_from_emails": unsubscribed_from_emails,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """
        You can fetch the details of a single contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    async def update(
        self,
        id: str,
        *,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        custom_attributes: Optional[object] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_seen_at: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        owner_id: Optional[int] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        role: str | NotGiven = NOT_GIVEN,
        signed_up_at: Optional[int] | NotGiven = NOT_GIVEN,
        unsubscribed_from_emails: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """You can update an existing contact (ie.

        user or lead).

        Args:
          avatar: An image URL containing the avatar of a contact

          custom_attributes: The custom attributes which are set for the contact

          email: The contacts email

          external_id: A unique identifier for the contact which is given to Intercom

          last_seen_at: The time when the contact was last seen (either where the Intercom Messenger was
              installed or when specified manually)

          name: The contacts name

          owner_id: The id of an admin that has been assigned account ownership of the contact

          phone: The contacts phone

          role: The role of the contact.

          signed_up_at: The time specified for when a contact signed up

          unsubscribed_from_emails: Whether the contact is unsubscribed from emails

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/contacts/{id}",
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "custom_attributes": custom_attributes,
                    "email": email,
                    "external_id": external_id,
                    "last_seen_at": last_seen_at,
                    "name": name,
                    "owner_id": owner_id,
                    "phone": phone,
                    "role": role,
                    "signed_up_at": signed_up_at,
                    "unsubscribed_from_emails": unsubscribed_from_emails,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactList:
        """You can fetch a list of all contacts."""
        return await self._get(
            "/contacts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactList,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactDeleted:
        """
        You can delete a single contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactDeleted,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactArchived:
        """
        You can archive a single contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/contacts/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactArchived,
        )

    async def merge(
        self,
        *,
        from_: str | NotGiven = NOT_GIVEN,
        into: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """
        You can merge a contact with a `role` of `lead` into a contact with a `role` of
        `user`.

        Args:
          from_: The unique identifier for the contact to merge away from. Must be a lead.

          into: The unique identifier for the contact to merge into. Must be a user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts/merge",
            body=maybe_transform(
                {
                    "from_": from_,
                    "into": into,
                },
                contact_merge_params.ContactMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    async def search(
        self,
        *,
        query: contact_search_params.Query,
        pagination: Optional[contact_search_params.Pagination] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactList:
        """
        You can search for multiple contacts by the value of their attributes in order
        to fetch exactly who you want.

        To search for contacts, you need to send a POST request to
        `https://api.intercom.io/contacts/search`. This will accept a query object in
        the body which will define your filters in order to search for contacts.

        > 🚧 Why is there a delay when creating contacts and searching for them?
        >
        > If a contact has recently been created, there is a possibility that it will
        > not yet be available when searching. This means that it may not appear in the
        > response. This delay can take a few minutes. If you need to be instantly
        > notified then you could use webhooks instead, which you'd currently have to
        > iterate on to see if they match your search filters.

        > 🚧 Nesting & Limitations
        >
        > You can nest these filters in order to get even more granular insights that
        > pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        > limitations to the amount of multiple's there can be:
        >
        > - There's a limit of max 2 nested filters
        > - There's a limit of max 15 filters for each AND or OR group

        > 🚧 Searching for Timestamp Fields

        > All timestamp fields (created_at, updated_at etc.) are indexed as Dates for
        > Contact Search queries; Datetime queries are not currently supported. This
        > means you can only query for timestamp fields by day - not hour, minute or
        > second. For example, if you search for all Contacts with a created_at value
        > greater (>) than 1577869200 (the UNIX timestamp for January 1st, 2020 9:00
        > AM), that will be interpreted as 1577836800 (January 1st, 2020 12:00 AM). The
        > search results will then include Contacts created from January 2nd, 2020 12:00
        > AM onwards. If you'd like to get contacts created on January 1st, 2020 you
        > should search with a created_at value equal (=) to 1577836800 (January 1st,
        > 2020 12:00 AM). This behaviour applies only to timestamps used in search
        > queries. The search results will still contain the full UNIX timestamp and be
        > sorted accordingly.

        ### Accepted Fields

        Most key listed as part of the Contacts Model are searchable, whether writeable
        or not. The value you search for has to match the accepted type, otherwise the
        query will fail (ie. as `created_at` accepts a date, the `value` cannot be a
        string such as `"foorbar"`).

        | Field                              | Type                           |
        | ---------------------------------- | ------------------------------ |
        | id                                 | String                         |
        | role                               | String<br>Accepts user or lead |
        | name                               | String                         |
        | avatar                             | String                         |
        | owner_id                           | Integer                        |
        | email                              | String                         |
        | phone                              | String                         |
        | formatted_phone                    | String                         |
        | external_id                        | String                         |
        | created_at                         | Date (UNIX Timestamp)          |
        | signed_up_at                       | Date (UNIX Timestamp)          |
        | updated_at                         | Date (UNIX Timestamp)          |
        | last_seen_at                       | Date (UNIX Timestamp)          |
        | last_contacted_at                  | Date (UNIX Timestamp)          |
        | last_replied_at                    | Date (UNIX Timestamp)          |
        | last_email_opened_at               | Date (UNIX Timestamp)          |
        | last_email_clicked_at              | Date (UNIX Timestamp)          |
        | language_override                  | String                         |
        | browser                            | String                         |
        | browser_language                   | String                         |
        | os                                 | String                         |
        | location.country                   | String                         |
        | location.region                    | String                         |
        | location.city                      | String                         |
        | unsubscribed_from_emails           | Boolean                        |
        | marked_email_as_spam               | Boolean                        |
        | has_hard_bounced                   | Boolean                        |
        | ios_last_seen_at                   | Date (UNIX Timestamp)          |
        | ios_app_version                    | String                         |
        | ios_device                         | String                         |
        | ios_app_device                     | String                         |
        | ios_os_version                     | String                         |
        | ios_app_name                       | String                         |
        | ios_sdk_version                    | String                         |
        | android_last_seen_at               | Date (UNIX Timestamp)          |
        | android_app_version                | String                         |
        | android_device                     | String                         |
        | android_app_name                   | String                         |
        | andoid_sdk_version                 | String                         |
        | segment_id                         | String                         |
        | tag_id                             | String                         |
        | custom_attributes.{attribute_name} | String                         |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts/search",
            body=maybe_transform(
                {
                    "query": query,
                    "pagination": pagination,
                },
                contact_search_params.ContactSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactList,
        )

    async def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactUnarchived:
        """
        You can unarchive a single contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/contacts/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUnarchived,
        )


class ContactsWithRawResponse:
    def __init__(self, contacts: Contacts) -> None:
        self.companies = CompaniesWithRawResponse(contacts.companies)
        self.notes = NotesWithRawResponse(contacts.notes)
        self.segments = SegmentsWithRawResponse(contacts.segments)
        self.subscriptions = SubscriptionsWithRawResponse(contacts.subscriptions)
        self.tags = TagsWithRawResponse(contacts.tags)

        self.create = to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contacts.update,
        )
        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = to_raw_response_wrapper(
            contacts.delete,
        )
        self.archive = to_raw_response_wrapper(
            contacts.archive,
        )
        self.merge = to_raw_response_wrapper(
            contacts.merge,
        )
        self.search = to_raw_response_wrapper(
            contacts.search,
        )
        self.unarchive = to_raw_response_wrapper(
            contacts.unarchive,
        )


class AsyncContactsWithRawResponse:
    def __init__(self, contacts: AsyncContacts) -> None:
        self.companies = AsyncCompaniesWithRawResponse(contacts.companies)
        self.notes = AsyncNotesWithRawResponse(contacts.notes)
        self.segments = AsyncSegmentsWithRawResponse(contacts.segments)
        self.subscriptions = AsyncSubscriptionsWithRawResponse(contacts.subscriptions)
        self.tags = AsyncTagsWithRawResponse(contacts.tags)

        self.create = async_to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contacts.update,
        )
        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contacts.delete,
        )
        self.archive = async_to_raw_response_wrapper(
            contacts.archive,
        )
        self.merge = async_to_raw_response_wrapper(
            contacts.merge,
        )
        self.search = async_to_raw_response_wrapper(
            contacts.search,
        )
        self.unarchive = async_to_raw_response_wrapper(
            contacts.unarchive,
        )
