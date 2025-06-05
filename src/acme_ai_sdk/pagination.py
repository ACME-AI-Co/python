# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncOffset", "AsyncOffset"]

_T = TypeVar("_T")


class SyncOffset(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    files: List[_T]
    total: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        files = self.files
        if not files:
            return []
        return files

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total = self.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffset(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    files: List[_T]
    total: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        files = self.files
        if not files:
            return []
        return files

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total = self.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None
