# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Domain", "Meta", "Object"]


class Meta(BaseModel):
    current_page: Optional[int] = None

    from_: Optional[int] = FieldInfo(alias="from", default=None)

    last_page: Optional[int] = None

    next_page: Optional[int] = None

    path: Optional[str] = None

    per_page: Optional[int] = None

    previous_page: Optional[int] = None

    to: Optional[int] = None

    total: Optional[int] = None


class Object(BaseModel):
    id: Optional[int] = None

    created: Optional[int] = None

    default: Optional[bool] = None

    domain: Optional[str] = None

    has_ssl: Optional[bool] = None

    homepage: Optional[str] = None

    modified: Optional[int] = None

    type: Optional[str] = None

    url_404: Optional[str] = None


class Domain(BaseModel):
    meta: Optional[Meta] = None

    objects: Optional[List[Object]] = None
