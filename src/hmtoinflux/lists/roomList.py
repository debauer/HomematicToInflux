import xml.etree.ElementTree as ET

from .baseList import BaseList
from hmtoinflux.data_types import Room


class RoomList(BaseList):
    def __init__(self, address: str, mode: str):
        BaseList.__init__(self, address, mode)
        self.rooms = []
        self.update()

    def rebuild(self, xml):
        self.rooms = []
        xmlp = ET.XMLParser(encoding=self.encoding)
        roomlist = ET.fromstring(xml, xmlp)

        for r in roomlist:
            room_name = r.attrib["name"]
            ise_id = r.attrib["ise_id"]
            channels = []
            for c in r:
                channels.append(c.attrib["ise_id"])
            new_room = Room(room_name, ise_id, channels)
            self.rooms.append(new_room)

    def print_all_rooms(self):
        for r in self.rooms:
            print(r)

    def get_room_count(self):
        return len(self.rooms)
