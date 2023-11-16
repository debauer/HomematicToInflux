from __future__ import annotations

from logging import getLogger

from defusedxml import ElementTree

from hmtoinflux.data_types import Room
from hmtoinflux.lists.base_list import BaseList


_log = getLogger()


class RoomList(BaseList):
    def __init__(self, address: str, mode: str) -> None:
        BaseList.__init__(self, address, mode)
        self.rooms: list[Room] = []
        self.update()

    def rebuild(self, xml: str) -> None:
        self.rooms = []
        xmlp = ElementTree.XMLParser(encoding=self.encoding)
        roomlist = ElementTree.fromstring(xml, xmlp)

        for r in roomlist:
            room_name = r.attrib["name"]
            ise_id = r.attrib["ise_id"]
            channels = [int(c.attrib["ise_id"]) for c in r]
            new_room = Room(
                name=room_name,
                ise_id=int(ise_id),
                channels=channels,
            )
            self.rooms.append(new_room)

    def print_all_rooms(self) -> None:
        for r in self.rooms:
            _log.info(r)

    def get_room_count(self) -> int:
        return len(self.rooms)
