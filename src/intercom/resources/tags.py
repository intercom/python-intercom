# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, overload

import httpx

from ..types import tag_create_or_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import required_args, maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options
from ..types.shared import Tag, TagList

if TYPE_CHECKING:
    from .._client import Intercom, AsyncIntercom

__all__ = ["Tags", "AsyncTags"]


class Tags(SyncAPIResource):
    with_raw_response: TagsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = TagsWithRawResponse(self)

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
    ) -> Tag:
        """You can fetch the details of tags that are on the workspace by their id.

        This
        will return a tag object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TagList:
        """You can fetch a list of all tags for a given workspace."""
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
        companies: List[tag_create_or_update_params.TagCompanyRequestCompany],
        name: str,
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
        companies: List[tag_create_or_update_params.UntagCompanyRequestCompany],
        name: str,
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
        users: List[tag_create_or_update_params.TagMultipleUsersRequestUser],
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["companies", "name"], ["companies", "name"], ["name", "users"])
    def create_or_update(
        self,
        *,
        name: str,
        id: str | NotGiven = NOT_GIVEN,
        companies: List[tag_create_or_update_params.TagCompanyRequestCompany]
        | List[tag_create_or_update_params.UntagCompanyRequestCompany]
        | NotGiven = NOT_GIVEN,
        users: List[tag_create_or_update_params.TagMultipleUsersRequestUser] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tag:
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


class AsyncTags(AsyncAPIResource):
    with_raw_response: AsyncTagsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncTagsWithRawResponse(self)

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
    ) -> Tag:
        """You can fetch the details of tags that are on the workspace by their id.

        This
        will return a tag object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TagList:
        """You can fetch a list of all tags for a given workspace."""
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
        companies: List[tag_create_or_update_params.TagCompanyRequestCompany],
        name: str,
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
        companies: List[tag_create_or_update_params.UntagCompanyRequestCompany],
        name: str,
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
        users: List[tag_create_or_update_params.TagMultipleUsersRequestUser],
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["companies", "name"], ["companies", "name"], ["name", "users"])
    async def create_or_update(
        self,
        *,
        name: str,
        id: str | NotGiven = NOT_GIVEN,
        companies: List[tag_create_or_update_params.TagCompanyRequestCompany]
        | List[tag_create_or_update_params.UntagCompanyRequestCompany]
        | NotGiven = NOT_GIVEN,
        users: List[tag_create_or_update_params.TagMultipleUsersRequestUser] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tag:
        return await self._post(
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


class TagsWithRawResponse:
    def __init__(self, tags: Tags) -> None:
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


class AsyncTagsWithRawResponse:
    def __init__(self, tags: AsyncTags) -> None:
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
