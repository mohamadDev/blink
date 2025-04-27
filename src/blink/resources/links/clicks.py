# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.links import (
    click_get_daily_params,
    click_get_total_params,
    click_get_hourly_params,
    click_get_by_city_params,
    click_get_by_device_params,
    click_get_by_region_params,
    click_get_by_country_params,
    click_get_by_referrer_params,
)
from ..._base_client import make_request_options
from ...types.links.click_get_daily_response import ClickGetDailyResponse
from ...types.links.click_get_total_response import ClickGetTotalResponse
from ...types.links.click_get_hourly_response import ClickGetHourlyResponse
from ...types.links.click_get_by_city_response import ClickGetByCityResponse
from ...types.links.click_get_by_device_response import ClickGetByDeviceResponse
from ...types.links.click_get_by_region_response import ClickGetByRegionResponse
from ...types.links.click_get_by_country_response import ClickGetByCountryResponse
from ...types.links.click_get_by_referrer_response import ClickGetByReferrerResponse

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

    def get_by_city(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByCityResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by city. A link ID and domain ID must be specified
        in the url parameters with the option to set a timestamp range and a page to
        retrieve the paginated results. If the timestamp range exceeds a day the hour
        The timestamp is assumed to be in UTC format and follow unix standards. The max
        time period allowed to query is a year. If no timestamp range is set, the output
        will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. The page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by country, region, and city.

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
            f"/{domain_id}/links/{link_id}/clicks/city",
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
                    click_get_by_city_params.ClickGetByCityParams,
                ),
            ),
            cast_to=ClickGetByCityResponse,
        )

    def get_by_country(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByCountryResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by country. A link ID and domain ID must be
        specified in the url parameters with the option to set a timestamp range and a
        page to retrieve the paginated results. If the timestamp range exceeds a day the
        hour The timestamp is assumed to be in UTC format and follow unix standards. The
        max time period allowed to query is a year. If no timestamp range is set, the
        output will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. The page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by country.

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
            f"/{domain_id}/links/{link_id}/clicks/country",
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
                    click_get_by_country_params.ClickGetByCountryParams,
                ),
            ),
            cast_to=ClickGetByCountryResponse,
        )

    def get_by_device(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByDeviceResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by device. A link ID and domain ID must be
        specified in the url parameters with the option to set a timestamp range and a
        page to retrieve the paginated results. If the timestamp range exceeds a day the
        hour The timestamp is assumed to be in UTC format and follow unix standards. The
        max time period allowed to query is a year. If no timestamp range is set, the
        output will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. The page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by device.

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
            f"/{domain_id}/links/{link_id}/clicks/device",
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
                    click_get_by_device_params.ClickGetByDeviceParams,
                ),
            ),
            cast_to=ClickGetByDeviceResponse,
        )

    def get_by_referrer(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByReferrerResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by referrer. A link ID and domain ID must be
        specified in the url parameters with the option to set a timestamp range and a
        page to retrieve the paginated results. If the timestamp range exceeds a day the
        hour The timestamp is assumed to be in UTC format and follow unix standards. The
        max time period allowed to query is a year. If no timestamp range is set, the
        output will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. The page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by referrer.

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
            f"/{domain_id}/links/{link_id}/clicks/referrer",
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
                    click_get_by_referrer_params.ClickGetByReferrerParams,
                ),
            ),
            cast_to=ClickGetByReferrerResponse,
        )

    def get_by_region(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByRegionResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by region. A link ID and domain ID must be
        specified in the url parameters with the option to set a timestamp range and a
        page to retrieve the paginated results. If the timestamp range exceeds a day the
        hour The timestamp is assumed to be in UTC format and follow unix standards. The
        max time period allowed to query is a year. If no timestamp range is set, the
        output will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. TThe page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by country and region.

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
            f"/{domain_id}/links/{link_id}/clicks/region",
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
                    click_get_by_region_params.ClickGetByRegionParams,
                ),
            ),
            cast_to=ClickGetByRegionResponse,
        )

    def get_daily(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetDailyResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain link grouped by days. A domain ID and link ID must be
        specified in the URL. Optionally, you may provide a timestamp range as well as a
        page number. The timestamp is assumed to be in UTC format and follow unix
        standards. The max time period allowed to query is a year. If no timestamp range
        is set, the output will be the total count from a week ago til today. If only
        the starting timestamp is set, the result will be the counts from a year ahead
        of starting timestamp. The ending timestamp cannot be specified on its own
        without a starting timestamp. The range cannot exceed a year at a time. The page
        defaults to 1 with a max number of results set to a predefined number 50. The
        counts are retrieved from a cached instance and therefore does not represent the
        real-time total but comes close. Result are sorted by day.

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
            f"/{domain_id}/links/{link_id}/clicks/daily",
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
                    click_get_daily_params.ClickGetDailyParams,
                ),
            ),
            cast_to=ClickGetDailyResponse,
        )

    def get_hourly(
        self,
        link_id: int,
        *,
        domain_id: int,
        from_unix: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickGetHourlyResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by hours. The hours are in the military time range
        from 0 - 23. Over a span of days this response reports the total clicks on a
        link for each hour. For example if a link has 5 clicks yesterday at 5pm and 2
        clicks at 5pm today and if the range is set for only those days. The report for
        hour:17 is 7 clicks; the sum of the clicks for that hour between the two days. A
        link ID and domain ID must be specified in the url parameters with the option to
        set a timestamp range. The timestamp is assumed to be in UTC format and follow
        unix standards. The max time period allowed to query is a year. If no timestamp
        range is set, the output will be the total count from a week ago til today. If
        only the starting timestamp is set, the result will be the counts from a year
        ahead of starting timestamp. The ending timestamp cannot be specified on its own
        without a starting timestamp. The range cannot exceed a year at a time. Result
        are sorted by hour.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/links/{link_id}/clicks/hourly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_unix": from_unix,
                        "to_unix": to_unix,
                    },
                    click_get_hourly_params.ClickGetHourlyParams,
                ),
            ),
            cast_to=ClickGetHourlyResponse,
        )

    def get_total(
        self,
        link_id: int,
        *,
        domain_id: int,
        from_unix: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickGetTotalResponse:
        """This endpoint retrieves the total and total unique clicks made on a link.

        A
        unique click is a click that comes from an individual IP address. If a person
        clicks twice from the same internet device that has a corresponding IP address
        the latter click will not be counted in the total unique clicks result. The
        total count and the total unique count are only displayed when no filter is
        applied, however the filtered count is only present when a timestamp is set. A
        link ID and domain ID must be specified in the url parameters with the option to
        set a timestamp range. The timestamp is assumed to be in UTC format and follow
        unix standards. The max time period allowed to query is a year. If no timestamp
        range is set, the output will be the total unique and total counts. If only the
        starting timestamp is set, the result will be the counts from a year ahead of
        starting timestamp. The ending timestamp cannot be specified on its own without
        a starting timestamp. The range cannot exceed a year at a time.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/links/{link_id}/clicks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_unix": from_unix,
                        "to_unix": to_unix,
                    },
                    click_get_total_params.ClickGetTotalParams,
                ),
            ),
            cast_to=ClickGetTotalResponse,
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

    async def get_by_city(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByCityResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by city. A link ID and domain ID must be specified
        in the url parameters with the option to set a timestamp range and a page to
        retrieve the paginated results. If the timestamp range exceeds a day the hour
        The timestamp is assumed to be in UTC format and follow unix standards. The max
        time period allowed to query is a year. If no timestamp range is set, the output
        will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. The page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by country, region, and city.

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
            f"/{domain_id}/links/{link_id}/clicks/city",
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
                    click_get_by_city_params.ClickGetByCityParams,
                ),
            ),
            cast_to=ClickGetByCityResponse,
        )

    async def get_by_country(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByCountryResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by country. A link ID and domain ID must be
        specified in the url parameters with the option to set a timestamp range and a
        page to retrieve the paginated results. If the timestamp range exceeds a day the
        hour The timestamp is assumed to be in UTC format and follow unix standards. The
        max time period allowed to query is a year. If no timestamp range is set, the
        output will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. The page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by country.

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
            f"/{domain_id}/links/{link_id}/clicks/country",
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
                    click_get_by_country_params.ClickGetByCountryParams,
                ),
            ),
            cast_to=ClickGetByCountryResponse,
        )

    async def get_by_device(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByDeviceResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by device. A link ID and domain ID must be
        specified in the url parameters with the option to set a timestamp range and a
        page to retrieve the paginated results. If the timestamp range exceeds a day the
        hour The timestamp is assumed to be in UTC format and follow unix standards. The
        max time period allowed to query is a year. If no timestamp range is set, the
        output will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. The page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by device.

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
            f"/{domain_id}/links/{link_id}/clicks/device",
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
                    click_get_by_device_params.ClickGetByDeviceParams,
                ),
            ),
            cast_to=ClickGetByDeviceResponse,
        )

    async def get_by_referrer(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByReferrerResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by referrer. A link ID and domain ID must be
        specified in the url parameters with the option to set a timestamp range and a
        page to retrieve the paginated results. If the timestamp range exceeds a day the
        hour The timestamp is assumed to be in UTC format and follow unix standards. The
        max time period allowed to query is a year. If no timestamp range is set, the
        output will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. The page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by referrer.

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
            f"/{domain_id}/links/{link_id}/clicks/referrer",
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
                    click_get_by_referrer_params.ClickGetByReferrerParams,
                ),
            ),
            cast_to=ClickGetByReferrerResponse,
        )

    async def get_by_region(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetByRegionResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by region. A link ID and domain ID must be
        specified in the url parameters with the option to set a timestamp range and a
        page to retrieve the paginated results. If the timestamp range exceeds a day the
        hour The timestamp is assumed to be in UTC format and follow unix standards. The
        max time period allowed to query is a year. If no timestamp range is set, the
        output will be the total count from a week ago til today. If only the starting
        timestamp is set, the result will be the counts from a year ahead of starting
        timestamp. The ending timestamp cannot be specified on its own without a
        starting timestamp. The range cannot exceed a year at a time. TThe page defaults
        to 1 with a max number of results set to a predefined number 50. The count is
        retrieved from a cached instance and therefore does not represent the real-time
        total. Results are sorted by popularity then by country and region.

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
            f"/{domain_id}/links/{link_id}/clicks/region",
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
                    click_get_by_region_params.ClickGetByRegionParams,
                ),
            ),
            cast_to=ClickGetByRegionResponse,
        )

    async def get_daily(
        self,
        link_id: int,
        *,
        domain_id: int,
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
    ) -> ClickGetDailyResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a domain link grouped by days. A domain ID and link ID must be
        specified in the URL. Optionally, you may provide a timestamp range as well as a
        page number. The timestamp is assumed to be in UTC format and follow unix
        standards. The max time period allowed to query is a year. If no timestamp range
        is set, the output will be the total count from a week ago til today. If only
        the starting timestamp is set, the result will be the counts from a year ahead
        of starting timestamp. The ending timestamp cannot be specified on its own
        without a starting timestamp. The range cannot exceed a year at a time. The page
        defaults to 1 with a max number of results set to a predefined number 50. The
        counts are retrieved from a cached instance and therefore does not represent the
        real-time total but comes close. Result are sorted by day.

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
            f"/{domain_id}/links/{link_id}/clicks/daily",
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
                    click_get_daily_params.ClickGetDailyParams,
                ),
            ),
            cast_to=ClickGetDailyResponse,
        )

    async def get_hourly(
        self,
        link_id: int,
        *,
        domain_id: int,
        from_unix: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickGetHourlyResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the total
        clicks made on a link grouped by hours. The hours are in the military time range
        from 0 - 23. Over a span of days this response reports the total clicks on a
        link for each hour. For example if a link has 5 clicks yesterday at 5pm and 2
        clicks at 5pm today and if the range is set for only those days. The report for
        hour:17 is 7 clicks; the sum of the clicks for that hour between the two days. A
        link ID and domain ID must be specified in the url parameters with the option to
        set a timestamp range. The timestamp is assumed to be in UTC format and follow
        unix standards. The max time period allowed to query is a year. If no timestamp
        range is set, the output will be the total count from a week ago til today. If
        only the starting timestamp is set, the result will be the counts from a year
        ahead of starting timestamp. The ending timestamp cannot be specified on its own
        without a starting timestamp. The range cannot exceed a year at a time. Result
        are sorted by hour.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/links/{link_id}/clicks/hourly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_unix": from_unix,
                        "to_unix": to_unix,
                    },
                    click_get_hourly_params.ClickGetHourlyParams,
                ),
            ),
            cast_to=ClickGetHourlyResponse,
        )

    async def get_total(
        self,
        link_id: int,
        *,
        domain_id: int,
        from_unix: int | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClickGetTotalResponse:
        """This endpoint retrieves the total and total unique clicks made on a link.

        A
        unique click is a click that comes from an individual IP address. If a person
        clicks twice from the same internet device that has a corresponding IP address
        the latter click will not be counted in the total unique clicks result. The
        total count and the total unique count are only displayed when no filter is
        applied, however the filtered count is only present when a timestamp is set. A
        link ID and domain ID must be specified in the url parameters with the option to
        set a timestamp range. The timestamp is assumed to be in UTC format and follow
        unix standards. The max time period allowed to query is a year. If no timestamp
        range is set, the output will be the total unique and total counts. If only the
        starting timestamp is set, the result will be the counts from a year ahead of
        starting timestamp. The ending timestamp cannot be specified on its own without
        a starting timestamp. The range cannot exceed a year at a time.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/links/{link_id}/clicks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_unix": from_unix,
                        "to_unix": to_unix,
                    },
                    click_get_total_params.ClickGetTotalParams,
                ),
            ),
            cast_to=ClickGetTotalResponse,
        )


