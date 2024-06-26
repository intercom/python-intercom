# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_minus_intercom import Intercom, AsyncIntercom
from python_minus_intercom.types import DataExport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataExports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_content_data(self, client: Intercom) -> None:
        data_export = client.data_exports.content_data(
            created_at_after=1717004390,
            created_at_before=1717022390,
        )
        assert_matches_type(DataExport, data_export, path=["response"])

    @parametrize
    def test_method_content_data_with_all_params(self, client: Intercom) -> None:
        data_export = client.data_exports.content_data(
            created_at_after=1717004390,
            created_at_before=1717022390,
            intercom_version="2.11",
        )
        assert_matches_type(DataExport, data_export, path=["response"])

    @parametrize
    def test_raw_response_content_data(self, client: Intercom) -> None:
        response = client.data_exports.with_raw_response.content_data(
            created_at_after=1717004390,
            created_at_before=1717022390,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExport, data_export, path=["response"])

    @parametrize
    def test_streaming_response_content_data(self, client: Intercom) -> None:
        with client.data_exports.with_streaming_response.content_data(
            created_at_after=1717004390,
            created_at_before=1717022390,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExport, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataExports:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_content_data(self, async_client: AsyncIntercom) -> None:
        data_export = await async_client.data_exports.content_data(
            created_at_after=1717004390,
            created_at_before=1717022390,
        )
        assert_matches_type(DataExport, data_export, path=["response"])

    @parametrize
    async def test_method_content_data_with_all_params(self, async_client: AsyncIntercom) -> None:
        data_export = await async_client.data_exports.content_data(
            created_at_after=1717004390,
            created_at_before=1717022390,
            intercom_version="2.11",
        )
        assert_matches_type(DataExport, data_export, path=["response"])

    @parametrize
    async def test_raw_response_content_data(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_exports.with_raw_response.content_data(
            created_at_after=1717004390,
            created_at_before=1717022390,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExport, data_export, path=["response"])

    @parametrize
    async def test_streaming_response_content_data(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_exports.with_streaming_response.content_data(
            created_at_after=1717004390,
            created_at_before=1717022390,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExport, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True
