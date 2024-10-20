from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_type_enum import DataTypeEnum

T = TypeVar("T", bound="DataMessageExtra")


@_attrs_define
class DataMessageExtra:
    """
    Attributes:
        hide_message (bool):
        data (Any):
        data_type (DataTypeEnum): * `custom` - Custom
            * `audio_b64` - Audio B64
            * `signal` - Signal
    """

    hide_message: bool
    data: Any
    data_type: DataTypeEnum
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hide_message = self.hide_message

        data = self.data

        data_type = self.data_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hide_message": hide_message,
                "data": data,
                "data_type": data_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hide_message = d.pop("hide_message")

        data = d.pop("data")

        data_type = DataTypeEnum(d.pop("data_type"))

        data_message_extra = cls(
            hide_message=hide_message,
            data=data,
            data_type=data_type,
        )

        data_message_extra.additional_properties = d
        return data_message_extra

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
