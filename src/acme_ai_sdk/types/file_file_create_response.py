# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileFileCreateResponse"]


class FileFileCreateResponse(BaseModel):
    file_id: Optional[str] = None
    """Unique identifier for the file"""

    status: Optional[Literal["pending", "processing"]] = None
    """Current processing status"""

    upload_time: Optional[datetime] = None
    """Time the file was uploaded"""
