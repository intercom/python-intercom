# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import (
    ContactList,
    ContactDeleted,
    ContactArchived,
    ContactUnarchived,
)
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Contact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestContacts:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        contact = client.contacts.create()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.create(
            avatar="https://www.example.com/avatar_image.jpg",
            custom_attributes={},
            email="jdoe@example.com",
            external_id="string",
            last_seen_at=1571672154,
            name="John Doe",
            owner_id=123,
            phone="+353871234567",
            role="string",
            signed_up_at=1571672154,
            unsubscribed_from_emails=True,
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.create()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        contact = client.contacts.retrieve(
            "string",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        contact = client.contacts.update(
            "string",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.update(
            "string",
            avatar="https://www.example.com/avatar_image.jpg",
            custom_attributes={},
            email="jdoe@example.com",
            external_id="string",
            last_seen_at=1571672154,
            name="John Doe",
            owner_id=123,
            phone="+353871234567",
            role="string",
            signed_up_at=1571672154,
            unsubscribed_from_emails=True,
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        contact = client.contacts.list()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        contact = client.contacts.delete(
            "string",
        )
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    def test_method_archive(self, client: Intercom) -> None:
        contact = client.contacts.archive(
            "string",
        )
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.archive(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    def test_method_merge(self, client: Intercom) -> None:
        contact = client.contacts.merge()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_merge_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.merge(
            from_="653a6a8835824d7a15ffe9a6",
            into="653a6a8835824d7a15ffe9a7",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_merge(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.merge()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_search(self, client: Intercom) -> None:
        contact = client.contacts.search(
            query={},
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.search(
            query={
                "field": "custom_attributes.social_network",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "page": 2,
                "starting_after": "1HaSB+xrOyyMXAkS/c1RteCL7BzOzTvYjmjakgTergIH31eoe2v4/sbLsJWP\nIncfQLD3ouPkZlCwJ86F\n",
            },
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.search(
            query={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_method_unarchive(self, client: Intercom) -> None:
        contact = client.contacts.unarchive(
            "string",
        )
        assert_matches_type(ContactUnarchived, contact, path=["response"])

    @parametrize
    def test_raw_response_unarchive(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.unarchive(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactUnarchived, contact, path=["response"])


class TestAsyncContacts:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.create()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.create(
            avatar="https://www.example.com/avatar_image.jpg",
            custom_attributes={},
            email="jdoe@example.com",
            external_id="string",
            last_seen_at=1571672154,
            name="John Doe",
            owner_id=123,
            phone="+353871234567",
            role="string",
            signed_up_at=1571672154,
            unsubscribed_from_emails=True,
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.create()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.retrieve(
            "string",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.update(
            "string",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.update(
            "string",
            avatar="https://www.example.com/avatar_image.jpg",
            custom_attributes={},
            email="jdoe@example.com",
            external_id="string",
            last_seen_at=1571672154,
            name="John Doe",
            owner_id=123,
            phone="+353871234567",
            role="string",
            signed_up_at=1571672154,
            unsubscribed_from_emails=True,
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.list()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.delete(
            "string",
        )
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    async def test_method_archive(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.archive(
            "string",
        )
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.archive(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    async def test_method_merge(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.merge()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_merge_with_all_params(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.merge(
            from_="653a6a8835824d7a15ffe9a6",
            into="653a6a8835824d7a15ffe9a7",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_merge(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.merge()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_search(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.search(
            query={},
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.search(
            query={
                "field": "custom_attributes.social_network",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "page": 2,
                "starting_after": "1HaSB+xrOyyMXAkS/c1RteCL7BzOzTvYjmjakgTergIH31eoe2v4/sbLsJWP\nIncfQLD3ouPkZlCwJ86F\n",
            },
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_raw_response_search(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.search(
            query={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_method_unarchive(self, client: AsyncIntercom) -> None:
        contact = await client.contacts.unarchive(
            "string",
        )
        assert_matches_type(ContactUnarchived, contact, path=["response"])

    @parametrize
    async def test_raw_response_unarchive(self, client: AsyncIntercom) -> None:
        response = await client.contacts.with_raw_response.unarchive(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactUnarchived, contact, path=["response"])
