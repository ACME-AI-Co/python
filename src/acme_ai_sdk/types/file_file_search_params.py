# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileFileSearchParams"]


class FileFileSearchParams(TypedDict, total=False):
    query: Required[str]
    """Natural language search query"""

    context_size: int
    """Number of characters to include before and after the match"""

    include_metadata: bool
    """Whether to include file metadata in response"""

    max_results: int
    """Maximum number of results to return"""
