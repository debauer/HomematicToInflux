from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Room:
    name: str
    ise_id: int
    channels: list[int]

    def get_name(self) -> str:
        return self.name

    def get_ise_id(self) -> int:
        return self.ise_id

    def get_channels(self) -> list[int]:
        return self.channels

    def is_id_in_channels(self, ise_id: int) -> bool:
        if ise_id in self.channels:
            return True
        return False

    def tostring(self) -> str:
        return f"room: {self.name:40} | ise_id: {self.ise_id:4} | channels: {len(self.channels)!s:14}"

    def __str__(self) -> str:
        return self.tostring()
