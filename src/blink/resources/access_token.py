# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import overload

import httpx

from ..types import access_token_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.access_token_create_response import AccessTokenCreateResponse

__all__ = ["AccessTokenResource", "AsyncAccessTokenResource"]


class AccessTokenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return AccessTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return AccessTokenResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTokenCreateResponse:
        """Returns a valid authentication token.

        When requesting a token it will return an
        existing not-expired token. If an existing expired token exists, it will
        generate a new token and return that. This will accept either a password for the
        account or a refresh token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        email: str,
        refresh_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTokenCreateResponse:
        """Returns a valid authentication token.

        When requesting a token it will return an
        existing not-expired token. If an existing expired token exists, it will
        generate a new token and return that. This will accept either a password for the
        account or a refresh token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["email", "password"], ["email", "refresh_token"])
    def create(
        self,
        *,
        email: str,
        password: str | NotGiven = NOT_GIVEN,
        refresh_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTokenCreateResponse:
        return self._post(
            "/access_token",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "refresh_token": refresh_token,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessTokenCreateResponse,
        )


class AsyncAccessTokenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return AsyncAccessTokenResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTokenCreateResponse:
        """Returns a valid authentication token.

        When requesting a token it will return an
        existing not-expired token. If an existing expired token exists, it will
        generate a new token and return that. This will accept either a password for the
        account or a refresh token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        email: str,
        refresh_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTokenCreateResponse:
        """Returns a valid authentication token.

        When requesting a token it will return an
        existing not-expired token. If an existing expired token exists, it will
        generate a new token and return that. This will accept either a password for the
        account or a refresh token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["email", "password"], ["email", "refresh_token"])
    async def create(
        self,
        *,
        email: str,
        password: str | NotGiven = NOT_GIVEN,
        refresh_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessTokenCreateResponse:
        return await self._post(
            "/access_token",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "refresh_token": refresh_token,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessTokenCreateResponse,
        )


class AccessTokenResourceWithRawResponse:
    def __init__(self, access_token: AccessTokenResource) -> None:
        self._access_token = access_token

        self.create = to_raw_response_wrapper(
            access_token.create,
        )


class AsyncAccessTokenResourceWithRawResponse:
    def __init__(self, access_token: AsyncAccessTokenResource) -> None:
        self._access_token = access_token

        self.create = async_to_raw_response_wrapper(
            access_token.create,
        )


class AccessTokenResourceWithStreamingResponse:
    def __init__(self, access_token: AccessTokenResource) -> None:
        self._access_token = access_token

        self.create = to_streamed_response_wrapper(
            access_token.create,
        )


class AsyncAccessTokenResourceWithStreamingResponse:
    def __init__(self, access_token: AsyncAccessTokenResource) -> None:
        self._access_token = access_token

        self.create = async_to_streamed_response_wrapper(
            access_token.create,
        )
