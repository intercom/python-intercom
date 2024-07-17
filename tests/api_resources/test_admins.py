# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types import AdminList
from python_intercom.types.shared import Admin

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        admin = client.admins.retrieve(
            id=123,
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        admin = client.admins.retrieve(
            id=123,
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.admins.with_raw_response.retrieve(
            id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.admins.with_streaming_response.retrieve(
            id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(Optional[Admin], admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        admin = client.admins.list()
        assert_matches_type(AdminList, admin, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        admin = client.admins.list(
            intercom_version="2.11",
        )
        assert_matches_type(AdminList, admin, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.admins.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminList, admin, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.admins.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminList, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_away(self, client: Intercom) -> None:
        admin = client.admins.set_away(
            id=0,
            away_mode_enabled=True,
            away_mode_reassign=True,
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    def test_method_set_away_with_all_params(self, client: Intercom) -> None:
        admin = client.admins.set_away(
            id=0,
            away_mode_enabled=True,
            away_mode_reassign=True,
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    def test_raw_response_set_away(self, client: Intercom) -> None:
        response = client.admins.with_raw_response.set_away(
            id=0,
            away_mode_enabled=True,
            away_mode_reassign=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    def test_streaming_response_set_away(self, client: Intercom) -> None:
        with client.admins.with_streaming_response.set_away(
            id=0,
            away_mode_enabled=True,
            away_mode_reassign=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(Optional[Admin], admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmins:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        admin = await async_client.admins.retrieve(
            id=123,
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        admin = await async_client.admins.retrieve(
            id=123,
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.admins.with_raw_response.retrieve(
            id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.admins.with_streaming_response.retrieve(
            id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(Optional[Admin], admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        admin = await async_client.admins.list()
        assert_matches_type(AdminList, admin, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        admin = await async_client.admins.list(
            intercom_version="2.11",
        )
        assert_matches_type(AdminList, admin, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.admins.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminList, admin, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.admins.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminList, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_away(self, async_client: AsyncIntercom) -> None:
        admin = await async_client.admins.set_away(
            id=0,
            away_mode_enabled=True,
            away_mode_reassign=True,
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    async def test_method_set_away_with_all_params(self, async_client: AsyncIntercom) -> None:
        admin = await async_client.admins.set_away(
            id=0,
            away_mode_enabled=True,
            away_mode_reassign=True,
            intercom_version="2.11",
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    async def test_raw_response_set_away(self, async_client: AsyncIntercom) -> None:
        response = await async_client.admins.with_raw_response.set_away(
            id=0,
            away_mode_enabled=True,
            away_mode_reassign=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    async def test_streaming_response_set_away(self, async_client: AsyncIntercom) -> None:
        async with async_client.admins.with_streaming_response.set_away(
            id=0,
            away_mode_enabled=True,
            away_mode_reassign=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(Optional[Admin], admin, path=["response"])

        assert cast(Any, response.is_closed) is True
