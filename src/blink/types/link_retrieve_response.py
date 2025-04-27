# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LinkRetrieveResponse", "Object", "ObjectTag"]


class ObjectTag(BaseModel):
    name: Optional[str] = None

    shared: Optional[bool] = None


class Object(BaseModel):
    id: Optional[int] = None

    alias: Optional[str] = None

    archive_on: Optional[int] = None

    click_count: Optional[int] = None

    created: Optional[int] = None

    delete_on: Optional[int] = None

    domain_id: Optional[int] = None

    groups: Optional[List[int]] = None

    modified: Optional[int] = None

    notes: Optional[str] = None

    notify_on_click: Optional[str] = None

    redirect_type: Optional[int] = None

    redirect_url: Optional[str] = None

    redirect_url_domain: Optional[str] = None
    """Redirect URL's Fully Qualified Domain Name (FQDN)"""

    redirect_url_path: Optional[str] = None
    """Redirect URL's path"""

    short_link: Optional[str] = None

    status: Optional[str] = None

    tags: Optional[List[ObjectTag]] = None

    template_id: Optional[int] = None

    url: Optional[str] = None

    user_id: Optional[int] = None


class LinkRetrieveResponse(BaseModel):
    objects: Optional[List[Object]] = None
