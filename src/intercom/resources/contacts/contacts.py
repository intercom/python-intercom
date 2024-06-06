# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional, overload

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .notes import (
    NotesResource,
    AsyncNotesResource,
    NotesResourceWithRawResponse,
    AsyncNotesResourceWithRawResponse,
    NotesResourceWithStreamingResponse,
    AsyncNotesResourceWithStreamingResponse,
)
from ...types import (
    contact_merge_params,
    contact_create_params,
    contact_search_params,
    contact_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from .segments import (
    SegmentsResource,
    AsyncSegmentsResource,
    SegmentsResourceWithRawResponse,
    AsyncSegmentsResourceWithRawResponse,
    SegmentsResourceWithStreamingResponse,
    AsyncSegmentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .companies import (
    CompaniesResource,
    AsyncCompaniesResource,
    CompaniesResourceWithRawResponse,
    AsyncCompaniesResourceWithRawResponse,
    CompaniesResourceWithStreamingResponse,
    AsyncCompaniesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from ...types.contact_list import ContactList
from ...types.shared.contact import Contact
from ...types.contact_deleted import ContactDeleted
from ...types.contact_archived import ContactArchived
from ...types.contact_unarchived import ContactUnarchived

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    @cached_property
    def companies(self) -> CompaniesResource:
        return CompaniesResource(self._client)

    @cached_property
    def notes(self) -> NotesResource:
        return NotesResource(self._client)

    @cached_property
    def segments(self) -> SegmentsResource:
        return SegmentsResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        body: object,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        body: object,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        body: object,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"])
    def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        return self._post(
            "/contacts",
            body=maybe_transform(body, contact_create_params.ContactCreateParams),
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
        """You can fetch a list of all contacts (ie.

        users or leads) in your workspace.
        {% admonition type="warning" name="Pagination" %} You can use pagination to
        limit the number of results returned. The default is `50` results per page. See
        the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis)
        for more details on how to use the `starting_after` param. {% /admonition %}
        """
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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

        To search for contacts, you need to send a `POST` request to
        `https://api.intercom.io/contacts/search`.

        This will accept a query object in the body which will define your filters in
        order to search for contacts.

        {% admonition type="warning" name="Optimizing search queries" %} Search queries
        can be complex, so optimizing them can help the performance of your search. Use
        the `AND` and `OR` operators to combine multiple filters to get the exact
        results you need and utilize pagination to limit the number of results returned.
        The default is `50` results per page. See the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request)
        for more details on how to use the `starting_after` param. {% /admonition %}

        ### Contact Creation Delay

        If a contact has recently been created, there is a possibility that it will not
        yet be available when searching. This means that it may not appear in the
        response. This delay can take a few minutes. If you need to be instantly
        notified it is recommended to use webhooks and iterate to see if they match your
        search filters.

        ### Nesting & Limitations

        You can nest these filters in order to get even more granular insights that
        pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        limitations to the amount of multiple's there can be:

        - There's a limit of max 2 nested filters
        - There's a limit of max 15 filters for each AND or OR group

        ### Searching for Timestamp Fields

        All timestamp fields (created_at, updated_at etc.) are indexed as Dates for
        Contact Search queries; Datetime queries are not currently supported. This means
        you can only query for timestamp fields by day - not hour, minute or second. For
        example, if you search for all Contacts with a created_at value greater (>) than
        1577869200 (the UNIX timestamp for January 1st, 2020 9:00 AM), that will be
        interpreted as 1577836800 (January 1st, 2020 12:00 AM). The search results will
        then include Contacts created from January 2nd, 2020 12:00 AM onwards. If you'd
        like to get contacts created on January 1st, 2020 you should search with a
        created_at value equal (=) to 1577836800 (January 1st, 2020 12:00 AM). This
        behaviour applies only to timestamps used in search queries. The search results
        will still contain the full UNIX timestamp and be sorted accordingly.

        ### Accepted Fields

        Most key listed as part of the Contacts Model are searchable, whether writeable
        or not. The value you search for has to match the accepted type, otherwise the
        query will fail (ie. as `created_at` accepts a date, the `value` cannot be a
        string such as `"foorbar"`).

        | Field                              | Type                  |
        | ---------------------------------- | --------------------- |
        | id                                 | String                |
        | role                               | String                |
        | Accepts user or lead               |
        | name                               | String                |
        | avatar                             | String                |
        | owner_id                           | Integer               |
        | email                              | String                |
        | email_domain                       | String                |
        | phone                              | String                |
        | formatted_phone                    | String                |
        | external_id                        | String                |
        | created_at                         | Date (UNIX Timestamp) |
        | signed_up_at                       | Date (UNIX Timestamp) |
        | updated_at                         | Date (UNIX Timestamp) |
        | last_seen_at                       | Date (UNIX Timestamp) |
        | last_contacted_at                  | Date (UNIX Timestamp) |
        | last_replied_at                    | Date (UNIX Timestamp) |
        | last_email_opened_at               | Date (UNIX Timestamp) |
        | last_email_clicked_at              | Date (UNIX Timestamp) |
        | language_override                  | String                |
        | browser                            | String                |
        | browser_language                   | String                |
        | os                                 | String                |
        | location.country                   | String                |
        | location.region                    | String                |
        | location.city                      | String                |
        | unsubscribed_from_emails           | Boolean               |
        | marked_email_as_spam               | Boolean               |
        | has_hard_bounced                   | Boolean               |
        | ios_last_seen_at                   | Date (UNIX Timestamp) |
        | ios_app_version                    | String                |
        | ios_device                         | String                |
        | ios_app_device                     | String                |
        | ios_os_version                     | String                |
        | ios_app_name                       | String                |
        | ios_sdk_version                    | String                |
        | android_last_seen_at               | Date (UNIX Timestamp) |
        | android_app_version                | String                |
        | android_device                     | String                |
        | android_app_name                   | String                |
        | andoid_sdk_version                 | String                |
        | segment_id                         | String                |
        | tag_id                             | String                |
        | custom_attributes.{attribute_name} | String                |

        ### Accepted Operators

        {% admonition type="attention" name="Searching based on `created_at`" %} You
        cannot use the `<=` or `>=` operators to search by `created_at`.
        {% /admonition %}

        The table below shows the operators you can use to define how you want to search
        for the value. The operator should be put in as a string (`"="`). The operator
        has to be compatible with the field's type (eg. you cannot search with `>` for a
        given string value as it's only compatible for integer's and dates).

        | Operator | Valid Types | Description   |
        | :------- | :---------- | :------------ |
        | =        | All         | Equals        |
        | !=       | All         | Doesn't Equal |
        | IN       | All         | In            |

        Shortcut for `OR` queries Values must be in Array | | NIN | All | Not In
        Shortcut for `OR !` queries Values must be in Array | | > | Integer Date (UNIX
        Timestamp) | Greater than | | < | Integer Date (UNIX Timestamp) | Lower than | |
        ~ | String | Contains | | !~ | String | Doesn't Contain | | ^ | String | Starts
        With | | $ | String | Ends With |

        Args:
          query: Search using Intercoms Search APIs with a single filter.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/contacts/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUnarchived,
        )


class AsyncContactsResource(AsyncAPIResource):
    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        return AsyncCompaniesResource(self._client)

    @cached_property
    def notes(self) -> AsyncNotesResource:
        return AsyncNotesResource(self._client)

    @cached_property
    def segments(self) -> AsyncSegmentsResource:
        return AsyncSegmentsResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        body: object,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        body: object,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        body: object,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"])
    async def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        return await self._post(
            "/contacts",
            body=await async_maybe_transform(body, contact_create_params.ContactCreateParams),
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/contacts/{id}",
            body=await async_maybe_transform(
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
        """You can fetch a list of all contacts (ie.

        users or leads) in your workspace.
        {% admonition type="warning" name="Pagination" %} You can use pagination to
        limit the number of results returned. The default is `50` results per page. See
        the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis)
        for more details on how to use the `starting_after` param. {% /admonition %}
        """
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
            body=await async_maybe_transform(
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

        To search for contacts, you need to send a `POST` request to
        `https://api.intercom.io/contacts/search`.

        This will accept a query object in the body which will define your filters in
        order to search for contacts.

        {% admonition type="warning" name="Optimizing search queries" %} Search queries
        can be complex, so optimizing them can help the performance of your search. Use
        the `AND` and `OR` operators to combine multiple filters to get the exact
        results you need and utilize pagination to limit the number of results returned.
        The default is `50` results per page. See the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request)
        for more details on how to use the `starting_after` param. {% /admonition %}

        ### Contact Creation Delay

        If a contact has recently been created, there is a possibility that it will not
        yet be available when searching. This means that it may not appear in the
        response. This delay can take a few minutes. If you need to be instantly
        notified it is recommended to use webhooks and iterate to see if they match your
        search filters.

        ### Nesting & Limitations

        You can nest these filters in order to get even more granular insights that
        pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        limitations to the amount of multiple's there can be:

        - There's a limit of max 2 nested filters
        - There's a limit of max 15 filters for each AND or OR group

        ### Searching for Timestamp Fields

        All timestamp fields (created_at, updated_at etc.) are indexed as Dates for
        Contact Search queries; Datetime queries are not currently supported. This means
        you can only query for timestamp fields by day - not hour, minute or second. For
        example, if you search for all Contacts with a created_at value greater (>) than
        1577869200 (the UNIX timestamp for January 1st, 2020 9:00 AM), that will be
        interpreted as 1577836800 (January 1st, 2020 12:00 AM). The search results will
        then include Contacts created from January 2nd, 2020 12:00 AM onwards. If you'd
        like to get contacts created on January 1st, 2020 you should search with a
        created_at value equal (=) to 1577836800 (January 1st, 2020 12:00 AM). This
        behaviour applies only to timestamps used in search queries. The search results
        will still contain the full UNIX timestamp and be sorted accordingly.

        ### Accepted Fields

        Most key listed as part of the Contacts Model are searchable, whether writeable
        or not. The value you search for has to match the accepted type, otherwise the
        query will fail (ie. as `created_at` accepts a date, the `value` cannot be a
        string such as `"foorbar"`).

        | Field                              | Type                  |
        | ---------------------------------- | --------------------- |
        | id                                 | String                |
        | role                               | String                |
        | Accepts user or lead               |
        | name                               | String                |
        | avatar                             | String                |
        | owner_id                           | Integer               |
        | email                              | String                |
        | email_domain                       | String                |
        | phone                              | String                |
        | formatted_phone                    | String                |
        | external_id                        | String                |
        | created_at                         | Date (UNIX Timestamp) |
        | signed_up_at                       | Date (UNIX Timestamp) |
        | updated_at                         | Date (UNIX Timestamp) |
        | last_seen_at                       | Date (UNIX Timestamp) |
        | last_contacted_at                  | Date (UNIX Timestamp) |
        | last_replied_at                    | Date (UNIX Timestamp) |
        | last_email_opened_at               | Date (UNIX Timestamp) |
        | last_email_clicked_at              | Date (UNIX Timestamp) |
        | language_override                  | String                |
        | browser                            | String                |
        | browser_language                   | String                |
        | os                                 | String                |
        | location.country                   | String                |
        | location.region                    | String                |
        | location.city                      | String                |
        | unsubscribed_from_emails           | Boolean               |
        | marked_email_as_spam               | Boolean               |
        | has_hard_bounced                   | Boolean               |
        | ios_last_seen_at                   | Date (UNIX Timestamp) |
        | ios_app_version                    | String                |
        | ios_device                         | String                |
        | ios_app_device                     | String                |
        | ios_os_version                     | String                |
        | ios_app_name                       | String                |
        | ios_sdk_version                    | String                |
        | android_last_seen_at               | Date (UNIX Timestamp) |
        | android_app_version                | String                |
        | android_device                     | String                |
        | android_app_name                   | String                |
        | andoid_sdk_version                 | String                |
        | segment_id                         | String                |
        | tag_id                             | String                |
        | custom_attributes.{attribute_name} | String                |

        ### Accepted Operators

        {% admonition type="attention" name="Searching based on `created_at`" %} You
        cannot use the `<=` or `>=` operators to search by `created_at`.
        {% /admonition %}

        The table below shows the operators you can use to define how you want to search
        for the value. The operator should be put in as a string (`"="`). The operator
        has to be compatible with the field's type (eg. you cannot search with `>` for a
        given string value as it's only compatible for integer's and dates).

        | Operator | Valid Types | Description   |
        | :------- | :---------- | :------------ |
        | =        | All         | Equals        |
        | !=       | All         | Doesn't Equal |
        | IN       | All         | In            |

        Shortcut for `OR` queries Values must be in Array | | NIN | All | Not In
        Shortcut for `OR !` queries Values must be in Array | | > | Integer Date (UNIX
        Timestamp) | Greater than | | < | Integer Date (UNIX Timestamp) | Lower than | |
        ~ | String | Contains | | !~ | String | Doesn't Contain | | ^ | String | Starts
        With | | $ | String | Ends With |

        Args:
          query: Search using Intercoms Search APIs with a single filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts/search",
            body=await async_maybe_transform(
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/contacts/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUnarchived,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

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

    @cached_property
    def companies(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self._contacts.companies)

    @cached_property
    def notes(self) -> NotesResourceWithRawResponse:
        return NotesResourceWithRawResponse(self._contacts.notes)

    @cached_property
    def segments(self) -> SegmentsResourceWithRawResponse:
        return SegmentsResourceWithRawResponse(self._contacts.segments)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._contacts.subscriptions)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._contacts.tags)


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

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

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self._contacts.companies)

    @cached_property
    def notes(self) -> AsyncNotesResourceWithRawResponse:
        return AsyncNotesResourceWithRawResponse(self._contacts.notes)

    @cached_property
    def segments(self) -> AsyncSegmentsResourceWithRawResponse:
        return AsyncSegmentsResourceWithRawResponse(self._contacts.segments)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._contacts.subscriptions)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._contacts.tags)


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contacts.update,
        )
        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contacts.delete,
        )
        self.archive = to_streamed_response_wrapper(
            contacts.archive,
        )
        self.merge = to_streamed_response_wrapper(
            contacts.merge,
        )
        self.search = to_streamed_response_wrapper(
            contacts.search,
        )
        self.unarchive = to_streamed_response_wrapper(
            contacts.unarchive,
        )

    @cached_property
    def companies(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self._contacts.companies)

    @cached_property
    def notes(self) -> NotesResourceWithStreamingResponse:
        return NotesResourceWithStreamingResponse(self._contacts.notes)

    @cached_property
    def segments(self) -> SegmentsResourceWithStreamingResponse:
        return SegmentsResourceWithStreamingResponse(self._contacts.segments)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._contacts.subscriptions)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._contacts.tags)


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contacts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contacts.delete,
        )
        self.archive = async_to_streamed_response_wrapper(
            contacts.archive,
        )
        self.merge = async_to_streamed_response_wrapper(
            contacts.merge,
        )
        self.search = async_to_streamed_response_wrapper(
            contacts.search,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            contacts.unarchive,
        )

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self._contacts.companies)

    @cached_property
    def notes(self) -> AsyncNotesResourceWithStreamingResponse:
        return AsyncNotesResourceWithStreamingResponse(self._contacts.notes)

    @cached_property
    def segments(self) -> AsyncSegmentsResourceWithStreamingResponse:
        return AsyncSegmentsResourceWithStreamingResponse(self._contacts.segments)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._contacts.subscriptions)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._contacts.tags)
