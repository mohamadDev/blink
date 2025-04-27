# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DomainUpdateParams"]


class DomainUpdateParams(TypedDict, total=False):
    op: Literal["replace"]
    """The operation to be performed. Currently only replace is supported"""

    path: Literal["status", "homepage", "url_404"]
    """Path or property you want updated"""

    value: str
    """
    The new value you want the path/property to take. When path is status, only
    'active' and 'disabled' are permitted. When path is homepage or url_404, they
    must be a valid URL including protocol e.g. 'https://'
    """
