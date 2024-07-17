# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataExport"]


class DataExport(BaseModel):
    download_expires_at: Optional[str] = None
    """The time after which you will not be able to access the data."""

    download_url: Optional[str] = None
    """The location where you can download your data."""

    job_identfier: Optional[str] = None
    """The identifier for your job."""

    status: Optional[Literal["pending", "in_progress", "failed", "completed", "no_data", "canceled"]] = None
    """The current state of your job."""
