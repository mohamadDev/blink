# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LinkGetRawClicksResponse", "Meta", "Object"]


class Meta(BaseModel):
    current_page: Optional[int] = None
    """The current page number."""

    from_: Optional[int] = FieldInfo(alias="from", default=None)
    """The first record of the current page"""

    last_page: Optional[int] = None
    """The last page number."""

    next_page: Optional[int] = None
    """The next page number, can be null if on last page."""

    path: Optional[str] = None
    """The base API endpoint for the current request."""

    per_page: Optional[int] = None
    """The items per page"""

    previous_page: Optional[int] = None
    """The previous page number, can be null if on first page."""

    to: Optional[int] = None
    """The last record of the current page"""

    total: Optional[int] = None
    """The total number of records in all pages. Unrelated to count or sum queries."""


class Object(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    created: Optional[int] = None

    device: Optional[str] = None

    engagement_id: Optional[str] = None

    referrer: Optional[str] = None

    region: Optional[str] = None

    type: Optional[str] = None


class LinkGetRawClicksResponse(BaseModel):
    click_count: Optional[int] = None
    """Total number of clicks for all links found not just the ones returned."""

    count: Optional[int] = None
    """Number of links returned in the `objects` array"""

    meta: Optional[Meta] = None
    """A set of meta data unrelated to the query but useful in various API scenarios."""

    objects: Optional[List[Object]] = None

    total: Optional[int] = None
    """Total number of links found by query"""
