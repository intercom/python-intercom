# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Note
from intercom.types.contacts import NoteList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestNotes:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        note = client.contacts.notes.create(
            0,
            body="Hello",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        note = client.contacts.notes.create(
            0,
            body="Hello",
            admin_id="string",
            contact_id="654b70866abd01feb7c11043",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.contacts.notes.with_raw_response.create(
            0,
            body="Hello",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        note = client.contacts.notes.list(
            0,
        )
        assert_matches_type(NoteList, note, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.contacts.notes.with_raw_response.list(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteList, note, path=["response"])


class TestAsyncNotes:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        note = await client.contacts.notes.create(
            0,
            body="Hello",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        note = await client.contacts.notes.create(
            0,
            body="Hello",
            admin_id="string",
            contact_id="654b70866abd01feb7c11043",
        )
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.contacts.notes.with_raw_response.create(
            0,
            body="Hello",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(Note, note, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        note = await client.contacts.notes.list(
            0,
        )
        assert_matches_type(NoteList, note, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.contacts.notes.with_raw_response.list(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteList, note, path=["response"])
