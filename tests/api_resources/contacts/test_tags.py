# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types.shared import Tag, TagList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        tag = client.contacts.tags.create(
            contact_id="63a07ddf05a32042dffac965",
            id="id",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        tag = client.contacts.tags.create(
            contact_id="63a07ddf05a32042dffac965",
            id="id",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.contacts.tags.with_raw_response.create(
            contact_id="63a07ddf05a32042dffac965",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.contacts.tags.with_streaming_response.create(
            contact_id="63a07ddf05a32042dffac965",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.tags.with_raw_response.create(
                contact_id="",
                id="id",
            )

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        tag = client.contacts.tags.list(
            contact_id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        tag = client.contacts.tags.list(
            contact_id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.contacts.tags.with_raw_response.list(
            contact_id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.contacts.tags.with_streaming_response.list(
            contact_id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagList, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.tags.with_raw_response.list(
                contact_id="",
            )

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        tag = client.contacts.tags.delete(
            id="7522907",
            contact_id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Intercom) -> None:
        tag = client.contacts.tags.delete(
            id="7522907",
            contact_id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.contacts.tags.with_raw_response.delete(
            id="7522907",
            contact_id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Intercom) -> None:
        with client.contacts.tags.with_streaming_response.delete(
            id="7522907",
            contact_id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.tags.with_raw_response.delete(
                id="7522907",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.tags.with_raw_response.delete(
                id="",
                contact_id="63a07ddf05a32042dffac965",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.contacts.tags.create(
            contact_id="63a07ddf05a32042dffac965",
            id="id",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.contacts.tags.create(
            contact_id="63a07ddf05a32042dffac965",
            id="id",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.tags.with_raw_response.create(
            contact_id="63a07ddf05a32042dffac965",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.tags.with_streaming_response.create(
            contact_id="63a07ddf05a32042dffac965",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.tags.with_raw_response.create(
                contact_id="",
                id="id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.contacts.tags.list(
            contact_id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.contacts.tags.list(
            contact_id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.tags.with_raw_response.list(
            contact_id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.tags.with_streaming_response.list(
            contact_id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagList, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.tags.with_raw_response.list(
                contact_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.contacts.tags.delete(
            id="7522907",
            contact_id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.contacts.tags.delete(
            id="7522907",
            contact_id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.tags.with_raw_response.delete(
            id="7522907",
            contact_id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.tags.with_streaming_response.delete(
            id="7522907",
            contact_id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.tags.with_raw_response.delete(
                id="7522907",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.tags.with_raw_response.delete(
                id="",
                contact_id="63a07ddf05a32042dffac965",
            )
