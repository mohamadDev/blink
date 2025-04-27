# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkUpdateParams", "Body"]


class LinkUpdateParams(TypedDict, total=False):
    domain_id: Required[int]

    body: Iterable[Body]


class Body(TypedDict, total=False):
    op: Literal["replace"]

    path: Literal["/alias", "/notes", "/notify_on_click", "/url", "/delete_on", "/archive_on"]
    """
    The path property accepts string values for all paths with the exception of
    notify_on_click which accepts only a 0 or 1. However, for the archive on and
    delete on paths a unix timestamp integer value can be accepted as an integer or
    string.
    """

    value: Union[str, int]
