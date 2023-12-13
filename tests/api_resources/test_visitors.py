# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Optional

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import Visitor, VisitorDeletedObject
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Contact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestVisitors:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        visitor = client.visitors.retrieve(
            user_id="string",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.retrieve(
            user_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_method_update_overload_1(self, client: Intercom) -> None:
        visitor = client.visitors.update(
            body={},
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.update(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_method_update_overload_2(self, client: Intercom) -> None:
        visitor = client.visitors.update(
            body={},
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.update(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_method_convert(self, client: Intercom) -> None:
        visitor = client.visitors.convert(
            type="user",
            user={},
            visitor={},
        )
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    def test_method_convert_with_all_params(self, client: Intercom) -> None:
        visitor = client.visitors.convert(
            type="user",
            user={
                "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "user_id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "email": "foo@bar.com",
            },
            visitor={
                "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "user_id": "3ecf64d0-9ed1-4e9f-88e1-da7d6e6782f3",
                "email": "winstonsmith@truth.org",
            },
        )
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    def test_raw_response_convert(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.convert(
            type="user",
            user={},
            visitor={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    def test_method_delete_by_id(self, client: Intercom) -> None:
        visitor = client.visitors.delete_by_id(
            "string",
        )
        assert_matches_type(VisitorDeletedObject, visitor, path=["response"])

    @parametrize
    def test_raw_response_delete_by_id(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.delete_by_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(VisitorDeletedObject, visitor, path=["response"])

    @parametrize
    def test_method_retrieve_by_id(self, client: Intercom) -> None:
        visitor = client.visitors.retrieve_by_id(
            "string",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    def test_raw_response_retrieve_by_id(self, client: Intercom) -> None:
        response = client.visitors.with_raw_response.retrieve_by_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])


class TestAsyncVisitors:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        visitor = await client.visitors.retrieve(
            user_id="string",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.visitors.with_raw_response.retrieve(
            user_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_method_update_overload_1(self, client: AsyncIntercom) -> None:
        visitor = await client.visitors.update(
            body={},
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, client: AsyncIntercom) -> None:
        response = await client.visitors.with_raw_response.update(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_method_update_overload_2(self, client: AsyncIntercom) -> None:
        visitor = await client.visitors.update(
            body={},
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, client: AsyncIntercom) -> None:
        response = await client.visitors.with_raw_response.update(
            body={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_method_convert(self, client: AsyncIntercom) -> None:
        visitor = await client.visitors.convert(
            type="user",
            user={},
            visitor={},
        )
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    async def test_method_convert_with_all_params(self, client: AsyncIntercom) -> None:
        visitor = await client.visitors.convert(
            type="user",
            user={
                "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "user_id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "email": "foo@bar.com",
            },
            visitor={
                "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
                "user_id": "3ecf64d0-9ed1-4e9f-88e1-da7d6e6782f3",
                "email": "winstonsmith@truth.org",
            },
        )
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    async def test_raw_response_convert(self, client: AsyncIntercom) -> None:
        response = await client.visitors.with_raw_response.convert(
            type="user",
            user={},
            visitor={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Contact, visitor, path=["response"])

    @parametrize
    async def test_method_delete_by_id(self, client: AsyncIntercom) -> None:
        visitor = await client.visitors.delete_by_id(
            "string",
        )
        assert_matches_type(VisitorDeletedObject, visitor, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_id(self, client: AsyncIntercom) -> None:
        response = await client.visitors.with_raw_response.delete_by_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(VisitorDeletedObject, visitor, path=["response"])

    @parametrize
    async def test_method_retrieve_by_id(self, client: AsyncIntercom) -> None:
        visitor = await client.visitors.retrieve_by_id(
            "string",
        )
        assert_matches_type(Optional[Visitor], visitor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_by_id(self, client: AsyncIntercom) -> None:
        response = await client.visitors.with_raw_response.retrieve_by_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor = response.parse()
        assert_matches_type(Optional[Visitor], visitor, path=["response"])
