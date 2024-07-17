# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["CursorPaginationPages", "CursorPaginationNext", "SyncCursorPagination", "AsyncCursorPagination"]

_T = TypeVar("_T")


class CursorPaginationNext(BaseModel):
    page: Optional[int] = None

    starting_after: Optional[str] = None


class CursorPaginationPages(BaseModel):
    next: Optional[CursorPaginationNext] = None

    page: Optional[int] = None

    total_pages: Optional[int] = None

    type: Optional[str] = None


class SyncCursorPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pages: Optional[CursorPaginationPages] = None
    total_count: Optional[int] = None
    data: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        starting_after = None
        if self.pages is not None:
            if self.pages.next is not None:
                starting_after = self.pages.next.starting_after
        if not starting_after:
            return None

        return PageInfo(params={"starting_after": starting_after})


class AsyncCursorPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pages: Optional[CursorPaginationPages] = None
    total_count: Optional[int] = None
    data: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        starting_after = None
        if self.pages is not None:
            if self.pages.next is not None:
                starting_after = self.pages.next.starting_after
        if not starting_after:
            return None

        return PageInfo(params={"starting_after": starting_after})