class ClicksResourceWithRawResponse:
    def __init__(self, clicks: ClicksResource) -> None:
        self._clicks = clicks

        self.get_by_city = to_raw_response_wrapper(
            clicks.get_by_city,
        )
        self.get_by_country = to_raw_response_wrapper(
            clicks.get_by_country,
        )
        self.get_by_device = to_raw_response_wrapper(
            clicks.get_by_device,
        )
        self.get_by_referrer = to_raw_response_wrapper(
            clicks.get_by_referrer,
        )
        self.get_by_region = to_raw_response_wrapper(
            clicks.get_by_region,
        )
        self.get_daily = to_raw_response_wrapper(
            clicks.get_daily,
        )
        self.get_hourly = to_raw_response_wrapper(
            clicks.get_hourly,
        )
        self.get_total = to_raw_response_wrapper(
            clicks.get_total,
        )


class AsyncClicksResourceWithRawResponse:
    def __init__(self, clicks: AsyncClicksResource) -> None:
        self._clicks = clicks

        self.get_by_city = async_to_raw_response_wrapper(
            clicks.get_by_city,
        )
        self.get_by_country = async_to_raw_response_wrapper(
            clicks.get_by_country,
        )
        self.get_by_device = async_to_raw_response_wrapper(
            clicks.get_by_device,
        )
        self.get_by_referrer = async_to_raw_response_wrapper(
            clicks.get_by_referrer,
        )
        self.get_by_region = async_to_raw_response_wrapper(
            clicks.get_by_region,
        )
        self.get_daily = async_to_raw_response_wrapper(
            clicks.get_daily,
        )
        self.get_hourly = async_to_raw_response_wrapper(
            clicks.get_hourly,
        )
        self.get_total = async_to_raw_response_wrapper(
            clicks.get_total,
        )


