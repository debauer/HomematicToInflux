import xml.etree.ElementTree as ET
import re

from hm import BaseList, State


class StateList(BaseList):
    def __init__(self, xml):
        BaseList.__init__(self, xml)
        self.states = []
        self.rebuild(xml)

    def rebuild(self, xml):
        self.states = []
        xmlp = ET.XMLParser(encoding=self.encoding)
        statelist = ET.fromstring(xml, xmlp)

        for device in statelist:
            device_name = device.attrib['name']
            ise_id = device.attrib['ise_id']
            datapoints = []
            for channel in device:
                for datapoint in channel:
                    obj = {}
                    for a in datapoint.attrib:
                        obj[a] = datapoint.attrib[a]
                    name = re.sub('.*:', '', obj['name'])  # replace bullshit
                    nr = re.sub('\..*', '', name)
                    name = name.replace(nr+'.', '') + '_' + nr
                    obj['name'] = name
                    datapoints.append(obj)
            new_state = State(device_name, ise_id, datapoints)
            self.states.append(new_state)

    def get_state_by_name(self, name):
        for s in self.states:
            if s.name == name:
                return s

    def print_all_states(self):
        for r in self.states:
            print(r)
