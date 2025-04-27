# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from blink.types import (
    ClickCityCountsResponse,
    ClickDailyCountsResponse,
    ClickDeviceCountsResponse,
    ClickRegionCountsResponse,
    ClickCountryCountsResponse,
    ClickReferrerCountsResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClicks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_city_counts(self, client: Blink) -> None:
        click = client.clicks.city_counts(
            domain_id=0,
        )
        assert_matches_type(ClickCityCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_city_counts_with_all_params(self, client: Blink) -> None:
        click = client.clicks.city_counts(
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
        assert_matches_type(ClickCityCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_city_counts(self, client: Blink) -> None:
        response = client.clicks.with_raw_response.city_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickCityCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_city_counts(self, client: Blink) -> None:
        with client.clicks.with_streaming_response.city_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickCityCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_country_counts(self, client: Blink) -> None:
        click = client.clicks.country_counts(
            domain_id=0,
        )
        assert_matches_type(ClickCountryCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_country_counts_with_all_params(self, client: Blink) -> None:
        click = client.clicks.country_counts(
            domain_id=0,
            country="country",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickCountryCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_country_counts(self, client: Blink) -> None:
        response = client.clicks.with_raw_response.country_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickCountryCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_country_counts(self, client: Blink) -> None:
        with client.clicks.with_streaming_response.country_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickCountryCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_daily_counts(self, client: Blink) -> None:
        click = client.clicks.daily_counts(
            domain_id=0,
        )
        assert_matches_type(ClickDailyCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_daily_counts_with_all_params(self, client: Blink) -> None:
        click = client.clicks.daily_counts(
            domain_id=0,
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickDailyCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_daily_counts(self, client: Blink) -> None:
        response = client.clicks.with_raw_response.daily_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickDailyCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_daily_counts(self, client: Blink) -> None:
        with client.clicks.with_streaming_response.daily_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickDailyCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_device_counts(self, client: Blink) -> None:
        click = client.clicks.device_counts(
            domain_id=0,
        )
        assert_matches_type(ClickDeviceCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_device_counts_with_all_params(self, client: Blink) -> None:
        click = client.clicks.device_counts(
            domain_id=0,
            device="device",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickDeviceCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_device_counts(self, client: Blink) -> None:
        response = client.clicks.with_raw_response.device_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickDeviceCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_device_counts(self, client: Blink) -> None:
        with client.clicks.with_streaming_response.device_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickDeviceCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_referrer_counts(self, client: Blink) -> None:
        click = client.clicks.referrer_counts(
            domain_id=0,
        )
        assert_matches_type(ClickReferrerCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_referrer_counts_with_all_params(self, client: Blink) -> None:
        click = client.clicks.referrer_counts(
            domain_id=0,
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            referrer="referrer",
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickReferrerCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_referrer_counts(self, client: Blink) -> None:
        response = client.clicks.with_raw_response.referrer_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickReferrerCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_referrer_counts(self, client: Blink) -> None:
        with client.clicks.with_streaming_response.referrer_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickReferrerCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_region_counts(self, client: Blink) -> None:
        click = client.clicks.region_counts(
            domain_id=0,
        )
        assert_matches_type(ClickRegionCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_region_counts_with_all_params(self, client: Blink) -> None:
        click = client.clicks.region_counts(
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
        assert_matches_type(ClickRegionCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_region_counts(self, client: Blink) -> None:
        response = client.clicks.with_raw_response.region_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = response.parse()
        assert_matches_type(ClickRegionCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_region_counts(self, client: Blink) -> None:
        with client.clicks.with_streaming_response.region_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = response.parse()
            assert_matches_type(ClickRegionCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClicks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_city_counts(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.city_counts(
            domain_id=0,
        )
        assert_matches_type(ClickCityCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_city_counts_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.city_counts(
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
        assert_matches_type(ClickCityCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_city_counts(self, async_client: AsyncBlink) -> None:
        response = await async_client.clicks.with_raw_response.city_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickCityCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_city_counts(self, async_client: AsyncBlink) -> None:
        async with async_client.clicks.with_streaming_response.city_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickCityCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_country_counts(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.country_counts(
            domain_id=0,
        )
        assert_matches_type(ClickCountryCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_country_counts_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.country_counts(
            domain_id=0,
            country="country",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickCountryCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_country_counts(self, async_client: AsyncBlink) -> None:
        response = await async_client.clicks.with_raw_response.country_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickCountryCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_country_counts(self, async_client: AsyncBlink) -> None:
        async with async_client.clicks.with_streaming_response.country_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickCountryCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_daily_counts(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.daily_counts(
            domain_id=0,
        )
        assert_matches_type(ClickDailyCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_daily_counts_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.daily_counts(
            domain_id=0,
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickDailyCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_daily_counts(self, async_client: AsyncBlink) -> None:
        response = await async_client.clicks.with_raw_response.daily_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickDailyCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_daily_counts(self, async_client: AsyncBlink) -> None:
        async with async_client.clicks.with_streaming_response.daily_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickDailyCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_counts(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.device_counts(
            domain_id=0,
        )
        assert_matches_type(ClickDeviceCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_counts_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.device_counts(
            domain_id=0,
            device="device",
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickDeviceCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_device_counts(self, async_client: AsyncBlink) -> None:
        response = await async_client.clicks.with_raw_response.device_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickDeviceCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_device_counts(self, async_client: AsyncBlink) -> None:
        async with async_client.clicks.with_streaming_response.device_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickDeviceCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_referrer_counts(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.referrer_counts(
            domain_id=0,
        )
        assert_matches_type(ClickReferrerCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_referrer_counts_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.referrer_counts(
            domain_id=0,
            from_unix=0,
            keyword="keyword",
            label_id="string",
            page=0,
            referrer="referrer",
            to_unix=0,
            user_id="string",
        )
        assert_matches_type(ClickReferrerCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_referrer_counts(self, async_client: AsyncBlink) -> None:
        response = await async_client.clicks.with_raw_response.referrer_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickReferrerCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_referrer_counts(self, async_client: AsyncBlink) -> None:
        async with async_client.clicks.with_streaming_response.referrer_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickReferrerCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_region_counts(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.region_counts(
            domain_id=0,
        )
        assert_matches_type(ClickRegionCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_region_counts_with_all_params(self, async_client: AsyncBlink) -> None:
        click = await async_client.clicks.region_counts(
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
        assert_matches_type(ClickRegionCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_region_counts(self, async_client: AsyncBlink) -> None:
        response = await async_client.clicks.with_raw_response.region_counts(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        click = await response.parse()
        assert_matches_type(ClickRegionCountsResponse, click, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_region_counts(self, async_client: AsyncBlink) -> None:
        async with async_client.clicks.with_streaming_response.region_counts(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            click = await response.parse()
            assert_matches_type(ClickRegionCountsResponse, click, path=["response"])

        assert cast(Any, response.is_closed) is True
