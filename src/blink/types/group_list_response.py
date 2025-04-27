# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["GroupListResponse", "Object"]


class Object(BaseModel):
    id: Optional[int] = None

    created: Optional[int] = None

    domain_id: Optional[int] = None

    is_global: Optional[str] = None

    modified: Optional[int] = None

    user_id: Optional[int] = None

    users: Optional[List[object]] = None


class GroupListResponse(BaseModel):
    objects: Optional[List[Object]] = None
