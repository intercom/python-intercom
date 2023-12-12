# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Optional

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import TicketTypeAttribute

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestAttributes:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        attribute = client.ticket_types.attributes.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        attribute = client.ticket_types.attributes.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
            allow_multiple_values=False,
            list_items="Low Priority,Medium Priority,High Priority",
            multiline=False,
            required_to_create=False,
            required_to_create_for_contacts=False,
            visible_on_create=True,
            visible_to_contacts=True,
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.ticket_types.attributes.with_raw_response.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        attribute = client.ticket_types.attributes.update(
            "string",
            ticket_type_id="string",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        attribute = client.ticket_types.attributes.update(
            "string",
            ticket_type_id="string",
            allow_multiple_values=False,
            archived=False,
            description="New Attribute Description",
            list_items="Low Priority,Medium Priority,High Priority",
            multiline=False,
            name="Bug Priority",
            required_to_create=False,
            required_to_create_for_contacts=False,
            visible_on_create=True,
            visible_to_contacts=True,
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.ticket_types.attributes.with_raw_response.update(
            "string",
            ticket_type_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])


class TestAsyncAttributes:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        attribute = await client.ticket_types.attributes.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        attribute = await client.ticket_types.attributes.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
            allow_multiple_values=False,
            list_items="Low Priority,Medium Priority,High Priority",
            multiline=False,
            required_to_create=False,
            required_to_create_for_contacts=False,
            visible_on_create=True,
            visible_to_contacts=True,
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.ticket_types.attributes.with_raw_response.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        attribute = await client.ticket_types.attributes.update(
            "string",
            ticket_type_id="string",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        attribute = await client.ticket_types.attributes.update(
            "string",
            ticket_type_id="string",
            allow_multiple_values=False,
            archived=False,
            description="New Attribute Description",
            list_items="Low Priority,Medium Priority,High Priority",
            multiline=False,
            name="Bug Priority",
            required_to_create=False,
            required_to_create_for_contacts=False,
            visible_on_create=True,
            visible_to_contacts=True,
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.ticket_types.attributes.with_raw_response.update(
            "string",
            ticket_type_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])
