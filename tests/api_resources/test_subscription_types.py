# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types.shared import SubscriptionTypeList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptionTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        subscription_type = client.subscription_types.list()
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        subscription_type = client.subscription_types.list(
            intercom_version="2.11",
        )
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.subscription_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_type = response.parse()
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.subscription_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription_type = response.parse()
            assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscriptionTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        subscription_type = await async_client.subscription_types.list()
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        subscription_type = await async_client.subscription_types.list(
            intercom_version="2.11",
        )
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.subscription_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_type = await response.parse()
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.subscription_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription_type = await response.parse()
            assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

        assert cast(Any, response.is_closed) is True
