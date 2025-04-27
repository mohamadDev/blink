# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccessTokenCreateResponse", "User"]


class User(BaseModel):
    email: Optional[str] = None

    nickname: Optional[str] = None

    user_id: Optional[int] = None


class AccessTokenCreateResponse(BaseModel):
    access_token: Optional[str] = None

    expires: Optional[int] = None
    """GMT Unix timestamp defining the date when the access_token expires"""

    success: Optional[int] = None

    user: Optional[User] = None
