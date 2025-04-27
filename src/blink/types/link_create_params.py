# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkCreateParams", "Tag"]


class LinkCreateParams(TypedDict, total=False):
    url: Required[str]
    """The long link. The URL protocol is optional."""

    alias: str
    """Short string that will be used at the end of the domain to build your short
    link.

    Alias
    """

    archive_on: int
    """GMT Unix timestamp defining the date to archive the link"""

    delete_on: int
    """GMT Unix timestamp defining the date to delete the link"""

    dupe_check: int
    """When set to 1, BL.INK will search for BL.INKs matching the url to be shortened.

    If one or more existing BL.INKs exist BL.INK will return the first already
    existing BL.INK. Otherwise it will create and return a new BL.INK
    """

    notes: str
    """Notes to attach onto the link."""

    notify_on_click: int
    """
    When set to 1, the user will be notified by email when this link has been
    clicked. The default is 0 no notification
    """

    override_404_check: int
    """
    When set to 1, creation will proceed without checking that the long URL returns
    a 404 response
    """

    rand_alias_length: int
    """The length of the randomly generated alias when one is not specified.

    It is ignored when an alias is specified.
    """

    redirect_type: Literal[301, 307]

    tags: Iterable[Tag]
    """Array of objects defining tags to be attached to the link"""

    utm_fields: object
    """Object defining key-value pairs for builder fields"""

    utm_template_id: int


class Tag(TypedDict, total=False):
    name: str
    """The tag name"""

    shared: bool
    """Indicates if this tag is shared with other users"""
