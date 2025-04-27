# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    tags,
    users,
    clicks,
    groups,
    domains,
    error_codes,
    access_token,
    utm_templates,
    validate_login,
    domains_domain_name,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.links import links

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Blink", "AsyncBlink", "Client", "AsyncClient"]


class Blink(SyncAPIClient):
    validate_login: validate_login.ValidateLoginResource
    access_token: access_token.AccessTokenResource
    users: users.UsersResource
    links: links.LinksResource
    clicks: clicks.ClicksResource
    tags: tags.TagsResource
    domains: domains.DomainsResource
    domains_domain_name: domains_domain_name.DomainsDomainNameResource
    utm_templates: utm_templates.UtmTemplatesResource
    groups: groups.GroupsResource
    error_codes: error_codes.ErrorCodesResource
    with_raw_response: BlinkWithRawResponse
    with_streaming_response: BlinkWithStreamedResponse

    # client options
    instance: str

    def __init__(
        self,
        *,
        instance: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Blink client instance.

        This automatically infers the `instance` argument from the `BLINK_INSTANCE` environment variable if it is not provided.
        """
        if instance is None:
            instance = os.environ.get("BLINK_INSTANCE") or "app"
        self.instance = instance

        if base_url is None:
            base_url = os.environ.get("BLINK_BASE_URL")
        if base_url is None:
            base_url = f"https://{instance}.bl.ink/api/v4"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.validate_login = validate_login.ValidateLoginResource(self)
        self.access_token = access_token.AccessTokenResource(self)
        self.users = users.UsersResource(self)
        self.links = links.LinksResource(self)
        self.clicks = clicks.ClicksResource(self)
        self.tags = tags.TagsResource(self)
        self.domains = domains.DomainsResource(self)
        self.domains_domain_name = domains_domain_name.DomainsDomainNameResource(self)
        self.utm_templates = utm_templates.UtmTemplatesResource(self)
        self.groups = groups.GroupsResource(self)
        self.error_codes = error_codes.ErrorCodesResource(self)
        self.with_raw_response = BlinkWithRawResponse(self)
        self.with_streaming_response = BlinkWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        instance: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            instance=instance or self.instance,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBlink(AsyncAPIClient):
    validate_login: validate_login.AsyncValidateLoginResource
    access_token: access_token.AsyncAccessTokenResource
    users: users.AsyncUsersResource
    links: links.AsyncLinksResource
    clicks: clicks.AsyncClicksResource
    tags: tags.AsyncTagsResource
    domains: domains.AsyncDomainsResource
    domains_domain_name: domains_domain_name.AsyncDomainsDomainNameResource
    utm_templates: utm_templates.AsyncUtmTemplatesResource
    groups: groups.AsyncGroupsResource
    error_codes: error_codes.AsyncErrorCodesResource
    with_raw_response: AsyncBlinkWithRawResponse
    with_streaming_response: AsyncBlinkWithStreamedResponse

    # client options
    instance: str

    def __init__(
        self,
        *,
        instance: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBlink client instance.

        This automatically infers the `instance` argument from the `BLINK_INSTANCE` environment variable if it is not provided.
        """
        if instance is None:
            instance = os.environ.get("BLINK_INSTANCE") or "app"
        self.instance = instance

        if base_url is None:
            base_url = os.environ.get("BLINK_BASE_URL")
        if base_url is None:
            base_url = f"https://{instance}.bl.ink/api/v4"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.validate_login = validate_login.AsyncValidateLoginResource(self)
        self.access_token = access_token.AsyncAccessTokenResource(self)
        self.users = users.AsyncUsersResource(self)
        self.links = links.AsyncLinksResource(self)
        self.clicks = clicks.AsyncClicksResource(self)
        self.tags = tags.AsyncTagsResource(self)
        self.domains = domains.AsyncDomainsResource(self)
        self.domains_domain_name = domains_domain_name.AsyncDomainsDomainNameResource(self)
        self.utm_templates = utm_templates.AsyncUtmTemplatesResource(self)
        self.groups = groups.AsyncGroupsResource(self)
        self.error_codes = error_codes.AsyncErrorCodesResource(self)
        self.with_raw_response = AsyncBlinkWithRawResponse(self)
        self.with_streaming_response = AsyncBlinkWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        instance: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            instance=instance or self.instance,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BlinkWithRawResponse:
    def __init__(self, client: Blink) -> None:
        self.validate_login = validate_login.ValidateLoginResourceWithRawResponse(client.validate_login)
        self.access_token = access_token.AccessTokenResourceWithRawResponse(client.access_token)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.links = links.LinksResourceWithRawResponse(client.links)
        self.clicks = clicks.ClicksResourceWithRawResponse(client.clicks)
        self.tags = tags.TagsResourceWithRawResponse(client.tags)
        self.domains = domains.DomainsResourceWithRawResponse(client.domains)
        self.domains_domain_name = domains_domain_name.DomainsDomainNameResourceWithRawResponse(
            client.domains_domain_name
        )
        self.utm_templates = utm_templates.UtmTemplatesResourceWithRawResponse(client.utm_templates)
        self.groups = groups.GroupsResourceWithRawResponse(client.groups)
        self.error_codes = error_codes.ErrorCodesResourceWithRawResponse(client.error_codes)


class AsyncBlinkWithRawResponse:
    def __init__(self, client: AsyncBlink) -> None:
        self.validate_login = validate_login.AsyncValidateLoginResourceWithRawResponse(client.validate_login)
        self.access_token = access_token.AsyncAccessTokenResourceWithRawResponse(client.access_token)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.links = links.AsyncLinksResourceWithRawResponse(client.links)
        self.clicks = clicks.AsyncClicksResourceWithRawResponse(client.clicks)
        self.tags = tags.AsyncTagsResourceWithRawResponse(client.tags)
        self.domains = domains.AsyncDomainsResourceWithRawResponse(client.domains)
        self.domains_domain_name = domains_domain_name.AsyncDomainsDomainNameResourceWithRawResponse(
            client.domains_domain_name
        )
        self.utm_templates = utm_templates.AsyncUtmTemplatesResourceWithRawResponse(client.utm_templates)
        self.groups = groups.AsyncGroupsResourceWithRawResponse(client.groups)
        self.error_codes = error_codes.AsyncErrorCodesResourceWithRawResponse(client.error_codes)


class BlinkWithStreamedResponse:
    def __init__(self, client: Blink) -> None:
        self.validate_login = validate_login.ValidateLoginResourceWithStreamingResponse(client.validate_login)
        self.access_token = access_token.AccessTokenResourceWithStreamingResponse(client.access_token)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.links = links.LinksResourceWithStreamingResponse(client.links)
        self.clicks = clicks.ClicksResourceWithStreamingResponse(client.clicks)
        self.tags = tags.TagsResourceWithStreamingResponse(client.tags)
        self.domains = domains.DomainsResourceWithStreamingResponse(client.domains)
        self.domains_domain_name = domains_domain_name.DomainsDomainNameResourceWithStreamingResponse(
            client.domains_domain_name
        )
        self.utm_templates = utm_templates.UtmTemplatesResourceWithStreamingResponse(client.utm_templates)
        self.groups = groups.GroupsResourceWithStreamingResponse(client.groups)
        self.error_codes = error_codes.ErrorCodesResourceWithStreamingResponse(client.error_codes)


class AsyncBlinkWithStreamedResponse:
    def __init__(self, client: AsyncBlink) -> None:
        self.validate_login = validate_login.AsyncValidateLoginResourceWithStreamingResponse(client.validate_login)
        self.access_token = access_token.AsyncAccessTokenResourceWithStreamingResponse(client.access_token)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.links = links.AsyncLinksResourceWithStreamingResponse(client.links)
        self.clicks = clicks.AsyncClicksResourceWithStreamingResponse(client.clicks)
        self.tags = tags.AsyncTagsResourceWithStreamingResponse(client.tags)
        self.domains = domains.AsyncDomainsResourceWithStreamingResponse(client.domains)
        self.domains_domain_name = domains_domain_name.AsyncDomainsDomainNameResourceWithStreamingResponse(
            client.domains_domain_name
        )
        self.utm_templates = utm_templates.AsyncUtmTemplatesResourceWithStreamingResponse(client.utm_templates)
        self.groups = groups.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.error_codes = error_codes.AsyncErrorCodesResourceWithStreamingResponse(client.error_codes)


Client = Blink

AsyncClient = AsyncBlink
