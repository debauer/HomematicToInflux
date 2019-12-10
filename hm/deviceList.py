from hm import BaseList


class Devicelist(BaseList):
    def __init__(self, xml):
        BaseList.__init__(self, xml)
        self.devices = []

        xmlp = ET.XMLParser(encoding=self.encoding)
        devicelist = ET.fromstring(xml, xmlp)

        for r in devicelist:
            device_name = r.attrib['name']
            ise_id = 1
            channels = []
            for c in r:
                channels.append(c.attrib['ise_id'])
            new_room = Device(device_name, ise_id, channels)
            self.devices.append(new_room)

    def print_all_rooms(self):
        for r in self.devices:
            print(r.tostring())