# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel


class Newsfeed(UncheckedBaseModel):
    """
    A newsfeed is a collection of news items, targeted to a specific audience.

    Newsfeeds currently cannot be edited through the API, please refer to [this article](https://www.intercom.com/help/en/articles/6362267-getting-started-with-news) to set up your newsfeeds in Intercom.
    """

    id: str = pydantic.Field()
    """
    The unique identifier for the newsfeed which is given by Intercom.
    """

    type: typing.Literal["newsfeed"] = pydantic.Field(default="newsfeed")
    """
    The type of object.
    """

    name: str = pydantic.Field()
    """
    The name of the newsfeed. This name will never be visible to your users.
    """

    created_at: int = pydantic.Field()
    """
    Timestamp for when the newsfeed was created.
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp for when the newsfeed was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
