# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import SubscriptionTypeList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestSubscriptionTypes:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        subscription_type = client.subscription_types.list()
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.subscription_types.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_type = response.parse()
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])


class TestAsyncSubscriptionTypes:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        subscription_type = await client.subscription_types.list()
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.subscription_types.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_type = response.parse()
        assert_matches_type(SubscriptionTypeList, subscription_type, path=["response"])
