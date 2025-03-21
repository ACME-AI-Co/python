# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileFileSearchResponse", "Metadata", "MetadataProcessingOptions", "Result", "ResultHighlightRange"]


class MetadataProcessingOptions(BaseModel):
    language: Optional[str] = None
    """Language used for processing"""

    ocr: Optional[bool] = None
    """Whether OCR was used"""


class Metadata(BaseModel):
    description: Optional[str] = None
    """User-provided description of the file"""

    file_id: Optional[str] = None
    """Unique identifier for the file"""

    file_type: Optional[str] = None
    """MIME type of the file"""

    filename: Optional[str] = None
    """Original name of the file"""

    page_count: Optional[int] = None
    """Number of pages (for documents)"""

    processing_options: Optional[MetadataProcessingOptions] = None

    upload_time: Optional[datetime] = None
    """Time the file was uploaded"""

    word_count: Optional[int] = None
    """Approximate word count"""


class ResultHighlightRange(BaseModel):
    end: Optional[int] = None
    """End index of highlight in passage"""

    start: Optional[int] = None
    """Start index of highlight in passage"""


class Result(BaseModel):
    additional_context: Optional[object] = None
    """Additional context information (document-type specific)"""

    highlight_ranges: Optional[List[ResultHighlightRange]] = None
    """Character ranges to highlight within the passage"""

    page_number: Optional[int] = None
    """Page number where the match was found (if applicable)"""

    passage: Optional[str] = None
    """Text passage containing the match with surrounding context"""

    relevance_score: Optional[float] = None
    """Relevance score of the result (0-1)"""


class FileFileSearchResponse(BaseModel):
    file_id: Optional[str] = None
    """Unique identifier of the searched file"""

    metadata: Optional[Metadata] = None
    """File metadata (only included if requested)"""

    query: Optional[str] = None
    """The search query used"""

    results: Optional[List[Result]] = None

    total_results: Optional[int] = None
    """Total number of results found"""
