# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from tests.utils import assert_matches_type
from blink.types.links import (
    ClickGetDailyResponse,
    ClickGetTotalResponse,
    ClickGetByCityResponse,
    ClickGetHourlyResponse,
    ClickGetByDeviceResponse,
    ClickGetByRegionResponse,
    ClickGetByCountryResponse,
    ClickGetByReferrerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClicks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_city(self, client: Blink) -> None:
        click = client.links.clicks.get_by_city(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByCityResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_city_with_all_params(self, client: Blink) -> None:
        click = client.links.clicks.get_by_city(
            link_id=0,
            domain_id=0,
            city="city",
            country="country",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            region="region",
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByCityResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_city(self, client: Blink) -> None:
        response = client.links.clicks.with_raw_response.get_by_city(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickGetByCityResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_city(self, client: Blink) -> None:
        with client.links.clicks.with_streaming_response.get_by_city(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickGetByCityResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_country(self, client: Blink) -> None:
        click = client.links.clicks.get_by_country(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByCountryResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_country_with_all_params(self, client: Blink) -> None:
        click = client.links.clicks.get_by_country(
            link_id=0,
            domain_id=0,
            country="country",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByCountryResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_country(self, client: Blink) -> None:
        response = client.links.clicks.with_raw_response.get_by_country(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickGetByCountryResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_country(self, client: Blink) -> None:
        with client.links.clicks.with_streaming_response.get_by_country(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickGetByCountryResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_device(self, client: Blink) -> None:
        click = client.links.clicks.get_by_device(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByDeviceResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_device_with_all_params(self, client: Blink) -> None:
        click = client.links.clicks.get_by_device(
            link_id=0,
            domain_id=0,
            device="device",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByDeviceResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_device(self, client: Blink) -> None:
        response = client.links.clicks.with_raw_response.get_by_device(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickGetByDeviceResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_device(self, client: Blink) -> None:
        with client.links.clicks.with_streaming_response.get_by_device(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickGetByDeviceResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_referrer(self, client: Blink) -> None:
        click = client.links.clicks.get_by_referrer(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByReferrerResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_referrer_with_all_params(self, client: Blink) -> None:
        click = client.links.clicks.get_by_referrer(
            link_id=0,
            domain_id=0,
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            referrer="referrer",
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByReferrerResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_referrer(self, client: Blink) -> None:
        response = client.links.clicks.with_raw_response.get_by_referrer(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickGetByReferrerResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_referrer(self, client: Blink) -> None:
        with client.links.clicks.with_streaming_response.get_by_referrer(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickGetByReferrerResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_region(self, client: Blink) -> None:
        click = client.links.clicks.get_by_region(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByRegionResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_region_with_all_params(self, client: Blink) -> None:
        click = client.links.clicks.get_by_region(
            link_id=0,
            domain_id=0,
            country="country",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            region="region",
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByRegionResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_region(self, client: Blink) -> None:
        response = client.links.clicks.with_raw_response.get_by_region(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickGetByRegionResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_region(self, client: Blink) -> None:
        with client.links.clicks.with_streaming_response.get_by_region(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickGetByRegionResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_daily(self, client: Blink) -> None:
        click = client.links.clicks.get_daily(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetDailyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_daily_with_all_params(self, client: Blink) -> None:
        click = client.links.clicks.get_daily(
            link_id=0,
            domain_id=0,
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetDailyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_daily(self, client: Blink) -> None:
        response = client.links.clicks.with_raw_response.get_daily(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickGetDailyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_daily(self, client: Blink) -> None:
        with client.links.clicks.with_streaming_response.get_daily(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickGetDailyResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_hourly(self, client: Blink) -> None:
        click = client.links.clicks.get_hourly(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetHourlyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_hourly_with_all_params(self, client: Blink) -> None:
        click = client.links.clicks.get_hourly(
            link_id=0,
            domain_id=0,
            from_unix=0,
            to_unix=0,
        )
        assert_matches_type(ClickGetHourlyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_hourly(self, client: Blink) -> None:
        response = client.links.clicks.with_raw_response.get_hourly(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickGetHourlyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_hourly(self, client: Blink) -> None:
        with client.links.clicks.with_streaming_response.get_hourly(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickGetHourlyResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_total(self, client: Blink) -> None:
        click = client.links.clicks.get_total(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetTotalResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_total_with_all_params(self, client: Blink) -> None:
        click = client.links.clicks.get_total(
            link_id=0,
            domain_id=0,
            from_unix=0,
            to_unix=0,
        )
        assert_matches_type(ClickGetTotalResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_total(self, client: Blink) -> None:
        response = client.links.clicks.with_raw_response.get_total(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickGetTotalResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_total(self, client: Blink) -> None:
        with client.links.clicks.with_streaming_response.get_total(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickGetTotalResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClicks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_city(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_city(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByCityResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_city_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_city(
            link_id=0,
            domain_id=0,
            city="city",
            country="country",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            region="region",
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByCityResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_city(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.clicks.with_raw_response.get_by_city(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickGetByCityResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_city(self, async_client: AsyncBlink) -> None:
        async with async_client.links.clicks.with_streaming_response.get_by_city(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickGetByCityResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_country(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_country(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByCountryResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_country_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_country(
            link_id=0,
            domain_id=0,
            country="country",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByCountryResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_country(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.clicks.with_raw_response.get_by_country(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickGetByCountryResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_country(self, async_client: AsyncBlink) -> None:
        async with async_client.links.clicks.with_streaming_response.get_by_country(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickGetByCountryResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_device(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_device(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByDeviceResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_device_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_device(
            link_id=0,
            domain_id=0,
            device="device",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByDeviceResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_device(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.clicks.with_raw_response.get_by_device(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickGetByDeviceResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_device(self, async_client: AsyncBlink) -> None:
        async with async_client.links.clicks.with_streaming_response.get_by_device(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickGetByDeviceResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_referrer(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_referrer(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByReferrerResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_referrer_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_referrer(
            link_id=0,
            domain_id=0,
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            referrer="referrer",
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByReferrerResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_referrer(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.clicks.with_raw_response.get_by_referrer(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickGetByReferrerResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_referrer(self, async_client: AsyncBlink) -> None:
        async with async_client.links.clicks.with_streaming_response.get_by_referrer(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickGetByReferrerResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_region(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_region(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetByRegionResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_region_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_by_region(
            link_id=0,
            domain_id=0,
            country="country",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            region="region",
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetByRegionResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_region(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.clicks.with_raw_response.get_by_region(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickGetByRegionResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_region(self, async_client: AsyncBlink) -> None:
        async with async_client.links.clicks.with_streaming_response.get_by_region(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickGetByRegionResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_daily(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_daily(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetDailyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_daily_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_daily(
            link_id=0,
            domain_id=0,
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickGetDailyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_daily(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.clicks.with_raw_response.get_daily(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickGetDailyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_daily(self, async_client: AsyncBlink) -> None:
        async with async_client.links.clicks.with_streaming_response.get_daily(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickGetDailyResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_hourly(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_hourly(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetHourlyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_hourly_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_hourly(
            link_id=0,
            domain_id=0,
            from_unix=0,
            to_unix=0,
        )
        assert_matches_type(ClickGetHourlyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_hourly(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.clicks.with_raw_response.get_hourly(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickGetHourlyResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_hourly(self, async_client: AsyncBlink) -> None:
        async with async_client.links.clicks.with_streaming_response.get_hourly(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickGetHourlyResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_total(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_total(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(ClickGetTotalResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_total_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.links.clicks.get_total(
            link_id=0,
            domain_id=0,
            from_unix=0,
            to_unix=0,
        )
        assert_matches_type(ClickGetTotalResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_total(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.clicks.with_raw_response.get_total(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickGetTotalResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_total(self, async_client: AsyncBlink) -> None:
        async with async_client.links.clicks.with_streaming_response.get_total(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickGetTotalResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True
