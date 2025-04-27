# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from blink.types import TagListResponse, TagCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Blink) -> None:
        tag = client.tags.create()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Blink) -> None:
        tag = client.tags.create(
            domain_id=0,
            name="name",
            notes="notes",
            shared=True,
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Blink) -> None:
        response = client.tags.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Blink) -> None:
        with client.tags.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Blink) -> None:
        tag = client.tags.list(
            domain_id=0,
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Blink) -> None:
        tag = client.tags.list(
            domain_id=0,
            search="search",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Blink) -> None:
        response = client.tags.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Blink) -> None:
        with client.tags.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncBlink) -> None:
        tag = await async_client.tags.create()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBlink) -> None:
        tag = await async_client.tags.create(
            domain_id=0,
            name="name",
            notes="notes",
            shared=True,
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBlink) -> None:
        response = await async_client.tags.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBlink) -> None:
        async with async_client.tags.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBlink) -> None:
        tag = await async_client.tags.list(
            domain_id=0,
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBlink) -> None:
        tag = await async_client.tags.list(
            domain_id=0,
            search="search",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlink) -> None:
        response = await async_client.tags.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlink) -> None:
        async with async_client.tags.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True
