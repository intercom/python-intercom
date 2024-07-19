# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types.shared import Note

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        note = client.notes.retrieve(
            id=1,
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        note = client.notes.retrieve(
            id=1,
            intercom_version="2.11",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.notes.with_raw_response.retrieve(
            id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.notes.with_streaming_response.retrieve(
            id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(Note, note, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        note = await async_client.notes.retrieve(
            id=1,
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        note = await async_client.notes.retrieve(
            id=1,
            intercom_version="2.11",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.notes.with_raw_response.retrieve(
            id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.notes.with_streaming_response.retrieve(
            id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(Note, note, path=["response"])

        assert cast(Any, response.is_closed) is True
