# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileFileslistResponse", "File"]


class File(BaseModel):
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


class FileFileslistResponse(BaseModel):
    files: Optional[List[File]] = None

    limit: Optional[int] = None
    """Maximum number of files returned"""

    offset: Optional[int] = None
    """Number of files skipped"""

    total: Optional[int] = None
    """Total number of files matching the filter"""
