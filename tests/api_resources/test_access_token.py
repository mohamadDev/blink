# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from blink.types import AccessTokenCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_1(self, client: Blink) -> None:
        access_token = client.access_token.create(
            email="bud@smartlinker.email",
            password="password",
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_1(self, client: Blink) -> None:
        response = client.access_token.with_raw_response.create(
            email="bud@smartlinker.email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Blink) -> None:
        with client.access_token.with_streaming_response.create(
            email="bud@smartlinker.email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = response.parse()
            assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_2(self, client: Blink) -> None:
        access_token = client.access_token.create(
            email="bud@smartlinker.email",
            refresh_token="sdafkjsdfhkwerohfkdsfhgkjhdsgfk",
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_2(self, client: Blink) -> None:
        response = client.access_token.with_raw_response.create(
            email="bud@smartlinker.email",
            refresh_token="sdafkjsdfhkwerohfkdsfhgkjhdsgfk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Blink) -> None:
        with client.access_token.with_streaming_response.create(
            email="bud@smartlinker.email",
            refresh_token="sdafkjsdfhkwerohfkdsfhgkjhdsgfk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = response.parse()
            assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccessToken:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncBlink) -> None:
        access_token = await async_client.access_token.create(
            email="bud@smartlinker.email",
            password="password",
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncBlink) -> None:
        response = await async_client.access_token.with_raw_response.create(
            email="bud@smartlinker.email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = await response.parse()
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncBlink) -> None:
        async with async_client.access_token.with_streaming_response.create(
            email="bud@smartlinker.email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = await response.parse()
            assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncBlink) -> None:
        access_token = await async_client.access_token.create(
            email="bud@smartlinker.email",
            refresh_token="sdafkjsdfhkwerohfkdsfhgkjhdsgfk",
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncBlink) -> None:
        response = await async_client.access_token.with_raw_response.create(
            email="bud@smartlinker.email",
            refresh_token="sdafkjsdfhkwerohfkdsfhgkjhdsgfk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = await response.parse()
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncBlink) -> None:
        async with async_client.access_token.with_streaming_response.create(
            email="bud@smartlinker.email",
            refresh_token="sdafkjsdfhkwerohfkdsfhgkjhdsgfk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = await response.parse()
            assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True
