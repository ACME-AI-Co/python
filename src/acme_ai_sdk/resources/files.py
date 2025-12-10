# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import file_fileslist_params, file_file_create_params, file_file_search_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffset, AsyncOffset
from .._base_client import AsyncPaginator, make_request_options
from ..types.file_fileslist_response import FileFileslistResponse
from ..types.file_file_create_response import FileFileCreateResponse
from ..types.file_file_search_response import FileFileSearchResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ACME-AI-Co/python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ACME-AI-Co/python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def file_create(
        self,
        *,
        file: FileTypes,
        description: str | NotGiven = NOT_GIVEN,
        processing_options: file_file_create_params.ProcessingOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileFileCreateResponse:
        """Upload a file for processing with AI.

        The file will be analyzed and made
        searchable using natural language queries.

        Args:
          file: The file to upload

          description: Optional description of the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "description": description,
                "processing_options": processing_options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/files/",
            body=maybe_transform(body, file_file_create_params.FileFileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileFileCreateResponse,
        )

    def file_search(
        self,
        file_id: str,
        *,
        query: str,
        context_size: int | NotGiven = NOT_GIVEN,
        include_metadata: bool | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileFileSearchResponse:
        """
        Search for content within a processed file using natural language queries.
        Returns relevant passages and their context.

        Args:
          query: Natural language search query

          context_size: Number of characters to include before and after the match

          include_metadata: Whether to include file metadata in response

          max_results: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/files/{file_id}/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "context_size": context_size,
                        "include_metadata": include_metadata,
                        "max_results": max_results,
                    },
                    file_file_search_params.FileFileSearchParams,
                ),
            ),
            cast_to=FileFileSearchResponse,
        )

    def fileslist(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["upload_time", "status"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "processing", "completed", "failed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffset[FileFileslistResponse]:
        """Retrieve a list of files.

        Can be filtered by status and sorted by upload time.

        Args:
          limit: Maximum number of files to return

          offset: Number of files to skip

          sort_by: Field to sort by

          sort_order: Sort order

          status: Filter by processing status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/files/",
            page=SyncOffset[FileFileslistResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "status": status,
                    },
                    file_fileslist_params.FileFileslistParams,
                ),
            ),
            model=FileFileslistResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ACME-AI-Co/python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ACME-AI-Co/python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def file_create(
        self,
        *,
        file: FileTypes,
        description: str | NotGiven = NOT_GIVEN,
        processing_options: file_file_create_params.ProcessingOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileFileCreateResponse:
        """Upload a file for processing with AI.

        The file will be analyzed and made
        searchable using natural language queries.

        Args:
          file: The file to upload

          description: Optional description of the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "description": description,
                "processing_options": processing_options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/files/",
            body=await async_maybe_transform(body, file_file_create_params.FileFileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileFileCreateResponse,
        )

    async def file_search(
        self,
        file_id: str,
        *,
        query: str,
        context_size: int | NotGiven = NOT_GIVEN,
        include_metadata: bool | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileFileSearchResponse:
        """
        Search for content within a processed file using natural language queries.
        Returns relevant passages and their context.

        Args:
          query: Natural language search query

          context_size: Number of characters to include before and after the match

          include_metadata: Whether to include file metadata in response

          max_results: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/files/{file_id}/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "context_size": context_size,
                        "include_metadata": include_metadata,
                        "max_results": max_results,
                    },
                    file_file_search_params.FileFileSearchParams,
                ),
            ),
            cast_to=FileFileSearchResponse,
        )

    def fileslist(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["upload_time", "status"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "processing", "completed", "failed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FileFileslistResponse, AsyncOffset[FileFileslistResponse]]:
        """Retrieve a list of files.

        Can be filtered by status and sorted by upload time.

        Args:
          limit: Maximum number of files to return

          offset: Number of files to skip

          sort_by: Field to sort by

          sort_order: Sort order

          status: Filter by processing status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/files/",
            page=AsyncOffset[FileFileslistResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "status": status,
                    },
                    file_fileslist_params.FileFileslistParams,
                ),
            ),
            model=FileFileslistResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.file_create = to_raw_response_wrapper(
            files.file_create,
        )
        self.file_search = to_raw_response_wrapper(
            files.file_search,
        )
        self.fileslist = to_raw_response_wrapper(
            files.fileslist,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.file_create = async_to_raw_response_wrapper(
            files.file_create,
        )
        self.file_search = async_to_raw_response_wrapper(
            files.file_search,
        )
        self.fileslist = async_to_raw_response_wrapper(
            files.fileslist,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.file_create = to_streamed_response_wrapper(
            files.file_create,
        )
        self.file_search = to_streamed_response_wrapper(
            files.file_search,
        )
        self.fileslist = to_streamed_response_wrapper(
            files.fileslist,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.file_create = async_to_streamed_response_wrapper(
            files.file_create,
        )
        self.file_search = async_to_streamed_response_wrapper(
            files.file_search,
        )
        self.fileslist = async_to_streamed_response_wrapper(
            files.fileslist,
        )
