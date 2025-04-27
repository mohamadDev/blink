# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserListResponse", "Domains"]


class Domains(BaseModel):
    name: Optional[str] = None
    """The domain name belonging to the user."""

    role: Optional[str] = None
    """The access level for the user and domain."""


class UserListResponse(BaseModel):
    domains: Optional[Domains] = None

    email_address: Optional[str] = None
    """The user's email"""

    first_name: Optional[str] = None
    """The user's first name"""

    last_name: Optional[str] = None
    """The user's last name"""
