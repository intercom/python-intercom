# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import DataEventSummary
from intercom._client import Intercom, AsyncIntercom

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestDataEvents:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    def test_raw_response_create_overload_1(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    def test_method_create_overload_2(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    def test_raw_response_create_overload_2(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    def test_method_create_overload_3(self, client: Intercom) -> None:
        data_event = client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    def test_raw_response_create_overload_3(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

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
        )
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.list(
            filter={"user_id": "string"},
            type="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert_matches_type(DataEventSummary, data_event, path=["response"])

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
        )
        assert data_event is None

    @parametrize
    def test_raw_response_summaries(self, client: Intercom) -> None:
        response = client.data_events.with_raw_response.summaries()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None


class TestAsyncDataEvents:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncIntercom) -> None:
        data_event = await client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    async def test_raw_response_create_overload_1(self, client: AsyncIntercom) -> None:
        response = await client.data_events.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncIntercom) -> None:
        data_event = await client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncIntercom) -> None:
        response = await client.data_events.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    async def test_method_create_overload_3(self, client: AsyncIntercom) -> None:
        data_event = await client.data_events.create(
            body={},
        )
        assert data_event is None

    @parametrize
    async def test_raw_response_create_overload_3(self, client: AsyncIntercom) -> None:
        response = await client.data_events.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        data_event = await client.data_events.list(
            filter={"user_id": "string"},
            type="string",
        )
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIntercom) -> None:
        data_event = await client.data_events.list(
            filter={"user_id": "string"},
            type="string",
            summary=True,
        )
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.data_events.with_raw_response.list(
            filter={"user_id": "string"},
            type="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert_matches_type(DataEventSummary, data_event, path=["response"])

    @parametrize
    async def test_method_summaries(self, client: AsyncIntercom) -> None:
        data_event = await client.data_events.summaries()
        assert data_event is None

    @parametrize
    async def test_method_summaries_with_all_params(self, client: AsyncIntercom) -> None:
        data_event = await client.data_events.summaries(
            event_summaries={
                "event_name": "invited-friend",
                "count": 1,
                "first": 1671028894,
                "last": 1671028894,
            },
            user_id="314159",
        )
        assert data_event is None

    @parametrize
    async def test_raw_response_summaries(self, client: AsyncIntercom) -> None:
        response = await client.data_events.with_raw_response.summaries()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_event = response.parse()
        assert data_event is None
