from __future__ import annotations

from logging import getLogger

from defusedxml import ElementTree

from hmtoinflux.data_types import Device
from hmtoinflux.lists import BaseList


_log = getLogger()


class DeviceList(BaseList):
    def __init__(self, address: str, mode: str) -> None:
        BaseList.__init__(self, address, mode)
        self.devices: list[Device] = []
        self.update()

    def rebuild(self, xml: str) -> None:
        self.devices = []
        xmlp = ElementTree.XMLParser(encoding=self.encoding)
        roomlist = ElementTree.fromstring(xml, xmlp)

        for r in roomlist:
            room_name = r.attrib["name"]
            device_type = r.attrib["device_type"]
            address = r.attrib["address"]
            ise_id = r.attrib["ise_id"]
            new_room = Device(room_name, ise_id, address, device_type)
            self.devices.append(new_room)

    def get_device_by_name(self, name: str) -> Device:
        for r in self.devices:
            if r.name == name:
                return r
        return Device(name="not found", ise_id=0, address="", device_type="unknown")

    def print_all_devices(self) -> None:
        for r in self.devices:
            _log.info(r)

    def get_device_count(self) -> int:
        return len(self.devices)
