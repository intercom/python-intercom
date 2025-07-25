# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .checkbox_component_save_state import CheckboxComponentSaveState
from .checkbox_option import CheckboxOption


class CheckboxComponent(UncheckedBaseModel):
    """
    A checkbox component is used to capture multiple choices from as many options as you want to provide. You can submit the options by:

    - Using a ButtonComponent (which will submit all interactive components in the canvas)

    When a submit action takes place, the results are given in a hash with the `id` from the checkbox component used as the key and an array containing the `id` of each chosen option as the value.
    """

    id: str = pydantic.Field()
    """
    A unique identifier for the component.
    """

    option: typing.List[CheckboxOption] = pydantic.Field()
    """
    The list of options. Minimum of 1.
    """

    label: str = pydantic.Field()
    """
    The text shown above the options.
    """

    value: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The option's that are selected by default.
    """

    save_state: typing.Optional[CheckboxComponentSaveState] = pydantic.Field(default=None)
    """
    Styles the input. Default is `unsaved`. Prevent action with `saved`.
    """

    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Styles all options and prevents the action. Default is false. Will be overridden if save_state is saved.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
