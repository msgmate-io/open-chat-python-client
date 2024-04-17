from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import Unset

T = TypeVar("T", bound="Person")


@_attrs_define
class Person:
    """
    Attributes:
        email (str):
        password (str):
        password_confirm (str):
    """

    email: str
    password: str
    password_confirm: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        password = self.password

        password_confirm = self.password_confirm

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
                "password_confirm": password_confirm,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")

        password = (
            self.password if isinstance(self.password, Unset) else (None, str(self.password).encode(), "text/plain")
        )

        password_confirm = (
            self.password_confirm
            if isinstance(self.password_confirm, Unset)
            else (None, str(self.password_confirm).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "email": email,
                "password": password,
                "password_confirm": password_confirm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        password = d.pop("password")

        password_confirm = d.pop("password_confirm")

        person = cls(
            email=email,
            password=password,
            password_confirm=password_confirm,
        )

        person.additional_properties = d
        return person

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
