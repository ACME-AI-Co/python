# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from acme_ai_sdk import AcmeAISDK, AsyncAcmeAISDK
from tests.utils import assert_matches_type
from acme_ai_sdk.types import (
    FileFileslistResponse,
    FileFileCreateResponse,
    FileFileSearchResponse,
)
from acme_ai_sdk.pagination import SyncOffset, AsyncOffset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_file_create(self, client: AcmeAISDK) -> None:
        file = client.files.file_create(
            file=b"raw file contents",
        )
        assert_matches_type(FileFileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_file_create_with_all_params(self, client: AcmeAISDK) -> None:
        file = client.files.file_create(
            file=b"raw file contents",
            description="description",
            processing_options={
                "language": "language",
                "ocr": True,
            },
        )
        assert_matches_type(FileFileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_file_create(self, client: AcmeAISDK) -> None:
        response = client.files.with_raw_response.file_create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileFileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_file_create(self, client: AcmeAISDK) -> None:
        with client.files.with_streaming_response.file_create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileFileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_file_search(self, client: AcmeAISDK) -> None:
        file = client.files.file_search(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
        )
        assert_matches_type(FileFileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_file_search_with_all_params(self, client: AcmeAISDK) -> None:
        file = client.files.file_search(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
            context_size=0,
            include_metadata=True,
            max_results=1,
        )
        assert_matches_type(FileFileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_file_search(self, client: AcmeAISDK) -> None:
        response = client.files.with_raw_response.file_search(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileFileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_file_search(self, client: AcmeAISDK) -> None:
        with client.files.with_streaming_response.file_search(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileFileSearchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_file_search(self, client: AcmeAISDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.file_search(
                file_id="",
                query="query",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_fileslist(self, client: AcmeAISDK) -> None:
        file = client.files.fileslist()
        assert_matches_type(SyncOffset[FileFileslistResponse], file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_fileslist_with_all_params(self, client: AcmeAISDK) -> None:
        file = client.files.fileslist(
            limit=1,
            offset=0,
            sort_by="upload_time",
            sort_order="asc",
            status="pending",
        )
        assert_matches_type(SyncOffset[FileFileslistResponse], file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_fileslist(self, client: AcmeAISDK) -> None:
        response = client.files.with_raw_response.fileslist()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncOffset[FileFileslistResponse], file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_fileslist(self, client: AcmeAISDK) -> None:
        with client.files.with_streaming_response.fileslist() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncOffset[FileFileslistResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_file_create(self, async_client: AsyncAcmeAISDK) -> None:
        file = await async_client.files.file_create(
            file=b"raw file contents",
        )
        assert_matches_type(FileFileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_file_create_with_all_params(self, async_client: AsyncAcmeAISDK) -> None:
        file = await async_client.files.file_create(
            file=b"raw file contents",
            description="description",
            processing_options={
                "language": "language",
                "ocr": True,
            },
        )
        assert_matches_type(FileFileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_file_create(self, async_client: AsyncAcmeAISDK) -> None:
        response = await async_client.files.with_raw_response.file_create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileFileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_file_create(self, async_client: AsyncAcmeAISDK) -> None:
        async with async_client.files.with_streaming_response.file_create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileFileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_file_search(self, async_client: AsyncAcmeAISDK) -> None:
        file = await async_client.files.file_search(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
        )
        assert_matches_type(FileFileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_file_search_with_all_params(self, async_client: AsyncAcmeAISDK) -> None:
        file = await async_client.files.file_search(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
            context_size=0,
            include_metadata=True,
            max_results=1,
        )
        assert_matches_type(FileFileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_file_search(self, async_client: AsyncAcmeAISDK) -> None:
        response = await async_client.files.with_raw_response.file_search(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileFileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_file_search(self, async_client: AsyncAcmeAISDK) -> None:
        async with async_client.files.with_streaming_response.file_search(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileFileSearchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_file_search(self, async_client: AsyncAcmeAISDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.file_search(
                file_id="",
                query="query",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_fileslist(self, async_client: AsyncAcmeAISDK) -> None:
        file = await async_client.files.fileslist()
        assert_matches_type(AsyncOffset[FileFileslistResponse], file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_fileslist_with_all_params(self, async_client: AsyncAcmeAISDK) -> None:
        file = await async_client.files.fileslist(
            limit=1,
            offset=0,
            sort_by="upload_time",
            sort_order="asc",
            status="pending",
        )
        assert_matches_type(AsyncOffset[FileFileslistResponse], file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_fileslist(self, async_client: AsyncAcmeAISDK) -> None:
        response = await async_client.files.with_raw_response.fileslist()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncOffset[FileFileslistResponse], file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_fileslist(self, async_client: AsyncAcmeAISDK) -> None:
        async with async_client.files.with_streaming_response.fileslist() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncOffset[FileFileslistResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True
