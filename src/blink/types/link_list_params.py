# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LinkListParams"]


class LinkListParams(TypedDict, total=False):
    from_unix: int
    """The UTC unix timestamp, query returns values after this date."""

    group_id: int
    """Search links by group_id"""

    keyword: str
    """Search link alias, notes, and redirect url for keyword"""

    order: str
    """Orders results differently.

    Possible values 'oldest' or 'latest'. Defaults to 'oldest'
    """

    page: int
    """Page number"""

    tag: str
    """Search links by tag"""

    to_unix: int
    """The UTC unix timestamp, query returns values before this date.

    Required if from_unix is specified.
    """

    url: str
    """long URL to search links by"""

    users: str
    """
    A flag for privileged users (domain admins or account admins) to specify
    returning all links from corresponding domain instead of just links they
    created. Example users=all
    """
