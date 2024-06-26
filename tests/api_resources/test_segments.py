# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_minus_intercom import Intercom, AsyncIntercom
from python_minus_intercom.types import Segment, SegmentList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSegments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        segment = client.segments.retrieve(
            "string",
        )
        assert_matches_type(Segment, segment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        segment = client.segments.retrieve(
            "string",
            intercom_version="2.11",
        )
        assert_matches_type(Segment, segment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.segments.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = response.parse()
        assert_matches_type(Segment, segment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.segments.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = response.parse()
            assert_matches_type(Segment, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.segments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        segment = client.segments.list()
        assert_matches_type(SegmentList, segment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        segment = client.segments.list(
            include_count=True,
            intercom_version="2.11",
        )
        assert_matches_type(SegmentList, segment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.segments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = response.parse()
        assert_matches_type(SegmentList, segment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.segments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = response.parse()
            assert_matches_type(SegmentList, segment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSegments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        segment = await async_client.segments.retrieve(
            "string",
        )
        assert_matches_type(Segment, segment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        segment = await async_client.segments.retrieve(
            "string",
            intercom_version="2.11",
        )
        assert_matches_type(Segment, segment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.segments.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = await response.parse()
        assert_matches_type(Segment, segment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.segments.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = await response.parse()
            assert_matches_type(Segment, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.segments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        segment = await async_client.segments.list()
        assert_matches_type(SegmentList, segment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        segment = await async_client.segments.list(
            include_count=True,
            intercom_version="2.11",
        )
        assert_matches_type(SegmentList, segment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.segments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = await response.parse()
        assert_matches_type(SegmentList, segment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.segments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = await response.parse()
            assert_matches_type(SegmentList, segment, path=["response"])

        assert cast(Any, response.is_closed) is True
