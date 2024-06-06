# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types.admins import ActivityLogList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActivityLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity_log = response.parse()
        assert_matches_type(ActivityLogList, activity_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.admins.activity_logs.with_streaming_response.list(
            created_at_after="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity_log = response.parse()
            assert_matches_type(ActivityLogList, activity_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActivityLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        activity_log = await async_client.admins.activity_logs.list(
            created_at_after="string",
        )
        assert_matches_type(ActivityLogList, activity_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        activity_log = await async_client.admins.activity_logs.list(
            created_at_after="string",
            created_at_before="string",
        )
        assert_matches_type(ActivityLogList, activity_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.admins.activity_logs.with_raw_response.list(
            created_at_after="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity_log = await response.parse()
        assert_matches_type(ActivityLogList, activity_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.admins.activity_logs.with_streaming_response.list(
            created_at_after="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity_log = await response.parse()
            assert_matches_type(ActivityLogList, activity_log, path=["response"])

        assert cast(Any, response.is_closed) is True
