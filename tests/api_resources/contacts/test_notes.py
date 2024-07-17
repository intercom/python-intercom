# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types.shared import Note
from python_intercom.types.contacts import NoteList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        note = client.contacts.notes.create(
            id=0,
            body="Hello",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        note = client.contacts.notes.create(
            id=0,
            body="Hello",
            admin_id="admin_id",
            contact_id="6657adde6abd0167d9419d00",
            intercom_version="2.11",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.contacts.notes.with_raw_response.create(
            id=0,
            body="Hello",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.contacts.notes.with_streaming_response.create(
            id=0,
            body="Hello",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(Note, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        note = client.contacts.notes.list(
            id=0,
        )
        assert_matches_type(NoteList, note, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        note = client.contacts.notes.list(
            id=0,
            intercom_version="2.11",
        )
        assert_matches_type(NoteList, note, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.contacts.notes.with_raw_response.list(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteList, note, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.contacts.notes.with_streaming_response.list(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(NoteList, note, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        note = await async_client.contacts.notes.create(
            id=0,
            body="Hello",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        note = await async_client.contacts.notes.create(
            id=0,
            body="Hello",
            admin_id="admin_id",
            contact_id="6657adde6abd0167d9419d00",
            intercom_version="2.11",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.notes.with_raw_response.create(
            id=0,
            body="Hello",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.notes.with_streaming_response.create(
            id=0,
            body="Hello",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(Note, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        note = await async_client.contacts.notes.list(
            id=0,
        )
        assert_matches_type(NoteList, note, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        note = await async_client.contacts.notes.list(
            id=0,
            intercom_version="2.11",
        )
        assert_matches_type(NoteList, note, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.notes.with_raw_response.list(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(NoteList, note, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.notes.with_streaming_response.list(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(NoteList, note, path=["response"])

        assert cast(Any, response.is_closed) is True
