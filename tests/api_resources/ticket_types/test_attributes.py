# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types.shared import TicketTypeAttribute

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttributes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            intercom_version="2.11",
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.ticket_types.attributes.with_streaming_response.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_type_id` but received ''"):
            client.ticket_types.attributes.with_raw_response.create(
                "",
                data_type="string",
                description="Attribute Description",
                name="Attribute Title",
            )

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
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.ticket_types.attributes.with_raw_response.update(
            "string",
            ticket_type_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.ticket_types.attributes.with_streaming_response.update(
            "string",
            ticket_type_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_type_id` but received ''"):
            client.ticket_types.attributes.with_raw_response.update(
                "string",
                ticket_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ticket_types.attributes.with_raw_response.update(
                "",
                ticket_type_id="string",
            )


class TestAsyncAttributes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        attribute = await async_client.ticket_types.attributes.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        attribute = await async_client.ticket_types.attributes.create(
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
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.ticket_types.attributes.with_raw_response.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.ticket_types.attributes.with_streaming_response.create(
            "string",
            data_type="string",
            description="Attribute Description",
            name="Attribute Title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_type_id` but received ''"):
            await async_client.ticket_types.attributes.with_raw_response.create(
                "",
                data_type="string",
                description="Attribute Description",
                name="Attribute Title",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        attribute = await async_client.ticket_types.attributes.update(
            "string",
            ticket_type_id="string",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        attribute = await async_client.ticket_types.attributes.update(
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
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.ticket_types.attributes.with_raw_response.update(
            "string",
            ticket_type_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.ticket_types.attributes.with_streaming_response.update(
            "string",
            ticket_type_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(Optional[TicketTypeAttribute], attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_type_id` but received ''"):
            await async_client.ticket_types.attributes.with_raw_response.update(
                "string",
                ticket_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ticket_types.attributes.with_raw_response.update(
                "",
                ticket_type_id="string",
            )
