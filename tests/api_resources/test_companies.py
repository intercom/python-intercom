# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types import (
    CompanyList,
    CompanyScroll,
    DeletedCompanyObject,
)
from python_intercom.types.shared import Company

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        company = client.companies.create()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        company = client.companies.create(
            company_id="company_remote_id",
            custom_attributes={
                "paid_subscriber": "string",
                "monthly_spend": "string",
                "team_mates": "string",
            },
            industry="Manufacturing",
            monthly_spend=1000,
            name="my company",
            plan="Enterprise",
            remote_created_at=1374138000,
            size=0,
            website="https://www.example.com",
            intercom_version="2.11",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.companies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.companies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Company, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        company = client.companies.retrieve(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        company = client.companies.retrieve(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
            intercom_version="2.11",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.companies.with_raw_response.retrieve(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.companies.with_streaming_response.retrieve(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Company, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.companies.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        company = client.companies.update(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        company = client.companies.update(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
            intercom_version="2.11",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.companies.with_raw_response.update(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.companies.with_streaming_response.update(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Company, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.companies.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        company = client.companies.list()
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        company = client.companies.list(
            order="order",
            page=0,
            per_page=0,
            intercom_version="2.11",
        )
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.companies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.companies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyList, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        company = client.companies.delete(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )
        assert_matches_type(DeletedCompanyObject, company, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Intercom) -> None:
        company = client.companies.delete(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
            intercom_version="2.11",
        )
        assert_matches_type(DeletedCompanyObject, company, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.companies.with_raw_response.delete(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(DeletedCompanyObject, company, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Intercom) -> None:
        with client.companies.with_streaming_response.delete(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(DeletedCompanyObject, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.companies.with_raw_response.delete(
                id="",
            )

    @parametrize
    def test_method_retrieve_list(self, client: Intercom) -> None:
        company = client.companies.retrieve_list()
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    def test_method_retrieve_list_with_all_params(self, client: Intercom) -> None:
        company = client.companies.retrieve_list(
            company_id="company_id",
            name="name",
            page=0,
            per_page=0,
            segment_id="segment_id",
            tag_id="tag_id",
            intercom_version="2.11",
        )
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    def test_raw_response_retrieve_list(self, client: Intercom) -> None:
        response = client.companies.with_raw_response.retrieve_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_list(self, client: Intercom) -> None:
        with client.companies.with_streaming_response.retrieve_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyList, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_scroll(self, client: Intercom) -> None:
        company = client.companies.scroll()
        assert_matches_type(Optional[CompanyScroll], company, path=["response"])

    @parametrize
    def test_method_scroll_with_all_params(self, client: Intercom) -> None:
        company = client.companies.scroll(
            scroll_param="scroll_param",
            intercom_version="2.11",
        )
        assert_matches_type(Optional[CompanyScroll], company, path=["response"])

    @parametrize
    def test_raw_response_scroll(self, client: Intercom) -> None:
        response = client.companies.with_raw_response.scroll()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Optional[CompanyScroll], company, path=["response"])

    @parametrize
    def test_streaming_response_scroll(self, client: Intercom) -> None:
        with client.companies.with_streaming_response.scroll() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Optional[CompanyScroll], company, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompanies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.create()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.create(
            company_id="company_remote_id",
            custom_attributes={
                "paid_subscriber": "string",
                "monthly_spend": "string",
                "team_mates": "string",
            },
            industry="Manufacturing",
            monthly_spend=1000,
            name="my company",
            plan="Enterprise",
            remote_created_at=1374138000,
            size=0,
            website="https://www.example.com",
            intercom_version="2.11",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.companies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.companies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Company, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.retrieve(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.retrieve(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
            intercom_version="2.11",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.companies.with_raw_response.retrieve(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.companies.with_streaming_response.retrieve(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Company, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.companies.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.update(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.update(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
            intercom_version="2.11",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.companies.with_raw_response.update(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.companies.with_streaming_response.update(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Company, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.companies.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.list()
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.list(
            order="order",
            page=0,
            per_page=0,
            intercom_version="2.11",
        )
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.companies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.companies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyList, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.delete(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )
        assert_matches_type(DeletedCompanyObject, company, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.delete(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
            intercom_version="2.11",
        )
        assert_matches_type(DeletedCompanyObject, company, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncIntercom) -> None:
        response = await async_client.companies.with_raw_response.delete(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(DeletedCompanyObject, company, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncIntercom) -> None:
        async with async_client.companies.with_streaming_response.delete(
            id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(DeletedCompanyObject, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.companies.with_raw_response.delete(
                id="",
            )

    @parametrize
    async def test_method_retrieve_list(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.retrieve_list()
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    async def test_method_retrieve_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.retrieve_list(
            company_id="company_id",
            name="name",
            page=0,
            per_page=0,
            segment_id="segment_id",
            tag_id="tag_id",
            intercom_version="2.11",
        )
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.companies.with_raw_response.retrieve_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyList, company, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.companies.with_streaming_response.retrieve_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyList, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_scroll(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.scroll()
        assert_matches_type(Optional[CompanyScroll], company, path=["response"])

    @parametrize
    async def test_method_scroll_with_all_params(self, async_client: AsyncIntercom) -> None:
        company = await async_client.companies.scroll(
            scroll_param="scroll_param",
            intercom_version="2.11",
        )
        assert_matches_type(Optional[CompanyScroll], company, path=["response"])

    @parametrize
    async def test_raw_response_scroll(self, async_client: AsyncIntercom) -> None:
        response = await async_client.companies.with_raw_response.scroll()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Optional[CompanyScroll], company, path=["response"])

    @parametrize
    async def test_streaming_response_scroll(self, async_client: AsyncIntercom) -> None:
        async with async_client.companies.with_streaming_response.scroll() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Optional[CompanyScroll], company, path=["response"])

        assert cast(Any, response.is_closed) is True
