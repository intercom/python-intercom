# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict

import httpx

from ...types import DeletedCompanyObject, company_create_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .contacts import (
    Contacts,
    AsyncContacts,
    ContactsWithRawResponse,
    AsyncContactsWithRawResponse,
)
from .segments import (
    Segments,
    AsyncSegments,
    SegmentsWithRawResponse,
    AsyncSegmentsWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.shared import Company

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Companies", "AsyncCompanies"]


class Companies(SyncAPIResource):
    contacts: Contacts
    segments: Segments
    with_raw_response: CompaniesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.contacts = Contacts(client)
        self.segments = Segments(client)
        self.with_raw_response = CompaniesWithRawResponse(self)

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
    ) -> Company:
        """
        You can fetch a single company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def update(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """
        You can update a single company

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
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
    ) -> DeletedCompanyObject:
        """
        You can delete a single company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedCompanyObject,
        )

    def create_update(
        self,
        *,
        company_id: str | NotGiven = NOT_GIVEN,
        custom_attributes: Dict[str, str] | NotGiven = NOT_GIVEN,
        industry: str | NotGiven = NOT_GIVEN,
        monthly_spend: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        plan: str | NotGiven = NOT_GIVEN,
        remote_created_at: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        website: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """
        You can create or update a company.

        > 📘 Companies with no users
        >
        > Companies will be only visible in Intercom when there is at least one
        > associated user.

        Companies are looked up via `company_id` in a `POST` request, if not found via
        `company_id`, the new company will be created, if found, that company will be
        updated.

        Args:
          company_id: The company id you have defined for the company. Can't be updated

          custom_attributes: A hash of key/value pairs containing any other data about the company you want
              Intercom to store.

          industry: The industry that this company operates in.

          monthly_spend: How much revenue the company generates for your business. Note that this will
              truncate floats. i.e. it only allow for whole integers, 155.98 will be truncated
              to 155. Note that this has an upper limit of 2\\**\\**31-1 or 2147483647..

          name: The name of the Company

          plan: The name of the plan you have associated with the company.

          remote_created_at: The time the company was created by you.

          size: The number of employees in this company.

          website: The URL for this company's website. Please note that the value specified here is
              not validated. Accepts any string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/companies",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "custom_attributes": custom_attributes,
                    "industry": industry,
                    "monthly_spend": monthly_spend,
                    "name": name,
                    "plan": plan,
                    "remote_created_at": remote_created_at,
                    "size": size,
                    "website": website,
                },
                company_create_update_params.CompanyCreateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )


class AsyncCompanies(AsyncAPIResource):
    contacts: AsyncContacts
    segments: AsyncSegments
    with_raw_response: AsyncCompaniesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.contacts = AsyncContacts(client)
        self.segments = AsyncSegments(client)
        self.with_raw_response = AsyncCompaniesWithRawResponse(self)

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
    ) -> Company:
        """
        You can fetch a single company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    async def update(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """
        You can update a single company

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
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
    ) -> DeletedCompanyObject:
        """
        You can delete a single company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedCompanyObject,
        )

    async def create_update(
        self,
        *,
        company_id: str | NotGiven = NOT_GIVEN,
        custom_attributes: Dict[str, str] | NotGiven = NOT_GIVEN,
        industry: str | NotGiven = NOT_GIVEN,
        monthly_spend: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        plan: str | NotGiven = NOT_GIVEN,
        remote_created_at: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        website: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """
        You can create or update a company.

        > 📘 Companies with no users
        >
        > Companies will be only visible in Intercom when there is at least one
        > associated user.

        Companies are looked up via `company_id` in a `POST` request, if not found via
        `company_id`, the new company will be created, if found, that company will be
        updated.

        Args:
          company_id: The company id you have defined for the company. Can't be updated

          custom_attributes: A hash of key/value pairs containing any other data about the company you want
              Intercom to store.

          industry: The industry that this company operates in.

          monthly_spend: How much revenue the company generates for your business. Note that this will
              truncate floats. i.e. it only allow for whole integers, 155.98 will be truncated
              to 155. Note that this has an upper limit of 2\\**\\**31-1 or 2147483647..

          name: The name of the Company

          plan: The name of the plan you have associated with the company.

          remote_created_at: The time the company was created by you.

          size: The number of employees in this company.

          website: The URL for this company's website. Please note that the value specified here is
              not validated. Accepts any string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/companies",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "custom_attributes": custom_attributes,
                    "industry": industry,
                    "monthly_spend": monthly_spend,
                    "name": name,
                    "plan": plan,
                    "remote_created_at": remote_created_at,
                    "size": size,
                    "website": website,
                },
                company_create_update_params.CompanyCreateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )


class CompaniesWithRawResponse:
    def __init__(self, companies: Companies) -> None:
        self.contacts = ContactsWithRawResponse(companies.contacts)
        self.segments = SegmentsWithRawResponse(companies.segments)

        self.retrieve = to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            companies.update,
        )
        self.delete = to_raw_response_wrapper(
            companies.delete,
        )
        self.create_update = to_raw_response_wrapper(
            companies.create_update,
        )


class AsyncCompaniesWithRawResponse:
    def __init__(self, companies: AsyncCompanies) -> None:
        self.contacts = AsyncContactsWithRawResponse(companies.contacts)
        self.segments = AsyncSegmentsWithRawResponse(companies.segments)

        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            companies.update,
        )
        self.delete = async_to_raw_response_wrapper(
            companies.delete,
        )
        self.create_update = async_to_raw_response_wrapper(
            companies.create_update,
        )
