# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types.shared import Tag

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        tag = client.tickets.tags.create(
            "string",
            id="string",
            admin_id="string",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.tickets.tags.with_raw_response.create(
            "string",
            id="string",
            admin_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.tickets.tags.with_streaming_response.create(
            "string",
            id="string",
            admin_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            client.tickets.tags.with_raw_response.create(
                "",
                id="string",
                admin_id="string",
            )

    @parametrize
    def test_method_remove(self, client: Intercom) -> None:
        tag = client.tickets.tags.remove(
            "string",
            ticket_id="64619700005694",
            admin_id="string",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Intercom) -> None:
        response = client.tickets.tags.with_raw_response.remove(
            "string",
            ticket_id="64619700005694",
            admin_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Intercom) -> None:
        with client.tickets.tags.with_streaming_response.remove(
            "string",
            ticket_id="64619700005694",
            admin_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            client.tickets.tags.with_raw_response.remove(
                "string",
                ticket_id="",
                admin_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tickets.tags.with_raw_response.remove(
                "",
                ticket_id="64619700005694",
                admin_id="string",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tickets.tags.create(
            "string",
            id="string",
            admin_id="string",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.tags.with_raw_response.create(
            "string",
            id="string",
            admin_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.tags.with_streaming_response.create(
            "string",
            id="string",
            admin_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            await async_client.tickets.tags.with_raw_response.create(
                "",
                id="string",
                admin_id="string",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncIntercom) -> None:
        tag = await async_client.tickets.tags.remove(
            "string",
            ticket_id="64619700005694",
            admin_id="string",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.tags.with_raw_response.remove(
            "string",
            ticket_id="64619700005694",
            admin_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.tags.with_streaming_response.remove(
            "string",
            ticket_id="64619700005694",
            admin_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            await async_client.tickets.tags.with_raw_response.remove(
                "string",
                ticket_id="",
                admin_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tickets.tags.with_raw_response.remove(
                "",
                ticket_id="64619700005694",
                admin_id="string",
            )
