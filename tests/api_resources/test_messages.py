# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Message

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestMessages:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Intercom) -> None:
        message = client.messages.create(
            body={},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Intercom) -> None:
        response = client.messages.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: Intercom) -> None:
        message = client.messages.create(
            body={},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Intercom) -> None:
        response = client.messages.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])


class TestAsyncMessages:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncIntercom) -> None:
        message = await client.messages.create(
            body={},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, client: AsyncIntercom) -> None:
        response = await client.messages.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncIntercom) -> None:
        message = await client.messages.create(
            body={},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncIntercom) -> None:
        response = await client.messages.with_raw_response.create(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])
