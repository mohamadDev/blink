# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..types import (
    click_city_counts_params,
    click_daily_counts_params,
    click_device_counts_params,
    click_region_counts_params,
    click_country_counts_params,
    click_referrer_counts_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.click_city_counts_response import ClickCityCountsResponse
from ..types.click_daily_counts_response import ClickDailyCountsResponse
from ..types.click_device_counts_response import ClickDeviceCountsResponse
from ..types.click_region_counts_response import ClickRegionCountsResponse
from ..types.click_country_counts_response import ClickCountryCountsResponse
from ..types.click_referrer_counts_response import ClickReferrerCountsResponse

__all__ = ["ClicksResource", "AsyncClicksResource"]


class ClicksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClicksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blink-python#accessing-raw-response-data-eg-headers
        """
        return ClicksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClicksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blink-python#with_streaming_response
        """
        return ClicksResourceWithStreamingResponse(self)

    def city_counts(
        self,
        domain_id: int,
        *,
        city: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickCityCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by city. A domain ID must be specified in the
        url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by country, region, and city.

        Args:
          city: The city to query the values

          country: The country to query the values

          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          region: The region to query the values

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/clicks/city",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "city": city,
                        "country": country,
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "region": region,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_city_counts_params.ClickCityCountsParams,
                ),
            ),
            cast_to=ClickCityCountsResponse,
        )

    def country_counts(
        self,
        domain_id: int,
        *,
        country: str | NotGiven = NOT_GIVEN,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickCountryCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by country. A domain ID must be specified in the
        url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by country.

        Args:
          country: The country to query the values

          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/clicks/country",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_country_counts_params.ClickCountryCountsParams,
                ),
            ),
            cast_to=ClickCountryCountsResponse,
        )

    def daily_counts(
        self,
        domain_id: int,
        *,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickDailyCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by days. A domain ID must be specified in the
        URL. Optionally, you may provide a timestamp range as well as a page number. The
        timestamp is assumed to be in UTC format and follow unix standards. The max time
        period allowed to query is a year. If no timestamp range is set, the output will
        be the total count from a week ago til today. If only the starting timestamp is
        set, the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The counts are retrieved from a
        cached instance and therefore does not represent the real-time total but comes
        close. Result are sorted by day.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/clicks/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_daily_counts_params.ClickDailyCountsParams,
                ),
            ),
            cast_to=ClickDailyCountsResponse,
        )

    def device_counts(
        self,
        domain_id: int,
        *,
        device: str | NotGiven = NOT_GIVEN,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickDeviceCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by device. A domain ID must be specified in the
        url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by device.

        Args:
          device: The device to query the values

          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/clicks/device",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "device": device,
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_device_counts_params.ClickDeviceCountsParams,
                ),
            ),
            cast_to=ClickDeviceCountsResponse,
        )

    def referrer_counts(
        self,
        domain_id: int,
        *,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        referrer: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickReferrerCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by referrer. A domain ID must be specified in
        the url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by referrer.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results. Defaults to 1.

          referrer: The referrer to query the values

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/clicks/referrer",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "referrer": referrer,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_referrer_counts_params.ClickReferrerCountsParams,
                ),
            ),
            cast_to=ClickReferrerCountsResponse,
        )

    def region_counts(
        self,
        domain_id: int,
        *,
        country: str | NotGiven = NOT_GIVEN,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickRegionCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by region. A domain ID must be specified in the
        url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. TThe page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by country and region.

        Args:
          country: The country to query the values

          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          region: The region to query the values

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/clicks/region",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "region": region,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_region_counts_params.ClickRegionCountsParams,
                ),
            ),
            cast_to=ClickRegionCountsResponse,
        )


class AsyncClicksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClicksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blink-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClicksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClicksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blink-python#with_streaming_response
        """
        return AsyncClicksResourceWithStreamingResponse(self)

    async def city_counts(
        self,
        domain_id: int,
        *,
        city: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickCityCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by city. A domain ID must be specified in the
        url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by country, region, and city.

        Args:
          city: The city to query the values

          country: The country to query the values

          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          region: The region to query the values

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/clicks/city",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "city": city,
                        "country": country,
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "region": region,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_city_counts_params.ClickCityCountsParams,
                ),
            ),
            cast_to=ClickCityCountsResponse,
        )

    async def country_counts(
        self,
        domain_id: int,
        *,
        country: str | NotGiven = NOT_GIVEN,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickCountryCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by country. A domain ID must be specified in the
        url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by country.

        Args:
          country: The country to query the values

          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/clicks/country",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_country_counts_params.ClickCountryCountsParams,
                ),
            ),
            cast_to=ClickCountryCountsResponse,
        )

    async def daily_counts(
        self,
        domain_id: int,
        *,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickDailyCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by days. A domain ID must be specified in the
        URL. Optionally, you may provide a timestamp range as well as a page number. The
        timestamp is assumed to be in UTC format and follow unix standards. The max time
        period allowed to query is a year. If no timestamp range is set, the output will
        be the total count from a week ago til today. If only the starting timestamp is
        set, the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The counts are retrieved from a
        cached instance and therefore does not represent the real-time total but comes
        close. Result are sorted by day.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/clicks/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_daily_counts_params.ClickDailyCountsParams,
                ),
            ),
            cast_to=ClickDailyCountsResponse,
        )

    async def device_counts(
        self,
        domain_id: int,
        *,
        device: str | NotGiven = NOT_GIVEN,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickDeviceCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by device. A domain ID must be specified in the
        url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by device.

        Args:
          device: The device to query the values

          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/clicks/device",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "device": device,
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_device_counts_params.ClickDeviceCountsParams,
                ),
            ),
            cast_to=ClickDeviceCountsResponse,
        )

    async def referrer_counts(
        self,
        domain_id: int,
        *,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        referrer: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickReferrerCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by referrer. A domain ID must be specified in
        the url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. The page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by referrer.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results. Defaults to 1.

          referrer: The referrer to query the values

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/clicks/referrer",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "referrer": referrer,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_referrer_counts_params.ClickReferrerCountsParams,
                ),
            ),
            cast_to=ClickReferrerCountsResponse,
        )

    async def region_counts(
        self,
        domain_id: int,
        *,
        country: str | NotGiven = NOT_GIVEN,
        from_unix: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        label_id: Union[str, int] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        user_id: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickRegionCountsResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain grouped by region. A domain ID must be specified in the
        url with the option to set a timestamp range and a page to retrieve the
        paginated results. If the timestamp range exceeds a day the hour The timestamp
        is assumed to be in UTC format and follow unix standards. The max time period
        allowed to query is a year. If no timestamp range is set, the output will be the
        total count from a week ago til today. If only the starting timestamp is set,
        the result will be the counts from a year ahead of starting timestamp. The
        ending timestamp cannot be specified on its own without a starting timestamp.
        The range cannot exceed a year at a time. TThe page defaults to 1 with a max
        number of results set to a predefined number 50. The count is retrieved from a
        cached instance and therefore does not represent the real-time total. Results
        are sorted by popularity then by country and region.

        Args:
          country: The country to query the values

          from_unix: The UTC unix timestamp, query returns values after this date.

          keyword: Search link alias, notes, and redirect url for keyword

          label_id: An optional parameter containing the label's ID to query.

          page: The page of to query the values from the paginated results.

          region: The region to query the values

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          user_id: An optional parameter containing the user's ID to query. Elevated privileges are
              required to specify another. Defaults to current user. Valid value 'all' is
              allowed for users of elevated privileges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/clicks/region",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "from_unix": from_unix,
                        "keyword": keyword,
                        "label_id": label_id,
                        "page": page,
                        "region": region,
                        "to_unix": to_unix,
                        "user_id": user_id,
                    },
                    click_region_counts_params.ClickRegionCountsParams,
                ),
            ),
            cast_to=ClickRegionCountsResponse,
        )


class ClicksResourceWithRawResponse:
    def __init__(self, clicks: ClicksResource) -> None:
        self._clicks = clicks

        self.city_counts = to_raw_response_wrapper(
            clicks.city_counts,
        )
        self.country_counts = to_raw_response_wrapper(
            clicks.country_counts,
        )
        self.daily_counts = to_raw_response_wrapper(
            clicks.daily_counts,
        )
        self.device_counts = to_raw_response_wrapper(
            clicks.device_counts,
        )
        self.referrer_counts = to_raw_response_wrapper(
            clicks.referrer_counts,
        )
        self.region_counts = to_raw_response_wrapper(
            clicks.region_counts,
        )


class AsyncClicksResourceWithRawResponse:
    def __init__(self, clicks: AsyncClicksResource) -> None:
        self._clicks = clicks

        self.city_counts = async_to_raw_response_wrapper(
            clicks.city_counts,
        )
        self.country_counts = async_to_raw_response_wrapper(
            clicks.country_counts,
        )
        self.daily_counts = async_to_raw_response_wrapper(
            clicks.daily_counts,
        )
        self.device_counts = async_to_raw_response_wrapper(
            clicks.device_counts,
        )
        self.referrer_counts = async_to_raw_response_wrapper(
            clicks.referrer_counts,
        )
        self.region_counts = async_to_raw_response_wrapper(
            clicks.region_counts,
        )


class ClicksResourceWithStreamingResponse:
    def __init__(self, clicks: ClicksResource) -> None:
        self._clicks = clicks

        self.city_counts = to_streamed_response_wrapper(
            clicks.city_counts,
        )
        self.country_counts = to_streamed_response_wrapper(
            clicks.country_counts,
        )
        self.daily_counts = to_streamed_response_wrapper(
            clicks.daily_counts,
        )
        self.device_counts = to_streamed_response_wrapper(
            clicks.device_counts,
        )
        self.referrer_counts = to_streamed_response_wrapper(
            clicks.referrer_counts,
        )
        self.region_counts = to_streamed_response_wrapper(
            clicks.region_counts,
        )


class AsyncClicksResourceWithStreamingResponse:
    def __init__(self, clicks: AsyncClicksResource) -> None:
        self._clicks = clicks

        self.city_counts = async_to_streamed_response_wrapper(
            clicks.city_counts,
        )
        self.country_counts = async_to_streamed_response_wrapper(
            clicks.country_counts,
        )
        self.daily_counts = async_to_streamed_response_wrapper(
            clicks.daily_counts,
        )
        self.device_counts = async_to_streamed_response_wrapper(
            clicks.device_counts,
        )
        self.referrer_counts = async_to_streamed_response_wrapper(
            clicks.referrer_counts,
        )
        self.region_counts = async_to_streamed_response_wrapper(
            clicks.region_counts,
        )
