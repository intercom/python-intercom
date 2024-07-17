# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    company_list_params,
    company_create_params,
    company_scroll_params,
    company_retrieve_list_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
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
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.company_list import CompanyList
from ...types.company_scroll import CompanyScroll
from ...types.shared.company import Company
from ...types.deleted_company_object import DeletedCompanyObject

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    @cached_property
    def segments(self) -> SegmentsResource:
        return SegmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self)

    def create(
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
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """
        You can create or update a company.

        Companies will be only visible in Intercom when there is at least one associated
        user.

        Companies are looked up via `company_id` in a `POST` request, if not found via
        `company_id`, the new company will be created, if found, that company will be
        updated.

        {% admonition type="attention" name="Using `company_id`" %} You can set a unique
        `company_id` value when creating a company. However, it is not possible to
        update `company_id`. Be sure to set a unique value once upon creation of the
        company. {% /admonition %}

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

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def retrieve(
        self,
        id: str,
        *,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
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
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """
        You can update a single company using the Intercom provisioned `id`.

        {% admonition type="attention" name="Using `company_id`" %} When updating a
        company it is not possible to update `company_id`. This can only be set once
        upon creation of the company. {% /admonition %}

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._put(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def list(
        self,
        *,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyList:
        """You can list companies.

        The company list is sorted by the `last_request_at`
        field and by default is ordered descending, most recently requested first.

        Note that the API does not include companies who have no associated users in
        list responses.

        When using the Companies endpoint and the pages object to iterate through the
        returned companies, there is a limit of 10,000 Companies that can be returned.
        If you need to list or iterate on more than 10,000 Companies, please use the
        [Scroll API](https://developers.intercom.com/reference#iterating-over-all-companies).
        {% admonition type="warning" name="Pagination" %} You can use pagination to
        limit the number of results returned. The default is `20` results per page. See
        the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis)
        for more details on how to use the `starting_after` param. {% /admonition %}

        Args:
          order: `asc` or `desc`. Return the companies in ascending or descending order. Defaults
              to desc

          page: The page of results to fetch. Defaults to first page

          per_page: How many results to return per page. Defaults to 15

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._post(
            "/companies/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=CompanyList,
        )

    def delete(
        self,
        id: str,
        *,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
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
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._delete(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedCompanyObject,
        )

    def retrieve_list(
        self,
        *,
        company_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        segment_id: str | NotGiven = NOT_GIVEN,
        tag_id: str | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyList:
        """
        You can fetch a single company by passing in `company_id` or `name`.

        `https://api.intercom.io/companies?name={name}`

        `https://api.intercom.io/companies?company_id={company_id}`

        You can fetch all companies and filter by `segment_id` or `tag_id` as a query
        parameter.

        `https://api.intercom.io/companies?tag_id={tag_id}`

        `https://api.intercom.io/companies?segment_id={segment_id}`

        Args:
          company_id: The `company_id` of the company to filter by.

          name: The `name` of the company to filter by.

          page: The page of results to fetch. Defaults to first page

          per_page: How many results to display per page. Defaults to 15

          segment_id: The `segment_id` of the company to filter by.

          tag_id: The `tag_id` of the company to filter by.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._get(
            "/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "segment_id": segment_id,
                        "tag_id": tag_id,
                    },
                    company_retrieve_list_params.CompanyRetrieveListParams,
                ),
            ),
            cast_to=CompanyList,
        )

    def scroll(
        self,
        *,
        scroll_param: str | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CompanyScroll]:
        """
        The `list all companies` functionality does not work well for huge datasets, and can result in errors and performance problems when paging deeply. The Scroll API provides an efficient mechanism for iterating over all companies in a dataset.

        - Each app can only have 1 scroll open at a time. You'll get an error message if
          you try to have more than one open per app.
        - If the scroll isn't used for 1 minute, it expires and calls with that scroll
          param will fail
        - If the end of the scroll is reached, "companies" will be empty and the scroll
          parameter will expire

        {% admonition type="info" name="Scroll Parameter" %} You can get the first page
        of companies by simply sending a GET request to the scroll endpoint. For
        subsequent requests you will need to use the scroll parameter from the response.
        {% /admonition %} {% admonition type="danger" name="Scroll network timeouts" %}
        Since scroll is often used on large datasets network errors such as timeouts can
        be encountered. When this occurs you will see a HTTP 500 error with the
        following message: "Request failed due to an internal network error. Please
        restart the scroll operation." If this happens, you will need to restart your
        scroll query: It is not possible to continue from a specific point when using
        scroll. {% /admonition %}

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._get(
            "/companies/scroll",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"scroll_param": scroll_param}, company_scroll_params.CompanyScrollParams),
            ),
            cast_to=CompanyScroll,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def contacts(self) -> AsyncContactsResource:
        return AsyncContactsResource(self._client)

    @cached_property
    def segments(self) -> AsyncSegmentsResource:
        return AsyncSegmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def create(
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
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """
        You can create or update a company.

        Companies will be only visible in Intercom when there is at least one associated
        user.

        Companies are looked up via `company_id` in a `POST` request, if not found via
        `company_id`, the new company will be created, if found, that company will be
        updated.

        {% admonition type="attention" name="Using `company_id`" %} You can set a unique
        `company_id` value when creating a company. However, it is not possible to
        update `company_id`. Be sure to set a unique value once upon creation of the
        company. {% /admonition %}

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

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/companies",
            body=await async_maybe_transform(
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
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    async def retrieve(
        self,
        id: str,
        *,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
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
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """
        You can update a single company using the Intercom provisioned `id`.

        {% admonition type="attention" name="Using `company_id`" %} When updating a
        company it is not possible to update `company_id`. This can only be set once
        upon creation of the company. {% /admonition %}

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._put(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    async def list(
        self,
        *,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyList:
        """You can list companies.

        The company list is sorted by the `last_request_at`
        field and by default is ordered descending, most recently requested first.

        Note that the API does not include companies who have no associated users in
        list responses.

        When using the Companies endpoint and the pages object to iterate through the
        returned companies, there is a limit of 10,000 Companies that can be returned.
        If you need to list or iterate on more than 10,000 Companies, please use the
        [Scroll API](https://developers.intercom.com/reference#iterating-over-all-companies).
        {% admonition type="warning" name="Pagination" %} You can use pagination to
        limit the number of results returned. The default is `20` results per page. See
        the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis)
        for more details on how to use the `starting_after` param. {% /admonition %}

        Args:
          order: `asc` or `desc`. Return the companies in ascending or descending order. Defaults
              to desc

          page: The page of results to fetch. Defaults to first page

          per_page: How many results to return per page. Defaults to 15

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/companies/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=CompanyList,
        )

    async def delete(
        self,
        id: str,
        *,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
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
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._delete(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedCompanyObject,
        )

    async def retrieve_list(
        self,
        *,
        company_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        segment_id: str | NotGiven = NOT_GIVEN,
        tag_id: str | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyList:
        """
        You can fetch a single company by passing in `company_id` or `name`.

        `https://api.intercom.io/companies?name={name}`

        `https://api.intercom.io/companies?company_id={company_id}`

        You can fetch all companies and filter by `segment_id` or `tag_id` as a query
        parameter.

        `https://api.intercom.io/companies?tag_id={tag_id}`

        `https://api.intercom.io/companies?segment_id={segment_id}`

        Args:
          company_id: The `company_id` of the company to filter by.

          name: The `name` of the company to filter by.

          page: The page of results to fetch. Defaults to first page

          per_page: How many results to display per page. Defaults to 15

          segment_id: The `segment_id` of the company to filter by.

          tag_id: The `tag_id` of the company to filter by.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "company_id": company_id,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "segment_id": segment_id,
                        "tag_id": tag_id,
                    },
                    company_retrieve_list_params.CompanyRetrieveListParams,
                ),
            ),
            cast_to=CompanyList,
        )

    async def scroll(
        self,
        *,
        scroll_param: str | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CompanyScroll]:
        """
        The `list all companies` functionality does not work well for huge datasets, and can result in errors and performance problems when paging deeply. The Scroll API provides an efficient mechanism for iterating over all companies in a dataset.

        - Each app can only have 1 scroll open at a time. You'll get an error message if
          you try to have more than one open per app.
        - If the scroll isn't used for 1 minute, it expires and calls with that scroll
          param will fail
        - If the end of the scroll is reached, "companies" will be empty and the scroll
          parameter will expire

        {% admonition type="info" name="Scroll Parameter" %} You can get the first page
        of companies by simply sending a GET request to the scroll endpoint. For
        subsequent requests you will need to use the scroll parameter from the response.
        {% /admonition %} {% admonition type="danger" name="Scroll network timeouts" %}
        Since scroll is often used on large datasets network errors such as timeouts can
        be encountered. When this occurs you will see a HTTP 500 error with the
        following message: "Request failed due to an internal network error. Please
        restart the scroll operation." If this happens, you will need to restart your
        scroll query: It is not possible to continue from a specific point when using
        scroll. {% /admonition %}

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/companies/scroll",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"scroll_param": scroll_param}, company_scroll_params.CompanyScrollParams
                ),
            ),
            cast_to=CompanyScroll,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            companies.update,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )
        self.delete = to_raw_response_wrapper(
            companies.delete,
        )
        self.retrieve_list = to_raw_response_wrapper(
            companies.retrieve_list,
        )
        self.scroll = to_raw_response_wrapper(
            companies.scroll,
        )

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self._companies.contacts)

    @cached_property
    def segments(self) -> SegmentsResourceWithRawResponse:
        return SegmentsResourceWithRawResponse(self._companies.segments)


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            companies.update,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            companies.delete,
        )
        self.retrieve_list = async_to_raw_response_wrapper(
            companies.retrieve_list,
        )
        self.scroll = async_to_raw_response_wrapper(
            companies.scroll,
        )

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self._companies.contacts)

    @cached_property
    def segments(self) -> AsyncSegmentsResourceWithRawResponse:
        return AsyncSegmentsResourceWithRawResponse(self._companies.segments)


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            companies.update,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )
        self.delete = to_streamed_response_wrapper(
            companies.delete,
        )
        self.retrieve_list = to_streamed_response_wrapper(
            companies.retrieve_list,
        )
        self.scroll = to_streamed_response_wrapper(
            companies.scroll,
        )

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self._companies.contacts)

    @cached_property
    def segments(self) -> SegmentsResourceWithStreamingResponse:
        return SegmentsResourceWithStreamingResponse(self._companies.segments)


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            companies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            companies.delete,
        )
        self.retrieve_list = async_to_streamed_response_wrapper(
            companies.retrieve_list,
        )
        self.scroll = async_to_streamed_response_wrapper(
            companies.scroll,
        )

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self._companies.contacts)

    @cached_property
    def segments(self) -> AsyncSegmentsResourceWithStreamingResponse:
        return AsyncSegmentsResourceWithStreamingResponse(self._companies.segments)
