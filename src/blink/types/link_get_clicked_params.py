# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LinkGetClickedParams"]


class LinkGetClickedParams(TypedDict, total=False):
    domain_id: Required[int]

    from_unix: int
    """The UTC unix timestamp, query returns values after this date."""

    from_user: str
    """An optional parameter.

    Valid value 'me' is allowed to only query for your links.
    """

    group_id: int
    """Search links by group_id"""

    keyword: str
    """Search link alias, notes, and redirect url for keyword"""

    page: int
    """The page of to query the values from the paginated results. Defaults to 1."""

    query_tag: Annotated[str, PropertyInfo(alias="tag")]
    """Search links by tag"""

    to_unix: int
    """The UTC unix timestamp, query returns values before this date.

    Required if from_unix is specified.
    """
