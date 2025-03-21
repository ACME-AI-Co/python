# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileFileslistParams"]


class FileFileslistParams(TypedDict, total=False):
    limit: int
    """Maximum number of files to return"""

    offset: int
    """Number of files to skip"""

    sort_by: Literal["upload_time", "status"]
    """Field to sort by"""

    sort_order: Literal["asc", "desc"]
    """Sort order"""

    status: Literal["pending", "processing", "completed", "failed"]
    """Filter by processing status"""
