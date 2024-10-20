from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_message_extra import DataMessageExtra


T = TypeVar("T", bound="CreateChat")


@_attrs_define
class CreateChat:
    """
    Attributes:
        text (str):
        chat_settings (Union[Unset, Any]):
        data_message (Union[Unset, DataMessageExtra]):
    """

    text: str
    chat_settings: Union[Unset, Any] = UNSET
    data_message: Union[Unset, "DataMessageExtra"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        chat_settings = self.chat_settings

        data_message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_message, Unset):
            data_message = self.data_message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if chat_settings is not UNSET:
            field_dict["chat_settings"] = chat_settings
        if data_message is not UNSET:
            field_dict["data_message"] = data_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_message_extra import DataMessageExtra

        d = src_dict.copy()
        text = d.pop("text")

        chat_settings = d.pop("chat_settings", UNSET)

        _data_message = d.pop("data_message", UNSET)
        data_message: Union[Unset, DataMessageExtra]
        if isinstance(_data_message, Unset):
            data_message = UNSET
        else:
            data_message = DataMessageExtra.from_dict(_data_message)

        create_chat = cls(
            text=text,
            chat_settings=chat_settings,
            data_message=data_message,
        )

        create_chat.additional_properties = d
        return create_chat

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
