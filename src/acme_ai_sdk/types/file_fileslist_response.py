# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileFileslistResponse"]


class FileFileslistResponse(BaseModel):
    completion_time: Optional[datetime] = None
    """Time processing was completed (if applicable)"""

    error: Optional[str] = None
    """Error message (if status is 'failed')"""

    file_id: Optional[str] = None
    """Unique identifier for the file"""

    file_size: Optional[int] = None
    """Size of the file in bytes"""

    filename: Optional[str] = None
    """Original name of the file"""

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None
    """Current processing status"""

    upload_time: Optional[datetime] = None
    """Time the file was uploaded"""
