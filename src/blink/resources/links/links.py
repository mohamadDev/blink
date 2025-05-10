# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .clicks import (
    ClicksResource,
    AsyncClicksResource,
    ClicksResourceWithRawResponse,
    AsyncClicksResourceWithRawResponse,
    ClicksResourceWithStreamingResponse,
    AsyncClicksResourceWithStreamingResponse,
)
from ...types import (
    link_list_params,
    link_create_params,
    link_get_qr_params,
    link_update_params,
    link_validate_params,
    link_get_clicked_params,
    link_get_by_alias_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.link_list_response import LinkListResponse
from ...types.link_create_response import LinkCreateResponse
from ...types.link_update_response import LinkUpdateResponse
from ...types.link_retrieve_response import LinkRetrieveResponse
from ...types.link_validate_response import LinkValidateResponse
from ...types.link_get_clicked_response import LinkGetClickedResponse
from ...types.link_get_by_alias_response import LinkGetByAliasResponse
from ...types.link_get_raw_clicks_response import LinkGetRawClicksResponse

__all__ = ["LinksResource", "AsyncLinksResource"]


class LinksResource(SyncAPIResource):
    @cached_property
    def clicks(self) -> ClicksResource:
        return ClicksResource(self._client)

    @cached_property
    def with_raw_response(self) -> LinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return LinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return LinksResourceWithStreamingResponse(self)

    def create(
        self,
        domain_id: int,
        *,
        url: str,
        alias: str | NotGiven = NOT_GIVEN,
        archive_on: int | NotGiven = NOT_GIVEN,
        delete_on: int | NotGiven = NOT_GIVEN,
        dupe_check: int | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        notify_on_click: int | NotGiven = NOT_GIVEN,
        override_404_check: int | NotGiven = NOT_GIVEN,
        rand_alias_length: int | NotGiven = NOT_GIVEN,
        redirect_type: Literal[301, 307] | NotGiven = NOT_GIVEN,
        tags: Iterable[link_create_params.Tag] | NotGiven = NOT_GIVEN,
        utm_fields: object | NotGiven = NOT_GIVEN,
        utm_template_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkCreateResponse:
        """
        Will take the passed in URL and create a new shortened link based on the
        parameters that are passed in.

        Args:
          url: The long link. The URL protocol is optional.

          alias: Short string that will be used at the end of the domain to build your short
              link. Alias

          archive_on: GMT Unix timestamp defining the date to archive the link

          delete_on: GMT Unix timestamp defining the date to delete the link

          dupe_check: When set to 1, BL.INK will search for BL.INKs matching the url to be shortened.
              If one or more existing BL.INKs exist BL.INK will return the first already
              existing BL.INK. Otherwise it will create and return a new BL.INK

          notes: Notes to attach onto the link.

          notify_on_click: When set to 1, the user will be notified by email when this link has been
              clicked. The default is 0 no notification

          override_404_check: When set to 1, creation will proceed without checking that the long URL returns
              a 404 response

          rand_alias_length: The length of the randomly generated alias when one is not specified. It is
              ignored when an alias is specified.

          tags: Array of objects defining tags to be attached to the link

          utm_fields: Object defining key-value pairs for builder fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/{domain_id}/links",
            body=maybe_transform(
                {
                    "url": url,
                    "alias": alias,
                    "archive_on": archive_on,
                    "delete_on": delete_on,
                    "dupe_check": dupe_check,
                    "notes": notes,
                    "notify_on_click": notify_on_click,
                    "override_404_check": override_404_check,
                    "rand_alias_length": rand_alias_length,
                    "redirect_type": redirect_type,
                    "tags": tags,
                    "utm_fields": utm_fields,
                    "utm_template_id": utm_template_id,
                },
                link_create_params.LinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkCreateResponse,
        )

    def retrieve(
        self,
        link_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkRetrieveResponse:
        """Returns a short link.

        Each short link has a corresponding domain it belongs to
        and and individual id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/links/{link_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkRetrieveResponse,
        )

    def update(
        self,
        link_id: int,
        *,
        domain_id: int,
        body: Iterable[link_update_params.Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkUpdateResponse:
        """Will take an array of objects defining operations to be performed.

        This is based
        on the JSON patch format as defined in
        [RFC 6902](https://tools.ietf.org/html/rfc6902).

        # Supported Operations:

        - replace

        # Supported paths:

        - /alias
        - /url
        - /notes
        - /notify_on_click
        - /delete_on
        - /archive_on

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/{domain_id}/links/{link_id}",
            body=maybe_transform(body, Iterable[link_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkUpdateResponse,
        )

    def list(
        self,
        domain_id: int,
        *,
        from_unix: int | NotGiven = NOT_GIVEN,
        group_id: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        users: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkListResponse:
        """
        Searches for all links matching the query parameters that belong to the API user

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          group_id: Search links by group_id

          keyword: Search link alias, notes, and redirect url for keyword

          order: Orders results differently. Possible values 'oldest' or 'latest'. Defaults to
              'oldest'

          page: Page number

          tag: Search links by tag

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          url: long URL to search links by

          users: A flag for privileged users (domain admins or account admins) to specify
              returning all links from corresponding domain instead of just links they
              created. Example users=all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_unix": from_unix,
                        "group_id": group_id,
                        "keyword": keyword,
                        "order": order,
                        "page": page,
                        "tag": tag,
                        "to_unix": to_unix,
                        "url": url,
                        "users": users,
                    },
                    link_list_params.LinkListParams,
                ),
            ),
            cast_to=LinkListResponse,
        )

    def get_by_alias(
        self,
        path_alias: str,
        *,
        domain_id: int,
        query_alias: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkGetByAliasResponse:
        """Returns a short link.

        Each short link has a corresponding domain it belongs to
        and the provided.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_alias:
            raise ValueError(f"Expected a non-empty value for `path_alias` but received {path_alias!r}")
        return self._get(
            f"/{domain_id}/links/exists?alias={path_alias}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query_alias": query_alias}, link_get_by_alias_params.LinkGetByAliasParams),
            ),
            cast_to=LinkGetByAliasResponse,
        )

    def get_clicked(
        self,
        path_tag: str,
        *,
        domain_id: int,
        from_unix: int | NotGiven = NOT_GIVEN,
        from_user: str | NotGiven = NOT_GIVEN,
        group_id: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        query_tag: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkGetClickedResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the links that
        have been clicked within a specified timeframe. A user with elevated privileges
        automatically queries all user's links under the domain and must use the
        'from_user' flag to specify themselves. See request parameters. A user without
        these privileges will only be able to query their own links. A domain ID must be
        specified in the URL. You may provide a timestamp range as well as a page
        number. The timestamp is assumed to be in UTC format and follow unix standards.
        The max time period allowed to query is a year. If no timestamp range is set,
        the output will return any links clicked from a week ago til today. If only the
        starting timestamp is set, the result will be the clicked links from a year
        ahead of starting timestamp. The ending timestamp cannot be specified on its own
        without a starting timestamp. The range cannot exceed a year at a time. The page
        defaults to 1 with a max number of results set to a predefined number 50. **The
        click count is retrieved from a cached instance and therefore does not represent
        the real-time total**. Results are sorted by most clicked.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          from_user: An optional parameter. Valid value 'me' is allowed to only query for your links.

          group_id: Search links by group_id

          keyword: Search link alias, notes, and redirect url for keyword

          page: The page of to query the values from the paginated results. Defaults to 1.

          query_tag: Search links by tag

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_tag:
            raise ValueError(f"Expected a non-empty value for `path_tag` but received {path_tag!r}")
        return self._get(
            f"/{domain_id}/links/clicked?tag={path_tag}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_unix": from_unix,
                        "from_user": from_user,
                        "group_id": group_id,
                        "keyword": keyword,
                        "page": page,
                        "query_tag": query_tag,
                        "to_unix": to_unix,
                    },
                    link_get_clicked_params.LinkGetClickedParams,
                ),
            ),
            cast_to=LinkGetClickedResponse,
        )

    def get_qr(
        self,
        link_id: int,
        *,
        domain_id: int,
        format: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Returns QR data for specified link, domain in the specified format.

        The API will
        return the image data in binary format.

        Args:
          format: png (default), eps, svg

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return self._get(
            f"/{domain_id}/links/{link_id}/qr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, link_get_qr_params.LinkGetQrParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_raw_clicks(
        self,
        link_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkGetRawClicksResponse:
        """
        This endpoint retrieves a list of the clicks made on a link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/{domain_id}/links/{link_id}/rawclicks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkGetRawClicksResponse,
        )

    def validate(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkValidateResponse:
        """Will take the passed in URL and validate it.

        Args:
          url: URL encoded URL.

        It's a URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/links/validate",
            body=maybe_transform({"url": url}, link_validate_params.LinkValidateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkValidateResponse,
        )


class AsyncLinksResource(AsyncAPIResource):
    @cached_property
    def clicks(self) -> AsyncClicksResource:
        return AsyncClicksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return AsyncLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return AsyncLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        domain_id: int,
        *,
        url: str,
        alias: str | NotGiven = NOT_GIVEN,
        archive_on: int | NotGiven = NOT_GIVEN,
        delete_on: int | NotGiven = NOT_GIVEN,
        dupe_check: int | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        notify_on_click: int | NotGiven = NOT_GIVEN,
        override_404_check: int | NotGiven = NOT_GIVEN,
        rand_alias_length: int | NotGiven = NOT_GIVEN,
        redirect_type: Literal[301, 307] | NotGiven = NOT_GIVEN,
        tags: Iterable[link_create_params.Tag] | NotGiven = NOT_GIVEN,
        utm_fields: object | NotGiven = NOT_GIVEN,
        utm_template_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkCreateResponse:
        """
        Will take the passed in URL and create a new shortened link based on the
        parameters that are passed in.

        Args:
          url: The long link. The URL protocol is optional.

          alias: Short string that will be used at the end of the domain to build your short
              link. Alias

          archive_on: GMT Unix timestamp defining the date to archive the link

          delete_on: GMT Unix timestamp defining the date to delete the link

          dupe_check: When set to 1, BL.INK will search for BL.INKs matching the url to be shortened.
              If one or more existing BL.INKs exist BL.INK will return the first already
              existing BL.INK. Otherwise it will create and return a new BL.INK

          notes: Notes to attach onto the link.

          notify_on_click: When set to 1, the user will be notified by email when this link has been
              clicked. The default is 0 no notification

          override_404_check: When set to 1, creation will proceed without checking that the long URL returns
              a 404 response

          rand_alias_length: The length of the randomly generated alias when one is not specified. It is
              ignored when an alias is specified.

          tags: Array of objects defining tags to be attached to the link

          utm_fields: Object defining key-value pairs for builder fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/{domain_id}/links",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "alias": alias,
                    "archive_on": archive_on,
                    "delete_on": delete_on,
                    "dupe_check": dupe_check,
                    "notes": notes,
                    "notify_on_click": notify_on_click,
                    "override_404_check": override_404_check,
                    "rand_alias_length": rand_alias_length,
                    "redirect_type": redirect_type,
                    "tags": tags,
                    "utm_fields": utm_fields,
                    "utm_template_id": utm_template_id,
                },
                link_create_params.LinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkCreateResponse,
        )

    async def retrieve(
        self,
        link_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkRetrieveResponse:
        """Returns a short link.

        Each short link has a corresponding domain it belongs to
        and and individual id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/links/{link_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkRetrieveResponse,
        )

    async def update(
        self,
        link_id: int,
        *,
        domain_id: int,
        body: Iterable[link_update_params.Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkUpdateResponse:
        """Will take an array of objects defining operations to be performed.

        This is based
        on the JSON patch format as defined in
        [RFC 6902](https://tools.ietf.org/html/rfc6902).

        # Supported Operations:

        - replace

        # Supported paths:

        - /alias
        - /url
        - /notes
        - /notify_on_click
        - /delete_on
        - /archive_on

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/{domain_id}/links/{link_id}",
            body=await async_maybe_transform(body, Iterable[link_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkUpdateResponse,
        )

    async def list(
        self,
        domain_id: int,
        *,
        from_unix: int | NotGiven = NOT_GIVEN,
        group_id: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        users: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkListResponse:
        """
        Searches for all links matching the query parameters that belong to the API user

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          group_id: Search links by group_id

          keyword: Search link alias, notes, and redirect url for keyword

          order: Orders results differently. Possible values 'oldest' or 'latest'. Defaults to
              'oldest'

          page: Page number

          tag: Search links by tag

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          url: long URL to search links by

          users: A flag for privileged users (domain admins or account admins) to specify
              returning all links from corresponding domain instead of just links they
              created. Example users=all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_unix": from_unix,
                        "group_id": group_id,
                        "keyword": keyword,
                        "order": order,
                        "page": page,
                        "tag": tag,
                        "to_unix": to_unix,
                        "url": url,
                        "users": users,
                    },
                    link_list_params.LinkListParams,
                ),
            ),
            cast_to=LinkListResponse,
        )

    async def get_by_alias(
        self,
        path_alias: str,
        *,
        domain_id: int,
        query_alias: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkGetByAliasResponse:
        """Returns a short link.

        Each short link has a corresponding domain it belongs to
        and the provided.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_alias:
            raise ValueError(f"Expected a non-empty value for `path_alias` but received {path_alias!r}")
        return await self._get(
            f"/{domain_id}/links/exists?alias={path_alias}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_alias": query_alias}, link_get_by_alias_params.LinkGetByAliasParams
                ),
            ),
            cast_to=LinkGetByAliasResponse,
        )

    async def get_clicked(
        self,
        path_tag: str,
        *,
        domain_id: int,
        from_unix: int | NotGiven = NOT_GIVEN,
        from_user: str | NotGiven = NOT_GIVEN,
        group_id: int | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        query_tag: str | NotGiven = NOT_GIVEN,
        to_unix: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkGetClickedResponse:
        """
        (**Team, Business, and Enterprise Only**) This endpoint retrieves the links that
        have been clicked within a specified timeframe. A user with elevated privileges
        automatically queries all user's links under the domain and must use the
        'from_user' flag to specify themselves. See request parameters. A user without
        these privileges will only be able to query their own links. A domain ID must be
        specified in the URL. You may provide a timestamp range as well as a page
        number. The timestamp is assumed to be in UTC format and follow unix standards.
        The max time period allowed to query is a year. If no timestamp range is set,
        the output will return any links clicked from a week ago til today. If only the
        starting timestamp is set, the result will be the clicked links from a year
        ahead of starting timestamp. The ending timestamp cannot be specified on its own
        without a starting timestamp. The range cannot exceed a year at a time. The page
        defaults to 1 with a max number of results set to a predefined number 50. **The
        click count is retrieved from a cached instance and therefore does not represent
        the real-time total**. Results are sorted by most clicked.

        Args:
          from_unix: The UTC unix timestamp, query returns values after this date.

          from_user: An optional parameter. Valid value 'me' is allowed to only query for your links.

          group_id: Search links by group_id

          keyword: Search link alias, notes, and redirect url for keyword

          page: The page of to query the values from the paginated results. Defaults to 1.

          query_tag: Search links by tag

          to_unix: The UTC unix timestamp, query returns values before this date. Required if
              from_unix is specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_tag:
            raise ValueError(f"Expected a non-empty value for `path_tag` but received {path_tag!r}")
        return await self._get(
            f"/{domain_id}/links/clicked?tag={path_tag}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_unix": from_unix,
                        "from_user": from_user,
                        "group_id": group_id,
                        "keyword": keyword,
                        "page": page,
                        "query_tag": query_tag,
                        "to_unix": to_unix,
                    },
                    link_get_clicked_params.LinkGetClickedParams,
                ),
            ),
            cast_to=LinkGetClickedResponse,
        )

    async def get_qr(
        self,
        link_id: int,
        *,
        domain_id: int,
        format: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Returns QR data for specified link, domain in the specified format.

        The API will
        return the image data in binary format.

        Args:
          format: png (default), eps, svg

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return await self._get(
            f"/{domain_id}/links/{link_id}/qr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, link_get_qr_params.LinkGetQrParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_raw_clicks(
        self,
        link_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkGetRawClicksResponse:
        """
        This endpoint retrieves a list of the clicks made on a link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/{domain_id}/links/{link_id}/rawclicks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkGetRawClicksResponse,
        )

    async def validate(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkValidateResponse:
        """Will take the passed in URL and validate it.

        Args:
          url: URL encoded URL.

        It's a URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/links/validate",
            body=await async_maybe_transform({"url": url}, link_validate_params.LinkValidateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkValidateResponse,
        )


class LinksResourceWithRawResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.create = to_raw_response_wrapper(
            links.create,
        )
        self.retrieve = to_raw_response_wrapper(
            links.retrieve,
        )
        self.update = to_raw_response_wrapper(
            links.update,
        )
        self.list = to_raw_response_wrapper(
            links.list,
        )
        self.get_by_alias = to_raw_response_wrapper(
            links.get_by_alias,
        )
        self.get_clicked = to_raw_response_wrapper(
            links.get_clicked,
        )
        self.get_qr = to_custom_raw_response_wrapper(
            links.get_qr,
            BinaryAPIResponse,
        )
        self.get_raw_clicks = to_raw_response_wrapper(
            links.get_raw_clicks,
        )
        self.validate = to_raw_response_wrapper(
            links.validate,
        )

    @cached_property
    def clicks(self) -> ClicksResourceWithRawResponse:
        return ClicksResourceWithRawResponse(self._links.clicks)


class AsyncLinksResourceWithRawResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.create = async_to_raw_response_wrapper(
            links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            links.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            links.update,
        )
        self.list = async_to_raw_response_wrapper(
            links.list,
        )
        self.get_by_alias = async_to_raw_response_wrapper(
            links.get_by_alias,
        )
        self.get_clicked = async_to_raw_response_wrapper(
            links.get_clicked,
        )
        self.get_qr = async_to_custom_raw_response_wrapper(
            links.get_qr,
            AsyncBinaryAPIResponse,
        )
        self.get_raw_clicks = async_to_raw_response_wrapper(
            links.get_raw_clicks,
        )
        self.validate = async_to_raw_response_wrapper(
            links.validate,
        )

    @cached_property
    def clicks(self) -> AsyncClicksResourceWithRawResponse:
        return AsyncClicksResourceWithRawResponse(self._links.clicks)


class LinksResourceWithStreamingResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.create = to_streamed_response_wrapper(
            links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            links.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            links.update,
        )
        self.list = to_streamed_response_wrapper(
            links.list,
        )
        self.get_by_alias = to_streamed_response_wrapper(
            links.get_by_alias,
        )
        self.get_clicked = to_streamed_response_wrapper(
            links.get_clicked,
        )
        self.get_qr = to_custom_streamed_response_wrapper(
            links.get_qr,
            StreamedBinaryAPIResponse,
        )
        self.get_raw_clicks = to_streamed_response_wrapper(
            links.get_raw_clicks,
        )
        self.validate = to_streamed_response_wrapper(
            links.validate,
        )

    @cached_property
    def clicks(self) -> ClicksResourceWithStreamingResponse:
        return ClicksResourceWithStreamingResponse(self._links.clicks)


class AsyncLinksResourceWithStreamingResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.create = async_to_streamed_response_wrapper(
            links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            links.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            links.update,
        )
        self.list = async_to_streamed_response_wrapper(
            links.list,
        )
        self.get_by_alias = async_to_streamed_response_wrapper(
            links.get_by_alias,
        )
        self.get_clicked = async_to_streamed_response_wrapper(
            links.get_clicked,
        )
        self.get_qr = async_to_custom_streamed_response_wrapper(
            links.get_qr,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_raw_clicks = async_to_streamed_response_wrapper(
            links.get_raw_clicks,
        )
        self.validate = async_to_streamed_response_wrapper(
            links.validate,
        )

    @cached_property
    def clicks(self) -> AsyncClicksResourceWithStreamingResponse:
        return AsyncClicksResourceWithStreamingResponse(self._links.clicks)
