# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_minus_intercom import Intercom, AsyncIntercom
from python_minus_intercom.types.help_center import (
    Collection,
    CollectionList,
    DeletedCollection,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        collection = client.help_center.collections.create(
            name="Thanks for everything",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        collection = client.help_center.collections.create(
            name="Thanks for everything",
            description="English description",
            help_center_id=0,
            parent_id="6871118",
            translated_content={
                "type": "group_translated_content",
                "ar": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bg": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ca": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "cs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "da": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "de": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "el": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "en": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "es": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "et": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "he": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hu": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "id": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "it": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ja": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ko": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "mn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nb": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ro": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ru": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "tr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "vi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt_br": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_cn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_tw": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
            },
            intercom_version="2.11",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.create(
            name="Thanks for everything",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.help_center.collections.with_streaming_response.create(
            name="Thanks for everything",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        collection = client.help_center.collections.retrieve(
            0,
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        collection = client.help_center.collections.retrieve(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.help_center.collections.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        collection = client.help_center.collections.update(
            0,
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        collection = client.help_center.collections.update(
            0,
            description="English description",
            name="Update collection name",
            parent_id="6871118",
            translated_content={
                "type": "group_translated_content",
                "ar": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bg": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ca": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "cs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "da": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "de": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "el": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "en": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "es": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "et": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "he": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hu": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "id": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "it": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ja": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ko": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "mn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nb": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ro": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ru": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "tr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "vi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt_br": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_cn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_tw": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
            },
            intercom_version="2.11",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.help_center.collections.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        collection = client.help_center.collections.list()
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        collection = client.help_center.collections.list(
            intercom_version="2.11",
        )
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.help_center.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionList, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        collection = client.help_center.collections.delete(
            0,
        )
        assert_matches_type(DeletedCollection, collection, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Intercom) -> None:
        collection = client.help_center.collections.delete(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(DeletedCollection, collection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(DeletedCollection, collection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Intercom) -> None:
        with client.help_center.collections.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(DeletedCollection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.create(
            name="Thanks for everything",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.create(
            name="Thanks for everything",
            description="English description",
            help_center_id=0,
            parent_id="6871118",
            translated_content={
                "type": "group_translated_content",
                "ar": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bg": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ca": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "cs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "da": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "de": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "el": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "en": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "es": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "et": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "he": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hu": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "id": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "it": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ja": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ko": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "mn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nb": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ro": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ru": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "tr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "vi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt_br": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_cn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_tw": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
            },
            intercom_version="2.11",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.help_center.collections.with_raw_response.create(
            name="Thanks for everything",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.help_center.collections.with_streaming_response.create(
            name="Thanks for everything",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.retrieve(
            0,
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.retrieve(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.help_center.collections.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.help_center.collections.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.update(
            0,
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.update(
            0,
            description="English description",
            name="Update collection name",
            parent_id="6871118",
            translated_content={
                "type": "group_translated_content",
                "ar": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bg": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ca": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "cs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "da": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "de": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "el": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "en": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "es": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "et": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "he": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hu": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "id": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "it": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ja": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ko": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "mn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nb": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ro": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ru": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "tr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "vi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt_br": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_cn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_tw": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
            },
            intercom_version="2.11",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.help_center.collections.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.help_center.collections.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.list()
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.list(
            intercom_version="2.11",
        )
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.help_center.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.help_center.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionList, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.delete(
            0,
        )
        assert_matches_type(DeletedCollection, collection, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncIntercom) -> None:
        collection = await async_client.help_center.collections.delete(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(DeletedCollection, collection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncIntercom) -> None:
        response = await async_client.help_center.collections.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(DeletedCollection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncIntercom) -> None:
        async with async_client.help_center.collections.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(DeletedCollection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True
