# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.admins import ActivityLogList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestActivityLogs:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        activity_log = client.admins.activity_logs.list(
            created_at_after="string",
        )
        assert_matches_type(ActivityLogList, activity_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        activity_log = client.admins.activity_logs.list(
            created_at_after="string",
            created_at_before="string",
        )
        assert_matches_type(ActivityLogList, activity_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.admins.activity_logs.with_raw_response.list(
            created_at_after="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity_log = response.parse()
        assert_matches_type(ActivityLogList, activity_log, path=["response"])


class TestAsyncActivityLogs:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        activity_log = await client.admins.activity_logs.list(
            created_at_after="string",
        )
        assert_matches_type(ActivityLogList, activity_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIntercom) -> None:
        activity_log = await client.admins.activity_logs.list(
            created_at_after="string",
            created_at_before="string",
        )
        assert_matches_type(ActivityLogList, activity_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.admins.activity_logs.with_raw_response.list(
            created_at_after="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity_log = response.parse()
        assert_matches_type(ActivityLogList, activity_log, path=["response"])