class ClicksResourceWithStreamingResponse:
    def __init__(self, clicks: ClicksResource) -> None:
        self._clicks = clicks

        self.get_by_city = to_streamed_response_wrapper(
            clicks.get_by_city,
        )
        self.get_by_country = to_streamed_response_wrapper(
            clicks.get_by_country,
        )
        self.get_by_device = to_streamed_response_wrapper(
            clicks.get_by_device,
        )
        self.get_by_referrer = to_streamed_response_wrapper(
            clicks.get_by_referrer,
        )
        self.get_by_region = to_streamed_response_wrapper(
            clicks.get_by_region,
        )
        self.get_daily = to_streamed_response_wrapper(
            clicks.get_daily,
        )
        self.get_hourly = to_streamed_response_wrapper(
            clicks.get_hourly,
        )
        self.get_total = to_streamed_response_wrapper(
            clicks.get_total,
        )


class AsyncClicksResourceWithStreamingResponse:
    def __init__(self, clicks: AsyncClicksResource) -> None:
        self._clicks = clicks

        self.get_by_city = async_to_streamed_response_wrapper(
            clicks.get_by_city,
        )
        self.get_by_country = async_to_streamed_response_wrapper(
            clicks.get_by_country,
        )
        self.get_by_device = async_to_streamed_response_wrapper(
            clicks.get_by_device,
        )
        self.get_by_referrer = async_to_streamed_response_wrapper(
            clicks.get_by_referrer,
        )
        self.get_by_region = async_to_streamed_response_wrapper(
            clicks.get_by_region,
        )
        self.get_daily = async_to_streamed_response_wrapper(
            clicks.get_daily,
        )
        self.get_hourly = async_to_streamed_response_wrapper(
            clicks.get_hourly,
        )
        self.get_total = async_to_streamed_response_wrapper(
            clicks.get_total,
        )
