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
    def test_method_retrieve(self, client: Intercom) -> None:
        tag = client.tags.retrieve(
            id="123",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        tag = client.tags.retrieve(
            id="123",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.tags.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tags.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        tag = client.tags.list()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        tag = client.tags.list(
            intercom_version="2.11",
        )
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagList, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        tag = client.tags.delete(
            id="123",
        )
        assert tag is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Intercom) -> None:
        tag = client.tags.delete(
            id="123",
            intercom_version="2.11",
        )
        assert tag is None

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @parametrize
    def test_streaming_response_delete(self, client: Intercom) -> None:
        with client.tags.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tags.with_raw_response.delete(
                id="",
            )

    @parametrize
    def test_method_create_or_update_overload_1(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params_overload_1(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            name="Independent",
            id="656452352",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create_or_update_overload_1(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.create_or_update(
            name="Independent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update_overload_1(self, client: Intercom) -> None:
        with client.tags.with_streaming_response.create_or_update(
            name="Independent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_or_update_overload_2(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params_overload_2(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            companies=[
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                },
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                },
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                },
            ],
            name="Independent",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create_or_update_overload_2(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update_overload_2(self, client: Intercom) -> None:
        with client.tags.with_streaming_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_or_update_overload_3(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params_overload_3(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            companies=[
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                    "untag": True,
                },
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                    "untag": True,
                },
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                    "untag": True,
                },
            ],
            name="Independent",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create_or_update_overload_3(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update_overload_3(self, client: Intercom) -> None:
        with client.tags.with_streaming_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_or_update_overload_4(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params_overload_4(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            name="Independent",
            users=[
                {"id": "5f7f0d217289f8d2f4262080"},
                {"id": "5f7f0d217289f8d2f4262080"},
                {"id": "5f7f0d217289f8d2f4262080"},
            ],
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create_or_update_overload_4(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update_overload_4(self, client: Intercom) -> None:
        with client.tags.with_streaming_response.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.retrieve(
            id="123",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.retrieve(
            id="123",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tags.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.tags.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tags.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.list()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.list(
            intercom_version="2.11",
        )
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagList, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.delete(
            id="123",
        )
        assert tag is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.delete(
            id="123",
            intercom_version="2.11",
        )
        assert tag is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tags.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncIntercom) -> None:
        async with async_client.tags.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tags.with_raw_response.delete(
                id="",
            )

    @parametrize
    async def test_method_create_or_update_overload_1(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.create_or_update(
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params_overload_1(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.create_or_update(
            name="Independent",
            id="656452352",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tags.with_raw_response.create_or_update(
            name="Independent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update_overload_1(self, async_client: AsyncIntercom) -> None:
        async with async_client.tags.with_streaming_response.create_or_update(
            name="Independent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_or_update_overload_2(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params_overload_2(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.create_or_update(
            companies=[
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                },
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                },
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                },
            ],
            name="Independent",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tags.with_raw_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update_overload_2(self, async_client: AsyncIntercom) -> None:
        async with async_client.tags.with_streaming_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_or_update_overload_3(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params_overload_3(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.create_or_update(
            companies=[
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                    "untag": True,
                },
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                    "untag": True,
                },
                {
                    "id": "531ee472cce572a6ec000006",
                    "company_id": "6",
                    "untag": True,
                },
            ],
            name="Independent",
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update_overload_3(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tags.with_raw_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update_overload_3(self, async_client: AsyncIntercom) -> None:
        async with async_client.tags.with_streaming_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_or_update_overload_4(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params_overload_4(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tags.create_or_update(
            name="Independent",
            users=[
                {"id": "5f7f0d217289f8d2f4262080"},
                {"id": "5f7f0d217289f8d2f4262080"},
                {"id": "5f7f0d217289f8d2f4262080"},
            ],
            intercom_version="2.11",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update_overload_4(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tags.with_raw_response.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update_overload_4(self, async_client: AsyncIntercom) -> None:
        async with async_client.tags.with_streaming_response.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True
