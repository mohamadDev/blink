# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LinkGetByAliasResponse", "Object"]


class Object(BaseModel):
    id: Optional[int] = None

    alias: Optional[str] = None

    archive_on: Optional[int] = None

    click_count: Optional[int] = None

    created: Optional[int] = None

    delete_on: Optional[int] = None

    domain_id: Optional[int] = None

    modified: Optional[int] = None

    notes: Optional[str] = None

    notify_on_click: Optional[str] = None

    redirect_type: Optional[int] = None

    redirect_url: Optional[str] = None

    short_link: Optional[str] = None

    status: Optional[str] = None

    template_id: Optional[int] = None

    url: Optional[str] = None

    user_id: Optional[int] = None


class LinkGetByAliasResponse(BaseModel):
    objects: Optional[List[Object]] = None
