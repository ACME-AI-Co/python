# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["FileFileCreateParams", "ProcessingOptions"]


class FileFileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to upload"""

    description: str
    """Optional description of the file"""

    processing_options: ProcessingOptions


class ProcessingOptions(TypedDict, total=False):
    language: str
    """Preferred language for processing"""

    ocr: bool
    """Enable OCR for image-based documents"""
