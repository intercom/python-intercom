# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types import (
    ContactList,
    ContactDeleted,
    ContactArchived,
    ContactUnarchived,
)
from python_intercom.types.shared import Contact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Intercom) -> None:
        contact = client.contacts.create(
            body={},
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Intercom) -> None:
        contact = client.contacts.create(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Intercom) -> None:
        contact = client.contacts.create(
            body={},
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Intercom) -> None:
        contact = client.contacts.create(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Intercom) -> None:
        contact = client.contacts.create(
            body={},
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Intercom) -> None:
        contact = client.contacts.create(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        contact = client.contacts.retrieve(
            id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.retrieve(
            id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.retrieve(
            id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.retrieve(
            id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        contact = client.contacts.update(
            id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.update(
            id="63a07ddf05a32042dffac965",
            avatar="https://www.example.com/avatar_image.jpg",
            custom_attributes={},
            email="jdoe@example.com",
            external_id="external_id",
            last_seen_at=1571672154,
            name="John Doe",
            owner_id=123,
            phone="+353871234567",
            role="role",
            signed_up_at=1571672154,
            unsubscribed_from_emails=True,
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.update(
            id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.update(
            id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        contact = client.contacts.list()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.list(
            intercom_version="2.11",
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactList, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        contact = client.contacts.delete(
            id="id",
        )
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.delete(
            id="id",
            intercom_version="2.11",
        )
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactDeleted, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.delete(
                id="",
            )

    @parametrize
    def test_method_archive(self, client: Intercom) -> None:
        contact = client.contacts.archive(
            id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    def test_method_archive_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.archive(
            id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.archive(
            id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.archive(
            id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactArchived, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.archive(
                id="",
            )

    @parametrize
    def test_method_merge(self, client: Intercom) -> None:
        contact = client.contacts.merge()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_merge_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.merge(
            from_="6657adf76abd0167d9419d1d",
            into="6657adf76abd0167d9419d1e",
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_merge(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.merge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_merge(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.merge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

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
                "field": "created_at",
                "operator": "=",
                "value": "value",
            },
            pagination={
                "per_page": 5,
                "starting_after": "your-cursor-from-response",
            },
            intercom_version="2.11",
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.search(
            query={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.search(
            query={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactList, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unarchive(self, client: Intercom) -> None:
        contact = client.contacts.unarchive(
            id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(ContactUnarchived, contact, path=["response"])

    @parametrize
    def test_method_unarchive_with_all_params(self, client: Intercom) -> None:
        contact = client.contacts.unarchive(
            id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(ContactUnarchived, contact, path=["response"])

    @parametrize
    def test_raw_response_unarchive(self, client: Intercom) -> None:
        response = client.contacts.with_raw_response.unarchive(
            id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactUnarchived, contact, path=["response"])

    @parametrize
    def test_streaming_response_unarchive(self, client: Intercom) -> None:
        with client.contacts.with_streaming_response.unarchive(
            id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactUnarchived, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unarchive(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.unarchive(
                id="",
            )


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.create(
            body={},
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.create(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.create(
            body={},
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.create(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.create(
            body={},
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.create(
            body={},
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.retrieve(
            id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.retrieve(
            id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.retrieve(
            id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.retrieve(
            id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.update(
            id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.update(
            id="63a07ddf05a32042dffac965",
            avatar="https://www.example.com/avatar_image.jpg",
            custom_attributes={},
            email="jdoe@example.com",
            external_id="external_id",
            last_seen_at=1571672154,
            name="John Doe",
            owner_id=123,
            phone="+353871234567",
            role="role",
            signed_up_at=1571672154,
            unsubscribed_from_emails=True,
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.update(
            id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.update(
            id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.list()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.list(
            intercom_version="2.11",
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactList, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.delete(
            id="id",
        )
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.delete(
            id="id",
            intercom_version="2.11",
        )
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactDeleted, contact, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactDeleted, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.delete(
                id="",
            )

    @parametrize
    async def test_method_archive(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.archive(
            id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.archive(
            id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.archive(
            id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactArchived, contact, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.archive(
            id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactArchived, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.archive(
                id="",
            )

    @parametrize
    async def test_method_merge(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.merge()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_merge_with_all_params(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.merge(
            from_="6657adf76abd0167d9419d1d",
            into="6657adf76abd0167d9419d1e",
            intercom_version="2.11",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.merge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.merge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.search(
            query={},
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.search(
            query={
                "field": "created_at",
                "operator": "=",
                "value": "value",
            },
            pagination={
                "per_page": 5,
                "starting_after": "your-cursor-from-response",
            },
            intercom_version="2.11",
        )
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.search(
            query={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactList, contact, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.search(
            query={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactList, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unarchive(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.unarchive(
            id="63a07ddf05a32042dffac965",
        )
        assert_matches_type(ContactUnarchived, contact, path=["response"])

    @parametrize
    async def test_method_unarchive_with_all_params(self, async_client: AsyncIntercom) -> None:
        contact = await async_client.contacts.unarchive(
            id="63a07ddf05a32042dffac965",
            intercom_version="2.11",
        )
        assert_matches_type(ContactUnarchived, contact, path=["response"])

    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncIntercom) -> None:
        response = await async_client.contacts.with_raw_response.unarchive(
            id="63a07ddf05a32042dffac965",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactUnarchived, contact, path=["response"])

    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncIntercom) -> None:
        async with async_client.contacts.with_streaming_response.unarchive(
            id="63a07ddf05a32042dffac965",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactUnarchived, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.unarchive(
                id="",
            )
