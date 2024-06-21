# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import Visitor
from intercom.types.shared import Contact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVisitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        visitor = client.visitors.retrieve(
            user_id="string",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        visitor = client.visitors.retrieve(
            user_id="string",
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.retrieve(
            user_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.visitors.with_streaming_response.retrieve(
            user_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor = response.parse()
            assert_matches_type(Optional[Visitor], visitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_1(self, client: Intercom) -> None:
        visitor = client.visitors.update(
            body={},
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Intercom) -> None:
        visitor = client.visitors.update(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.update(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Intercom) -> None:
        with client.visitors.with_streaming_response.update(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor = response.parse()
            assert_matches_type(Optional[Visitor], visitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_2(self, client: Intercom) -> None:
        visitor = client.visitors.update(
            body={},
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Intercom) -> None:
        visitor = client.visitors.update(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.update(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Intercom) -> None:
        with client.visitors.with_streaming_response.update(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor = response.parse()
            assert_matches_type(Optional[Visitor], visitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_convert(self, client: Intercom) -> None:
        visitor = client.visitors.convert(
            type="user",
            user={},
            visitor={},
        )
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    def test_method_convert_with_all_params(self, client: Intercom) -> None:
        visitor = client.visitors.convert(
            type="user",
            user={
                "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "user_id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "email": "foo@bar.com",
            },
            visitor={
                "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "user_id": "3ecf64d0-9ed1-4e9f-88e1-da7d6e6782f3",
                "email": "winstonsmith@truth.org",
            },
            intercom_version="2.11",
        )
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    def test_raw_response_convert(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.convert(
            type="user",
            user={},
            visitor={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    def test_streaming_response_convert(self, client: Intercom) -> None:
        with client.visitors.with_streaming_response.convert(
            type="user",
            user={},
            visitor={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor = response.parse()
            assert_matches_type(Contact, visitor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVisitors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        visitor = await async_client.visitors.retrieve(
            user_id="string",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        visitor = await async_client.visitors.retrieve(
            user_id="string",
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.visitors.with_raw_response.retrieve(
            user_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = await response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.visitors.with_streaming_response.retrieve(
            user_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor = await response.parse()
            assert_matches_type(Optional[Visitor], visitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncIntercom) -> None:
        visitor = await async_client.visitors.update(
            body={},
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncIntercom) -> None:
        visitor = await async_client.visitors.update(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.visitors.with_raw_response.update(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = await response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncIntercom) -> None:
        async with async_client.visitors.with_streaming_response.update(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor = await response.parse()
            assert_matches_type(Optional[Visitor], visitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncIntercom) -> None:
        visitor = await async_client.visitors.update(
            body={},
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncIntercom) -> None:
        visitor = await async_client.visitors.update(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.visitors.with_raw_response.update(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = await response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncIntercom) -> None:
        async with async_client.visitors.with_streaming_response.update(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor = await response.parse()
            assert_matches_type(Optional[Visitor], visitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_convert(self, async_client: AsyncIntercom) -> None:
        visitor = await async_client.visitors.convert(
            type="user",
            user={},
            visitor={},
        )
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    async def test_method_convert_with_all_params(self, async_client: AsyncIntercom) -> None:
        visitor = await async_client.visitors.convert(
            type="user",
            user={
                "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "user_id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "email": "foo@bar.com",
            },
            visitor={
                "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "user_id": "3ecf64d0-9ed1-4e9f-88e1-da7d6e6782f3",
                "email": "winstonsmith@truth.org",
            },
            intercom_version="2.11",
        )
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    async def test_raw_response_convert(self, async_client: AsyncIntercom) -> None:
        response = await async_client.visitors.with_raw_response.convert(
            type="user",
            user={},
            visitor={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = await response.parse()
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    async def test_streaming_response_convert(self, async_client: AsyncIntercom) -> None:
        async with async_client.visitors.with_streaming_response.convert(
            type="user",
            user={},
            visitor={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor = await response.parse()
            assert_matches_type(Contact, visitor, path=["response"])

        assert cast(Any, response.is_closed) is True
