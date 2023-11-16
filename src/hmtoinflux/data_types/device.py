from __future__ import annotations


class Device:
    def __init__(self, name: str, ise_id: int, address: str, device_type: str) -> None:
        self.name = name
        self.ise_id = ise_id
        self.address = address
        self.device_type = device_type

    def get_name(self) -> str:
        return self.name

    def get_ise_id(self) -> int:
        return self.ise_id

    def get_address(self) -> str:
        return self.address

    def get_device_type(self) -> str:
        return self.device_type

    def tostring(self) -> str:
        return (
            "device: {:40} | ise_id: {:4} | address: {:14} | device_type: {:10}".format(
                self.name,
                self.ise_id,
                self.address,
                self.device_type,
            )
        )

    def __str__(self) -> str:
        return self.tostring()
