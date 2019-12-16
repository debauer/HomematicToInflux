from hm import BaseList, Device
import xml.etree.ElementTree as ET


class DeviceList(BaseList):
    def __init__(self, xml):
        BaseList.__init__(self, xml)
        self.devices = []

        xmlp = ET.XMLParser(encoding=self.encoding)
        roomlist = ET.fromstring(xml, xmlp)

        for r in roomlist:
            room_name = r.attrib['name']
            device_type = r.attrib['device_type']
            address = r.attrib['address']
            ise_id = r.attrib['ise_id']
            new_room = Device(room_name, ise_id, address, device_type)
            self.devices.append(new_room)

    def get_device_by_name(self, name):
        for r in self.devices:
            if r.name == name:
                return r

    def print_all_devices(self):
        for r in self.devices:
            print(r)

    def get_device_count(self):
        return len(self.devices)
