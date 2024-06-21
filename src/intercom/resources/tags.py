# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, overload
from typing_extensions import Literal

import httpx

from ..types import tag_create_or_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    required_args,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.shared.tag import Tag
from ..types.shared.tag_list import TagList

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self)

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
    ) -> Tag:
        """You can fetch the details of tags that are on the workspace by their id.

        This
        will return a tag object.

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
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._get(
            f"/tags/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    def list(
        self,
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
    ) -> TagList:
        """
        You can fetch a list of all tags for a given workspace.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._get(
            "/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagList,
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
    ) -> None:
        """
        You can delete the details of tags that are on the workspace by passing in the
        id.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._delete(
            f"/tags/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    def create_or_update(
        self,
        *,
        name: str,
        id: str | NotGiven = NOT_GIVEN,
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
    ) -> Tag:
        """You can use this endpoint to perform the following operations:

        **1.

        Create a new tag:** You can create a new tag by passing in the tag name as
        specified in "Create or Update Tag Request Payload" described below.

        **2. Update an existing tag:** You can update an existing tag by passing the id
        of the tag as specified in "Create or Update Tag Request Payload" described
        below.

        **3. Tag Companies:** You can tag single company or a list of companies. You can
        tag a company by passing in the tag name and the company details as specified in
        "Tag Company Request Payload" described below. Also, if the tag doesn't exist
        then a new one will be created automatically.

        **4. Untag Companies:** You can untag a single company or a list of companies.
        You can untag a company by passing in the tag id and the company details as
        specified in "Untag Company Request Payload" described below.

        **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by
        passing in the tag name and the user details as specified in "Tag Users Request
        Payload" described below.

        Each operation will return a tag object.

        Args:
          name: The name of the tag, which will be created if not found, or the new name for the
              tag if this is an update request. Names are case insensitive.

          id: The id of tag to updates.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_or_update(
        self,
        *,
        companies: Iterable[tag_create_or_update_params.TagCompanyRequestCompany],
        name: str,
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
    ) -> Tag:
        """You can use this endpoint to perform the following operations:

        **1.

        Create a new tag:** You can create a new tag by passing in the tag name as
        specified in "Create or Update Tag Request Payload" described below.

        **2. Update an existing tag:** You can update an existing tag by passing the id
        of the tag as specified in "Create or Update Tag Request Payload" described
        below.

        **3. Tag Companies:** You can tag single company or a list of companies. You can
        tag a company by passing in the tag name and the company details as specified in
        "Tag Company Request Payload" described below. Also, if the tag doesn't exist
        then a new one will be created automatically.

        **4. Untag Companies:** You can untag a single company or a list of companies.
        You can untag a company by passing in the tag id and the company details as
        specified in "Untag Company Request Payload" described below.

        **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by
        passing in the tag name and the user details as specified in "Tag Users Request
        Payload" described below.

        Each operation will return a tag object.

        Args:
          companies: The id or company_id of the company can be passed as input parameters.

          name: The name of the tag, which will be created if not found.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_or_update(
        self,
        *,
        companies: Iterable[tag_create_or_update_params.UntagCompanyRequestCompany],
        name: str,
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
    ) -> Tag:
        """You can use this endpoint to perform the following operations:

        **1.

        Create a new tag:** You can create a new tag by passing in the tag name as
        specified in "Create or Update Tag Request Payload" described below.

        **2. Update an existing tag:** You can update an existing tag by passing the id
        of the tag as specified in "Create or Update Tag Request Payload" described
        below.

        **3. Tag Companies:** You can tag single company or a list of companies. You can
        tag a company by passing in the tag name and the company details as specified in
        "Tag Company Request Payload" described below. Also, if the tag doesn't exist
        then a new one will be created automatically.

        **4. Untag Companies:** You can untag a single company or a list of companies.
        You can untag a company by passing in the tag id and the company details as
        specified in "Untag Company Request Payload" described below.

        **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by
        passing in the tag name and the user details as specified in "Tag Users Request
        Payload" described below.

        Each operation will return a tag object.

        Args:
          companies: The id or company_id of the company can be passed as input parameters.

          name: The name of the tag which will be untagged from the company

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_or_update(
        self,
        *,
        name: str,
        users: Iterable[tag_create_or_update_params.TagMultipleUsersRequestUser],
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
    ) -> Tag:
        """You can use this endpoint to perform the following operations:

        **1.

        Create a new tag:** You can create a new tag by passing in the tag name as
        specified in "Create or Update Tag Request Payload" described below.

        **2. Update an existing tag:** You can update an existing tag by passing the id
        of the tag as specified in "Create or Update Tag Request Payload" described
        below.

        **3. Tag Companies:** You can tag single company or a list of companies. You can
        tag a company by passing in the tag name and the company details as specified in
        "Tag Company Request Payload" described below. Also, if the tag doesn't exist
        then a new one will be created automatically.

        **4. Untag Companies:** You can untag a single company or a list of companies.
        You can untag a company by passing in the tag id and the company details as
        specified in "Untag Company Request Payload" described below.

        **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by
        passing in the tag name and the user details as specified in "Tag Users Request
        Payload" described below.

        Each operation will return a tag object.

        Args:
          name: The name of the tag, which will be created if not found.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["companies", "name"], ["name", "users"])
    def create_or_update(
        self,
        *,
        name: str,
        id: str | NotGiven = NOT_GIVEN,
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
        companies: Iterable[tag_create_or_update_params.TagCompanyRequestCompany]
        | Iterable[tag_create_or_update_params.UntagCompanyRequestCompany]
        | NotGiven = NOT_GIVEN,
        users: Iterable[tag_create_or_update_params.TagMultipleUsersRequestUser] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tag:
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._post(
            "/tags",
            body=maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "companies": companies,
                    "users": users,
                },
                tag_create_or_update_params.TagCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )


class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self)

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
    ) -> Tag:
        """You can fetch the details of tags that are on the workspace by their id.

        This
        will return a tag object.

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
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._get(
            f"/tags/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    async def list(
        self,
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
    ) -> TagList:
        """
        You can fetch a list of all tags for a given workspace.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._get(
            "/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagList,
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
    ) -> None:
        """
        You can delete the details of tags that are on the workspace by passing in the
        id.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._delete(
            f"/tags/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    async def create_or_update(
        self,
        *,
        name: str,
        id: str | NotGiven = NOT_GIVEN,
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
    ) -> Tag:
        """You can use this endpoint to perform the following operations:

        **1.

        Create a new tag:** You can create a new tag by passing in the tag name as
        specified in "Create or Update Tag Request Payload" described below.

        **2. Update an existing tag:** You can update an existing tag by passing the id
        of the tag as specified in "Create or Update Tag Request Payload" described
        below.

        **3. Tag Companies:** You can tag single company or a list of companies. You can
        tag a company by passing in the tag name and the company details as specified in
        "Tag Company Request Payload" described below. Also, if the tag doesn't exist
        then a new one will be created automatically.

        **4. Untag Companies:** You can untag a single company or a list of companies.
        You can untag a company by passing in the tag id and the company details as
        specified in "Untag Company Request Payload" described below.

        **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by
        passing in the tag name and the user details as specified in "Tag Users Request
        Payload" described below.

        Each operation will return a tag object.

        Args:
          name: The name of the tag, which will be created if not found, or the new name for the
              tag if this is an update request. Names are case insensitive.

          id: The id of tag to updates.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_or_update(
        self,
        *,
        companies: Iterable[tag_create_or_update_params.TagCompanyRequestCompany],
        name: str,
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
    ) -> Tag:
        """You can use this endpoint to perform the following operations:

        **1.

        Create a new tag:** You can create a new tag by passing in the tag name as
        specified in "Create or Update Tag Request Payload" described below.

        **2. Update an existing tag:** You can update an existing tag by passing the id
        of the tag as specified in "Create or Update Tag Request Payload" described
        below.

        **3. Tag Companies:** You can tag single company or a list of companies. You can
        tag a company by passing in the tag name and the company details as specified in
        "Tag Company Request Payload" described below. Also, if the tag doesn't exist
        then a new one will be created automatically.

        **4. Untag Companies:** You can untag a single company or a list of companies.
        You can untag a company by passing in the tag id and the company details as
        specified in "Untag Company Request Payload" described below.

        **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by
        passing in the tag name and the user details as specified in "Tag Users Request
        Payload" described below.

        Each operation will return a tag object.

        Args:
          companies: The id or company_id of the company can be passed as input parameters.

          name: The name of the tag, which will be created if not found.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_or_update(
        self,
        *,
        companies: Iterable[tag_create_or_update_params.UntagCompanyRequestCompany],
        name: str,
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
    ) -> Tag:
        """You can use this endpoint to perform the following operations:

        **1.

        Create a new tag:** You can create a new tag by passing in the tag name as
        specified in "Create or Update Tag Request Payload" described below.

        **2. Update an existing tag:** You can update an existing tag by passing the id
        of the tag as specified in "Create or Update Tag Request Payload" described
        below.

        **3. Tag Companies:** You can tag single company or a list of companies. You can
        tag a company by passing in the tag name and the company details as specified in
        "Tag Company Request Payload" described below. Also, if the tag doesn't exist
        then a new one will be created automatically.

        **4. Untag Companies:** You can untag a single company or a list of companies.
        You can untag a company by passing in the tag id and the company details as
        specified in "Untag Company Request Payload" described below.

        **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by
        passing in the tag name and the user details as specified in "Tag Users Request
        Payload" described below.

        Each operation will return a tag object.

        Args:
          companies: The id or company_id of the company can be passed as input parameters.

          name: The name of the tag which will be untagged from the company

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_or_update(
        self,
        *,
        name: str,
        users: Iterable[tag_create_or_update_params.TagMultipleUsersRequestUser],
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
    ) -> Tag:
        """You can use this endpoint to perform the following operations:

        **1.

        Create a new tag:** You can create a new tag by passing in the tag name as
        specified in "Create or Update Tag Request Payload" described below.

        **2. Update an existing tag:** You can update an existing tag by passing the id
        of the tag as specified in "Create or Update Tag Request Payload" described
        below.

        **3. Tag Companies:** You can tag single company or a list of companies. You can
        tag a company by passing in the tag name and the company details as specified in
        "Tag Company Request Payload" described below. Also, if the tag doesn't exist
        then a new one will be created automatically.

        **4. Untag Companies:** You can untag a single company or a list of companies.
        You can untag a company by passing in the tag id and the company details as
        specified in "Untag Company Request Payload" described below.

        **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by
        passing in the tag name and the user details as specified in "Tag Users Request
        Payload" described below.

        Each operation will return a tag object.

        Args:
          name: The name of the tag, which will be created if not found.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["companies", "name"], ["name", "users"])
    async def create_or_update(
        self,
        *,
        name: str,
        id: str | NotGiven = NOT_GIVEN,
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
        companies: Iterable[tag_create_or_update_params.TagCompanyRequestCompany]
        | Iterable[tag_create_or_update_params.UntagCompanyRequestCompany]
        | NotGiven = NOT_GIVEN,
        users: Iterable[tag_create_or_update_params.TagMultipleUsersRequestUser] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tag:
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            "/tags",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "companies": companies,
                    "users": users,
                },
                tag_create_or_update_params.TagCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.retrieve = to_raw_response_wrapper(
            tags.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tags.list,
        )
        self.delete = to_raw_response_wrapper(
            tags.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            tags.create_or_update,
        )


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.retrieve = async_to_raw_response_wrapper(
            tags.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tags.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tags.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            tags.create_or_update,
        )


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.retrieve = to_streamed_response_wrapper(
            tags.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tags.list,
        )
        self.delete = to_streamed_response_wrapper(
            tags.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            tags.create_or_update,
        )


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.retrieve = async_to_streamed_response_wrapper(
            tags.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tags.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tags.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            tags.create_or_update,
        )
