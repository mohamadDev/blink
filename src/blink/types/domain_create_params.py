# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DomainCreateParams"]


class DomainCreateParams(TypedDict, total=False):
    domain: Required[str]
    """the domain name"""

    default: bool
    """boolean denoting whether this domain should be the user's default domain"""

    homepage: str
    """
    The address you would like to redirect users to when they visit your domain
    without an alias. Must be a valid URL including protocol e.g. 'https://'
    """

    url_404: str
    """The address you would like 404 errors to redirect to.

    Must be a valid URL including protocol e.g. 'https://'
    """
