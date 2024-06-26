# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_minus_intercom import Intercom, AsyncIntercom
from python_minus_intercom.types.help_center import HelpCenter, HelpCenterList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHelpCenters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        help_center = client.help_center.help_centers.retrieve(
            0,
        )
        assert_matches_type(HelpCenter, help_center, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        help_center = client.help_center.help_centers.retrieve(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(HelpCenter, help_center, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.help_center.help_centers.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        help_center = response.parse()
        assert_matches_type(HelpCenter, help_center, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.help_center.help_centers.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            help_center = response.parse()
            assert_matches_type(HelpCenter, help_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        help_center = client.help_center.help_centers.list()
        assert_matches_type(HelpCenterList, help_center, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        help_center = client.help_center.help_centers.list(
            intercom_version="2.11",
        )
        assert_matches_type(HelpCenterList, help_center, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.help_center.help_centers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        help_center = response.parse()
        assert_matches_type(HelpCenterList, help_center, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.help_center.help_centers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            help_center = response.parse()
            assert_matches_type(HelpCenterList, help_center, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHelpCenters:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        help_center = await async_client.help_center.help_centers.retrieve(
            0,
        )
        assert_matches_type(HelpCenter, help_center, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        help_center = await async_client.help_center.help_centers.retrieve(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(HelpCenter, help_center, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.help_center.help_centers.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        help_center = await response.parse()
        assert_matches_type(HelpCenter, help_center, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.help_center.help_centers.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            help_center = await response.parse()
            assert_matches_type(HelpCenter, help_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        help_center = await async_client.help_center.help_centers.list()
        assert_matches_type(HelpCenterList, help_center, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        help_center = await async_client.help_center.help_centers.list(
            intercom_version="2.11",
        )
        assert_matches_type(HelpCenterList, help_center, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.help_center.help_centers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        help_center = await response.parse()
        assert_matches_type(HelpCenterList, help_center, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.help_center.help_centers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            help_center = await response.parse()
            assert_matches_type(HelpCenterList, help_center, path=["response"])

        assert cast(Any, response.is_closed) is True
