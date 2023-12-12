# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Optional

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import PhoneSwitch
from intercom._client import Intercom, AsyncIntercom

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestPhoneCallRedirects:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        phone_call_redirect = client.phone_call_redirects.create(
            phone="+353832345678",
        )
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        phone_call_redirect = client.phone_call_redirects.create(
            phone="+353832345678",
            custom_attributes={
                "issue_type": "Billing",
                "priority": "High",
            },
        )
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.phone_call_redirects.with_raw_response.create(
            phone="+353832345678",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call_redirect = response.parse()
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])


class TestAsyncPhoneCallRedirects:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        phone_call_redirect = await client.phone_call_redirects.create(
            phone="+353832345678",
        )
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        phone_call_redirect = await client.phone_call_redirects.create(
            phone="+353832345678",
            custom_attributes={
                "issue_type": "Billing",
                "priority": "High",
            },
        )
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.phone_call_redirects.with_raw_response.create(
            phone="+353832345678",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call_redirect = response.parse()
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])
