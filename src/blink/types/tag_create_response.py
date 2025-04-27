# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TagCreateResponse", "Object"]


class Object(BaseModel):
    id: Optional[int] = None

    created: Optional[int] = None

    domain_id: Optional[int] = None

    modified: Optional[int] = None

    name: Optional[str] = None

    notes: Optional[str] = None

    shared: Optional[bool] = None

    user_id: Optional[int] = None


class TagCreateResponse(BaseModel):
    objects: Optional[List[Object]] = None
