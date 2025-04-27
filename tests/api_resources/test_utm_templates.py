# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from blink.types import UtmTemplateListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUtmTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Blink) -> None:
        utm_template = client.utm_templates.list(
            domain_id=0,
        )
        assert_matches_type(UtmTemplateListResponse, utm_template, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Blink) -> None:
        response = client.utm_templates.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        utm_template = response.parse()
        assert_matches_type(UtmTemplateListResponse, utm_template, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Blink) -> None:
        with client.utm_templates.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            utm_template = response.parse()
            assert_matches_type(UtmTemplateListResponse, utm_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUtmTemplates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBlink) -> None:
        utm_template = await async_client.utm_templates.list(
            domain_id=0,
        )
        assert_matches_type(UtmTemplateListResponse, utm_template, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlink) -> None:
        response = await async_client.utm_templates.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        utm_template = await response.parse()
        assert_matches_type(UtmTemplateListResponse, utm_template, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlink) -> None:
        async with async_client.utm_templates.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            utm_template = await response.parse()
            assert_matches_type(UtmTemplateListResponse, utm_template, path=["response"])

        assert cast(Any, response.is_closed) is True
