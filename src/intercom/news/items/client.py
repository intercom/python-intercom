# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.deleted_object import DeletedObject
from ...types.news_item_request_state import NewsItemRequestState
from ...types.paginated_news_item_response import PaginatedNewsItemResponse
from ..types.news_item import NewsItem
from ..types.newsfeed_assignment import NewsfeedAssignment
from .raw_client import AsyncRawItemsClient, RawItemsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawItemsClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> PaginatedNewsItemResponse:
        """
        You can fetch a list of all news items

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedNewsItemResponse
            successful

        Examples
        --------
        from intercom import Intercom

        client = Intercom(
            token="YOUR_TOKEN",
        )
        client.news.items.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        title: str,
        sender_id: int,
        body: typing.Optional[str] = OMIT,
        state: typing.Optional[NewsItemRequestState] = OMIT,
        deliver_silently: typing.Optional[bool] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        reactions: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        newsfeed_assignments: typing.Optional[typing.Sequence[NewsfeedAssignment]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NewsItem:
        """
        You can create a news item

        Parameters
        ----------
        title : str
            The title of the news item.

        sender_id : int
            The id of the sender of the news item. Must be a teammate on the workspace.

        body : typing.Optional[str]
            The news item body, which may contain HTML.

        state : typing.Optional[NewsItemRequestState]
            News items will not be visible to your users in the assigned newsfeeds until they are set live.

        deliver_silently : typing.Optional[bool]
            When set to `true`, the news item will appear in the messenger newsfeed without showing a notification badge.

        labels : typing.Optional[typing.Sequence[str]]
            Label names displayed to users to categorize the news item.

        reactions : typing.Optional[typing.Sequence[typing.Optional[str]]]
            Ordered list of emoji reactions to the news item. When empty, reactions are disabled.

        newsfeed_assignments : typing.Optional[typing.Sequence[NewsfeedAssignment]]
            A list of newsfeed_assignments to assign to the specified newsfeed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewsItem
            successful

        Examples
        --------
        from intercom import Intercom
        from intercom.news import NewsfeedAssignment

        client = Intercom(
            token="YOUR_TOKEN",
        )
        client.news.items.create(
            title="Halloween is here!",
            body="<p>New costumes in store for this spooky season</p>",
            sender_id=991267734,
            state="live",
            deliver_silently=True,
            labels=["Product", "Update", "New"],
            reactions=["😆", "😅"],
            newsfeed_assignments=[
                NewsfeedAssignment(
                    newsfeed_id=53,
                    published_at=1664638214,
                )
            ],
        )
        """
        _response = self._raw_client.create(
            title=title,
            sender_id=sender_id,
            body=body,
            state=state,
            deliver_silently=deliver_silently,
            labels=labels,
            reactions=reactions,
            newsfeed_assignments=newsfeed_assignments,
            request_options=request_options,
        )
        return _response.data

    def find(self, news_item_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> NewsItem:
        """
        You can fetch the details of a single news item.

        Parameters
        ----------
        news_item_id : str
            The unique identifier for the news item which is given by Intercom.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewsItem
            successful

        Examples
        --------
        from intercom import Intercom

        client = Intercom(
            token="YOUR_TOKEN",
        )
        client.news.items.find(
            news_item_id="123",
        )
        """
        _response = self._raw_client.find(news_item_id, request_options=request_options)
        return _response.data

    def update(
        self,
        news_item_id: str,
        *,
        title: str,
        sender_id: int,
        body: typing.Optional[str] = OMIT,
        state: typing.Optional[NewsItemRequestState] = OMIT,
        deliver_silently: typing.Optional[bool] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        reactions: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        newsfeed_assignments: typing.Optional[typing.Sequence[NewsfeedAssignment]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NewsItem:
        """
        Parameters
        ----------
        news_item_id : str
            The unique identifier for the news item which is given by Intercom.

        title : str
            The title of the news item.

        sender_id : int
            The id of the sender of the news item. Must be a teammate on the workspace.

        body : typing.Optional[str]
            The news item body, which may contain HTML.

        state : typing.Optional[NewsItemRequestState]
            News items will not be visible to your users in the assigned newsfeeds until they are set live.

        deliver_silently : typing.Optional[bool]
            When set to `true`, the news item will appear in the messenger newsfeed without showing a notification badge.

        labels : typing.Optional[typing.Sequence[str]]
            Label names displayed to users to categorize the news item.

        reactions : typing.Optional[typing.Sequence[typing.Optional[str]]]
            Ordered list of emoji reactions to the news item. When empty, reactions are disabled.

        newsfeed_assignments : typing.Optional[typing.Sequence[NewsfeedAssignment]]
            A list of newsfeed_assignments to assign to the specified newsfeed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewsItem
            successful

        Examples
        --------
        from intercom import Intercom

        client = Intercom(
            token="YOUR_TOKEN",
        )
        client.news.items.update(
            news_item_id="123",
            title="Christmas is here!",
            body="<p>New gifts in store for the jolly season</p>",
            sender_id=991267745,
            reactions=["😝", "😂"],
        )
        """
        _response = self._raw_client.update(
            news_item_id,
            title=title,
            sender_id=sender_id,
            body=body,
            state=state,
            deliver_silently=deliver_silently,
            labels=labels,
            reactions=reactions,
            newsfeed_assignments=newsfeed_assignments,
            request_options=request_options,
        )
        return _response.data

    def delete(self, news_item_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeletedObject:
        """
        You can delete a single news item.

        Parameters
        ----------
        news_item_id : str
            The unique identifier for the news item which is given by Intercom.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletedObject
            successful

        Examples
        --------
        from intercom import Intercom

        client = Intercom(
            token="YOUR_TOKEN",
        )
        client.news.items.delete(
            news_item_id="123",
        )
        """
        _response = self._raw_client.delete(news_item_id, request_options=request_options)
        return _response.data


class AsyncItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawItemsClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> PaginatedNewsItemResponse:
        """
        You can fetch a list of all news items

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedNewsItemResponse
            successful

        Examples
        --------
        import asyncio

        from intercom import AsyncIntercom

        client = AsyncIntercom(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.news.items.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        title: str,
        sender_id: int,
        body: typing.Optional[str] = OMIT,
        state: typing.Optional[NewsItemRequestState] = OMIT,
        deliver_silently: typing.Optional[bool] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        reactions: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        newsfeed_assignments: typing.Optional[typing.Sequence[NewsfeedAssignment]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NewsItem:
        """
        You can create a news item

        Parameters
        ----------
        title : str
            The title of the news item.

        sender_id : int
            The id of the sender of the news item. Must be a teammate on the workspace.

        body : typing.Optional[str]
            The news item body, which may contain HTML.

        state : typing.Optional[NewsItemRequestState]
            News items will not be visible to your users in the assigned newsfeeds until they are set live.

        deliver_silently : typing.Optional[bool]
            When set to `true`, the news item will appear in the messenger newsfeed without showing a notification badge.

        labels : typing.Optional[typing.Sequence[str]]
            Label names displayed to users to categorize the news item.

        reactions : typing.Optional[typing.Sequence[typing.Optional[str]]]
            Ordered list of emoji reactions to the news item. When empty, reactions are disabled.

        newsfeed_assignments : typing.Optional[typing.Sequence[NewsfeedAssignment]]
            A list of newsfeed_assignments to assign to the specified newsfeed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewsItem
            successful

        Examples
        --------
        import asyncio

        from intercom import AsyncIntercom
        from intercom.news import NewsfeedAssignment

        client = AsyncIntercom(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.news.items.create(
                title="Halloween is here!",
                body="<p>New costumes in store for this spooky season</p>",
                sender_id=991267734,
                state="live",
                deliver_silently=True,
                labels=["Product", "Update", "New"],
                reactions=["😆", "😅"],
                newsfeed_assignments=[
                    NewsfeedAssignment(
                        newsfeed_id=53,
                        published_at=1664638214,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            title=title,
            sender_id=sender_id,
            body=body,
            state=state,
            deliver_silently=deliver_silently,
            labels=labels,
            reactions=reactions,
            newsfeed_assignments=newsfeed_assignments,
            request_options=request_options,
        )
        return _response.data

    async def find(self, news_item_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> NewsItem:
        """
        You can fetch the details of a single news item.

        Parameters
        ----------
        news_item_id : str
            The unique identifier for the news item which is given by Intercom.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewsItem
            successful

        Examples
        --------
        import asyncio

        from intercom import AsyncIntercom

        client = AsyncIntercom(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.news.items.find(
                news_item_id="123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find(news_item_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        news_item_id: str,
        *,
        title: str,
        sender_id: int,
        body: typing.Optional[str] = OMIT,
        state: typing.Optional[NewsItemRequestState] = OMIT,
        deliver_silently: typing.Optional[bool] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        reactions: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        newsfeed_assignments: typing.Optional[typing.Sequence[NewsfeedAssignment]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NewsItem:
        """
        Parameters
        ----------
        news_item_id : str
            The unique identifier for the news item which is given by Intercom.

        title : str
            The title of the news item.

        sender_id : int
            The id of the sender of the news item. Must be a teammate on the workspace.

        body : typing.Optional[str]
            The news item body, which may contain HTML.

        state : typing.Optional[NewsItemRequestState]
            News items will not be visible to your users in the assigned newsfeeds until they are set live.

        deliver_silently : typing.Optional[bool]
            When set to `true`, the news item will appear in the messenger newsfeed without showing a notification badge.

        labels : typing.Optional[typing.Sequence[str]]
            Label names displayed to users to categorize the news item.

        reactions : typing.Optional[typing.Sequence[typing.Optional[str]]]
            Ordered list of emoji reactions to the news item. When empty, reactions are disabled.

        newsfeed_assignments : typing.Optional[typing.Sequence[NewsfeedAssignment]]
            A list of newsfeed_assignments to assign to the specified newsfeed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewsItem
            successful

        Examples
        --------
        import asyncio

        from intercom import AsyncIntercom

        client = AsyncIntercom(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.news.items.update(
                news_item_id="123",
                title="Christmas is here!",
                body="<p>New gifts in store for the jolly season</p>",
                sender_id=991267745,
                reactions=["😝", "😂"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            news_item_id,
            title=title,
            sender_id=sender_id,
            body=body,
            state=state,
            deliver_silently=deliver_silently,
            labels=labels,
            reactions=reactions,
            newsfeed_assignments=newsfeed_assignments,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, news_item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletedObject:
        """
        You can delete a single news item.

        Parameters
        ----------
        news_item_id : str
            The unique identifier for the news item which is given by Intercom.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletedObject
            successful

        Examples
        --------
        import asyncio

        from intercom import AsyncIntercom

        client = AsyncIntercom(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.news.items.delete(
                news_item_id="123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(news_item_id, request_options=request_options)
        return _response.data
