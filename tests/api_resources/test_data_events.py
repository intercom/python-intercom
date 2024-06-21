# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import (
    DataEventSummary,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
            intercom_version="2.11",
        )
        assert data_event is None

    @parametrize
    def test_raw_response_create_overload_1(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Intercom) -> None:
        with client.data_events.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = response.parse()
            assert data_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
            intercom_version="2.11",
        )
        assert data_event is None

    @parametrize
    def test_raw_response_create_overload_2(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Intercom) -> None:
        with client.data_events.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = response.parse()
            assert data_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
            intercom_version="2.11",
        )
        assert data_event is None

    @parametrize
    def test_raw_response_create_overload_3(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Intercom) -> None:
        with client.data_events.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = response.parse()
            assert data_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        data_event = client.data_events.list(
            filter={"user_id": "string"},
            type="string",
        )
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        data_event = client.data_events.list(
            filter={"user_id": "string"},
            type="string",
            summary=True,
            intercom_version="2.11",
        )
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.list(
            filter={"user_id": "string"},
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.data_events.with_streaming_response.list(
            filter={"user_id": "string"},
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = response.parse()
            assert_matches_type(DataEventSummary, data_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summaries(self, client: Intercom) -> None:
        data_event = client.data_events.summaries()
        assert data_event is None

    @parametrize
    def test_method_summaries_with_all_params(self, client: Intercom) -> None:
        data_event = client.data_events.summaries(
            event_summaries={
                "event_name": "invited-friend",
                "count": 1,
                "first": 1671028894,
                "last": 1671028894,
            },
            user_id="314159",
            intercom_version="2.11",
        )
        assert data_event is None

    @parametrize
    def test_raw_response_summaries(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.summaries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    def test_streaming_response_summaries(self, client: Intercom) -> None:
        with client.data_events.with_streaming_response.summaries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = response.parse()
            assert data_event is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDataEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.create(
            body={},
            intercom_version="2.11",
        )
        assert data_event is None

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_events.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = await response.parse()
        assert data_event is None

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_events.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = await response.parse()
            assert data_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.create(
            body={},
            intercom_version="2.11",
        )
        assert data_event is None

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_events.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = await response.parse()
        assert data_event is None

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_events.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = await response.parse()
            assert data_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.create(
            body={},
            intercom_version="2.11",
        )
        assert data_event is None

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_events.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = await response.parse()
        assert data_event is None

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_events.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = await response.parse()
            assert data_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.list(
            filter={"user_id": "string"},
            type="string",
        )
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.list(
            filter={"user_id": "string"},
            type="string",
            summary=True,
            intercom_version="2.11",
        )
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_events.with_raw_response.list(
            filter={"user_id": "string"},
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = await response.parse()
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_events.with_streaming_response.list(
            filter={"user_id": "string"},
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = await response.parse()
            assert_matches_type(DataEventSummary, data_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summaries(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.summaries()
        assert data_event is None

    @parametrize
    async def test_method_summaries_with_all_params(self, async_client: AsyncIntercom) -> None:
        data_event = await async_client.data_events.summaries(
            event_summaries={
                "event_name": "invited-friend",
                "count": 1,
                "first": 1671028894,
                "last": 1671028894,
            },
            user_id="314159",
            intercom_version="2.11",
        )
        assert data_event is None

    @parametrize
    async def test_raw_response_summaries(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_events.with_raw_response.summaries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = await response.parse()
        assert data_event is None

    @parametrize
    async def test_streaming_response_summaries(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_events.with_streaming_response.summaries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_event = await response.parse()
            assert data_event is None

        assert cast(Any, response.is_closed) is True
